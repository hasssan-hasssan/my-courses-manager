DETAIL = "detail"

WELCOME_TO_MCM = "به MCM خوش آمدید . برای فعال سازی حساب خود در MCM باید آن را تایید کنید. مابرای شما یک ایمیل فعال سازی ارسال کردیم ، لطفا ایمیل خود را ا بررسی کنید. دقت کنید که زمان لینک فعال سازی محدود است ."
ACTIVATION_ACCOUNT = "فعال سازی حساب کاربری در MCM"
ACTIVATION_LINK = "برای فعال سازی حساب خود از لینک زیر استفاده کنید. مدت زمان این لینک محدود است."
def LINK(token):
    return f"http://127.0.0.1:8000/api/v1/users/verify/{str(token)}/"

ERR_SENT_EMAIL = "در ارسال ایمیل  فعال سازی حساب کاربری مشکلی بوجود آمد. لطفا دوباره امتحان کنید."
ACCOUNT_IS_EX_BUT_NOT_ACTIVE = "حساب کاربری با این ایمیل قبلا ثبت شده اما فعال نشده . لطفا ایمیل آن را بررسی کنید . ما برای شما یک ایمیل فعال سازی ارسال کردیم."
PLEASE_LOGIN = "حساب کاربری با این ایمیل قبلا ثبت شده و فعال هم است . لطفا وارد شوید. دقت کنید که از کلمه عبور جدید استفاده کنید."

ACTIVATOIN_SUCCESS = "تبریک! حساب شما هم اکنون فعال شد. میتوانید وارد شوید."
ACTIVATOIN_FAIL = "حساب کاربری شما فعال نشد. لطفا دوباره امتحان کنید."


# Course 
COURSES_NOT_EX_YET = "هنوز دوره ای ثبت نکرده اید."
COURSE_CREATE_SUCCESS = "دوره با موفقیت ایجاد شد."
COURSE_CREATE_FAIL = "در ثبت دوره مشکلی بوجود آمد. لطفا دوباره امتحان کنید."
