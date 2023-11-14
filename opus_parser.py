from bs4 import BeautifulSoup as bs

filename = 'en-ko.tmx'
src, tgt = filename.split('.')[0].split('-')

with open(filename, 'r', encoding='utf-8') as file:
    tmx_data = file.read()

soup = bs(tmx_data, 'lxml-xml')

def clense_sentence(s):
    tmp = s.replace("\r\n", " ")
    tmp = tmp.replace("\n", " ")
    while "  " in tmp:
        tmp.replace("  ", " ")
    return tmp


with open (f'{src}.{src}', 'a', encoding='utf-8') as src_out,\
    open(f'{tgt}.{tgt}', 'a', encoding='utf-8') as tgt_out:
        
    for tu in soup.find_all('tu'):
        source_text = clense_sentence(tu.find('tuv', {'xml:lang': f'{src}'}).find('seg').text)
        target_text = clense_sentence(tu.find('tuv', {'xml:lang': f'{tgt}'}).find('seg').text)
        print(f"Source: {source_text}, Target: {target_text}")
        
        src_out.write(source_text+"\n")
        tgt_out.write(target_text+"\n")