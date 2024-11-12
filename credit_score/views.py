from django.shortcuts import render
from django.http import JsonResponse
from .models import Question, UserResponse,CreditScore
from .utils import calculate_credit_score
import json 
from django.core import serializers
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'home/Home.html')

def question_view(request):
    questions = Question.objects.all()
    questions_json = serializers.serialize('json', questions) 
    return render(request, "credit/Question.html", {"questions_json": questions_json})

@login_required
def submit_answer(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            question = Question.objects.get(id=data["question_id"])
            answer = data["answer"]

            if answer not in dict(Question.QUESTION_CHOICES):
                return JsonResponse({"status": "failed", "message": "Invalid answer choice"}, status=400)

            UserResponse.objects.create(user=request.user, question=question, answer=answer)
            return JsonResponse({"status": "success"})
        except (KeyError, ValueError, Question.DoesNotExist):
            return JsonResponse({"status": "failed", "message": "Invalid data"}, status=400)
    return JsonResponse({"status": "failed"}, status=400)

def calculate_credit_score(user_responses):
    score = 0
    for response in user_responses:
        if response.answer == 'A':
            score += 10
        elif response.answer == 'B':
            score += 5
        elif response.answer == 'C':
            score += 2
    return score

def results_view(request):
    user_responses = UserResponse.objects.filter(user=request.user)
    credit_score = calculate_credit_score(user_responses)
    credit_score_record, created = CreditScore.objects.get_or_create(user=request.user)
    credit_score_record.score = credit_score
    credit_score_record.save()
    return render(request, "credit/Answer.html", {"credit_score": credit_score})