class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashSet<Character>set = new HashSet<>();
        int max = 0;
        int i=0;//left pointer
        for(int j=0;j<s.length();j++){//right pointer
            while(set.contains(s.charAt(j))){
                set.remove(s.charAt(i));
                i++;
            }
            set.add(s.charAt(j));
            max = Math.max(max,j-i+1);
        }
        return max;
    }
}