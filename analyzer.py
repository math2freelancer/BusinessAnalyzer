# Business Survival Analyzer
# تحلیلگر بقای کسب‌وکار

def get_financial_inputs():
    """دریافت اطلاعات مالی از کاربر"""
    print("📋 وارد کردن اطلاعات پروژه")
    print("="*40)
    
    data = {}
    
    data['initial_cash'] = float(input("موجودی اولیه (تومان): "))
    data['future_income'] = float(input("درآمد آینده (تومان): "))
    data['months_until_income'] = int(input("چند ماه دیگر می‌رسد؟ "))
    
    print("\n💸 هزینه‌های ماهانه:")
    data['monthly_rent'] = float(input("اجاره ماهانه: "))
    data['monthly_utilities'] = float(input("هزینه قبوض: "))
    data['other_monthly_costs'] = float(input("سایر هزینه‌های ماهانه: "))
    
    print("\n👨‍🏫 هزینه‌های آموزشی:")
    data['courses_count'] = int(input("تعداد دوره‌ها: "))
    data['teacher_per_course'] = float(input("حقوق استاد برای هر دوره: "))
    
    is_monthly = input("آیا این حقوق ماهانه است؟ (بله/خیر): ").lower()
    if is_monthly == 'بله':
        data['monthly_teacher_cost'] = data['courses_count'] * data['teacher_per_course']
    else:
        total_teacher_cost = data['courses_count'] * data['teacher_per_course']
        data['monthly_teacher_cost'] = total_teacher_cost / data['months_until_income']
    
    print("\n🔧 هزینه‌های یک‌بارمصرف:")
    data['one_time_costs'] = float(input("هزینه تجهیزات/راه‌اندازی: "))
    
    return data

def calculate_financials(data):
    """انجام محاسبات مالی"""
    # هزینه ماهانه کل
    data['total_monthly_cost'] = (
        data['monthly_rent'] +
        data['monthly_utilities'] +
        data['other_monthly_costs'] +
        data['monthly_teacher_cost']
    )
    
    # هزینه کل دوره
    data['total_project_cost'] = (
        data['total_monthly_cost'] * data['months_until_income'] +
        data['one_time_costs']
    )
    
    # کسری/مازاد
    data['cash_deficit'] = data['total_project_cost'] - data['initial_cash']
    
    # ماه‌های بقا
    data['months_survivable'] = data['initial_cash'] / data['total_monthly_cost']
    
    # سوددهی
    data['net_profit'] = data['future_income'] - data['total_project_cost']
    if data['initial_cash'] > 0:
        data['roi'] = (data['net_profit'] / data['initial_cash']) * 100
    else:
        data['roi'] = 0
    
    return data

def generate_report(data):
    """تولید گزارش تحلیل"""
    print("\n" + "="*50)
    print("📊 گزارش تحلیل کسب‌وکار")
    print("="*50)
    
    print(f"\n💰 منابع مالی:")
    print(f"  موجودی اولیه: {data['initial_cash']:,.0f} تومان")
    print(f"  درآمد آینده: {data['future_income']:,.0f} تومان")
    print(f"  زمان تا درآمد: {data['months_until_income']} ماه")
    
    print(f"\n💸 هزینه‌های ماهانه:")
    print(f"  اجاره: {data['monthly_rent']:,.0f}")
    print(f"  قبوض: {data['monthly_utilities']:,.0f}")
    print(f"  سایر: {data['other_monthly_costs']:,.0f}")
    print(f"  اساتید: {data['monthly_teacher_cost']:,.0f}")
    print(f"  **مجموع ماهانه: {data['total_monthly_cost']:,.0f}**")
    
    print(f"\n🔧 هزینه یک‌بارمصرف: {data['one_time_costs']:,.0f}")
    print(f"📊 کل هزینه پروژه: {data['total_project_cost']:,.0f}")
    
    print(f"\n⚠️ وضعیت نقدینگی:")
    if data['cash_deficit'] > 0:
        print(f"  کسری بودجه: {data['cash_deficit']:,.0f} تومان")
        print(f"  ماه‌های بقا: {data['months_survivable']:.1f} ماه")
        
        if data['months_survivable'] < data['months_until_income']:
            print(f"  ❌ خطر: قبل از دریافت درآمد ورشکست می‌شوید!")
        else:
            print(f"  ✅ قابل انجام است")
    else:
        print(f"  ✅ مازاد: {abs(data['cash_deficit']):,.0f} تومان")
    
    print(f"\n📈 تحلیل سوددهی:")
    print(f"  سود خالص: {data['net_profit']:,.0f} تومان")
    print(f"  بازده سرمایه: {data['roi']:.1f}%")
    
    if data['net_profit'] > 0:
        print(f"  🎯 پروژه سودده است!")
    else:
        print(f"  ⚠️ پروژه ضررده است!")

def suggest_solutions(data):
    """پیشنهاد راه‌حل"""
    if data['cash_deficit'] > 0:
        print(f"\n💡 پیشنهادات برای کسری {data['cash_deficit']:,.0f} تومانی:")
        
        reduction = (data['cash_deficit'] / data['total_project_cost']) * 100
        print(f"۱. کاهش {reduction:.1f}% از کل هزینه‌ها")
        
        monthly_deficit = data['cash_deficit'] / data['months_until_income']
        print(f"۲. تأمین ماهانه {monthly_deficit:,.0f} تومان")
        print(f"۳. ایجاد درآمد جانبی {monthly_deficit:,.0f} تومان ماهانه")

def main():
    """تابع اصلی برنامه"""
    print("🧮 تحلیلگر بقای کسب‌وکار")
    print("="*50)
    
    try:
        # دریافت اطلاعات
        data = get_financial_inputs()
        
        # محاسبات
        data = calculate_financials(data)
        
        # گزارش
        generate_report(data)
        suggest_solutions(data)
        
        # ذخیره نتایج
        save = input("\nآیا می‌خواهید نتایج را در فایل ذخیره کنید؟ (بله/خیر): ")
        if save.lower() == 'بله':
            with open("business_report.txt", "w", encoding="utf-8") as f:
                f.write(f"گزارش تحلیل کسب‌وکار\n")
                for key, value in data.items():
                    if isinstance(value, (int, float)):
                        f.write(f"{key}: {value:,.0f}\n")
            print("✅ گزارش در business_report.txt ذخیره شد")
            
    except ValueError:
        print("❌ لطفاً فقط عدد وارد کنید!")
    except ZeroDivisionError:
        print("❌ خطا: تقسیم بر صفر!")
    except Exception as e:
        print(f"❌ خطا: {e}")

# اجرای برنامه
if __name__ == "__main__":
    main()
