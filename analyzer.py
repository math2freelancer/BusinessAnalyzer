# Business Survival Analyzer PRO
# تحلیلگر حرفه‌ای بقای کسب‌وکار
# نسخه: 2.0 | توسعه‌دهنده: math2freelancer

def get_financial_inputs():
    """دریافت اطلاعات مالی از کاربر"""
    print("🧮 تحلیلگر بقای کسب‌وکار - نسخه حرفه‌ای")
    print("=" * 50)
    
    print("\n📋 لطفاً اطلاعات مالی پروژه خود را وارد کنید:")
    print("-" * 40)
    
    data = {}
    
    # دریافت اطلاعات اصلی
    data['initial_cash'] = float(input("💰 موجودی اولیه (تومان): "))
    data['future_income'] = float(input("📈 درآمد آینده (تومان): "))
    data['months_until_income'] = int(input("📅 چند ماه دیگر می‌رسد؟ "))
    
    print("\n💸 هزینه‌های ماهانه:")
    data['monthly_rent'] = float(input("   اجاره محل: "))
    data['monthly_utilities'] = float(input("   هزینه قبوض (آب، برق، گاز): "))
    data['other_monthly_costs'] = float(input("   سایر هزینه‌های ماهانه: "))
    
    print("\n👨‍🏫 هزینه‌های آموزشی:")
    data['courses_count'] = int(input("   تعداد دوره‌ها: "))
    data['teacher_per_course'] = float(input("   حق‌التدریس هر دوره: "))
    
    # محاسبه هزینه اساتید
    is_monthly = input("   آیا این حقوق ماهانه است؟ (بله/خیر): ").lower()
    if is_monthly == 'بله':
        data['monthly_teacher_cost'] = data['courses_count'] * data['teacher_per_course']
    else:
        total_teacher_cost = data['courses_count'] * data['teacher_per_course']
        data['monthly_teacher_cost'] = total_teacher_cost / data['months_until_income']
    
    print("\n🔧 هزینه‌های یک‌بارمصرف:")
    data['one_time_costs'] = float(input("   هزینه تجهیزات/راه‌اندازی: "))
    
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
    if data['total_monthly_cost'] > 0:
        data['months_survivable'] = data['initial_cash'] / data['total_monthly_cost']
    else:
        data['months_survivable'] = float('inf')  # اگر هزینه صفر باشد
    
    # سوددهی
    data['net_profit'] = data['future_income'] - data['total_project_cost']
    if data['initial_cash'] > 0:
        data['roi'] = (data['net_profit'] / data['initial_cash']) * 100
    else:
        data['roi'] = 0
    
    return data

def generate_basic_report(data):
    """تولید گزارش تحلیل پایه"""
    print("\n" + "=" * 50)
    print("📊 گزارش تحلیل پایه")
    print("=" * 50)
    
    print(f"\n💰 منابع مالی:")
    print(f"  • موجودی اولیه: {data['initial_cash']:,.0f} تومان")
    print(f"  • درآمد آینده: {data['future_income']:,.0f} تومان")
    print(f"  • زمان تا درآمد: {data['months_until_income']} ماه")
    
    print(f"\n💸 هزینه‌های ماهانه:")
    print(f"  • اجاره: {data['monthly_rent']:,.0f} تومان")
    print(f"  • قبوض: {data['monthly_utilities']:,.0f} تومان")
    print(f"  • سایر: {data['other_monthly_costs']:,.0f} تومان")
    print(f"  • اساتید: {data['monthly_teacher_cost']:,.0f} تومان")
    print(f"  🔸 مجموع ماهانه: {data['total_monthly_cost']:,.0f} تومان")
    
    print(f"\n🔧 هزینه یک‌بارمصرف: {data['one_time_costs']:,.0f} تومان")
    print(f"📊 کل هزینه پروژه: {data['total_project_cost']:,.0f} تومان")

def analyze_survival(data):
    """تحلیل وضعیت بقا"""
    print(f"\n⚠️ وضعیت نقدینگی:")
    
    if data['cash_deficit'] > 0:
        print(f"  • کسری بودجه: {data['cash_deficit']:,.0f} تومان")
        print(f"  • ماه‌های بقا: {data['months_survivable']:.1f} ماه")
        
        if data['months_survivable'] < data['months_until_income']:
            months_short = data['months_until_income'] - data['months_survivable']
            print(f"  ❌ خطر: {months_short:.1f} ماه زودتر پول تمام می‌شود!")
        else:
            print(f"  ✅ از نظر نقدینگی سالم هستید")
    else:
        print(f"  ✅ مازاد بودجه: {abs(data['cash_deficit']):,.0f} تومان")

