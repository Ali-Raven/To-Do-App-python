# To-Do-App-python

### Main part of this project : 
* back-end logic and **database**
* app feature's like sorting and add and removing the **tasks and priority of the tasks**
* implementing the App GUI with [tkinter](https://docs.python.org/3/library/tkinter.html) or other library in python


### how to use Project locally ? 
you must fork the project with your github , then you have copy of the project in your system and you can clone this with : 
```
git clone <address of your github and repo>
```
> [!TIP]
> with this command you create **folder** of this project in your **desktop or any path you are** now in your pc

> [!WARNING]
> avoid **making change** to other's file and directory as much as possible

#### The address you can clone with it is in your github and you can use http or SSH to create a remote for clone : 
![screen_shot_of_address_clone](./Screenshot%20from%202025-07-05%2011-33-12.png)


## How to install the packages for easy usage
**use pipereqs to install or create requirements.txt file for your package**(_Recommended_)
* first install the pipreqs : 
    ```
    pip install pipreqs
    ```
* **or you can use freeze :**
    ```
    pip install freeze
    ```
> [!TIP]
> if you want create list of your package use : 
    ```
    pipreqs <path of your project and files>
    ```
    **this create requiremnets.txt of your packages**
    
> [!TIP]
> craete with **freeze** is very simple : 
    ```
    pip freeze > requirements.txt
    ```    
* to install all package from requirements.txt : 
    ```
    pip install -r requirements.txt
    ```
## How to install and run Redis on Windows and Linux
### Windows
to install redis and running on windows you should use **WSL(Windows Subsystems for Linux)** : 
* to install WSL you should Open PowerShell as Administrator and run: 
    ```
    wsl --install
    ```
* if you prefer to use other distro of linux you can see the list of linux distro that is oneline : 
    ```
    wsl --list --online
    ```
* to install on of them use : 
    ```
    wsl --install -d <Distribution Name>
    ```
after you install the **wsl** on **windows** you should install **Redis** through this link : [[How to install Redis?]](https://redis.io/docs/latest/operate/oss_and_stack/install/archive/install-redis/install-redis-on-windows/)
## Tips you should know !
### Http Methods
| Method | Descriptions | 
| -- | -- |
| GET | get a file or document or any data from server | 
| HEAD | request to server to get **only header** but **no data or file** from server |
| POST | send data to the server for processing |
| PUT | **for updating** , to store the body of request on the server | 
| TRACE | trace the message through the proxy server on a server | 
| OPTIONS | determined what methods can **operate** on the server | 
| DELETE | to **remove or delete** some data on the server |
#### **status codes that are very important :**

| Overal Range | Defined Range | Category | 
| -- | -- | -- | 
| 100-199 | 100-101 | Informational | 
| 200-299 | 200-206 | Successful | 
| 300-399 | 300-305 | Redirection |
| 400-499 | 400-415 | Client Error | 
| 500-599 | 500-505 | Server Error |   


### URL (Uniform Resource Locator)
### Structure of every part 
URL is stand for (**uniform resource locator**) and it is very important in web scrowling and exploit the vulnerability of any web server or web application

it has some part : 
1. Scheme (**Protocol**)
2. username:password (**for protected URL**)
3. host (**show the web or server that host the files**)
4. path (**path and route the files in web server trace , it shows which file are located where , on the web server**)
5. query (**specify what data or static file you want from web server**)
6. Fragment (**only is for clinet side and not work in the server**)














