from pathlib import Path
import re
import logging
import os
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login as auth_login, get_user_model, logout as auth_logout
from django.shortcuts import render, redirect
from vvouch import forms
from django.core.mail import send_mail
from django.conf import settings
from main.utils import generate_activation_key
from vvouch.models import Activation, Products, ProductImages
from django.core.exceptions import FieldDoesNotExist, ObjectDoesNotExist
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.db import connection
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
import json
import shutil
from django.conf import settings
from django.conf.urls.static import static
# from django.core.urlresolvers import reverse

SHA1_RE = re.compile('^[a-f0-9]{40}$')
logger = logging.getLogger('django')


@login_required
def index(request):
    path = settings.FILE_ROOT + '/data.json'
    f = open(path, )
    jsonData = json.load(f)
    f.close()
    finalCategory = []
    finalSubCategory = []
    if jsonData:
        for categories in jsonData['categories']:
            if categories['title']:
                categoryObject = {}
                categoryObject['category_title'] = categories['title']
                finalCategory.append(categoryObject)
                if 'subcategories' in categories:
                    for subcategory in categories['subcategories']:
                        subCategoryObject = {}
                        subCategoryObject['subcategory_title'] = subcategory['title']
                        finalSubCategory.append(subCategoryObject)

    return render(request, 'vvouch/index.html', {'categories': jsonData['categories'], "finalCategory": finalCategory, "finalSubCategory": finalSubCategory})

@login_required
def get_subcategory(request):
    data = {}
    path = settings.FILE_ROOT + '/data.json'
    f = open(path, )
    jsonData = json.load(f)
    f.close()
    finalCategory = []
    finalSubCategory = []
    if jsonData:
        for categories in jsonData['categories']:
            if categories['title'] == request.POST['category_title']:
                if 'subcategories' in categories:
                    for subcategory in categories['subcategories']:
                        subCategoryObject = {}
                        subCategoryObject['subcategory_title'] = subcategory['title']
                        finalSubCategory.append(subCategoryObject)

    data['success'] = 1
    data['data'] = finalSubCategory

    return JsonResponse(data)

def add_archivo(request):
    data = {}
    if request.method == 'POST':
        files = request.FILES.getlist('files')
        files_list_length = len(files)
        for f in range(files_list_length):
            handle_uploaded_file(files[f], str(files[f]), request)

        data["success"] = 1
    return JsonResponse(data)

