try:
    raise Exception('Preemptive strike!')
    print(undefinedVariable)
except Exception as ex:
    print("Oh man, who could've guessed?", ex)
