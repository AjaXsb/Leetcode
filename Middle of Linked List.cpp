/* https://leetcode.com/problems/middle-of-the-linked-list/ */

class Solution {
public:

    ListNode* middleNode(ListNode* head) {

        ListNode* p1 = head;
        ListNode* p2 = head;

        if (head != NULL)
        {
        while (p2 != NULL && p2->next != NULL)
        {
        p2 = p2->next->next;
        p1 = p1->next;
        }
        return p1;
        }
        return 0;
    }
};
