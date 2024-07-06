class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] res = new int[k];
        for (int i : nums) {
            map.put(i, map.getOrDefault(i, 0) + 1);
        }
        for (int i = 0; i < k; i++) {
            int max = -1;
            int key = 0;
            for (Map.Entry<Integer, Integer> e : map.entrySet()) {
                if (e.getValue() > max) {
                    max = e.getValue();
                    key = e.getKey();
                }
            }
            map.remove(key);
            res[i] = key;
        }
        return res;

    }
}