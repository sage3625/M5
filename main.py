from binary_expression_tree import BinaryExpressionTree
from triage_system import TriageSystem


postfix_expressions = [
    "5 3 +",
    "8 2 - 3 +",
    "5 3 8 * +",
    "6 2 / 3 +",
    "5 8 + 3 -",
    "5 3 + 8 *",
    "8 2 3 * + 6 -",
    "5 3 8 * + 2 /",
    "8 2 + 3 6 * -",
    "5 3 + 8 2 / -"
]

print("----- Binary Expression Tree -----\n")

for expr in postfix_expressions:
    tree = BinaryExpressionTree()
    tree.build_from_postfix(expr)

    infix = tree.infix_traversal()
    postfix = tree.postfix_traversal()
    result = tree.evaluate_tree()

    print(f"Infix Expression: {infix}")
    print(f"Postfix Expression: {postfix}")
    print(f"Evaluated Result: {result}\n")



def main():
    triage = TriageSystem()

    # Test data
    patients = [
        ("Sofia", 5),
        ("Bob", 2),
        ("Charlie", 4),
        ("Diana", 3),
        ("Eli", 1),
        ("Tom", 4),
        ("Alice", 5),
        ("Rachel", 4),
    ]

    # Add patients
    for name, severity in patients:
        triage.AddPatient(name, severity)

    print("----- Hospital Triage System -----\n")
    print("="*30 + "\n")
    print("Processing patients:\n")

    # Process in priority order
    while not triage.IsEmpty():
        patient = triage.ProcessNext()
        if patient is None:
            break
        name, severity = patient
        print(f"Now treating: {name} (Severity {severity})")