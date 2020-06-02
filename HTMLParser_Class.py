class HTMLParser:

    def __init__(self,text):
        self.text = text

    def __str__(self):
        return(self.text)

    def tag_format(self,tag,clas = '',id=''):
        tags = []
        tags.append('<' + tag )
        tags.append('</' + tag)
        return tags

    def find_all(self,tag):
        tags = self.tag_format(tag)
        tag_indexs = self.tag_index(tags)
        contents_list = []
        for i in range(0,len(tag_indexs),2):
            contents_list.append(self.tag_contents(tag_indexs[i]+len(tag)+2,tag_indexs[i+1]))
        print(contents_list)

    def tag_index(self,tags):
        l1 = []
        index =0
        tags_index = 0
        length = len(self.text)
        while index < length:
            i = self.text.find(tags[tags_index],index)
            if i == -1:
                return l1
            else:
                l1.append(i)
                index = i+1
                tags_index = (tags_index * -1) + 1

        return l1

    def test_tag_index(self,tags,clas = '',id=''):
        index = []

        text = self.text


    def start_tag(self,text,index=0):
        tag_data = ''
        within_tag = False

        for i in range(index, len(text)):
            if within_tag == True:
                if text[i] == '>':
                    within_tag = False
                    return tag_data,i
                else:
                    tag_data += text[i]
            elif text[i] == '<':
                within_tag = True
        return tag_data,i

    def end_tag(self,text,index):
        tag_data = ''
        within_tag = False
        for i in range(index, len(text)):
            if within_tag == True:
                if text[i] == '>':
                    within_tag = False
                    return tag_data,i
                else:
                    tag_data += text[i]
            elif text[i] == '<' and text[i+1] == '/':
                within_tag = True

        return tag_data,i

    def tag_contents(self,start_index,end_index):
        content = ''
        for i in range(start_index,end_index):
            content += self.text[i]
        return content

    def tag_filter(self,tag_content,tag,type = 'none',filter = ''):
        if tag_content.find(tag)!= -1:
            if type == 'none':
                return True

            elif type == 'id':
                search_string = 'id="' + filter + '"'
                if tag_content.find(search_string)!= -1:
                    return True
                else: return False

            elif type == 'class':
                search_string = 'class="' + filter + '"'
                if tag_content.find(search_string) != -1:
                    return True
                else:
                    return False

        else: return False

    def find(self,tag,id='',clas='',i=0):
        index = []
        length = len(self.text)
        while i < length-1:
            tag_contents,i = self.start_tag(self.text,i)
            if self.tag_filter(tag_contents,tag) == True:
                if tag_contents == tag and id == '' and clas == '':
                    index.append(i+1)
                    break
                if id != '':
                    if self.tag_filter(tag_contents,tag,type = 'id',filter = id) == True:
                        index.append(i+1)
                        break
                elif clas != '':
                    if self.tag_filter(tag_contents,tag,type = 'class',filter = clas) == True:
                        index.append(i+1)
                        break
        while i < length-1:
            tag_contents,i = self.end_tag(self.text,i)
            if self.tag_filter(tag_contents,tag) == True:
                index.append(i-len(tag)-2)
                break
        try:
            data = self.tag_contents(index[0],index[1])
            return data,i
        except:
            return "No tag found",i


    def find_all(self,tag,id='',clas=''):
        data = []
        i=0
        length = len(self.text)
        while i < length-1:
            temp_data,i = self.find(tag,id,clas,i)
            if temp_data != "No tag found":
                data.append(temp_data)
        return data

    def clean(self,content):
        within_tag = False
        remove_indexs = []
        for i in range(0,len(content)):
            if content[i] ==  '<':
                remove_indexs.append(i)
                within_tag = True
            elif content[i] == '>':
                remove_indexs.append(i)
                within_tag = False
            elif within_tag == True:
                remove_indexs.append(i)

        remove_indexs = remove_indexs[::-1]
        content_list = list(content)
        for i in remove_indexs:
            content_list.pop(i)

        print("".join(content_list))


#text = 'bla bla <tag id="myTag"> this is the contents of the tag </tag>. <tag id="myTog"> this is the second tag attempt </tag> <tag class="myTog"> this is the third tag attempt </tag>'
#test = HTMLParser(text)

#tag = 'tag'
#tag_data = test.find(tag,id = 'myTog')
#print(test.tag_filter(tag_data,type = 'id',filter = 'myTag'))

