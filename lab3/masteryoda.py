def master_yoda(text):
    txt_elements=text.split()
    ind=-1
    reverse=[]
    i=0
    while i < len(txt_elements):
        reverse.append(txt_elements[ind])
        ind=ind-1
        i+=1
    final=' '.join(reverse)
    return final
print(master_yoda('Qantar caused by is Government'))