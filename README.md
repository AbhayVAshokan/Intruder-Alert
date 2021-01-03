# Intruder-Alert
A simple OpenCV project to detect intruders in the live feed. It checks the differences in the subsequent frames and determines whether it is an intruder or not.

### Steps
1. Calculate absolute difference between subsequent frames.
2. Apply Gaussian blur filter
3. Apply Binary Threshold
4. Calculate average intensity of the resultant frame.
5. If the average intensity is >= 150, then it is flagged as an intruder.
