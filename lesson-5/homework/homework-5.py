#task1
def convert_cel_to_far(celsius: float) -> float:
    return round(celsius * 9/5 + 32, 2)
def convert_far_to_cel(fahrenheit: float) -> float:
    return round((fahrenheit - 32) * 5/9, 2)
def main():
    fahrenheit = float(input("Enter a temperature in degrees F: "))
    celsius = convert_far_to_cel(fahrenheit)
    print(f"{fahrenheit} degrees F = {celsius} degrees C\n")
    celsius = float(input("Enter a temperature in degrees C: "))
    fahrenheit = convert_cel_to_far(celsius)
    print(f"{celsius} degrees C = {fahrenheit} degrees F")
if __name__ == "__main__":
    main()

#task2
def invest(amount: float, rate: float, years: int):
    for year in range(1, years + 1):
        amount += amount * rate
        print(f"year {year}: ${amount:.2f}")
def main():
    principal = float(input("Enter the initial amount: "))
    annual_rate = float(input("Enter the annual rate of return: "))
    num_years = int(input("Enter the number of years: "))
    invest(principal, annual_rate, num_years)
if __name__ == "__main__":
    main()

#task3
def find_factors(n: int):
    for i in range(1, n + 1):
        if n % i == 0:
            print(f"{i} is a factor of {n}")
def main():
    num = int(input("Enter a positive integer: "))
    find_factors(num)
if __name__ == "__main__":
    main()

#task4
import statistics
def enrollment_stats(universities):
    students = [uni[1] for uni in universities]
    tuitions = [uni[2] for uni in universities]
    return students, tuitions
def mean(values):
    return sum(values) / len(values)
def median(values):
    return statistics.median(values)
def main():
    universities = [
        ['California Institute of Technology', 2175, 37704],
        ['Harvard', 19627, 39849],
        ['Massachusetts Institute of Technology', 10566, 40732],
        ['Princeton', 7802, 37000],
        ['Rice', 5879, 35551],
        ['Stanford', 19535, 40569],
        ['Yale', 11701, 40500]
    ]
    students, tuitions = enrollment_stats(universities)
    total_students = sum(students)
    total_tuition = sum(tuitions)
    print("*" * 30)
    print(f"Total students: {total_students:,}")
    print(f"Total tuition: $ {total_tuition:,}")
    print()
    print(f"Student mean: {mean(students):,.2f}")
    print(f"Student median: {median(students):,}")
    print()
    print(f"Tuition mean: $ {mean(tuitions):,.2f}")
    print(f"Tuition median: $ {median(tuitions):,}")
    print("*" * 30)
if __name__ == "__main__":
    main()

#task5
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True
