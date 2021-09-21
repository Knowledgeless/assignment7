
try:
    g = int(input("grr: "))
    print(g/0)

except ValueError:
    print("ValueError")
except KeyboardInterrupt:
    print("\nKeyboardInterrupt")
except ZeroDivisionError:
    print("ZeroDivisionError")
    
# except Exception as e:
#     print(str(e))
#     print("-----------")

# except(KeyboardInterrupt, ValueError) as e:
#     print(e)