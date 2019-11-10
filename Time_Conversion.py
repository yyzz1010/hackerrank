import re 

s = input()
regex_match = re.match('(\d+)(\:\d+\:\d+)', s)
hour = regex_match.group(1)
if re.search('AM', s):
    if hour == '12':
        hour = '00'
    else:
        hour = hour
else:
    if hour == '12':
        hour = hour
    else:
        hour = int(regex_match.group(1)) + 12
print(str(hour) + regex_match.group(2))
