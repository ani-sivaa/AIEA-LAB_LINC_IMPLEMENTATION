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
        
        # Check premises
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
    """Function to test the reasoner's capabilities"""
    reasoner = LINCReasoner()
    
    # Load the test knowledge base
    print("Loading knowledge base...")
    reasoner.load_knowledge_base("test_kb.pl")
    
    # Test 1: Basic fact query
    print("\nTest 1: Basic fact query")
    result = reasoner.query("student(alex_thompson)")
    print(f"Is alex_thompson a student? {bool(result)}")
    
    # Test 2: Rule-based query
    print("\nTest 2: Rule-based query")
    result = reasoner.query("academic(alex_thompson)")
    print(f"Is alex_thompson an academic? {bool(result)}")
    
    # Test 3: Logical entailment
    print("\nTest 3: Logical entailment")
    premises = ["student(alex_thompson)"]
    conclusion = "academic(alex_thompson)"
    result = reasoner.check_logical_entailment(premises, conclusion)
    print(f"Does {conclusion} follow from {premises}? {result}")
    
    # Test 4: Explanation
    print("\nTest 4: Explanation of reasoning")
    explanation = reasoner.explain_reasoning(premises, conclusion)
    print(explanation)

if __name__ == "__main__":
    test_reasoner()