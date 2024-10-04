class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def __repr__(self, level=0):
        ret = "--->" * level + repr(self.value) + "\n"

        for child in self.children:
            ret += child.__repr__(level + 1)
        return ret

    def add_child(self, child):
        self.children.append(child)

    def remove_child(self, child_to_remove):
        self.children = [child for child in self.children if child is not child_to_remove]

    def traverse(self):
        nodes_to_visit = [self]
        while nodes_to_visit:
            current = nodes_to_visit.pop()
            print(current.value)
            nodes_to_visit.extend(current.children)


if __name__ == "__main__":
    # Test
    company = [
        "Monkey Business CEO",
        "VP of Bananas",
        "VP of Lazing Around",
        "Associate Chimp",
        "Chief Bonobo", "Produce Manager", "Tire Swing R & D"]
    root = TreeNode(company.pop(0))
    for count in range(2):
        child_ = TreeNode(company.pop(0))
        root.add_child(child_)

    root.children[0].add_child(TreeNode(company.pop(0)))
    root.children[0].add_child(TreeNode(company.pop(0)))
    root.children[1].add_child(TreeNode(company.pop(0)))
    root.children[1].add_child(TreeNode(company.pop(0)))
    print("MONKEY BUSINESS, LLC.")
    print("=====================")
    print(root)
