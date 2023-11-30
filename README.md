# 1
Title-
Install Google App Engine. Create hello world app and other simple web applications

using python/java

Steps-
a. Download python from-https://www.python.org/downloads/
b. Download Google Cloud SDK from-
https://cloud.google.com/sdk/docs/install#windows
c. Launch the installer and follow the prompts
d. Perform initial setup by running "gcloud init"
e. Grant authorization to Cloud SDK tools to access Google Cloud
f. Write python 'test.py' file with Namaste world statement
g. Write 'app.yaml' configuration file
h. Open the shell
i. Run the application with the following command in shell:
j. cmd> py google-cloud-sdk\bin\dev_appserver.py <path to the directory where
application reside>
k. Open the web browser and type http://localhost:8000

Video Link-
https://www.youtube.com/watch?v=7UtLfGnmh1U


in app.yml:
we have mentioned 4 things: Runtime, API version of that partiular SDK, Threadsafe (for single thread and not multiple threads to run), Handlers.


in google cloud sdk shell: run "py google-cloud-sdk\bin\dev_appserver.py folderlocation" and then press enter. Then copy the link which will look like this: "http://localhost:8080" and then paste in browser. If you want to change in the text, then change text in test.py file then ctrl+s then ctrl+r in browser.
