#!/usr/bin/env python3

import random as rand

responses = [
	"I'm flattered, but I am very happy where I am. Thank you!",
	"Thank you for reaching out. At this time, I am not interested in the position personally. However, if you would like I can certainly forward the position to any colleagues I think may be interested. At this time, I do not have anyone in mind specifically.",
	"Thanks for the info. Not interested in this position but please keep me in mind for others that might come your way.",
	"Thank you for reaching out regarding this opportunity. I am currently happy with my employment, but thank you again for considering me.",
	"Thank you for reaching out to me, I appreciate the inquiry. I would normally be very interested in exploring this particular opportunity further. However, I am currently happy with my role",
	"Thanks for reaching out to me. I am currently not in the market, but feel free to send me anything you think may be of interest. If I know someone who would be a good fit, I'll happily send them along to you.",
	"Thanks for the email. I appreciate the thought. I am very happy where I am, and I'll see if I know anyone who might be a fit for the role.",
	"I am not interested in making a move at this time.",
	"Thank you for thinking of me for this interesting position -- I truly appreciate it. However, I am very happy in my current job and do not have any plans to leave or relocate. I will gladly keep eyes and ears open for a candidate that might satisfy the requirements and skill set outlined in the position description.",
]


random_msg = responses[rand.randint(0, len(responses))] 

print("\n\n\n\n")
print(random_msg)
print("\n\n\n\n")
