ipAddress = input("Please enter an IP Address : ")
if len(ipAddress) > 0 and ipAddress[-1] != '.':
    ipAddress += '.'

segment = 1
segment_length = 0
character = ""

for character in ipAddress:
    if character == ".":
        print("Segment {} has {} length".format(segment, segment_length))
        segment += 1
        segment_length = 0
    else:
        segment_length += 1

if character != ".":
    print("Segment {} has {} length".format(segment, segment_length))