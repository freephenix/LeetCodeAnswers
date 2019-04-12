<?php

class Solution {

    /**
     * @param Integer[] $nums
     * @return Integer
     */
    function removeDuplicates(&$nums) {
        $p = 0;
        $str = $nums[0];
        for($i = 0; $i < sizeof($nums); $i++){
            if($str != $nums[$i]){
                if($p < $i){
                    $str = $nums[$i];
                    $nums[++$p] = $nums[$i];
                }
            }
        }
        $p += 1;
        array_splice($nums, $p, sizeof($nums) - $p);
        return $p;
    }
}