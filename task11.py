import re
text="""
Hey! Contact me at person@example.com.  
The event was on 04/07/2025, and another one on July 4, 2025. 
Visit for more info... 
We also met on 2025-07-04. 
Call me!!!    Or not... 😅😅   
"""
x=re.findall("[0-9]+/[0-9]+/[0-9]+",text)
print(x)
clean_text=re.sub(r"[0-9]+[/-][0-9]+[-/][0-9]+","",text)
print(clean_text)
clean_text=re.sub(r"\b(?:jan|feb|mar|apr|may}jun|jul|aug|sep|oct|nov|dec)[a-z]* \d{1,2}, \d{4}\b","",clean_text,flags=re.I)
print(clean_text)
clean_text=re.sub(r"[a-zA-z0-9_%]+@[a-zA-Z-_.]+\.com","",clean_text)
print(clean_text)
clean_text=re.sub(r'[^\x00-\x7F]+',"",clean_text)
print(clean_text)
clean_text=re.sub(r'([.!?,])\1+', r'\1',clean_text)
print(clean_text)
clean_text=re.sub(r"\s+"," ",clean_text)
print(clean_text)
"""output:
    (base) PS C:\Users\shaim\Desktop\pythonlab> python task11.py
['04/07/2025']

Hey! Contact me at person@example.com.
The event was on , and another one on July 4, 2025.
Visit for more info...
We also met on .
Call me!!!    Or not... 😅😅


Hey! Contact me at person@example.com.
The event was on , and another one on .
Visit for more info...
We also met on .
Call me!!!    Or not... 😅😅


Hey! Contact me at .
The event was on , and another one on .
Visit for more info...
We also met on .
Call me!!!    Or not... 😅😅


Hey! Contact me at .
The event was on , and another one on .
Visit for more info...
We also met on .
Call me!!!    Or not...


Hey! Contact me at .
The event was on , and another one on .
Visit for more info.
We also met on .
Call me!    Or not.

 Hey! Contact me at . The event was on , and another one on . Visit for more info. We also met on . Call me! Or not.
(base) PS C:\Users\shaim\Desktop\pythonlab> 
"""