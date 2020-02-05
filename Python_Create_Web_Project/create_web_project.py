import os
import webbrowser


print("Enter your project folder name")
# TODO check mac or windows desktop?

if os.name == "posix":
    project_folder_name = "/Users/tommypurkiss/Desktop/Projects" + "/" + input()
elif os.name == "nt":
    project_folder_name = "C:/Users/Tommy/Desktop" + "/" + input()
else:
    print("OS unknown")

css_folder = "/css"
js_folder = "/js"
assets_folder = "/assets" + "/imgs"



index_html_file = ("index.html")
main_css_file = ("main.css")


html_boilerplate = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">

     <!-- CSS -->
     <link rel="stylesheet" href="./css/main.css">

     <!-- GOOGLE FONTS  -->


     <!-- JQUERY UI CSS -->
    <link rel="stylesheet" type="text/css" href="http://code.jquery.com/ui/1.10.3/themes/smoothness/jquery-ui.css" />
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bluebird/3.7.0/bluebird.core.min.js"></script>
    
    <!-- JQUERY -->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
    <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
    <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
    <script src="./js/jquery.js"></script>

    <title>Document</title>
</head>
<body>
    
    <!-- WEB CONTENT GOES HERE-->

    <h1>Document Heading</h1>

    <p>
        new web project boilerplate code created from a python script!
    </p>


    <!-- WEB CONTENT ENDS HERE -->


    <!-- JAVASCRIPT -->
    <script src="./js/app.js"></script>
    
</body>
</html>
"""


css_boilerplate = """
* {
    box-sizing: border-box;
}

html {
    padding: 0;
    margin: 0;
    width: 100%;
    height: 100vh;
    -webkit-font-smoothing: antialiased;
}

body {
    padding: 0;
    margin: 0;
    width: 100%;
}

h1 {
    text-align: center;
}

p {
    text-align: center;
    font-size: 1.5em;
}
"""

try:
    if not os.path.exists(project_folder_name):
        
        os.makedirs(project_folder_name, exist_ok = True)
        open(os.path.join(project_folder_name, index_html_file), 'w+').write(html_boilerplate)

        css_dir = project_folder_name + css_folder
        os.makedirs(css_dir)
        open(os.path.join(css_dir, main_css_file), 'w+').write(css_boilerplate)
        

        js_dir = project_folder_name + js_folder
        os.makedirs(js_dir)
        # with open(os.path.join(js_dir, 'app.js'), 'w'):
        #     pass

        # with open(os.path.join(js_dir, 'jquery.js'), 'w'):
        #     pass
        open(os.path.join(js_dir, 'app.js'), 'w')
            
        open(os.path.join(js_dir, 'jquery.js'), 'w')
        

        os.makedirs(project_folder_name + assets_folder)


        if os.name == "posix":
            webbrowser.open(project_folder_name)
        elif os.name == "nt":
            os.startfile(project_folder_name) # windows only
        else:
            print("Cannot open in file explorer or finder")
        # os.startfile(project_folder_name) # windows only
        # webbrowser.open(project_folder_name)

        # print("DIRECTORY WITH SUB DIRECTORIES AND FILES CREATED SUCCESSFULLY")
    else:
        print("Directory already exists!")

        

except OSError:
    print ("Creation of the directory %s failed" % project_folder_name)
else:
    print ("Successfully created the directory %s" % project_folder_name)




