import random 

when = ["20th January", " Tomorrow", 'Yesterday','the day before', " Day after tomorrow", 'Previous night']
who = ["rabbit ", " turtle ", 'pig ','snake ', " duck ", 'monkey ']
name = [" harsh", " hrishita", ' hiya',' daksh', " rajnish", ' anjali']
residence = ["India ", " Pakistan ", 'Venezuela ','Spain ', " Portugal ", 'Nepal ']
went = ["laundry ", " unniversity " , 'abroad ','to the lake ', " park ", 'cinema ']
happend = ["made alot of friends ", " got an ice ream ", 'played with a toy ', 'saw a dog ', " ate a goldfish ", 'solved a mystery ' ]
print(random.choice(when) + ', ' + random.choice(who) + 'named ' + random.choice(name) + ' that lived in ' + random.choice(residence)
        + 'went to the ' + random.choice(went) + 'and' + random.choice(happend) + ".")