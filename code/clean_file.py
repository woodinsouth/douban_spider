# encoding=utf8
import os
import jieba 
import time

def process_file():
    i = 0 # for count the .txt 
    for  root, dirs, files in os.walk("/Users/caorunnan/Desktop/douban_spider/article"):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)

                '''
                i = i+1
                string = str(i)
                new_file_name = string + file_path[-4:]
                #print new_file_name

                os.rename(file_path, new_file_name)
                #print file
                '''
                print file
                #t_filename=file_path[-4:]+'_triple.txt'
                #tf=open(t_filename,'w')

                with open(file_path,'rw') as f:
                    text = f.read()
                    word_list = jieba.lcut(text)

                    # print(", ".join(word_list))

                    for index in range(len(word_list)):
                        word = word_list[index]
                        if word == u"的" or word == u"地" or word == u"得":
                            word_triple =  word_list[index-1] + word + word_list[index+1]
                            if word_list[index+1] == u"“" or word_list[index+1] == u"《":
                                word_triple =  word_triple + word_list[index+2] + word_list[index+3]
                            if word_list[index-1] == u"”" or word_list[index-1] == u"》":
                                word_triple =  word_list[index-3] + word_list[index-2] + word_triple              
        
                            print word_triple.encode('utf8')
                            #tf.write(word_triple.encode('utf8')+"\n")

                #tf.close()
                #time.sleep(10)

if __name__ == '__main__':
    process_file()