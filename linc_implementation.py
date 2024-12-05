from pyswip import Prolog
from typing import List, Dict, Any, Optional

class LINCReasoner:
    def __init__(self):
        self.prolog = Prolog()
        
    def load_knowledge_base(self, kb_file: str) -> None:
        """Load a Prolog knowledge base file"""
        self.prolog.consult(kb_file)

    def query(self, query_str: str) -> List[Dict[str, Any]]:
        """Execute a Prolog query"""
        return list(self.prolog.query(query_str))
    
    def add_temporary_rule(self, rule_str: str) -> None:
        """Add a temporary rule to the knowledge base"""
        self.prolog.assertz(rule_str)
        
    def check_logical_entailment(self, premises: List[str], conclusion: str) -> bool:
        """Check if conclusion follows from premises using direct querying"""
        try:
            # First check if all premises are true
            for premise in premises:
                if not list(self.prolog.query(premise)):
                    return False
                    
            # Then check if conclusion follows
            result = list(self.prolog.query(conclusion))
            return bool(result)
            
        except Exception as e:
            print(f"Error in entailment check: {e}")
            return False

    def explain_reasoning(self, premises: List[str], conclusion: str) -> str:
        """Provide explanation for the reasoning process"""
        explanation = "Reasoning Process:\n"
        
        explanation += "\nChecking premises:\n"
        all_premises_true = True
        for premise in premises:
            try:
                is_true = bool(list(self.prolog.query(premise)))
                explanation += f"- {premise}: {'True' if is_true else 'False'}\n"
                if not is_true:
                    all_premises_true = False
            except Exception as e:
                explanation += f"- {premise}: Error ({str(e)})\n"
                all_premises_true = False
        
        # Check conclusion
        explanation += "\nChecking conclusion:\n"
        if not all_premises_true:
            explanation += "Cannot check conclusion as not all premises are true."
            return explanation
            
        try:
            conclusion_result = bool(list(self.prolog.query(conclusion)))
            explanation += f"- {conclusion}: {'True' if conclusion_result else 'False'}\n"
            
            explanation += "\nFinal Result:\n"
            if conclusion_result:
                explanation += "The conclusion logically follows from the premises."
            else:
                explanation += "The conclusion does not logically follow from the premises."
                
        except Exception as e:
            explanation += f"Error checking conclusion: {str(e)}\n"
            
        return explanation

def test_reasoner():
    """Function to test the reasoner's capabilities with the new knowledge base"""
    reasoner = LINCReasoner()
    
    # Load the knowledge base
    print("Loading knowledge base...")
    reasoner.load_knowledge_base("test_kb.pl")  # THIS IS WHERE test-kb.pl gets loaded in
    
    # Test 1: Basic student fact query
    print("\nTest 1: Basic student query")
    result = reasoner.query("student(varnit_b)")
    print(f"Is Varnit a student? {bool(result)}")
    
    # Test 2: Programmer rule query
    print("\nTest 2: Programmer rule query")
    result = reasoner.query("programmer(varnit_b)")
    print(f"Is Varnit a programmer? {bool(result)}")
    
    # Test 3: Study buddies relationship
    print("\nTest 3: Study buddies relationship")
    result = reasoner.query("study_buddies(varnit_b, kevin_g)")
    print(f"Are Varnit and Kevin study buddies? {bool(result)}")
    
    # Test 4: Logical entailment example
    print("\nTest 4: Logical entailment")
    premises = ["student(varnit_b)", "likes_coding(varnit_b)"]
    conclusion = "programmer(varnit_b)"
    result = reasoner.check_logical_entailment(premises, conclusion)
    print(f"Does {conclusion} follow from {premises}? {result}")
    
    # Test 5: Explanation of study buddies reasoning
    print("\nTest 5: Explanation of study buddies reasoning")
    premises = ["classmates(varnit_b, kevin_g)", "likes_coding(varnit_b)", "likes_coding(kevin_g)"]
    conclusion = "study_buddies(varnit_b, kevin_g)"
    explanation = reasoner.explain_reasoning(premises, conclusion)
    print(explanation)

    # Additional test: Find all study buddies
    print("\nTest 6: Finding all study buddies")
    study_buddies_pairs = reasoner.query("study_buddies(X, Y)")
    print("Study buddy pairs:")
    for pair in study_buddies_pairs:
        print(f"- {pair['X']} and {pair['Y']}")

if __name__ == "__main__":
    test_reasoner()