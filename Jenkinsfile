pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Application') {
            steps {
                sh 'python3 app.py'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 test.py'
            }
        }

        stage('Build') {
            steps {
                echo 'Build completed successfully'
            }
        }
    }

    post {
        success {
            echo 'Jenkins Build Successful'
        }

        failure {
            echo 'Jenkins Build Failed'
        }
    }
}

Experiment – 5 : Jenkins and Slack integration

1. Create a GitHub repository
1.	Open GitHub.
2.	Click New repository.
3.	Repository name: Slack-Experiment.
4.	Select Public.
5.	Click Create repository.

2. Create main.py
1.	Open the newly created repository.
2.	Click Add file → Create new file.
3.	File name: main.py.
4.	Enter the following code:
print("DevOps")
print(“VVCE”)
5. Click Commit changes to save the file.

3. Create a Jenkins project
1.	Open Jenkins.
2.	Click New Item.
3.	Enter item name: Slack-Notifier.
4.	Select Freestyle project.
5.	Click OK.

4. Configure Source Code Management
In the project configuration page:
1.	Go to Source Code Management.
2.	Select Git.
3.	Repository URL: Copy and paste your GitHub repository URL.
Example:
https://github.com/username/Slack-Experiment.git
4.	Under Branches to build, change the branch name to:
*/main

5. Configure Build Steps
1.	Scroll to Build Steps.
2.	Click Add build step.
3.	Select Execute Windows batch command.
4.	Open Command Prompt and execute:
where python
5.	Copy the first Python installation path.
6.	In the Jenkins command box, enter:
"path" main.py

6. Configure Post-build Actions
1.	Scroll down to Post-build Actions.
2.	Select Slack Notifications.
3.	Enable these options:
o	Notify Build Start
o	Notify Success
o	Notify Every Failure
4.	Click Apply.
5.	Click Save.
Jenkins job configuration completed

7. Create a Slack workspace
1.	Open Google Chrome.
2.	Search for Slack Login.
3.	Click Continue with Google.
4.	Log in using your Google account.
5.	Create a workspace with the name:
Vvce
6.	Click Create.
7.	Skip the invitation and other optional setup steps.

8. Create a Slack channel
1.	Open your Slack workspace dashboard.
2.	Under Channels, click the + icon.
3.	Select Create a channel.
4.	Enter the channel name:
demo_exp9
5.	Select Public.
6.	Click Create.
7.	Skip adding members.
Slack workspace and channel created.

9. Add Jenkins application to Slack
1.	In Slack, click Agents and Tools or the three-dot menu, depending on the interface.
2.	Select Apps.
3.	Search for Jenkins.
4.	Select the Jenkins CI application.
5.	Click Add to Slack.
6.	It will open the Jenkins Slack application page in a new browser tab.
7.	Click Add to Slack again.
8.	Select the channel demo_exp9 from the channel dropdown.
9.	Click Add Jenkins CI integration. 
After authorization, you will get the Slack integration details.
•	Team Subdomain: Your Slack workspace subdomain (for example, vvce or the actual subdomain displayed). (vvce-r935744)
•	Bot User OAuth Token: The secret token generated for the Jenkins Slack application.
(rXJUzMSj4wg1rKShfVa9XXsH)

10. Configure Slack in Jenkins
1.	Open Jenkins Dashboard.
2.	Go to Settings → System
3.	Scroll down to the Slack section.
4.	Workspace: vvce-r935744
Credential:  Click on Add 
                      Select Global -> Secret text -> Next 
                                    Secret: rXJUzMSj4wg1rKShfVa9XXsH
                                    ID: ----
                                    Description: notifier
                       Click on create

Default channel: Type the channel name created (demo_exp9)

Select the description name in the credential drop down (notifier)

Click on test connection 
OUTPUT: success

Click on apply - > Save

5.	Open the Slack_Notifier -> Click on build -> Build success
Output: DevOps
               VVCE

and 

OUTPUT in slack :

Slack-Notifier
Build #1 completed successfully.
Started by user “username”
Job: Slack-Notifier
Status: SUCCESS



