# jupyter, RStudio & pycharm set up with github, do commit, make pull/push requests.

IMPORTANT STEPS TO SET WORKING ENVIRONMENT

1.HOW TO INTEGRATE JUPYTERLAB WITH GITHUB ?

  PULL THE LATEST VERSION: it takes some time based on internet speed.
        
    sudo docker pull jupyter/datascience-notebook:latest
  
2.To install perform the following steps, with pip:

    pip install --upgrade jupyterlab jupyterlab-git
    jupyter lab build

or with conda:

    conda install -c conda-forge jupyterlab jupyterlab-git
    jupyter lab build
            

3.UI Settings
  to do that connect to jupyter lab
  run the following command to install git with jupyterlab
    
    pip install jupyterlab-git
  GitPython-3.1.11
  
 SERVER SETTINGS:
 
 Post git init actions: It is possible to provide a list of commands to be executed in a folder after it is initialized as Git repository.
 In ~/.jupyter/jupyter_notebook_config.py:
 
      c.JupyterLabGit.actions = {"post_init": ["touch dummy_init.dat"]}
  Or equivalently in jupyter_notebook_config.json:
  
    {
    "JupyterLabGit": {
    "actions": {
      "post_init": [
        "touch dummy_init.dat"
       ]
    }
    }
    }
    
 TROUBLESHOOTING :
 Before consulting the following list, be sure the server extension and the frontend extension have the same version by executing the following commands:
 
    jupyter serverextension list
    jupyter labextension list
 

Issue: the Git panel does not recognize that you are in a Git repository.

Possible fixes:

   Be sure to be in a Git repository in the filebrowser tab
   Check the server log. If you see a warning with a 404 code similar to: [W 00:27:41.800 LabApp] 404 GET /git/settings?version=0.20.0
   Explicitly enable the server extension by running:

    jupyter serverextension enable --py jupyterlab_git

If you are using JupyterHub or some other technologies requiring an initialization script which includes the jupyterlab-git extension, be sure to install both the frontend and the server extension before launching JupyterLab.

Issue: the Git panel is not visible.

Possible fixes:

   Check that the JupyterLab extension is installed:
   
    jupyter labextension list

   If you don't see @jupyterlab/git v... enabled OK in the list, explicitly install the jupyter labextension by running:

    jupyter labextension install @jupyterlab/git

Development
Install

Requires NodeJS

# Install new-ish JupyterLab
    pip install -U jupyterlab

# Clone the repo to your local environment
    git clone https://github.com/jupyterlab/jupyterlab-git.git
    cd jupyterlab-git

# Install the server extension in development mode and enable it
    pip install -e .[test]
    pre-commit install
    jupyter serverextension enable --py jupyterlab_git --sys-prefix

# Build and install your development version of the extension
    jlpm
    jupyter labextension install .

To rebuild the package after a change and the JupyterLab app:

    jlpm run build
    jupyter lab build

To continuously monitor the project for changes and automatically trigger a rebuild, start Jupyter in watch mode:

    jupyter lab --watch

And in a separate session, begin watching the source directory for changes:

    jlpm run watch 
    
Now every change will be built locally and bundled into JupyterLab. Be sure to refresh your browser page after saving file changes to reload the extension (note: you'll need to wait for webpack to finish, which can take 10s+ at times).

To execute the tests

    pytest jupyterlab_git
    jlpm run test
   by running the above command we get to know the exact errors.

IN CASE IF YOU DO NOT PROPERLY CONFIGURE SERVER SETTINGS YOU SEE THE BELOW ERROR. when you reload the page you see the below error.
Failed to load the jupyterlab-git server extension :
    Git server extension is unavailable. Please ensure you have installed the JupyterLab Git server extension 
    by running: pip install --upgrade jupyterlab-git.  To confirm that the server extension is installed, run: jupyter serverextension list.
    
    pip install -U jupyterlab jupyterlab-git
    jupyter labextension install @jupyterlab/git
    jupyter serverextension enable --py jupyterlab_git

also a runtime check exhibits this

    jupyter labextension list
        JupyterLab v2.2.4
        Known labextensions:
        app dir: /opt/conda/share/jupyter/lab
        @jupyterlab/git v0.21.0-alpha.0  enabled  OK
        jupyterlab-jupytext v1.2.1  enabled  OK
        nbdime-jupyterlab v2.0.0  enabled  OK

    pip show jupyterlab-git

    sudo -E conda install jupyterlab-git -c conda-forge


#Install pycharm in linux ubuntu
  
    tar xzf pycharm-*.tar.gz -C <new_archive_folder>
#i moved my pycharm into the new directory so that we can access easily.

    tar xzf pycharm2020-*.tar.gz -C /opt/
#Navigate into directory where you moved. move to linux file system path "ops"

    cd <new archive folder>/pycharm-*/bin
    cd /opt/pycharm-*/bin
#then run the below command to start the pycharm ide.
        
    sh pycharm.sh
    
#configure pycharm with github

    the easy way to do is once you install pycharm ide, go to settins-->preferences--> version control --> add github account
    then goto file-->open any project which is already cloned any github project. then write your code, on the top right corner find git hub navigation icons to        make commit, push , pull requests. its bit hand if you use new version of pycharm ide 2020 either community/professional edition. thats it. now you successfully configured github to your pycharm ide.
#install packages in pycharm ide
  
    goto settings-->preferences-->project interpreter-->you see some packages listed or else clich on + icon  to see more packages listed, simply search and     install it. that's it . now ou successfully installed your packages to your projects.
    now you can run the project.
---------------------------------------------

      #python 3.6 context
      26. Strings
      27. boolean operators in python
      28. Tuples in python
      29. Sets in python    
Data types in python :
1)str
2)int
3)float
4)complex
5)tuple
6)set
7)dict
8)list
9)bool
10)frozenset
11)bytes
12)bytesarray
13)range
14)memoryview(bytes(5))

Python castings:
1)int
2)float
3)str

Python Strings:
1)multiline strings(using 2 double quotes / single quotes), hint : """,'''
2)strings are arrays 
3)looping through a string
4)string length
5)check string (required string is present in the pharse)
6)check string using 'if' condition
7)print string if not present in the given string. hint : IF NOT

python slicing strings:
1)print characters from 3 position to 6 position
2)print the character starting from to 5th position
3)print the character from 3rd position to end of phase
4)negative indexing

python modify strings:
1)print the one string upper case
2)print the one string lower case
3)remove white spaces in the statement
4)replace another string on existing place\
5)split strings into sub-strings
6)concatenating two strings or sentenses and add spaces word to word or sentenses

python format strings:
1)add a text and number and print the complete statement.
2)give indexing like 0,1,2,3 etc and arrange in order of statement

python escape characters:
1)print a statemnet using blackslash and double quotes
2)print backslash in the stmt
3)print in a new line using "\n" and "\r"(carriage return)
4)print in tab i.e tab of space
5)print a statement and elimenate one character and concatenate two words using "\b"
6)print a statement using "\f" like form feed

python built-in methods
1)print a statement with only starting letter in capital and rest all small letters using "capitalize()" method
2)print all the characters in lower letter using "casefold()" method.
3)