<?php

/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val) { $this->val = $val; }
 * }
 */
class Solution {

    /**
     * @param ListNode $head
     * @return Boolean
     */
    function isPalindrome($head) {
        // $thead = new ListNode(null);
        // $thead->next = $head;
        // $centerNode = $doubleNode = $thead;

        $centerNode = $doubleNode = $head;
        //快慢指针，定位中间位置
        while($doubleNode && $doubleNode->next){
            $centerNode = $centerNode->next;
            $doubleNode = $doubleNode->next->next;
        }

        //反转后半链表
        $dummyHead = new ListNode(null);
        // $mheadTmp = $centerNode->next;
        $mheadTmp = $centerNode;
        while($mheadTmp){
            $curNode = $mheadTmp;
            $mheadTmp = $mheadTmp->next;
            $curNode->next = $dummyHead->next;
            $dummyHead->next = $curNode;
        }
        
        $mhead = $dummyHead->next;
        $thead = $head;
        // while($mhead){
        //     echo $mhead->val . '->';
        //     $mhead = $mhead->next;
        // }
        // echo '<br>';
        // while($thead){
        //     echo $thead->val . '->';
        //     $thead = $thead->next;
        // }
        while($thead && $mhead){
            if($thead->val != $mhead->val){
                return false;
            } else {
                $thead = $thead->next;
                $mhead = $mhead->next;
            }
        }
        return true;
    }
}