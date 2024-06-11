# handling kwargs

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f" {key} : {value}")

print_kwargs(name="Rakteem", standard="College", hobby="Coding")
print_kwargs(name="Anish", standard="College", sports="football")
