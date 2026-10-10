from typing import Optional


class TreeNode:
    """Binary tree root for the org chart."""
    def __init__(self, salary=0, left=None, right=None):
        self.salary = salary
        self.left = left
        self.right = right


def count_fair_managers(root: Optional[TreeNode]) -> int:
    """
    Problem 3: Fair managers in an org chart.

    Given the root of a binary tree where each root has a `salary`,
    count the number of roots whose salary equals the floor-division
    average salary of their entire subtree (including themselves).

    Args:
        root: root Treeroot of the org chart (or None for empty chart).

    Returns:
        Number of fair managers in the tree.
    """
    x = 0

    def dfs(node):
            nonlocal x
            if node is None:
                return 0, 0
            ls, ln = dfs(node.left)
            rs, rn = dfs(node.right)
            total = node.salary + ls + rs
            size = 1 + ln + rn
            if node.salary == total:
                x += 1
            return total, size

    dfs(root)
    return x
    pass


if __name__ == "__main__":
    # Example sanity check (see test.py for the real test cases)
    # root = [1] -> a single employee is trivially a fair manager
    root = TreeNode(1)
    print(count_fair_managers(root))  # expected: 1
