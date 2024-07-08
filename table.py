def print_table(metrics, title, dim):
    total = sum(metrics.values())
    rows = []
    column_widths = [0, 0, 0, 0]
    for (name, amount) in metrics.items():
        percent = round((amount * 100) / total, 1)
        amount, percent, bar = f'{amount:_}{dim}', f'{percent}%', '#' * int(percent)
        rows.append([name, amount, percent, bar])
        name_len, amount_len, percent_len, bar_len = len(name), len(amount), len(percent), len(bar)
        if (name_len > column_widths[0]): column_widths[0] = name_len
        if (amount_len > column_widths[1]): column_widths[1] = amount_len
        if (percent_len > column_widths[2]): column_widths[2] = percent_len
        if (bar_len > column_widths[3]): column_widths[3] = bar_len
    total = f'TOTAL: {total}{dim}'
    last_column = len(column_widths) - 1
    table_width = max(len(title), len(total), sum(column_widths) + len(' | ') * last_column)
    hr = '-' * table_width
    header = f'{hr}\n{title.center(table_width, '-')}\n{hr}'
    footer = f'\n{total}\n'
    print(header)
    for row in rows:
        for column, width in enumerate(column_widths):
            if column != last_column: row[column] = row[column].rjust(width)
        print(' | '.join(row))
    print(footer)
