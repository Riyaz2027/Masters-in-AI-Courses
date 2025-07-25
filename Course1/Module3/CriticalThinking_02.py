input_time=int(input('Enter the current time (in hours): '))
wait_alarm=int(input('Enter the alarm time to go off (in hours): '))
final_time=input_time + wait_alarm
rem_time=final_time % 24
print('Time will be on a 24-hour clock when the alarm goes off: ', rem_time, 'hours')