def handle_uploaded_file(file, filename, request):
    filename= filename.replace(' ', '_').replace('#', '')
    if request.POST['category'] and request.POST['subcategory']:
        with open(settings.CATEGORY_ROOT + "/" + request.POST['category'] + "/" + request.POST['subcategory'] + "/" + filename, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
    else:
        with open(settings.CATEGORY_ROOT + "/" + request.POST['category'] + "/" + filename, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
    path = settings.FILE_ROOT + '/data.json'
    write_archivo_json(request, path, filename)


@login_required
def handle_dragged_file(request):
    category = request.POST.get('category')
    subcategory = request.POST.get('subcategory')
    filename = request.POST.get('filename')
    json_path = settings.FILE_ROOT + '/data.json'

    if category and subcategory:
        destination_path = settings.CATEGORY_ROOT + "/" + category + "/" + subcategory + "/" + filename
    elif category:
        destination_path = settings.CATEGORY_ROOT + "/" + category + "/" + filename
    for root, _, files in os.walk(settings.CATEGORY_ROOT):
        if filename in files:
            current_path = os.path.join(root, filename)
            delete_dragged_archivo_json(request, json_path, current_path, filename)
            file_exists = os.path.exists(destination_path)
            if not file_exists:
                shutil.move(current_path, destination_path)
                break
                
    write_dragged_archivo_json(request, json_path, filename)
    return JsonResponse({'message': 'Done'})

def delete_dragged_archivo_json(new_data, filename, current_path, fileName):
    
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        for categories in file_data['categories']:
            parent_directory = os.path.basename(os.path.dirname(current_path))
            parent_parent_directory = os.path.basename(os.path.dirname(os.path.dirname(current_path)))
            if parent_parent_directory == "categories":
                if categories['title'] == parent_directory:
                    if "files" in categories:
                        categories['files'] = [f for f in categories['files'] if not (f['file'] == fileName)]
            else:
                if categories['title'] == parent_parent_directory:
                    if "subcategories" in categories:
                            for subcategories in categories['subcategories']:
                                if subcategories['title'] == parent_directory:
                                    if "files" in subcategories:
                                        subcategories['files'] = [f for f in subcategories['files'] if not (f['file'] == fileName)]

        file.truncate(0)
        file.seek(0)
        json.dump(file_data, file, indent = 4)
        file.close()


def write_dragged_archivo_json(new_data, filename, fileName):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        if 'category' in new_data.POST and 'subcategory' in new_data.POST:
            for categories in file_data['categories']:
                    if categories['title'] == new_data.POST['category']:
                        if "subcategories" in categories:
                            for subcategories in categories['subcategories']:
                                if subcategories['title'] == new_data.POST['subcategory']:
                                    if "files" in subcategories:
                                        subcategories['files'].append({"title": "{}".format(fileName.split(".")[0]),"file": "{}".format(fileName)})
                                    else:
                                        subcategories.update({"files": []})
                                        subcategories['files'].append({"title": "{}".format(fileName.split(".")[0]),"file": "{}".format(fileName)})
            
        elif 'category' in new_data.POST:
            for categories in file_data['categories']:
                if categories['title'] == new_data.POST['category']:
                    if "files" in categories:
                        categories['files'].append({"title": "{}".format(fileName.split(".")[0]), "file": "{}".format(fileName)})
                    else:
                        categories.update({"files": []})
                        categories['files'].append({"title": "{}".format(fileName.split(".")[0]), "file": "{}".format(fileName)})
        
        file.truncate(0)
        file.seek(0)
        json.dump(file_data, file, indent = 4)
        file.close()

def write_archivo_json(new_data, filename, fileName):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        if new_data.POST['category'] and new_data.POST['subcategory']:
                for categories in file_data['categories']:
                    if categories['title'] == new_data.POST['category']:
                        if "subcategories" in categories:
                            for subcategories in categories['subcategories']:
                                if subcategories['title'] == new_data.POST['subcategory']:
                                    if "files" in subcategories:
                                        subcategories['files'].append({"title": "{}".format(fileName.split(".")[0]),"file": "{}".format(fileName)})
                                    else:
                                        subcategories.update({"files": []})
                                        subcategories['files'].append({"title": "{}".format(fileName.split(".")[0]),"file": "{}".format(fileName)})
        else:
            for categories in file_data['categories']:
                if categories['title'] == new_data.POST['category']:
                    if "files" in categories:
                        categories['files'].append({"title": "{}".format(fileName.split(".")[0]), "file": "{}".format(fileName)})
                    else:
                        categories.update({"files": []})
                        categories['files'].append({"title": "{}".format(fileName.split(".")[0]), "file": "{}".format(fileName)})
        file.truncate(0)
        file.seek(0)
        json.dump(file_data, file, indent = 4)
        file.close()


@login_required
def add_category(request):
    data = {}
    if request.method == 'POST':
        try:
            path = settings.FILE_ROOT + '/data.json'
            f = open(path,)
            jsonData = json.load(f)
            for categories in jsonData['categories']:
                if categories['title'] == request.POST['category_title']:
                    data['error'] = 2

            if 2 not in data:
                write_json(request, path)
                directory = request.POST['category_title']
                parent_dir = settings.CATEGORY_ROOT
                path = os.path.join(parent_dir, directory)
                os.mkdir(path)
                f.close()

                data['success'] = 1
        except Exception as e:
            data['error'] = 1
            logger.exception(e)
    else:
        data['error'] = 1

    return JsonResponse(data)


def write_json(new_data, filename):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        file_data['categories'].append({"title":  "{}".format(new_data.POST['category_title']), "permissions":  json.loads(new_data.POST['permissions'])})
        file.seek(0)
        json.dump(file_data, file, indent = 4)


@login_required
def edit_category(request):
    data = {}
    if request.method == 'POST':
        try:
            path = settings.FILE_ROOT + '/data.json'
            write_edit_category_json(request, path)
            try:
                old_directory = request.POST['old_title']
                directory = request.POST['category_title']
                parent_dir = settings.CATEGORY_ROOT
                #     path = os.path.join(parent_dir, directory)
                os.rename(parent_dir + "/" + old_directory, parent_dir + "/" + directory)
                data["success"] = 1
            except OSError as error:
                directory = request.POST['category_title']
                parent_dir = settings.CATEGORY_ROOT
                path = os.path.join(parent_dir, directory)
                os.mkdir(path)
                print(error)
                data["success"]=1
        except Exception as e:
            data['error'] = 1
            logger.exception(e)
    else:
        data['error'] = 1

    return JsonResponse(data)


def write_edit_category_json(request, filename):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        count = 0
        for categories in file_data['categories']:
            count += 1
            print(categories['title'])
            # print(request.POST['old_title'])
            if categories['title'] == request.POST['old_title']:
                file_data['categories'][count-1]['title'] = categories['title'].replace(categories['title'], request.POST['category_title'])
                file_data['categories'][count-1]['permissions'] = json.loads(request.POST['permissions'])
        
        file.truncate(0)
        file.seek(0)
        json.dump(file_data, file, indent = 4)
        file.close()


@login_required
def edit_subcategory(request):
    data = {}
    if request.method == 'POST':
        try:
            path = settings.FILE_ROOT + '/data.json'
            old_subcategory_title = request.POST['old_subcategory_title']
            subcategory_title = request.POST['subcategory_title']
            old_category_title = request.POST['old_category_title']
            category_title = request.POST['category_title']
            if old_subcategory_title == subcategory_title and category_title == old_category_title:
                data['error']=2
            else:
                write_edit_subcategory_json(request, path)

                try:
                    parent_dir = settings.CATEGORY_ROOT
                    if subcategory_title != old_subcategory_title:
                        os.rename(parent_dir + "/" +  category_title + "/" + old_subcategory_title, parent_dir + "/" +  category_title + "/" + subcategory_title)

                    source = parent_dir + "/" + old_category_title + "/" + subcategory_title
                    destination =  parent_dir + "/" + category_title + "/" + subcategory_title
                    dest = shutil.move(source, destination)
                    data["success"] = 1
                except OSError as error:
                    directory = parent_dir + "/" + category_title + "/" + subcategory_title
                    parent_dir = settings.CATEGORY_ROOT
                    path = os.path.join(parent_dir, directory)
                    os.mkdir(path)
                    data["success"]=1
        except Exception as e:
            data['error'] = 1
            logger.exception(e)
    else:
        data['error'] = 1

    return JsonResponse(data)


@login_required
def write_edit_subcategory_json(request, filename):
    old_subcategory_title = request.POST['old_subcategory_title']
    subcategory_title = request.POST['subcategory_title']
    old_category_title = request.POST['old_category_title']
    category_title = request.POST['category_title']
    permissions = json.loads(request.POST['permissions'])
    with open(filename,'r+') as file:
        file_data = json.load(file)
        count = 0
        count2 = 0
        count3 = 0
        count4 = 0

    # adding edit permissions
        spec_count = 0
        spec_count_1 = 0
        for categories in file_data['categories']:
            spec_count += 1
            if(categories['title'] == old_category_title):
                for subcates in file_data['categories'][spec_count-1]['subcategories']:
                    spec_count_1 += 1
                    if(subcates['title'] == old_subcategory_title):
                        for x in permissions:
                            if x not in file_data['categories'][spec_count-1]['subcategories'][spec_count_1-1]['permissions']:
                                file_data['categories'][spec_count-1]['subcategories'][spec_count_1-1]['permissions'].append(x)

        for categories in file_data['categories']:
            if (categories['title'] == old_category_title):
                count3 += 1
            count += 1

            if categories['title'] == category_title and category_title == old_category_title and subcategory_title != old_subcategory_title:
                for subcategories in categories['subcategories']:
                    count2 += 1
                    if( file_data['categories'][count - 1]['subcategories'][count2 - 1]['title'] == old_subcategory_title ):
                        file_data['categories'][count - 1]['subcategories'][count2 - 1]['title'] = subcategories[
                                'title'].replace(subcategories['title'], subcategory_title)
                        break
                print( "Only SubCategory" )
                break
            elif categories['title'] == category_title and category_title != old_category_title and subcategory_title == old_subcategory_title:
                print(file_data)

                for nsubcate in file_data['categories'][count3 - 1]['subcategories']:
                    count4 += 1
                    if nsubcate['title'] == subcategory_title:
                        file_data['categories'][count - 1]['subcategories'].append( nsubcate )
                        break
                file_data['categories'][count3 - 1]['subcategories'].pop(count4-1)
                break
            elif categories[
                'title'] == category_title and category_title != old_category_title and subcategory_title != old_subcategory_title:

                for nsubcate in file_data['categories'][count3 - 1]['subcategories']:
                    count4 += 1
                    file_data['categories'][count - 1]['subcategories'].append(nsubcate)
                    file_data['categories'][count3 - 1]['subcategories'].pop(count4 - 1)

                for subcategories in categories['subcategories']:
                    count2 += 1
                    if (file_data['categories'][count - 1]['subcategories'][count2 - 1][
                        'title'] == old_subcategory_title):
                        print(subcategory_title)
                        file_data['categories'][count - 1]['subcategories'][count2 - 1]['title'] = subcategories[
                            'title'].replace(subcategories['title'], subcategory_title)
                break
        file.truncate(0)
        file.seek(0)
        json.dump(file_data, file, indent = 4)
        file.close()


@login_required
def edit_archivo(request):
    data = {}
    if request.method == 'POST':
        files = request.FILES.getlist('files')
        files_list_length = len(files)
        for f in range(files_list_length):
            handle_edit_uploaded_file(files[f], str(files[f]), request)

    data["success"] = 1
    return JsonResponse(data)


@login_required
def handle_edit_uploaded_file(file, filename, request):
    filename= filename.replace(' ', '_').replace('#', '')
    if request.POST['category'] and request.POST['subcategory']:
        with open(settings.CATEGORY_ROOT + "/" + request.POST['category'] + "/" + request.POST['subcategory'] + "/" + filename, 'wb+') as destination:
            try:
                for chunk in file.chunks():
                    destination.write(chunk)
                    print(destination)
            except chunk as error:
                print(error)
        path = settings.FILE_ROOT + '/data.json'
        edit_archivo_json(request, path, filename)


@login_required
def edit_archivo_json(new_data, filename, fileName):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        count=0
        count1=0
        count2=0
        if new_data.POST['category'] and new_data.POST['subcategory']:
                for categories in file_data['categories']:
                    count+=1
                    if categories['title'] == new_data.POST['category']:
                        if "subcategories" in categories:
                            for subcategories in categories['subcategories']:
                                count1+=1
                                if subcategories['title'] == new_data.POST['subcategory']:
                                    if "files" in subcategories:
                                        for files in subcategories['files']:
                                            count2+1
                                            if files['file'] == new_data.POST['old_file']:
                                                file_data['categories'][count-1]['subcategories'][count1-1]['files'][count2+1]['title'] = fileName.split(".")[0]
                                                file_data['categories'][count - 1]['subcategories'][count1 - 1][
                                                    'files'][count2+1]['file'] = fileName
                                                break

        file.truncate(0)                                            
        file.seek(0)
        json.dump(file_data, file, indent = 4)
        file.close()


@login_required
def edit_archivo_category_files(request):
    data = {}
    if request.method == 'POST':
        files = request.FILES.getlist('files')
        files_list_length = len(files)
        for f in range(files_list_length):
            handle_edit_cat_uploaded_file(files[f], str(files[f]), request)

    data["success"] = 1
    return JsonResponse(data)


@login_required
def handle_edit_cat_uploaded_file(file, filename, request):
    filename= filename.replace(' ', '_').replace('#', '')
    if request.POST['categoryfiles']:
        with open(settings.CATEGORY_ROOT + "/" + request.POST['categoryfiles'] + "/" + filename, 'wb+') as destination:
            try:
                for chunk in file.chunks():
                    destination.write(chunk)
                    print(destination)
            except chunk as error:
                print(error)
        path = settings.FILE_ROOT + '/data.json'
        edit_archivo_json(request, path, filename)

def edit_archivo_json(new_data, filename, fileName):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        count=0
        count2=0
        if new_data.POST['categoryfiles']:
                for categories in file_data['categories']:
                    count += 1
                    if new_data.POST['categoryfiles'] == categories['title']:
                        if "files" in categories:
                            for files in categories['files']:
                                count2+1
                                if files['file'] == new_data.POST['old_cat_file']:
                                    file_data['categories'][count-1]['files'][count2+1]['title'] = fileName.split(".")[0]
                                    file_data['categories'][count - 1]['files'][count2+1]['file'] = fileName
                                    break

        file.truncate(0)                            
        file.seek(0)
        json.dump(file_data, file, indent = 4)
        file.close()

@login_required
def edit_dragged_archivo_json(new_data, filename, fileName):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        count=0
        count2=0
        if new_data.POST['categoryfiles']:
                for categories in file_data['categories']:
                    count += 1
                    if new_data.POST['categoryfiles'] == categories['title']:
                        if "files" in categories:
                            for files in categories['files']:
                                count2+1
                                if files['file'] == new_data.POST['old_cat_file']:
                                    file_data['categories'][count-1]['files'][count2+1]['title'] = fileName.split(".")[0]
                                    file_data['categories'][count - 1]['files'][count2+1]['file'] = fileName
                                    break

        file.truncate(0)                            
        file.seek(0)
        json.dump(file_data, file, indent = 4)
        file.close()



@login_required
def add_subcategory(request):
    success = ''
    data = {}
    if request.method == 'POST':
        try:
            path = settings.FILE_ROOT + '/data.json'
            f = open(path,)
            jsonData = json.load(f)
            for categories in jsonData['categories']:
                if categories['title'] == request.POST['category']:
                    write_subcategory_json(request, path)
            f.close()
            data['success'] = 1
        except Exception as e:
            data['error'] = 1
            logger.exception(e)
    else:
        data['error'] = 1
    return JsonResponse(data)


def write_subcategory_json(new_data, filename):
    with open(filename,'r+') as file:
        file_data = json.load(file)
        for categories in file_data['categories']:
            if categories['title'] == new_data.POST['category']:
                if "subcategories" in categories:
                      categories['subcategories'].append({"title": "{}".format(new_data.POST['subcategory_title']), "permissions":  json.loads(new_data.POST['permissions'])})
                else:
                    categories.update({"subcategories": []})
                    categories['subcategories'].append({"title": "{}".format(new_data.POST['subcategory_title']), "permissions":  json.loads(new_data.POST['permissions'])})
                  
        file.seek(0)
        json.dump(file_data, file, indent = 4)
        directory = new_data.POST['subcategory_title']
        parent_dir = settings.CATEGORY_ROOT + "/" + new_data.POST['category']
        path = os.path.join(parent_dir, directory)
        os.mkdir(path)

@login_required
def delete_category(request):
    success = ''
    data = {}
    if request.method == 'POST':
        try:
            path = settings.FILE_ROOT + '/data.json'
            FolderToBeDeleted = settings.CATEGORY_ROOT + '/' + request.POST['category_title']
            f = open(path,)
            jsonData = json.load(f)
            for categories in jsonData['categories']:
                if categories['title'] == request.POST['category_title']:
                    delete_category_json(request, path)
            f.close()
            if os.path.exists(FolderToBeDeleted):
                shutil.rmtree(FolderToBeDeleted)
            else:
                logging.warning("Error while deleting the folder")
            data['success'] = 1
        except Exception as e:
            data['error'] = 1
            logger.exception(e)
    else:
        data['error'] = 1
    return JsonResponse(data)


@login_required
def delete_category_json(request, filename):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        count=0
        if request.POST['category_title']:
                for categories in file_data['categories']:
                    count += 1
                    if request.POST['category_title'] == categories['title']:
                        file_data['categories'].pop(count - 1)
                        break

        file.truncate(0)                
        file.seek(0)
        json.dump(file_data, file, indent = 4)
        file.close()


@login_required
def delete_subcategory(request):
    success = ''
    data = {}
    if request.method == 'POST':
        try:
            path = settings.FILE_ROOT + '/data.json'
            pathToBeDeleted = settings.CATEGORY_ROOT + '/' + request.POST['category_title'] + '/' + request.POST['subcategory_title'] 
            f = open(path,)
            jsonData = json.load(f)
            for categories in jsonData['categories']:
                if categories['title'] == request.POST['category_title']:
                    delete_subcategory_json(request, path)
            f.close()

            if os.path.exists(pathToBeDeleted):
                shutil.rmtree(pathToBeDeleted)
            else:
                logging.warning("Issue while delete the folder")
            data['success'] = 1
        except Exception as e:
            data['error'] = 1
            logger.exception(e)
    else:
        data['error'] = 1
    return JsonResponse(data)


@login_required
def delete_subcategory_json(request, filename):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        count=0
        count1 = 0
        if request.POST['category_title']:
                for categories in file_data['categories']:
                    count += 1
                    if request.POST['category_title'] == categories['title']:
                        if "subcategories" in categories:
                            for subcategories in categories['subcategories']:
                                count1 += 1
                                if request.POST['subcategory_title'] == subcategories['title']:
                                    file_data['categories'][count-1]['subcategories'].pop(count1 - 1)
                                    break

        file.truncate(0)                                
        file.seek(0)
        json.dump(file_data, file, indent = 4)
        file.close()



@login_required
def delete_category_files(request):
    success = ''
    data = {}
    if request.method == 'POST':
        try:
            path = settings.FILE_ROOT + '/data.json'
            deleteFilePath = settings.CATEGORY_ROOT + '/' + request.POST['category_title'] + '/' + request.POST['category_file_name']
            f = open(path,)
            jsonData = json.load(f)
            for categories in jsonData['categories']:
                if categories['title'] == request.POST['category_title']:
                    delete_category_files_json(request, path)
            
            if os.path.exists(deleteFilePath):
                os.remove(deleteFilePath)
            else:
                logging.warning("File not removed")

            f.close()
            data['success'] = 1
        except Exception as e:
            data['error'] = 1
            logger.exception(e)
    else:
        data['error'] = 1
    return JsonResponse(data)


@login_required
def delete_category_files_json(request, filename):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        count=0
        count1 = 0
        if request.POST['category_title']:
                for categories in file_data['categories']:
                    count += 1
                    if request.POST['category_title'] == categories['title']:
                        if "files" in categories:
                            for files in categories['files']:
                                count1 += 1
                                if request.POST['category_file_name'] == files['file']:
                                    file_data['categories'][count-1]['files'].pop(count1 - 1)
        file.truncate(0)
        file.seek(0)
        json.dump(file_data, file, indent = 4)
        file.close()


@login_required
def delete_subcategory_files(request):
    success = ''
    data = {}
    if request.method == 'POST':
        try:
            path = settings.FILE_ROOT + '/data.json'
            deleteFilePath = settings.CATEGORY_ROOT + '/' + request.POST['category_title'] + '/' + request.POST['subcategory_title'] + '/' + request.POST['subcategory_file_name']
            f = open(path,)
            jsonData = json.load(f)
            for categories in jsonData['categories']:
                if categories['title'] == request.POST['category_title']:
                    delete_subcategory_files_json(request, path)
            f.close()
            
            if os.path.exists(deleteFilePath):
                os.remove(deleteFilePath)
            else:
                logging.warning("File not Exits")
                logging.warning(deleteFilePath)

            data['success'] = 1
        except Exception as e:
            data['error'] = 1
            logger.exception(e)
    else:
        data['error'] = 1
    return JsonResponse(data)


@login_required
def delete_subcategory_files_json(request, filename):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        count=0
        count1 = 0
        count2 = 0
        if request.POST['category_title']:
                for categories in file_data['categories']:
                    count += 1
                    if request.POST['category_title'] == categories['title']:
                        if 'subcategories' in categories:
                            for subcategories in categories['subcategories']:
                                count1 += 1
                                if request.POST['subcategory_title'] == subcategories['title']:
                                    if "files" in subcategories:
                                        for files in subcategories['files']:
                                            count2 += 1
                                            if request.POST['subcategory_file_name'] == files['file']:
                                                index = count2-1
                                                file_data['categories'][count-1]['subcategories'][count1-1]['files'].pop(index)
        file.truncate(0)
        file.seek(0)
        json.dump(file_data, file, indent=4)
        file.close()


@login_required
def get_subcategory_permission(request):
    packet = {}
    path = settings.FILE_ROOT + '/data.json'
    with open(path, 'r+') as file:
        file_data = json.load(file)
        count=0
        if request.POST['category_title']:
                for categories in file_data['categories']:
                    count += 1
                    if request.POST['category_title'] == categories['title']:
                       packet['data'] = file_data['categories'][count-1]['permissions'] 
                       return JsonResponse(packet)
        
        packet['success'] = 1
        file.close()        
        return JsonResponse(packet)

@login_required
def get_edit_subcategory_permission(request):
    packet={}
    path = settings.FILE_ROOT + '/data.json'
    with open(path, 'r+') as file:
        file_data = json.load(file)

        if request.POST['category_title']:
            for categories in file_data['categories']:
                if request.POST['category_title'] == categories['title']:
                    logging.warning(request.POST['category_title'])
                    if 'subcategories' in categories:
                        for subcategories in categories['subcategories']:
                            if subcategories['title'] == request.POST['subcategories_title']:
                                logging.warning(request.POST['subcategories_title'])
                                packet['data'] = subcategories['permissions']
                                return JsonResponse(packet)
    packet['success'] = 1
    file.close()        
    return JsonResponse(packet)
        
def data_json(request):
    path = settings.FILE_ROOT + '/data.json'
    with open(path, 'r+') as file:
        file_data = json.load(file)
        return JsonResponse(file_data)


@login_required
def edit_permissions_in_subcategories(request):
    packet={}
    path = settings.FILE_ROOT + '/data.json'
    with open(path, 'r+') as file:
        file_data = json.load(file)
        count=0
        count1=0
        if request.POST['category_title']:
            for categories in file_data['categories']:
                count=+1
                if request.POST['category_title'] == categories['title']:
                    cat = file_data['categories'][count-1]
                    if 'subcategories' in cat:
                        for subcategories in cat['subcategories']:
                            count1+=1
                            if subcategories['title'] == request.POST['subcategories_title']:
                                packet['data'] = cat['subcategories'][count1-1]['permissions']
                                logging.warning(packet)
                                file_data['categories'][count-1]['subcategories'][count1-1]['permissions'] = request.POST['editable_permissions']
    packet['data'] = 1
    return JsonResponse(packet)

    file.close()