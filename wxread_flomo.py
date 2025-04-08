import requests

URL = 'https://flomoapp.com/xxxx'  # 你的 flomo API 地址

if __name__ == "__main__":
    with open('wx_notes.txt', 'r') as f:
        wxread_notes = f.readlines()

    hashtag = '#读书笔记/' + wxread_notes[0].strip().replace(' ', '、') + '-' + wxread_notes[2].strip().replace(' ', '、')
    chapter = ''
    content = ''
    for i in range(5, len(wxread_notes)):
        # skip empty lines
        if not wxread_notes[i].strip():
            continue
        # stop at the end
        if wxread_notes[i].__contains__('- 来自微信读书'):
            break
        # chapter title
        if (not wxread_notes[i].startswith('◆') and wxread_notes[i].strip() and not wxread_notes[i - 1].strip() and
                not wxread_notes[i - 2].startswith('◆') and not wxread_notes[i - 2].__contains__('发表想法') and not
                wxread_notes[i - 4].startswith('◆') and not wxread_notes[i - 4].__contains__('发表想法')):
            chapter = wxread_notes[i].strip()
        # content
        else:
            if wxread_notes[i].startswith('◆') and wxread_notes[i].__contains__('发表想法'):
                content += wxread_notes[i].replace('◆', '').strip()
                continue
            if wxread_notes[i - 2].startswith('◆') and wxread_notes[i - 2].__contains__('发表想法'):
                content += ('\n' + (wxread_notes[i].replace('◆', '').strip() + '\n--------------------------------'))
                continue
            if not content:
                content += wxread_notes[i].replace('◆', '').strip()
            else:
                content += '\n' + wxread_notes[i].replace('◆', '').strip()
            if i == len(wxread_notes) - 1 or not wxread_notes[i + 1].strip():
                headers = {
                    'Content-type': 'application/json',
                    }
                data = {
                    'content': f'{hashtag}\n\n{content}\n\n{chapter}'
                    }
                print(f'{hashtag}\n\n{content}\n\n{chapter}')
                response = requests.post(URL, headers=headers, json=data)
                print(response.json())
                if response.json()['code'] == -1 and response.json()[
                    'message'] == '每日通过 API 最多记录 100 条，贪多嚼不烂。':
                    break
                content = ''
            else:
                continue
