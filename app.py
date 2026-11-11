print("Hello from Python Application")

name = "VVCE"

print("Welcome to", name)
print("Application executed successfully")
print("NEW CHANGE: Jenkins automatic build triggered!")

Experiment – 2: Maven dependencies 
1.	Open eclipse
2.	File -> new -> maven project 
3.	Click next -> type “maven-archetype-quickstart” -> select latest version (1.1 or 1.5) -> click on next
4.	Type: 
Group ID: Test1
ArtifactID: test1
Click on finish
5.	After building.. Type y in terminal
6.	Right click on project->new->class
Classname – ReadJson
Type the code: (ReadJson.java)
package Test1.test1;
import java.io.*;
import org.json.simple.*;
import org.json.simple.parser.*;

public class ReadJson {
	public static void main(String[] args) throws Exception{
		JSONParser jsonparser=new JSONParser();
		FileReader reader=new FileReader("./JSON/student.json");
		
		Object obj=jsonparser.parse(reader);
		JSONObject studentobj=(JSONObject) obj;
		
		String fname=(String) studentobj.get("firstname");
		String lname=(String) studentobj.get("lastname");
		
		System.out.println("First name: "+fname);
		System.out.println("Last name: "+lname);
	}
}
7.	Right click on project -> New Folder -> Folder name: JSON 
8.	Right click on JSON -> New File -> File name: student.json
9.	Type the code: 
{ “firstname” : “ABC”,
   “lastname” : “D”  }
10.	Open browser -> type “maven repositories” ->  search “simple json” ->click on first one
11.	Scroll down to versions -> Select “1.1” version -> Scroll down -> Copy the code snippet
12.	Open pom.xml in eclipse -> find <dependencies> part -> paste the code snippet copied inside <dependencies> -> Save the file
13.	Json.simple.1.1 will be there under maven dependencies in the project structure at left.
Try changing 1.1 in the pom.xml to 1.1.1 and the file under maven dependencies will be updated to 1.1.1
14.	Open ReadJson and click on run
OUTPUT: First name: ABC
                 Last name: D

