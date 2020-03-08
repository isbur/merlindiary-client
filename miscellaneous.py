def sprint(obj):
    [print(attr, i) for attr, i in obj.__dict__.items()]