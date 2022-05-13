# Strings
text = "X-DSPAM-Confidence:    0.8475";
a= text.find(':')
b= text.find('5')
c= text[a+1:b+1]

d= float(c.lstrip())

print(d)
