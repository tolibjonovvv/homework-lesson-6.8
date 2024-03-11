from django.shortcuts import render
from django.utils.translation import gettext as _

def weekdays(request):
    weekdays_uz = [_('Dushanba'), _('Seshanba'), _('Chorshanba'), _('Payshanba'), _('Juma'), _('Shanba'), _('Yakshanba')]
    weekdays_en = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    weekdays_ru = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    lang = request.GET.get('lang', 'all')

    if lang == 'uz':
        weekdays = weekdays_uz
    elif lang == 'en':
        weekdays = weekdays_en
    elif lang == 'ru':
        weekdays = weekdays_ru
    else:
        weekdays = zip(weekdays_uz, weekdays_en, weekdays_ru)

    return render(request, 'weekdays/weekdays.html', {'weekdays': weekdays})

