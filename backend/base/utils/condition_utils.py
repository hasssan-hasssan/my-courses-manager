def areLessonsRecordAndConfirm(course):
    # پیدا کردن درس هایی که تایید و یا ضبط نشده
    lessons = course.lesson_set.all()
    lesson_counter = 0
    for i in lessons:
        if i.isRecord == False or i.isConfirm == False:
            lesson_counter += 1
    if lesson_counter == 0:
        return True
    else:
        return False