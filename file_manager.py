import os, shutil

#### file extentions dictionary
extention_dict = {
        'audio_extentions' :  ('.aac','.afi','.aiff','.mp3','.m4a','.wav'),
        'videos_extentions': ('.mp4','.mkv','.MKV','flv','.mpeg'),
        'document_extention' : ('.doc','.pdf','.txt','.docx','.ppt','.pptx'),
        'images_extiontions' : ('.jpg','.png','.gif','.jpeg'),
   }

####### Enter file path
folders_path = input('Enter folder path : ')

#### file finder functinality
def file_finder(folder_path,file_extention):
    files = []
    for file in os.listdir(folder_path):
        for extention in file_extention:
            if file.endswith(extention):
                files.append(file)

    return files

###### driver code
for file_name,extentions in extention_dict.items():
    given_files = file_finder(folders_path,extentions)
    if given_files :
        folder_name = file_name.split("_")[0]
        new_folder_path = os.path.join(folders_path,folder_name)
        try:
            os.mkdir(new_folder_path)
            for item in given_files:
                new_item_path = os.path.join(folders_path,item)
                shutil.move(new_item_path,new_folder_path)
        except:
            for item in given_files:
                new_item_path = os.path.join(folders_path,item)
                shutil.move(new_item_path,new_folder_path)
            

