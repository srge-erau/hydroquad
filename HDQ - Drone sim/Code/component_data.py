# component_data.py
# This file stores empirical performance data for motors and propellers.
# Data is structured by Motor -> KV -> Propeller for a cascaded selection workflow.

MOTOR_PERFORMANCE_DATA = {
    "T-MOTOR F60 Pro V-LV 2207.5": {
        # ... (previous motor data remains here, unchanged) ...
        1950: {
            "T-MOTOR T5146-3": {
                20: {"voltage": 25.2, "current": 2.5, "rpm": 12041, "thrust_g": 259.6, "power_w": 63.2, "efficiency_g_w": 4.11},
                40: {"voltage": 25.2, "current": 8.3, "rpm": 18405, "thrust_g": 646.2, "power_w": 208.2, "efficiency_g_w": 3.1},
                60: {"voltage": 25.1, "current": 17, "rpm": 22689, "thrust_g": 1009.4, "power_w": 426.3, "efficiency_g_w": 2.37},
                80: {"voltage": 24.9, "current": 29, "rpm": 27722, "thrust_g": 1544, "power_w": 721.6, "efficiency_g_w": 2.14},
                100: {"voltage": 24.7, "current": 46.8, "rpm": 32031, "thrust_g": 1966.1, "power_w": 1154.6, "efficiency_g_w": 1.7}
            },
            "T-MOTOR T5147-3": {
                20: {"voltage": 25.2, "current": 2.5, "rpm": 11662, "thrust_g": 262.5, "power_w": 63.2, "efficiency_g_w": 4.16},
                40: {"voltage": 25.2, "current": 8.3, "rpm": 17791, "thrust_g": 645.3, "power_w": 208.9, "efficiency_g_w": 3.09},
                60: {"voltage": 25.1, "current": 17.4, "rpm": 22331, "thrust_g": 1044.1, "power_w": 435.9, "efficiency_g_w": 2.39},
                80: {"voltage": 24.9, "current": 30.4, "rpm": 27203, "thrust_g": 1591.9, "power_w": 756.3, "efficiency_g_w": 2.1},
                100: {"voltage": 24.7, "current": 48.3, "rpm": 30968, "thrust_g": 2012.6, "power_w": 1191.2, "efficiency_g_w": 1.69}
            },
            "GF51466-3": {
                20: {"voltage": 25.2, "current": 2.4, "rpm": 12486, "thrust_g": 255.1, "power_w": 59.4, "efficiency_g_w": 4.3},
                40: {"voltage": 25.1, "current": 8.2, "rpm": 19013, "thrust_g": 637.9, "power_w": 207.2, "efficiency_g_w": 3.08},
                60: {"voltage": 25.1, "current": 16.1, "rpm": 23222, "thrust_g": 981.1, "power_w": 402.3, "efficiency_g_w": 2.44},
                80: {"voltage": 24.9, "current": 27.8, "rpm": 28400, "thrust_g": 1484.8, "power_w": 692.3, "efficiency_g_w": 2.24},
                100: {"voltage": 24.7, "current": 45.6, "rpm": 32749, "thrust_g": 1995.8, "power_w": 1125.9, "efficiency_g_w": 1.77}
            }
        },
        2020: {
            "T-MOTOR T5146-3": {
                20: {"voltage": 25.2, "current": 2.7, "rpm": 12396, "thrust_g": 282.7, "power_w": 66.9, "efficiency_g_w": 4.23},
                40: {"voltage": 25.1, "current": 9.5, "rpm": 18986, "thrust_g": 703.4, "power_w": 239.8, "efficiency_g_w": 2.93},
                60: {"voltage": 25, "current": 18.4, "rpm": 23297, "thrust_g": 1075.3, "power_w": 459.5, "efficiency_g_w": 2.34},
                80: {"voltage": 24.9, "current": 32.5, "rpm": 28611, "thrust_g": 1642.4, "power_w": 808.4, "efficiency_g_w": 2.03},
                100: {"voltage": 24.6, "current": 51.5, "rpm": 32529, "thrust_g": 2029.5, "power_w": 1269.5, "efficiency_g_w": 1.6}
            },
            "T-MOTOR T5147-3": {
                20: {"voltage": 25.2, "current": 2.7, "rpm": 12034, "thrust_g": 282.2, "power_w": 68.3, "efficiency_g_w": 4.13},
                40: {"voltage": 25.1, "current": 9.6, "rpm": 18423, "thrust_g": 696.5, "power_w": 241.6, "efficiency_g_w": 2.88},
                60: {"voltage": 25, "current": 20.3, "rpm": 22649, "thrust_g": 1076.1, "power_w": 508.5, "efficiency_g_w": 2.12},
                80: {"voltage": 24.8, "current": 34, "rpm": 27834, "thrust_g": 1669.3, "power_w": 844.4, "efficiency_g_w": 1.98},
                100: {"voltage": 24.6, "current": 53.1, "rpm": 31409, "thrust_g": 2083.5, "power_w": 1306.1, "efficiency_g_w": 1.6}
            },
            "GF51466-3": {
                20: {"voltage": 25.2, "current": 2.6, "rpm": 12865, "thrust_g": 277.9, "power_w": 65.7, "efficiency_g_w": 4.23},
                40: {"voltage": 25.1, "current": 9.4, "rpm": 19549, "thrust_g": 688.5, "power_w": 235.2, "efficiency_g_w": 2.92},
                60: {"voltage": 25, "current": 17.7, "rpm": 23970, "thrust_g": 1052.4, "power_w": 444.7, "efficiency_g_w": 2.37},
                80: {"voltage": 24.9, "current": 31.4, "rpm": 28994, "thrust_g": 1618.5, "power_w": 780.1, "efficiency_g_w": 2.07},
                100: {"voltage": 24.7, "current": 50.9, "rpm": 33426, "thrust_g": 2063, "power_w": 1253.1, "efficiency_g_w": 1.65}
            }
        }
    },
    "T-MOTOR VELOX V3 2207": {
        1750: {
            "T-MOTOR P4943-3": {
                20: {"voltage": 24.0, "current": 2.2, "rpm": 12307.3, "thrust_g": 194.5, "power_w": 52.1, "efficiency_g_w": 3.73},
                40: {"voltage": 24.0, "current": 6.6, "rpm": 18546.7, "thrust_g": 470.0, "power_w": 159.1, "efficiency_g_w": 2.95},
                60: {"voltage": 23.9, "current": 9.4, "rpm": 22433.6, "thrust_g": 704.2, "power_w": 280.2, "efficiency_g_w": 2.51},
                80: {"voltage": 23.8, "current": 17.9, "rpm": 26349.9, "thrust_g": 979.6, "power_w": 424.8, "efficiency_g_w": 2.31},
                100: {"voltage": 23.6, "current": 30.2, "rpm": 31202.4, "thrust_g": 1370.9, "power_w": 711.2, "efficiency_g_w": 1.93}
            },
             "T5147-3": {
                    20: {"voltage": 24.0, "current": 2.2, "rpm": 11293.6, "thrust_g": 210.1, "power_w": 53.2, "efficiency_g_w": 3.95},
                    40: {"voltage": 24.0, "current": 7.0, "rpm": 17179.4, "thrust_g": 525.7, "power_w": 167.3, "efficiency_g_w": 3.14},
                    60: {"voltage": 23.8, "current": 12.7, "rpm": 20865.8, "thrust_g": 784.6, "power_w": 301.7, "efficiency_g_w": 2.60},
                    80: {"voltage": 23.7, "current": 21.1, "rpm": 25070.7, "thrust_g": 1158.9, "power_w": 499.9, "efficiency_g_w": 2.32},
                    100: {"voltage": 23.5, "current": 34.6, "rpm": 29447.1, "thrust_g": 1591.1, "power_w": 814.3, "efficiency_g_w": 1.95},
             },
        },

        1950: {
            "T-MOTOR P4943-3": {
                20: {"voltage": 24.0, "current": 8.4, "rpm": 13356.0, "thrust_g": 233.7, "power_w": 65.6, "efficiency_g_w": 3.56},
                40: {"voltage": 23.9, "current": 8.5, "rpm": 19836.8, "thrust_g": 546.2, "power_w": 203.4, "efficiency_g_w": 2.69},
                60: {"voltage": 23.8, "current": 14.7, "rpm": 24087.5, "thrust_g": 815.0, "power_w": 349.3, "efficiency_g_w": 2.33},
                80: {"voltage": 23.7, "current": 23.5, "rpm": 28670.4, "thrust_g": 1166.7, "power_w": 557.4, "efficiency_g_w": 2.09},
                100: {"voltage": 23.4, "current": 39.5, "rpm": 33871.8, "thrust_g": 1582.0, "power_w": 925.9, "efficiency_g_w": 1.70}
            },
            "T5147-3": {
                    20: {"voltage": 24.0, "current": 2.8, "rpm": 12172.8, "thrust_g": 241.6, "power_w": 67.5, "efficiency_g_w": 3.58},
                    40: {"voltage": 23.9, "current": 9.0, "rpm": 18446.7, "thrust_g": 601.1, "power_w": 214.5, "efficiency_g_w": 2.80},
                    60: {"voltage": 23.8, "current": 16.4, "rpm": 22518.4, "thrust_g": 913.8, "power_w": 390.6, "efficiency_g_w": 2.34},
                    80: {"voltage": 23.6, "current": 27.6, "rpm": 27149.5, "thrust_g": 1349.3, "power_w": 651.7, "efficiency_g_w": 2.07},
                    100: {"voltage": 23.4, "current": 45.0, "rpm": 31612.6, "thrust_g": 1788.2, "power_w": 1050.5, "efficiency_g_w": 1.70},
            },
        },
        2050: {
            "T-MOTOR P4943-3": {
                20: {"voltage": 24.0, "current": 3.2, "rpm": 13798.0, "thrust_g": 239.3, "power_w": 75.9, "efficiency_g_w": 3.15},
                40: {"voltage": 23.9, "current": 9.8, "rpm": 20520.4, "thrust_g": 573.0, "power_w": 234.9, "efficiency_g_w": 2.44},
                60: {"voltage": 23.8, "current": 16.3, "rpm": 24789.8, "thrust_g": 852.0, "power_w": 388.1, "efficiency_g_w": 2.20},
                80: {"voltage": 23.6, "current": 26.7, "rpm": 29484.8, "thrust_g": 1204.2, "power_w": 631.3, "efficiency_g_w": 1.91},
                100: {"voltage": 23.4, "current": 44.7, "rpm": 34693.4, "thrust_g": 1634.3, "power_w": 1043.5, "efficiency_g_w": 1.57}
            },
            "T5147-3": {
                    20: {"voltage": 24.0, "current": 3.3, "rpm": 12622.9, "thrust_g": 257.5, "power_w": 78.1, "efficiency_g_w": 3.30},
                    40: {"voltage": 23.9, "current": 10.4, "rpm": 19040.7, "thrust_g": 639.2, "power_w": 247.3, "efficiency_g_w": 2.60},
                    60: {"voltage": 23.7, "current": 18.9, "rpm": 23118.0, "thrust_g": 955.8, "power_w": 448.5, "efficiency_g_w": 2.10},
                    80: {"voltage": 23.6, "current": 31.0, "rpm": 27736.0, "thrust_g": 1396.6, "power_w": 731.1, "efficiency_g_w": 1.90},
                    100: {"voltage": 23.3, "current": 49.5, "rpm": 32134.3, "thrust_g": 1830.4, "power_w": 1153.4, "efficiency_g_w": 1.60},
            },
        },

        2550: {
            "T-MOTOR P4943-3": {
                20: {"voltage": 16.0, "current": 2.9, "rpm": 11409.8, "thrust_g": 158.4, "power_w": 45.9, "efficiency_g_w": 3.45},
                40: {"voltage": 15.9, "current": 8.8, "rpm": 17473.3, "thrust_g": 402.6, "power_w": 139.7, "efficiency_g_w": 2.88},
                60: {"voltage": 15.8, "current": 15.2, "rpm": 21299.1, "thrust_g": 605.9, "power_w": 240.9, "efficiency_g_w": 2.52},
                80: {"voltage": 15.7, "current": 23.2, "rpm": 24911.5, "thrust_g": 845.2, "power_w": 364.1, "efficiency_g_w": 2.32},
                100: {"voltage": 15.4, "current": 38.0, "rpm": 29422.0, "thrust_g": 1191.8, "power_w": 586.4, "efficiency_g_w": 2.03}
            },
            "T5147-3": {
                    20: {"voltage": 16.0, "current": 3.0, "rpm": 10788.2, "thrust_g": 177.9, "power_w": 47.2, "efficiency_g_w": 3.80},
                    40: {"voltage": 15.9, "current": 9.0, "rpm": 16672.2, "thrust_g": 462.1, "power_w": 143.8, "efficiency_g_w": 3.20},
                    60: {"voltage": 15.8, "current": 16.2, "rpm": 20270.4, "thrust_g": 696.3, "power_w": 256.1, "efficiency_g_w": 2.70},
                    80: {"voltage": 15.6, "current": 25.7, "rpm": 24123.5, "thrust_g": 991.7, "power_w": 401.8, "efficiency_g_w": 2.50},
                    100: {"voltage": 15.4, "current": 41.8, "rpm": 28322.4, "thrust_g": 1392.3, "power_w": 642.5, "efficiency_g_w": 2.20},
            }
        }

    },
    "T-MOTOR F80 Pro 2408": {
        1900: {
            "5055 Tri-Blade": {
                50: {"thrust_g": 790.04, "voltage": 23.89, "current": 11.11, "rpm": 19932, "power_w": 265.36, "efficiency_g_w": 2.98},
                55: {"thrust_g": 908.12, "voltage": 23.84, "current": 13.67, "rpm": 21379, "power_w": 326.01, "efficiency_g_w": 2.79},
                60: {"thrust_g": 1042.01, "voltage": 23.78, "current": 16.61, "rpm": 22752, "power_w": 395.05, "efficiency_g_w": 2.64},
                65: {"thrust_g": 1182.98, "voltage": 23.71, "current": 19.67, "rpm": 24172, "power_w": 466.49, "efficiency_g_w": 2.54},
                70: {"thrust_g": 1323.01, "voltage": 23.63, "current": 23.04, "rpm": 25353, "power_w": 544.56, "efficiency_g_w": 2.43},
                75: {"thrust_g": 1418.16, "voltage": 23.54, "current": 26.09, "rpm": 26680, "power_w": 614.28, "efficiency_g_w": 2.31},
                80: {"thrust_g": 1555.57, "voltage": 23.41, "current": 29.91, "rpm": 27697, "power_w": 700.37, "efficiency_g_w": 2.22},
                85: {"thrust_g": 1683.97, "voltage": 23.28, "current": 33.90, "rpm": 28525, "power_w": 789.23, "efficiency_g_w": 2.13},
                90: {"thrust_g": 1793.47, "voltage": 23.14, "current": 38.02, "rpm": 29579, "power_w": 879.73, "efficiency_g_w": 2.04},
                95: {"thrust_g": 1896.57, "voltage": 22.99, "current": 42.09, "rpm": 30357, "power_w": 967.77, "efficiency_g_w": 1.96},
                100: {"thrust_g": 2114.78, "voltage": 22.83, "current": 49.16, "rpm": 31924, "power_w": 1122.32, "efficiency_g_w": 1.88}
            }
        },
        2200: {
            "5055 Tri-Blade": {
                50: {"thrust_g": 704.65, "voltage": 19.89, "current": 11.16, "rpm": 18832, "power_w": 221.95, "efficiency_g_w": 3.17},
                55: {"thrust_g": 818.27, "voltage": 19.84, "current": 13.79, "rpm": 20104, "power_w": 273.51, "efficiency_g_w": 2.99},
                60: {"thrust_g": 907.14, "voltage": 19.79, "current": 16.47, "rpm": 21492, "power_w": 325.87, "efficiency_g_w": 2.78},
                65: {"thrust_g": 1031.42, "voltage": 19.72, "current": 19.73, "rpm": 22710, "power_w": 389.04, "efficiency_g_w": 2.65},
                70: {"thrust_g": 1154.17, "voltage": 19.64, "current": 23.00, "rpm": 23980, "power_w": 451.81, "efficiency_g_w": 2.55},
                75: {"thrust_g": 1287.66, "voltage": 19.53, "current": 26.77, "rpm": 24983, "power_w": 522.90, "efficiency_g_w": 2.46},
                80: {"thrust_g": 1388.59, "voltage": 19.42, "current": 30.22, "rpm": 26014, "power_w": 586.76, "efficiency_g_w": 2.37},
                85: {"thrust_g": 1492.02, "voltage": 19.29, "current": 34.01, "rpm": 26950, "power_w": 656.15, "efficiency_g_w": 2.27},
                90: {"thrust_g": 1589.63, "voltage": 19.16, "current": 37.84, "rpm": 27796, "power_w": 724.97, "efficiency_g_w": 2.19},
                95: {"thrust_g": 1661.82, "voltage": 19.01, "current": 41.77, "rpm": 28554, "power_w": 794.20, "efficiency_g_w": 2.09},
                100: {"thrust_g": 1867.94, "voltage": 18.87, "current": 48.35, "rpm": 29706, "power_w": 912.15, "efficiency_g_w": 2.05}
            },
            "6040 2-Blade": {
                50: {"thrust_g": 736.57, "voltage": 19.89, "current": 11.18, "rpm": 18754, "power_w": 222.46, "efficiency_g_w": 3.31},
                55: {"thrust_g": 847.93, "voltage": 19.84, "current": 13.69, "rpm": 20131, "power_w": 271.77, "efficiency_g_w": 3.12},
                60: {"thrust_g": 993.47, "voltage": 19.78, "current": 16.85, "rpm": 21330, "power_w": 333.29, "efficiency_g_w": 2.98},
                65: {"thrust_g": 1110.80, "voltage": 19.71, "current": 19.96, "rpm": 22574, "power_w": 393.52, "efficiency_g_w": 2.82},
                70: {"thrust_g": 1239.35, "voltage": 19.64, "current": 23.09, "rpm": 23884, "power_w": 453.43, "efficiency_g_w": 2.73},
                75: {"thrust_g": 1396.62, "voltage": 19.53, "current": 26.93, "rpm": 24790, "power_w": 525.83, "efficiency_g_w": 2.66},
                80: {"thrust_g": 1540.87, "voltage": 19.40, "current": 30.77, "rpm": 25715, "power_w": 596.89, "efficiency_g_w": 2.58},
                85: {"thrust_g": 1661.79, "voltage": 19.27, "current": 34.76, "rpm": 26640, "power_w": 669.79, "efficiency_g_w": 2.48},
                90: {"thrust_g": 1741.02, "voltage": 19.14, "current": 38.47, "rpm": 27495, "power_w": 736.30, "efficiency_g_w": 2.36},
                95: {"thrust_g": 1851.99, "voltage": 18.98, "current": 42.95, "rpm": 28202, "power_w": 815.02, "efficiency_g_w": 2.27},
                100: {"thrust_g": 2037.30, "voltage": 18.79, "current": 49.40, "rpm": 29613, "power_w": 928.25, "efficiency_g_w": 2.19}
            }
        },
        2500: {
            "5055 Tri-Blade": {
                50: {"thrust_g": 591.73, "voltage": 15.85, "current": 11.10, "rpm": 17325, "power_w": 175.99, "efficiency_g_w": 3.36},
                55: {"thrust_g": 676.24, "voltage": 15.79, "current": 13.56, "rpm": 18568, "power_w": 214.09, "efficiency_g_w": 3.16},
                60: {"thrust_g": 751.15, "voltage": 15.73, "current": 16.09, "rpm": 19781, "power_w": 253.24, "efficiency_g_w": 2.97},
                65: {"thrust_g": 843.19, "voltage": 15.67, "current": 19.01, "rpm": 20809, "power_w": 297.95, "efficiency_g_w": 2.83},
                70: {"thrust_g": 945.44, "voltage": 15.61, "current": 22.30, "rpm": 21783, "power_w": 348.03, "efficiency_g_w": 2.72},
                75: {"thrust_g": 1010.05, "voltage": 15.52, "current": 25.57, "rpm": 22951, "power_w": 397.01, "efficiency_g_w": 2.54},
                80: {"thrust_g": 1120.09, "voltage": 15.42, "current": 29.13, "rpm": 23807, "power_w": 449.12, "efficiency_g_w": 2.49},
                85: {"thrust_g": 1222.90, "voltage": 15.29, "current": 33.01, "rpm": 24520, "power_w": 504.80, "efficiency_g_w": 2.42},
                90: {"thrust_g": 1304.56, "voltage": 15.17, "current": 36.80, "rpm": 25256, "power_w": 558.15, "efficiency_g_w": 2.34},
                95: {"thrust_g": 1363.42, "voltage": 15.04, "current": 40.40, "rpm": 25960, "power_w": 607.82, "efficiency_g_w": 2.24},
                100: {"thrust_g": 1516.82, "voltage": 14.88, "current": 46.67, "rpm": 27110, "power_w": 694.45, "efficiency_g_w": 2.18}
            },
            "6040 2-Blade": {
                50: {"thrust_g": 625.57, "voltage": 15.87, "current": 11.27, "rpm": 17282, "power_w": 178.91, "efficiency_g_w": 3.50},
                55: {"thrust_g": 719.71, "voltage": 15.81, "current": 13.76, "rpm": 18554, "power_w": 217.53, "efficiency_g_w": 3.31},
                60: {"thrust_g": 816.18, "voltage": 15.70, "current": 16.46, "rpm": 19641, "power_w": 258.31, "efficiency_g_w": 3.16},
                65: {"thrust_g": 917.09, "voltage": 15.65, "current": 19.45, "rpm": 20632, "power_w": 304.29, "efficiency_g_w": 3.01},
                70: {"thrust_g": 1004.55, "voltage": 15.59, "current": 22.49, "rpm": 21763, "power_w": 350.72, "efficiency_g_w": 2.86},
                75: {"thrust_g": 1106.85, "voltage": 15.52, "current": 25.91, "rpm": 22791, "power_w": 402.14, "efficiency_g_w": 2.75},
                # Note: The CSV has a typo here listing KV2200 data under the KV2500 section.
                # I have used the correct KV2500 data row from the table.
                80: {"thrust_g": 1228.74, "voltage": 15.40, "current": 29.81, "rpm": 23566, "power_w": 459.04, "efficiency_g_w": 2.68},
                85: {"thrust_g": 1320.52, "voltage": 15.28, "current": 33.42, "rpm": 24389, "power_w": 510.73, "efficiency_g_w": 2.59},
                90: {"thrust_g": 1419.87, "voltage": 15.15, "current": 37.29, "rpm": 25078, "power_w": 565.15, "efficiency_g_w": 2.51},
                95: {"thrust_g": 1527.30, "voltage": 15.02, "current": 41.45, "rpm": 25597, "power_w": 622.61, "efficiency_g_w": 2.45},
                100: {"thrust_g": 1700.76, "voltage": 14.83, "current": 47.62, "rpm": 26793, "power_w": 706.20, "efficiency_g_w": 2.41}
            }
        }
    }
}