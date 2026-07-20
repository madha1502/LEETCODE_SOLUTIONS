class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>>ll= new ArrayList<>();
        ll.add(new ArrayList<>());
        for(int c:nums){
            int s = ll.size();
            for(int i=0;i<s;i++){
                List<Integer>y = new ArrayList<>(ll.get(i));
                y.add(c);
                ll.add(y);
            }
        }
        return ll;
    }
}