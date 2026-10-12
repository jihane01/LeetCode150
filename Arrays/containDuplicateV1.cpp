#include <stdio.h>

int main() {
    int nums[] = {1, 2, 3, 3, 4};
    int len = sizeof(nums) / sizeof(nums[0]);

    for (int i = 0; i < len; i++) {
        for (int j = i + 1; j < len; j++) {
            if (nums[i] == nums[j]) {
                printf("Duplicate found: %d\n", nums[i]);
                break;
            }
        }
    }

    return 0;
}