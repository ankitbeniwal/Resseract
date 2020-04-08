from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import ResumeReader.core.reader as reader
import os, ResumeReader


def home(request):
    error = ''
    parsed = 0
    if request.method == 'POST' and request.FILES['newDoc']:
        newDoc = request.FILES['newDoc']
        fs = FileSystemStorage()
        newDocName = fs.save(newDoc.name, newDoc)
        location = os.path.abspath(ResumeReader.__path__[0]) + '/..'
        uploaded_file_url = location + fs.url(newDocName)
        reader.preprocess
        name, email, phone, linkedinUrl, lineCount, charCount, pageCount, fonts, fontSizes, tableCount, imageCount, data, error = reader.readDetails(uploaded_file_url)
        csvLink, xlsxLink = reader.generateFiles(data,location)
        fs.delete(newDocName)
        if error:
            parsed = 0
        else:
            parsed = 1
        return render(request, 'core/home.html', {
            'parsed': parsed,
            'name': name,
            'email': email,
            'phone': phone,
            'linkedinUrl': linkedinUrl, 
            'lines': lineCount, 
            'chars': charCount,
            'pages': pageCount,
            'styles': fonts,
            'sizes': fontSizes , 
            'tables': tableCount,
            'images': imageCount,
            'csvLink': csvLink,
            'xlsxLink': xlsxLink,
            'error': error
        })

    return render(request, 'core/home.html', {
        'parsed': parsed
    })