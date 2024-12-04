from linc_implementation import LINCReasoner

def run_tests():
    reasoner = LINCReasoner()
    
    # Load knowledge base
    print("Loading knowledge base...")
    reasoner.load_knowledge_base("test_kb.pl")
    
    # Test case 1: Basic student queries
    print("\nTest case 1: Basic Facts")
    print("\nStep-by-step reasoning:")
    print("1. Checking if Varnit is a student:")
    student_result = reasoner.query("student(varnit_b)")
    print(f"   student(varnit_b) is {bool(student_result)}")
    
    print("\n2. Checking if Kevin is a programmer:")
    programmer_result = reasoner.query("programmer(kevin_g)")
    print(f"   programmer(kevin_g) is {bool(programmer_result)}")
    
    # Test case 2: Classmate relationships
    print("\nTest case 3: Classmate Relationships")
    classmates_result = reasoner.query("classmates(varnit_b, ramneek_s)")
    print(f"Are Varnit and Ramneek classmates? {bool(classmates_result)}")
    
    # Test case 3: Study buddies
    print("\nTest case 4: Study Buddies")
    premises = [
        "student(ramneek_s)",
        "student(anirudh_s)",
        "likes_gaming(ramneek_s)",
        "likes_gaming(anirudh_s)"
    ]
    conclusion = "study_buddies(ramneek_s, anirudh_s)"
    
    print("\nChecking if Ramneek and Anirudh are study buddies:")
    explanation = reasoner.explain_reasoning(premises, conclusion)
    print(explanation)
    
    # Test case 4: Find all study buddy pairs
    print("\nTest case 5: All Study Buddy Pairs")
    study_buddies_result = list(reasoner.query("study_buddies(X, Y)"))
    print("\nAll study buddy pairs:")
    for pair in study_buddies_result:
        print(f"- {pair['X']} and {pair['Y']} are study buddies")

if __name__ == "__main__":
    run_tests()