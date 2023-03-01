from mediapp import get_coordinator

words_data = []

# get coordinates only for alphabetes
alphabetes = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i in alphabetes:
    words_data.append({'url': f"/word/{i}/{i}-abc.mp4", 'title': i})

for word in words_data:
    get_coordinator(word)