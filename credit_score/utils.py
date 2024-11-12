def calculate_credit_score(user_responses):
    score_map = {
        'A': 1,  
        'B': 5,  
        'C': 10, 
        'D': 1  
    }
    total_score = sum(score_map[response.answer] for response in user_responses)    
    max_score = len(user_responses) * max(score_map.values())    
    credit_score = (total_score / max_score) * 100
    return round(credit_score)