def analyze_profitability(data):
    """تحلیل سوددهی"""
    print(f"\n📈 تحلیل سوددهی:")
    print(f"  • سود/زیان خالص: {data['net_profit']:,.0f} تومان")
    print(f"  • بازده سرمایه: {data['roi']:.1f}%")
    
    if data['net_profit'] > 0:
        print(f"  🎯 پروژه سودده است!")
        if data['roi'] > 100:
            print(f"  ✨ بازده عالی! (بیشتر از ۱۰۰٪)")
    else:
        print(f"  ⚠️ پروژه ضررده است")

def suggest_scenarios(data):
    """پیشنهاد سناریوهای بهبود"""
    print("\n" + "=" * 50)
    print("📈 تحلیل سناریوهای بهبود")
    print("=" * 50)
    
    if data['cash_deficit'] > 0 and data['months_survivable'] < data['months_until_income']:
        print(f"\n🔹 برای نجات پروژه:")
        
        # سناریو کاهش هزینه
        for reduction in [5, 10, 15, 20]:
            new_monthly = data['total_monthly_cost'] * (1 - reduction/100)
            new_survival = data['initial_cash'] / new_monthly
            deficit_saved = (data['total_monthly_cost'] - new_monthly) * data['months_until_income']
            
            print(f"\n   اگر {reduction}% هزینه کم کنید:")
            print(f"   • هزینه جدید: {new_monthly:,.0f} تومان")
            print(f"   • ماه‌های بقا: {new_survival:.1f} ماه")
            print(f"   • صرفه‌جویی: {deficit_saved:,.0f} تومان")
            
            if new_survival >= data['months_until_income']:
                print(f"   ✅ با این کاهش، پروژه نجات پیدا می‌کند!")
        
        # سناریو افزایش سرمایه
        print(f"\n🔹 یا با افزایش سرمایه:")
        needed_cash = data['cash_deficit']
        print(f"   • نیاز به: {needed_cash:,.0f} تومان سرمایه اضافی")
        print(f"   • یا ماهانه: {needed_cash/data['months_until_income']:,.0f} تومان")

def save_report(data):
    """ذخیره گزارش در فایل"""
    from datetime import datetime
    
    save = input("\n💾 آیا می‌خواهید گزارش را ذخیره کنید؟ (بله/خیر): ")
    if save.lower() == "بله":
        filename = input("📝 نام فایل (بدون پسوند): ") or "گزارش_تحلیل"
        filename = f"{filename}.txt"
        
        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"گزارش تحلیل بقای کسب‌وکار\n")
            f.write(f"تاریخ: {datetime.now().strftime('%Y/%m/%d %H:%M')}\n")
            f.write("=" * 50 + "\n")
            f.write(f"موجودی اولیه: {data['initial_cash']:,.0f} تومان\n")
            f.write(f"هزینه ماهانه: {data['total_monthly_cost']:,.0f} تومان\n")
            f.write(f"ماه‌های بقا: {data['months_survivable']:.1f} ماه\n")
            f.write(f"کسری بودجه: {data['cash_deficit']:,.0f} تومان\n")
            f.write(f"سود پیش‌بینی: {data['net_profit']:,.0f} تومان\n")
            f.write(f"بازده سرمایه: {data['roi']:.1f}%\n")
        
        print(f"✅ گزارش در '{filename}' ذخیره شد")
        print(f"📁 می‌توانید این فایل را به مشتری تحویل دهید")

def main():
    """تابع اصلی برنامه"""
    try:
        # دریافت اطلاعات
        data = get_financial_inputs()
        
        # محاسبات
        data = calculate_financials(data)
        
        # گزارش‌ها
        generate_basic_report(data)
        analyze_survival(data)
        analyze_profitability(data)
        
        # اگر مشکل وجود دارد، سناریوهای بهبود را نشان بده
        if data['cash_deficit'] > 0 and data['months_survivable'] < data['months_until_income']:
            suggest_scenarios(data)
        
        # ذخیره گزارش
        save_report(data)
        
        print("\n" + "=" * 50)
        print("🎉 تحلیل شما کامل شد!")
        print("💼 این سرویس را می‌توانید به دیگران ارائه دهید.")
        print("💰 قیمت پیشنهادی: ۵۰,۰۰۰ تا ۳۰۰,۰۰۰ تومان")
        print("=" * 50)
        
    except ValueError:
        print("\n❌ خطا: لطفاً فقط عدد وارد کنید!")
    except ZeroDivisionError:
        print("\n❌ خطا: هزینه ماهانه نمی‌تواند صفر باشد!")
    except Exception as e:
        print(f"\n❌ خطای ناشناخته: {e}")

# اجرای برنامه
if __name__ == "__main__":
    main()
