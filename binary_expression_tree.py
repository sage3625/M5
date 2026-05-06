from stack import Stack

# A binary expression tree is a binary tree where each internal node represents an operator and each leaf node represents an operand.
class TreeNode:
    

    def __init__(self, value):
        self.value = value      # operator or operand (string)
        self.left = None
        self.right = None

#    Build an expression tree from a postfix string, supports
#    evaluation, infix traversal, and postfix traversal.
        
class BinaryExpressionTree:
   



    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def clear_tree(self):
        self.root = None

    def build_from_postfix(self, postfix):
        tokens = postfix.split()
        stack = Stack()

        for token in tokens:
            # Operand (number)
            if self._is_number(token):
                node = TreeNode(token)
                stack.push(node)

            # Operator
            elif token in "+-*/":
                if stack.is_empty():
                    raise ValueError("Too few operands for operator")

                right = stack.pop()

                if stack.is_empty():
                    raise ValueError("Too few operands for operator")

                left = stack.pop()

                node = TreeNode(token)
                node.left = left
                node.right = right
                stack.push(node)

            else:
                raise ValueError(f"Invalid token: {token}")

        if stack.is_empty():
            raise ValueError("No expression provided")

        self.root = stack.pop()

        if not stack.is_empty():
            raise ValueError("Extra tokens left after building tree")

    def evaluate_tree(self):
        #Evaluate the expression represented by the tree.
        if self.root is None:
            raise ValueError("Tree is empty")
        return self._evaluate(self.root)

    def _evaluate(self, node):
        # Leaf node: operand
        if node.left is None and node.right is None:
            return float(node.value)

        # Internal node: operator
        x = self._evaluate(node.left)
        y = self._evaluate(node.right)
        op = node.value

        if op == "+":
            return x + y
        elif op == "-":
            return x - y
        elif op == "*":
            return x * y
        elif op == "/":
            if y == 0:
                raise ZeroDivisionError("Division by zero")
            return x / y
        else:
            raise ValueError(f"Unknown operator: {op}")

    def infix_traversal(self):
        #Return an infix string with parentheses.
        if self.root is None:
            raise ValueError("Tree is empty")
        out = []
        self._inorder(self.root, out)
        return "".join(out)

    def _inorder(self, node, out):
        if node is None:
            return
        is_internal = node.left is not None or node.right is not None
        if is_internal:
            out.append("(")
        self._inorder(node.left, out)
        out.append(f"{node.value} ")
        self._inorder(node.right, out)
        if is_internal:
            out.append(")")

    def postfix_traversal(self):
        #Return a space-separated postfix string.
        if self.root is None:
            raise ValueError("Tree is empty")
        out = []
        self._postorder(self.root, out)
        return " ".join(out)

    def _postorder(self, node, out):
        if node is None:
            return
        self._postorder(node.left, out)
        self._postorder(node.right, out)
        out.append(node.value)

    def _is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False