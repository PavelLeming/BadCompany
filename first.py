import math, pygame, os

TG = {0.0: 0, 0.1: 6, 0.2: 11, 0.3: 17, 0.4: 22, 0.5: 27, 0.6: 31, 0.7: 35, 0.8: 39, 0.9: 42,
      1.0: 45, 1.1: 48, 1.2: 50, 1.4: 55, 1.5: 56, 1.6: 58, 1.7: 60, 1.8: 61, 1.9: 63, 2.0: 64,
      2.1: 65, 2.2: 66, 2.3: 67, 2.4: 68, 2.6: 69, 2.7: 70, 2.8: 70, 2.9: 71, 3.0: 72, 3.1: 72, 3.2: 73,
      3.3: 73, 3.4: 74, 3.5: 74, 3.6: 75, 3.7: 75, 3.8: 75, 3.9: 76, 4.0: 76, 4.1: 76, 4.2: 77, 4.3: 77,
      4.4: 77, 4.5: 77, 4.6: 78, 4.7: 78, 4.8: 78, 4.9: 78, 5.0: 79, 5.1: 79, 5.2: 79, 5.3: 79, 5.4: 79,
      5.5: 79, 5.6: 80, 5.7: 80, 5.8: 80, 5.9: 80, 6.0: 80, 6.1: 80, 6.2: 80, 6.3: 81, 6.4: 81, 6.5: 81,
      6.6: 81, 6.7: 81, 6.8: 81, 6.9: 81, 7.0: 81, 7.1: 82, 7.2: 82, 7.3: 82, 7.4: 82, 7.5: 82, 7.6: 82,
      7.7: 82, 7.8: 82, 7.9: 82, 8.0: 82, 8.1: 83, 8.2: 83, 8.3: 83, 8.4: 83, 8.5: 83, 8.6: 83, 8.7: 83,
      8.8: 83, 8.9: 83, 9.0: 83, 9.1: 83, 9.2: 83, 9.3: 83, 9.4: 83, 9.5: 84, 9.6: 84, 9.7: 84, 9.8: 84,
      9.9: 84, 10.0: 84, 10.1: 84, 10.2: 84, 10.3: 84, 10.4: 84, 10.5: 84, 10.6: 84, 10.7: 84, 10.8: 84,
      10.9: 84, 11.0: 84, 11.1: 84, 11.2: 84, 11.3: 84, 11.4: 85, 11.5: 85, 11.6: 85, 11.7: 85, 11.8: 85,
      11.9: 85, 12.0: 85, 12.1: 85, 12.2: 85, 12.3: 85, 12.4: 85, 12.5: 85, 12.6: 85, 12.7: 85, 12.8: 85,
      12.9: 85, 13.0: 85, 13.1: 85, 13.2: 85, 13.3: 85, 13.4: 85, 13.5: 85, 13.6: 85, 13.7: 85, 13.8: 85,
      13.9: 85, 14.0: 85, 14.1: 85, 14.2: 85, 14.3: 86, 14.4: 86, 14.5: 86, 14.6: 86, 14.7: 86, 14.8: 86,
      14.9: 86, 15.0: 86, 15.1: 86, 15.2: 86, 15.3: 86, 15.4: 86, 15.5: 86, 15.6: 86, 15.7: 86, 15.8: 86,
      15.9: 86, 16.0: 86, 16.1: 86, 16.2: 86, 16.3: 86, 16.4: 86, 16.5: 86, 16.6: 86, 16.7: 86, 16.8: 86,
      16.9: 86, 17.0: 86, 17.1: 86, 17.2: 86, 17.3: 86, 17.4: 86, 17.5: 86, 17.6: 86, 17.7: 86, 17.8: 86,
      17.9: 86, 18.0: 86, 18.1: 86, 18.2: 86, 18.3: 86, 18.4: 86, 18.5: 86, 18.6: 86, 18.7: 86, 18.8: 86,
      18.9: 86, 19.0: 87, 19.1: 87, 19.2: 87, 19.3: 87, 19.4: 87, 19.5: 87, 19.6: 87, 19.7: 87, 19.8: 87,
      19.9: 87, 20.0: 87, 20.1: 87, 20.2: 87, 20.3: 87, 20.4: 87, 20.5: 87, 20.6: 87, 20.7: 87, 20.8: 87,
      20.9: 87, 21.0: 87, 21.1: 87, 21.2: 87, 21.3: 87, 21.4: 87, 21.5: 87, 21.6: 87, 21.7: 87, 21.8: 87,
      21.9: 87, 22.0: 87, 22.1: 87, 22.2: 87, 22.3: 87, 22.4: 87, 22.5: 87, 22.6: 87, 22.7: 87, 22.8: 87,
      22.9: 87, 23.0: 87, 23.1: 87, 23.2: 87, 23.3: 87, 23.4: 87, 23.5: 87, 23.6: 87, 23.7: 87, 23.8: 87,
      23.9: 87, 24.0: 87, 24.1: 87, 24.2: 87, 24.3: 87, 24.4: 87, 24.5: 87, 24.6: 87, 24.7: 87, 24.8: 87,
      24.9: 87, 25.0: 87, 25.1: 87, 25.2: 87, 25.3: 87, 25.4: 87, 25.5: 87, 25.6: 87, 25.7: 87, 25.8: 87,
      25.9: 87, 26.0: 87, 26.1: 87, 26.2: 87, 26.3: 87, 26.4: 87, 26.5: 87, 26.6: 87, 26.7: 87, 26.8: 87,
      26.9: 87, 27.0: 87, 27.1: 87, 27.2: 87, 27.3: 87, 27.4: 87, 27.5: 87, 27.6: 87, 27.7: 87, 27.8: 87,
      27.9: 87, 28.0: 87, 28.1: 87, 28.2: 87, 28.3: 87, 28.4: 87, 28.5: 87, 28.6: 88, 28.7: 88, 28.8: 88,
      28.9: 88, 29.0: 88, 29.1: 88, 29.2: 88, 29.3: 88, 29.4: 88, 29.5: 88, 29.6: 88, 29.7: 88, 29.8: 88,
      29.9: 88, 30.0: 88, 30.1: 88, 30.2: 88, 30.3: 88, 30.4: 88, 30.5: 88, 30.6: 88, 30.7: 88, 30.8: 88,
      30.9: 88, 31.0: 88, 31.1: 88, 31.2: 88, 31.3: 88, 31.4: 88, 31.5: 88, 31.6: 88, 31.7: 88, 31.8: 88,
      31.9: 88, 32.0: 88, 32.1: 88, 32.2: 88, 32.3: 88, 32.4: 88, 32.5: 88, 32.6: 88, 32.7: 88, 32.8: 88,
      32.9: 88, 33.0: 88, 33.1: 88, 33.2: 88, 33.3: 88, 33.4: 88, 33.5: 88, 33.6: 88, 33.7: 88, 33.8: 88,
      33.9: 88, 34.0: 88, 34.1: 88, 34.2: 88, 34.3: 88, 34.4: 88, 34.5: 88, 34.6: 88, 34.7: 88, 34.8: 88,
      34.9: 88, 35.0: 88, 35.1: 88, 35.2: 88, 35.3: 88, 35.4: 88, 35.5: 88, 35.6: 88, 35.7: 88, 35.8: 88,
      35.9: 88, 36.0: 88, 36.1: 88, 36.2: 88, 36.3: 88, 36.4: 88, 36.5: 88, 36.6: 88, 36.7: 88, 36.8: 88,
      36.9: 88, 37.0: 88, 37.1: 88, 37.2: 88, 37.3: 88, 37.4: 88, 37.5: 88, 37.6: 88, 37.7: 88, 37.8: 88,
      37.9: 88, 38.0: 88, 38.1: 88, 38.2: 88, 38.3: 88, 38.4: 88, 38.5: 88, 38.6: 88, 38.7: 88, 38.8: 88,
      38.9: 88, 39.0: 88, 39.1: 88, 39.2: 88, 39.3: 88, 39.4: 88, 39.5: 88, 39.6: 88, 39.7: 88, 39.8: 88,
      39.9: 88, 40.0: 88, 40.1: 88, 40.2: 88, 40.3: 88, 40.4: 88, 40.5: 88, 40.6: 88, 40.7: 88, 40.8: 88,
      40.9: 88, 41.0: 88, 41.1: 88, 41.2: 88, 41.3: 88, 41.4: 88, 41.5: 88, 41.6: 88, 41.7: 88, 41.8: 88,
      41.9: 88, 42.0: 88, 42.1: 88, 42.2: 88, 42.3: 88, 42.4: 88, 42.5: 88, 42.6: 88, 42.7: 88, 42.8: 88,
      42.9: 88, 43.0: 88, 43.1: 88, 43.2: 88, 43.3: 88, 43.4: 88, 43.5: 88, 43.6: 88, 43.7: 88, 43.8: 88,
      43.9: 88, 44.0: 88, 44.1: 88, 44.2: 88, 44.3: 88, 44.4: 88, 44.5: 88, 44.6: 88, 44.7: 88, 44.8: 88,
      44.9: 88, 45.0: 88, 45.1: 88, 45.2: 88, 45.3: 88, 45.4: 88, 45.5: 88, 45.6: 88, 45.7: 88, 45.8: 88,
      45.9: 88, 46.0: 88, 46.1: 88, 46.2: 88, 46.3: 88, 46.4: 88, 46.5: 88, 46.6: 88, 46.7: 88, 46.8: 88,
      46.9: 88, 47.0: 88, 47.1: 88, 47.2: 88, 47.3: 88, 47.4: 88, 47.5: 88, 47.6: 88, 47.7: 88, 47.8: 88,
      47.9: 88, 48.0: 88, 48.1: 88, 48.2: 88, 48.3: 88, 48.4: 88, 48.5: 88, 48.6: 88, 48.7: 88, 48.8: 88,
      48.9: 88, 49.0: 88, 49.1: 88, 49.2: 88, 49.3: 88, 49.4: 88, 49.5: 88, 49.6: 88, 49.7: 88, 49.8: 88,
      49.9: 88, 50.0: 88, 50.1: 88, 50.2: 88, 50.3: 88, 50.4: 88, 50.5: 88, 50.6: 88, 50.7: 88, 50.8: 88,
      50.9: 88, 51.0: 88, 51.1: 88, 51.2: 88, 51.3: 88, 51.4: 88, 51.5: 88, 51.6: 88, 51.7: 88, 51.8: 88,
      51.9: 88, 52.0: 88, 52.1: 88, 52.2: 88, 52.3: 88, 52.4: 88, 52.5: 88, 52.6: 88, 52.7: 88, 52.8: 88,
      52.9: 88, 53.0: 88, 53.1: 88, 53.2: 88, 53.3: 88, 53.4: 88, 53.5: 88, 53.6: 88, 53.7: 88, 53.8: 88,
      53.9: 88, 54.0: 88, 54.1: 88, 54.2: 88, 54.3: 88, 54.4: 88, 54.5: 88, 54.6: 88, 54.7: 88, 54.8: 88,
      54.9: 88, 55.0: 88, 55.1: 88, 55.2: 88, 55.3: 88, 55.4: 88, 55.5: 88, 55.6: 88, 55.7: 88, 55.8: 88,
      55.9: 88, 56.0: 88, 56.1: 88, 56.2: 88, 56.3: 88, 56.4: 88, 56.5: 88, 56.6: 88, 56.7: 88, 56.8: 88,
      56.9: 88, 57.0: 88, 57.1: 88, 57.2: 89}
