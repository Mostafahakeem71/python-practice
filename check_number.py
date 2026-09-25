def check_number(num):
    if num > 0:
        print(f"الرقم {num} موجب (Positive)")
    elif num < 0:
        print(f"الرقم {num} سالب (Negative)")
    else:
        print("الرقم هو صفر (Zero)")

# اختبار الدالة
check_number(15)
check_number(-7)
check_number(0)