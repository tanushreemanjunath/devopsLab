import unittest

class TestApplication(unittest.TestCase):

    def test_application(self):
        name = "VVCE"
        self.assertEqual(name, "VVCE")

    def test_department(self):
        department = "CSE"
        self.assertEqual(department, "CSE")

if __name__ == "__main__":
    unittest.main()
Experiment – 3 : Docker container
1.	Open VS Code 
2.	Create a folder –> Create files index.html and dockerfile
3.	Type the code: 

index.html
<html>
<head>
         <title> Welcome ! </title>
</head>
<body>
         <h1> Hello from docker ! </h1>
         <p> Web app is successfully containerized </p>
</body>
</html>

dockerfile
FROM httpd:latest
COPY index.html /usr/local/apache2/htdocs/

4.	Login to docker desktop and docker hub
5.	Type commands
docker build -t profile .
docker run -d –name c1 -p 9090:80 profile
6.	Open browser and type url 
localhost:9090
7.	Open docker desktop -> Go to images -> Copy the image ID
8.	Type commands
docker tag (paste image ID) “username”/profile
9.	Push
docker push “username”/profile
10.	Pull from others
docker pull “username”/”imagename”

