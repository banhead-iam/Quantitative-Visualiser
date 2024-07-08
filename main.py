from table import print_table

EACH_MONTH = 365 // 30; EACH_WEEK = 365 // 7; EACH_2_WEEKS = 365 // 14
annual_exp = {
    'dorm': 1_500 * EACH_MONTH,
    'food': 500 * EACH_WEEK,
    'train': 136 * EACH_2_WEEKS,
    'phone': 713 * EACH_MONTH,
    'music': 99 * EACH_MONTH,
    'parties': 1_500 * EACH_MONTH
}

print_table(annual_exp, ' ANNUAL EXPENDITURE ', '₽')