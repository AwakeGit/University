# Дана переменная, в которой хранится шестизначное число — номер билета.
# Напишите программу, которая будет определять, является ли билет счастливым.
# Билет счастливый, если сумма первых трёх цифр равна сумме последних трёх цифр.


def check_ticket(data):
    first_ticket_sum: int = sum(map(int, data[:3]))
    second_ticket_sum: int = sum(map(int, data[3:]))
    if first_ticket_sum == second_ticket_sum:
        return 'Билет счастливый'
    return 'Не счастливый'


if __name__ == '__main__':
    ticket: str = input('Введите номер билета: ')
    if len(ticket) == 6:
        print(check_ticket(ticket))
    else:
        print('Введите правильный формат билета')
