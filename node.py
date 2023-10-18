from __future__ import annotations

from typing import Any, List


class Node(object):
    __slots__ = ("state", "cost", "action", "parent")

    def __init__(
        self,
        state: Any,
        cost: int = 0,
        action: Any = None,
        parent: Node = None,
    ) -> None:
        self.state = state
        self.cost = cost
        self.action = action
        self.parent = parent

    def get_actions_from_root(self) -> List[Any]:
        """Get the sequence of actions from the root node to `self`

        Returns:
            A list containing the sequence of actions sorted from
            `root` to `self`.
        """
        actions = []
        node = self
        while node.parent:
            actions.append(node.action)
            node = node.parent
        actions.reverse()
        return actions


if __name__ == "__main__":
    node1 = Node(0)
    node2 = Node(1, cost=1, action="a1", parent=node1)
    node3 = Node(2, cost=2, action="a2", parent=node2)
    node4 = Node(3, cost=3, action="a3", parent=node3)

    print(node4.get_actions_from_root())