TGMX = {-57.2: 91, -28.6: 92, -19.0: 93, -14.3: 94, -11.4: 95, -9.5: 96, -8.1: 97, -7.1: 98,
        -6.3: 99, -5.6: 100, -5.1: 101, -4.7: 102, -4.3: 103, -4.0: 104, -3.7: 105, -3.4: 106,
        -3.2: 107, -3.0: 108,-2.9: 109, -2.7: 110, -2.6: 111,-2.4: 112, -2.3: 113, -2.2: 114,
        -2.1: 115, -2.0: 116, -1.9: 117, -1.8: 119, -1.7: 120, -1.6: 122, -1.5: 123, -1.4: 125,
        -1.3: 127, -1.2: 130, -1.1: 132, -1.0: 135, -0.9: 138, -0.8: 141, -0.7: 145, -0.6: 150,
        -0.5: 155, -0.4: 160, -0.3: 165, -0.2: 170, -0.1: 175}
TGMM = {0.0: 180, 0.1: 185, 0.2: 190, 0.3: 195, 0.4: 200, 0.5: 205, 0.6: 210, 0.7: 215, 0.8: 220, 0.9: 222,
      1.0: 225, 1.1: 228, 1.2: 230, 1.3: 232, 1.4: 235, 1.5: 236, 1.6: 238, 1.7: 240, 1.8: 241, 1.9: 242, 2.0: 244,
      2.1: 245, 2.2: 246, 2.3: 247, 2.4: 248, 2.6: 249, 2.7: 250, 2.8: 250, 2.9: 251, 3.0: 253, 3.1: 253, 3.2: 253,
      3.3: 253, 3.4: 254, 3.5: 254, 3.6: 254, 3.7: 255, 3.8: 255, 3.9: 255, 4.0: 256, 4.1: 256, 4.2: 256, 4.3: 257,
      4.4: 257, 4.5: 257, 4.6: 257, 4.7: 258, 4.8: 258, 4.9: 258, 5.0: 258, 5.1: 259, 5.2: 259, 5.3: 259, 5.4: 259,
      5.5: 259, 5.6: 260, 5.7: 260, 5.8: 260, 5.9: 260, 6.0: 260, 6.1: 260, 6.2: 260, 6.3: 261, 6.4: 261, 6.5: 261,
      6.6: 261, 6.7: 26181, 6.8: 261, 6.9: 261, 7.0: 261, 7.1: 262, 7.2: 262, 7.3: 262, 7.4: 262, 7.5: 262, 7.6: 262,
      7.7: 262, 7.8: 262, 7.9: 262, 8.0: 262, 8.1: 263, 8.2: 263, 8.3: 263, 8.4: 263, 8.5: 263, 8.6: 263, 8.7: 263,
      8.8: 263, 8.9: 263, 9.0: 263, 9.1: 263, 9.2: 263, 9.3: 263, 9.4: 263, 9.5: 264, 9.6: 264, 9.7: 264, 9.8: 264,
      9.9: 264, 10.0: 264, 10.1: 264, 10.2: 264, 10.3: 264, 10.4: 264, 10.5: 264, 10.6: 264, 10.7: 264, 10.8: 264,
      10.9: 264, 11.0: 264, 11.1: 264, 11.2: 264, 11.3: 264, 11.4: 265, 11.5: 265, 11.6: 265, 11.7: 265, 11.8: 265,
      11.9: 265, 12.0: 265, 12.1: 265, 12.2: 265, 12.3: 265, 12.4: 265, 12.5: 265, 12.6: 265, 12.7: 265, 12.8: 265,
      12.9: 265, 13.0: 265, 13.1: 265, 13.2: 265, 13.3: 265, 13.4: 265, 13.5: 265, 13.6: 265, 13.7: 265, 13.8: 265,
      13.9: 265, 14.0: 265, 14.1: 265, 14.2: 265, 14.3: 266, 14.4: 266, 14.5: 266, 14.6: 266, 14.7: 266, 14.8: 266,
      14.9: 266, 15.0: 266, 15.1: 266, 15.2: 266, 15.3: 266, 15.4: 266, 15.5: 266, 15.6: 266, 15.7: 266, 15.8: 266,
      15.9: 266, 16.0: 266, 16.1: 266, 16.2: 266, 16.3: 266, 16.4: 266, 16.5: 266, 16.6: 266, 16.7: 266, 16.8: 266,
      16.9: 266, 17.0: 266, 17.1: 266, 17.2: 266, 17.3: 266, 17.4: 266, 17.5: 266, 17.6: 266, 17.7: 266, 17.8: 266,
      17.9: 266, 18.0: 266, 18.1: 266, 18.2: 266, 18.3: 266, 18.4: 266, 18.5: 266, 18.6: 266, 18.7: 266, 18.8: 266,
      18.9: 266, 19.0: 267, 19.1: 267, 19.2: 267, 19.3: 267, 19.4: 267, 19.5: 267, 19.6: 267, 19.7: 267, 19.8: 267,
      19.9: 267, 20.0: 267, 20.1: 267, 20.2: 267, 20.3: 267, 20.4: 267, 20.5: 267, 20.6: 267, 20.7: 267, 20.8: 267,
      20.9: 267, 21.0: 267, 21.1: 267, 21.2: 267, 21.3: 267, 21.4: 267, 21.5: 267, 21.6: 267, 21.7: 267, 21.8: 267,
      21.9: 267, 22.0: 267, 22.1: 267, 22.2: 267, 22.3: 267, 22.4: 267, 22.5: 267, 22.6: 267, 22.7: 267, 22.8: 267,
      22.9: 267, 23.0: 267, 23.1: 267, 23.2: 267, 23.3: 267, 23.4: 267, 23.5: 267, 23.6: 267, 23.7: 267, 23.8: 267,
      23.9: 267, 24.0: 267, 24.1: 267, 24.2: 267, 24.3: 267, 24.4: 267, 24.5: 267, 24.6: 267, 24.7: 267, 24.8: 267,
      24.9: 267, 25.0: 267, 25.1: 267, 25.2: 267, 25.3: 267, 25.4: 267, 25.5: 267, 25.6: 267, 25.7: 267, 25.8: 267,
      25.9: 267, 26.0: 267, 26.1: 267, 26.2: 267, 26.3: 267, 26.4: 267, 26.5: 267, 26.6: 267, 26.7: 267, 26.8: 267,
      26.9: 267, 27.0: 267, 27.1: 267, 27.2: 267, 27.3: 267, 27.4: 267, 27.5: 267, 27.6: 267, 27.7: 267, 27.8: 267,
      27.9: 267, 28.0: 267, 28.1: 267, 28.2: 267, 28.3: 267, 28.4: 267, 28.5: 267, 28.6: 268, 28.7: 268, 28.8: 268,
      28.9: 268, 29.0: 268, 29.1: 268, 29.2: 268, 29.3: 268, 29.4: 268, 29.5: 268, 29.6: 268, 29.7: 268, 29.8: 268,
      29.9: 268, 30.0: 268, 30.1: 268, 30.2: 268, 30.3: 268, 30.4: 268, 30.5: 268, 30.6: 268, 30.7: 268, 30.8: 268,
      30.9: 268, 31.0: 268, 31.1: 268, 31.2: 268, 31.3: 268, 31.4: 268, 31.5: 268, 31.6: 268, 31.7: 268, 31.8: 268,
      31.9: 268, 32.0: 268, 32.1: 268, 32.2: 268, 32.3: 268, 32.4: 268, 32.5: 268, 32.6: 268, 32.7: 268, 32.8: 268,
      32.9: 268, 33.0: 268, 33.1: 268, 33.2: 268, 33.3: 268, 33.4: 268, 33.5: 268, 33.6: 268, 33.7: 268, 33.8: 268,
      33.9: 268, 34.0: 268, 34.1: 268, 34.2: 268, 34.3: 268, 34.4: 268, 34.5: 268, 34.6: 268, 34.7: 268, 34.8: 268,
      34.9: 268, 35.0: 268, 35.1: 268, 35.2: 268, 35.3: 268, 35.4: 268, 35.5: 268, 35.6: 268, 35.7: 268, 35.8: 268,
      35.9: 268, 36.0: 268, 36.1: 268, 36.2: 268, 36.3: 268, 36.4: 268, 36.5: 268, 36.6: 268, 36.7: 268, 36.8: 268,
      36.9: 268, 37.0: 268, 37.1: 268, 37.2: 268, 37.3: 268, 37.4: 268, 37.5: 268, 37.6: 268, 37.7: 268, 37.8: 268,
      37.9: 268, 38.0: 268, 38.1: 268, 38.2: 268, 38.3: 268, 38.4: 268, 38.5: 268, 38.6: 268, 38.7: 268, 38.8: 268,
      38.9: 268, 39.0: 268, 39.1: 268, 39.2: 268, 39.3: 268, 39.4: 268, 39.5: 268, 39.6: 268, 39.7: 268, 39.8: 268,
      39.9: 268, 40.0: 268, 40.1: 268, 40.2: 268, 40.3: 268, 40.4: 268, 40.5: 268, 40.6: 268, 40.7: 268, 40.8: 268,
      40.9: 268, 41.0: 268, 41.1: 268, 41.2: 268, 41.3: 268, 41.4: 268, 41.5: 268, 41.6: 268, 41.7: 268, 41.8: 268,
      41.9: 268, 42.0: 268, 42.1: 268, 42.2: 268, 42.3: 268, 42.4: 268, 42.5: 268, 42.6: 268, 42.7: 268, 42.8: 268,
      42.9: 268, 43.0: 268, 43.1: 268, 43.2: 268, 43.3: 268, 43.4: 268, 43.5: 268, 43.6: 268, 43.7: 268, 43.8: 268,
      43.9: 268, 44.0: 268, 44.1: 268, 44.2: 268, 44.3: 268, 44.4: 268, 44.5: 268, 44.6: 268, 44.7: 268, 44.8: 268,
      44.9: 268, 45.0: 268, 45.1: 268, 45.2: 268, 45.3: 268, 45.4: 268, 45.5: 268, 45.6: 268, 45.7: 268, 45.8: 268,
      45.9: 268, 46.0: 268, 46.1: 268, 46.2: 268, 46.3: 268, 46.4: 268, 46.5: 268, 46.6: 268, 46.7: 268, 46.8: 268,
      46.9: 268, 47.0: 268, 47.1: 268, 47.2: 268, 47.3: 268, 47.4: 268, 47.5: 268, 47.6: 268, 47.7: 268, 47.8: 268,
      47.9: 268, 48.0: 268, 48.1: 268, 48.2: 268, 48.3: 268, 48.4: 268, 48.5: 268, 48.6: 268, 48.7: 268, 48.8: 268,
      48.9: 268, 49.0: 268, 49.1: 268, 49.2: 268, 49.3: 268, 49.4: 268, 49.5: 268, 49.6: 268, 49.7: 268, 49.8: 268,
      49.9: 268, 50.0: 268, 50.1: 268, 50.2: 268, 50.3: 268, 50.4: 268, 50.5: 268, 50.6: 268, 50.7: 268, 50.8: 268,
      50.9: 268, 51.0: 268, 51.1: 268, 51.2: 268, 51.3: 268, 51.4: 268, 51.5: 268, 51.6: 268, 51.7: 268, 51.8: 268,
      51.9: 268, 52.0: 268, 52.1: 268, 52.2: 268, 52.3: 268, 52.4: 268, 52.5: 268, 52.6: 268, 52.7: 268, 52.8: 268,
      52.9: 268, 53.0: 268, 53.1: 268, 53.2: 268, 53.3: 268, 53.4: 268, 53.5: 268, 53.6: 268, 53.7: 268, 53.8: 268,
      53.9: 268, 54.0: 268, 54.1: 268, 54.2: 268, 54.3: 268, 54.4: 268, 54.5: 268, 54.6: 268, 54.7: 268, 54.8: 268,
      54.9: 268, 55.0: 268, 55.1: 268, 55.2: 268, 55.3: 268, 55.4: 268, 55.5: 268, 55.6: 268, 55.7: 268, 55.8: 268,
      55.9: 268, 56.0: 268, 56.1: 268, 56.2: 268, 56.3: 268, 56.4: 268, 56.5: 268, 56.6: 268, 56.7: 268, 56.8: 268,
      56.9: 268, 57.0: 268, 57.1: 268, 57.2: 269}
