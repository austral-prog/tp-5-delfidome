def number_to_month(month):
    if month <= 1 or month <= 12:
        months = [
            'January', 'February', 'March', 'April', 'May', 'June', 'July',
            'August', 'September', 'October', 'November', 'December'
            ]
        return months [month - 1]
    else:
        return "error"

    print(number_to_month(1))
    print(number_to_month(2))
    print(number_to_month(13))
