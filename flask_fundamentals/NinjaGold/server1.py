def processmoney():

    if request.form.get('action') == "farm":
        earnings = random.randrange(10, 20)
        session['gold'] += earnings
        session['activities'].append(
            'Earned ' + str(earnings) + ' gold from the farm! (' +
            '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
        )
    elif request.form.get('action') == "cave":
        earnings = random.randrange(5, 10)
        session['gold'] += earnings
        session['activities'].append(
            'Earned ' + str(earnings) + ' gold from the cave! (' +
            '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
        )
    elif request.form.get('action') == "house":
        earnings = random.randrange(2, 5)
        session['gold'] += earnings
        session['activities'].append(
            'Earned ' + str(earnings) + ' gold from the house! (' +
            '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
        )
    elif request.form.get('action') == "casino":
        earnings = random.randrange(-50, 50)
        session['gold'] += earnings
        if earnings > 0:
            session['activities'].append(
                'Entered a casino and Won ' + str(earnings) + ' gold! Ouch! (' +
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
            )
        else:
            session['activities'].append(
                'Entered a casino and Lost ' + str(earnings) + ' gold. Holy Cow! (' +
                '{:%Y/%m/%d %I:%M %p})'.format(datetime.datetime.now())
            )
    return redirect('/')