TGMY = {-57.2: 271, -28.6: 272, -19.0: 273, -14.3: 274, -11.4: 275, -9.5: 276, -8.1: 277, -7.1: 278,
        -6.3: 279, -5.6: 280, -5.1: 281, -4.7: 282, -4.3: 283, -4.0: 284, -3.7: 285, -3.4: 286,
        -3.2: 287, -3.0: 288, -2.9: 289, -2.7: 290, -2.6: 291, -2.4: 292, -2.3: 293, -2.2: 294,
        -2.1: 295, -2.0: 296, -1.9: 297, -1.8: 299, -1.7: 300, -1.6: 302, -1.5: 303, -1.4: 305,
        -1.3: 307, -1.2: 310, -1.1: 312, -1.0: 315, -0.9: 318, -0.8: 321, -0.7: 325, -0.6: 330,
        -0.5: 335, -0.4: 340, -0.3: 345, -0.2: 350, -0.1: 355, -0.0: 360}

pygame.init()
size = width, height = 960, 520
screen = pygame.display.set_mode(size)
background1 = pygame.sprite.Group()
background2 = pygame.sprite.Group()
choose = pygame.sprite.Group()
friend = pygame.sprite.Group()
pers = pygame.sprite.Group()
aim = pygame.sprite.Group()
all_sprites = [pers, choose]
FPS = 60
ZX = 0


