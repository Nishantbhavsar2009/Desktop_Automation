import os

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folderName, files):
    for file in files:
        os.replace(file, f'{folderName}/{file}')
files = os.listdir()
files.remove('main.py')
#print(files)
createIfNotExist('Images')
createIfNotExist('Docs')
createIfNotExist('Media')
createIfNotExist('Apps')
createIfNotExist('Programs')
createIfNotExist('Others')

imgExts = ['.png', '.jpeg', '.jpg', '.gif']
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts]
#print(images)

docExts = ['.docx', '.txt', '.ppt', '.doc', '.pdf', '.xls', '.xlsx', '.pptx', '.odt']
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]
#print(docs)

mediaExts = ['.mp4', '.flv', '.mp3']
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]
#print(media)

appsExts = ['.dmg']
apps = [file for file in files if os.path.splitext(file)[1].lower() in appsExts]
#print(apps)

programExts = ['.py', '.html', '.css', '.js', '.php']
programs = [file for file in files if os.path.splitext(file)[1].lower() in programExts]
#print(programs)

others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in mediaExts) and (ext not in docExts) and (ext not in programExts) and (ext not in appsExts) and os.path.isfile(file):
        others.append(file)

print(others)

for media in medias:
    os.replace(media, f'Media/{media}')

for image in images:
    os.replace(image, f'Images/{image}')

for doc in docs:
    os.replace(doc, f'Docs/{doc}')

for app in apps:
    os.replace(app, f'Apps/{app}')

for program in programs:
    os.replace(program, f'Programs/{program}')

for other in others:
    os.replace(other, f'Others/{others}')
#move('Image', images)