def load_image(name, k, colorkey=None):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert_alpha()
    image = pygame.transform.scale(image, (int(image.get_width() * k), int(image.get_height() * k)))
    if colorkey is not None:
        if colorkey == -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey)
    else:
        image = image.convert_alpha()
    return image


class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)


class AnimatedSprite(pygame.sprite.Sprite):
    def __init__(self, sheet, columns, rows, x, y, group):
        super().__init__(group)
        self.frames = []
        self.cut_sheet(sheet, columns, rows)
        self.cur_frame = 0
        self.k = 0
        self.image = self.frames[self.cur_frame]
        self.rect = self.rect.move(x, y)

    def cut_sheet(self, sheet, columns, rows):
        self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                sheet.get_height() // rows)
        for j in range(rows):
            for i in range(columns):
                frame_location = (self.rect.w * i, self.rect.h * j)
                self.frames.append(sheet.subsurface(pygame.Rect(
                    frame_location, self.rect.size)))

    def update(self):
        if int(self.cur_frame) != 0:
            self.cur_frame = (self.cur_frame + 7 / FPS * self.k) % len(self.frames)
            self.image = self.frames[int(self.cur_frame)]
        else:
            self.k = 0


class Arrow(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__(aim)
        self.image = load_image('aim.png', 1 / 24)
        self.rect = pygame.Rect(0, 0, self.image.get_width() * 0.3, self.image.get_height() * 0.3)
        self.y = (self.rect.x - 260) // 50
        self.x = 0
        self.tipe = 0
        self.f = False

    def opr(self):
        if pygame.sprite.spritecollideany(self, pers) and not self.f:
            self.image = load_image('aimFriend.png', 1 / 16)
        elif self.f and any(i.activ == 1 for i in PERSES):
            self.image = load_image('aimTarg.png', 1 / 32)
            self.rect.x -= self.image.get_width() // 2
            self.rect.y -= self.image.get_height() // 2
        else:
            self.image = load_image('aim.png', 1 / 24)

    def update(self):
        self.y = (self.rect.y - 260) // 50
        self.x = (self.rect.x - (self.rect.y - 260) + 70) // 100
        if 0 <= self.y <= 2 and 0 <= self.x < len(MAP[0]):
            MAP[self.y][self.x] = 2

    def action(self):
        if pygame.sprite.spritecollideany(self, pers) and not self.f:
            PERSES[
                [str(i) for i in PERSES].index(pygame.sprite.spritecollide(self, pers, False)[0].tipe[0])].activ *= -1
        if not self.f and any(i.activ == 1 for i in PERSES) \
                and not self.f and any(i.activ == 1 for i in PERSES):
            if 0 <= self.y <= 2 and 0 <= self.x <= len(MAP[0]):
                for i in PERSES:
                    if i.activ == 1:
                        i.ytarg = (self.rect.y - 260) // 50
                        i.xtarg = (self.rect.x - (self.rect.y - 260) + 70) // 100
        elif self.f and any(i.activ == 1 for i in PERSES):
            if pygame.sprite.spritecollideany(self, pers):
                PERSES[[i.activ for i in PERSES].index(True)].targ \
                    = pygame.sprite.spritecollideany(self, pers).tipe


class Pers:
    def __init__(self, stats, pazzle, t, x, y, gun=None):
        self.hp = stats[0]
        self.dmg = stats[1]
        self.armor = stats[2]
        self.dodge = stats[3]
        self.aim = stats[4]
        self.speed = stats[5]
        self.pazzle = pazzle
        self.dk = 1
        self.tipe = t
        self.targ = '0'
        self.gun = gun
        self.activ = -1
        self.y = y * 50 + 290
        self.x = x * 100 + y * 50
        self.pazzle[-1].x = self.x - self.pazzle[-1].image.get_width() // 2
        self.pazzle[-1].y = self.y - self.pazzle[-1].image.get_height()
        self.pazzle[-1].rect.x = int(self.pazzle[-1].x)
        self.pazzle[-1].rect.y = int(self.pazzle[-1].y)
        self.xp = x
        self.yp = y
        self.xtarg = x
        self.ytarg = y
        self.spx = 0
        self.sp = 0
        self.a = 1 / 180
        self.r = 0
        for i in range(len(self.pazzle[:-1]) - 1, -1, -1):
            self.pazzle[i].x = self.pazzle[i + 1].x + self.pazzle[i].sx
            self.pazzle[i].rect.x = int(self.pazzle[i].x)
            self.pazzle[i].y = self.pazzle[i + 1].y - self.pazzle[i].image.get_width() + self.pazzle[i].sy
            self.pazzle[i].rect.y = int(self.pazzle[i].y)
        if self.gun is not None:
            self.gun.x = self.pazzle[-1].x + self.gun.sx
            self.gun.rect.x = int(self.gun.x)
            self.gun.y = self.pazzle[-1].y - self.gun.image.get_width() + self.gun.sy
            self.gun.rect.y = int(self.gun.y)

    def __str__(self):
        return self.tipe

    def update(self):
        MAP[int(self.yp)][int(self.xp)] = int(self.tipe)
        if int(self.x) != self.xtarg * 100 + self.ytarg * 50:
            if int(self.x) > self.xtarg * 100 + self.ytarg * 50:
                for i in self.pazzle + [self]:
                    i.x -= self.speed / FPS
                    if int(self.pazzle[-1].cur_frame) == 0:
                        self.pazzle[-1].cur_frame = -1
                        self.pazzle[-1].k = -0.85
                    if i != self:
                        i.rect.x = int(i.x)
            elif int(self.x) < self.xtarg * 100 + self.ytarg * 50:
                for i in self.pazzle + [self]:
                    i.x += self.speed / FPS
                    if int(self.pazzle[-1].cur_frame) == 0:
                        self.pazzle[-1].cur_frame = 1
                        self.pazzle[-1].k = 0.9
                    if i != self:
                        i.rect.x = int(i.x)
        if int(self.y) != self.ytarg * 50 + 290:
            if int(self.y) > self.ytarg * 50 + 290:
                for i in self.pazzle + [self]:
                    i.y -= self.speed / FPS
                    if i != self:
                        i.rect.y = int(i.y)
            if int(self.y) < self.ytarg * 50 + 290:
                for i in self.pazzle + [self]:
                    i.y += self.speed / FPS
                    if i != self:
                        i.rect.y = int(i.y)
        if int(self.pazzle[0].cur_frame) == 0:
            self.pazzle[0].cur_frame = 1
            self.pazzle[0].k = 1
        self.pazzle[0].update()
        self.pazzle[-1].update()
        for i in range(len(self.pazzle[:-1]) - 1, -1, -1):
            self.pazzle[i].x = self.pazzle[i + 1].x + self.pazzle[i].sx
            if i == 0:
                self.pazzle[i].x -= self.spx
            self.pazzle[i].rect.x = int(self.pazzle[i].x)
            self.pazzle[i].rect.y = self.pazzle[i + 1].rect.y - self.pazzle[i].image.get_width() + self.pazzle[i].sy
        if self.gun is not None:
            self.gun.x = self.pazzle[-1].x + self.gun.sx
            self.gun.rect.x = int(self.gun.x)
            self.gun.y = self.pazzle[-1].y - self.gun.image.get_width() + self.gun.sy
            self.gun.rect.y = int(self.gun.y)
        self.yp = (self.y - 290) // 50
        self.xp = (self.x - self.yp * 50) // 100
        if self.targ != '0':
            if int(self.gun.cur_frame) == 0:
                self.pazzle[1].k = 1
                self.pazzle[1].cur_frame = 1
                self.gun.k = 1
                self.gun.cur_frame = 1
                self.sp = 12 / 60
                self.spx = 0
                rdmg = self.dmg
                if self.targ[1] == '0':
                    rdmg *= 5
                PERSES[[str(i) for i in PERSES].index(self.targ[0])].hp -= rdmg
            self.gun.update()
            self.sp -= self.a
            self.spx += self.sp
            self.pazzle[1].update()
            self.r += 2
            oldc = self.gun.rect.center
            if self.gun.rect.center[0] < PERSES[[str(i) for i in PERSES].index(self.targ[0])].pazzle[int(self.targ[1])].rect.center[0]:
                if self.gun.rect.center[1] < PERSES[[str(i) for i in PERSES].index(self.targ[0])].pazzle[int(self.targ[1])].rect.center[1]:
                    self.gun.image = pygame.transform.rotate(self.gun.image,
                                                             -TG[round((PERSES[[str(i) for i in PERSES].index(self.targ[0])].pazzle[int(self.targ[1])].rect.center[1] - self.gun.rect.center[1])
                                                                       / (PERSES[[str(i) for i in PERSES].index(self.targ[0])].pazzle[int(self.targ[1])].rect.center[0] - self.gun.rect.center[0]), 1)])
                if self.gun.rect.center[1] > PERSES[[str(i) for i in PERSES].index(self.targ[0])].pazzle[int(self.targ[1])].rect.center[1]:
                    self.gun.image = pygame.transform.rotate(self.gun.image,
                                                             -TGMY[round((PERSES[[str(i) for i in PERSES].index(self.targ[0])].pazzle[int(self.targ[1])].rect.center[1] - self.gun.rect.center[1])
                                                                       / (PERSES[[str(i) for i in PERSES].index(self.targ[0])].pazzle[int(self.targ[1])].rect.center[0] - self.gun.rect.center[0]), 1)])
            self.gun.rect = self.gun.image.get_rect()
            self.gun.rect.center = oldc


class PersShild(Pers):
    def __init__(self, stats, pazzle, t, x, y):
        super().__init__(stats, pazzle, t, x, y)


class PersHead(AnimatedSprite):
    def __init__(self, sheet, columns, rows, group, t, sx, sy):
        super().__init__(sheet, columns, rows, 0, 0, group)
        self.tipe = t
        self.sx = sx
        self.sy = sy


class PersBody(AnimatedSprite):
    def __init__(self, sheet, columns, rows, group, t, sx, sy):
        super().__init__(sheet, columns, rows, 0, 0, group)
        self.tipe = t
        self.sx = sx
        self.sy = sy


class PersLegs(AnimatedSprite):
    def __init__(self, sheet, columns, rows, group, t):
        super().__init__(sheet, columns, rows, 0, 0, group)
        self.tipe = t


class PersGun(AnimatedSprite):
    def __init__(self, sheet, columns, rows, group, t, sx, sy):
        super().__init__(sheet, columns, rows, 0, 0, group)
        self.tipe = t
        self.rect = self.image.get_rect()
        self.sx = sx
        self.sy = sy


class Background(pygame.sprite.Sprite):
    def __init__(self, image, b):
        super().__init__(b)
        self.image = image
        self.rect = self.image.get_rect()
        self.moveLeft = False
        self.moveRight = False
        self.rect.x = 0
        self.x = 0
        self.rect.y = 0

    def update(self):
        global ZX
        if self.moveLeft and self.x - 100 / FPS > - 1480:
            self.x -= 100 / FPS
            ZX += 50 / FPS
        if self.moveRight and self.x + 100 / FPS < 0:
            self.x += 100 / FPS
            ZX -= 50 / FPS
        self.rect.x = int(self.x)

    def move(self, event):
        if event.key == pygame.K_LEFT:
            self.moveRight = True
        elif event.key == pygame.K_RIGHT:
            self.moveLeft = True

    def notmove(self, event):
        if event.key == pygame.K_LEFT:
            self.moveRight = False
        elif event.key == pygame.K_RIGHT:
            self.moveLeft = False


def mapDraw():
    z = -70
    for i in range(len(MAP)):
        for j in range(len(MAP[0])):
            pygame.draw.polygon(screen, chColor(MAP[i][j]),
                                [(j * 100 + z - int(ZX), 260 + 50 * i - poz(MAP[i][j])),
                                 ((j + 1) * 100 + z - int(ZX), 260 + 50 * i - poz(MAP[i][j])),
                                 (int((j + 1.5) * 100) + z - int(ZX), 260 + 50 * (i + 1) - poz(MAP[i][j])),
                                 (int((j + 0.5) * 100) + z - int(ZX), 260 + 50 * (i + 1) - poz(MAP[i][j]))],
                                dlin(MAP[i][j]))
        z += 50


def chColor(i):
    if i == 0:
        return pygame.Color('white')
    elif i == 1:
        return pygame.Color('red')
    elif i == 2:
        return pygame.Color('green')


def poz(i):
    if i == 0:
        return 0
    elif i == 1:
        return 2
    elif i == 2:
        return 2


def dlin(i):
    if i == 0:
        return 1
    elif i == 1:
        return 3
    elif i == 2:
        return 3


MAP = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
back1 = Background(pygame.transform.scale(load_image('poleu.png', 1), (2440, 520)), background1)
clock = pygame.time.Clock()
camera = Camera()
running = True
ev = False
First = Pers([10, 1, 0, 0, 0, 50], [PersHead(load_image('head.png', 2), 8, 1, pers, '10', 4, 10),
                                PersBody(load_image('body.png', 2), 11, 1, pers, '11', -2, 4),
                                PersLegs(load_image('go.png', 2), 8, 1, pers, '12')], '1', 1, 0,
             PersGun(load_image('firet.png', 2), 11, 1, pers, '1', -12, 42))
Enemy = PersShild([10, 0, 0, 0, 0, 10], [PersHead(load_image('enemyHead.png', 2), 1, 1, pers, '20', 38, 16),
                                     PersBody(load_image('enemyBody.png', 2), 12, 1, pers, '21', -32, 26),
                                     PersLegs(load_image('enemyLegs.png', 2), 7, 1, pers, '22')], '2', 6, 1)
PERSES = [First, Enemy]
back2 = Background(pygame.transform.scale(load_image('poled.png', 1), (2440, 520)), background2)
aimn = Arrow()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            back1.move(event)
            back2.move(event)
            if event.key == pygame.K_a:
                aimn.f = True
        if event.type == pygame.KEYUP:
            back1.notmove(event)
            back2.notmove(event)
            if event.key == pygame.K_a:
                aimn.f = False
        if event.type == pygame.MOUSEMOTION:
            x, y = event.pos
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                aimn.action()
    if pygame.mouse.get_focused():
        pygame.mouse.set_visible(False)
        aimn.rect.x = x
        aimn.rect.y = y
    back1.update()
    back2.update()
    [i.update() for i in PERSES]
    aimn.opr()
    background1.draw(screen)
    aimn.update()
    mapDraw()
    pers.draw(screen)
    MAP = [[0 for i in range(30)] for i in range(3)]
    background2.draw(screen)
    aim.draw(screen)
    clock.tick(FPS)
    pygame.display.flip()


