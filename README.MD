

"My" version of our platterz hack (Yukuan, Arnav and Christina and me)
(the site got changed at 3am for some reason...)

Lessons learnt on my end:
1. usefulness/how to use pyenv/virtualenv

how to use it (high-level): 
pretty much it is just like creating a "folder-env", then you can go to that folder and activate it. Once you are in there,
the prompt is different, and all actions you take are run in the context of that environment. (Yes, even pip install)
Hence, you can install packages, etc. without worrying about existing dependencies/counter-dependencies (things that prevent something
from being installed) 

List:

pyenv = just used for different python versions

virtualenv = used for different sets of packages

pip = just a python package manager

Apparently `conda` supersedes virtualenv, so definitely look into that

https://stackoverflow.com/questions/34398676/does-conda-replace-the-need-for-virtualenv

2. django girls is really an OP guide
3. sqlite db are essentially files that can be transported.
4. worked through a real live "migration" => putting stuff on the db
5. found django to be a bit finicky, due to how coupled everything is => trying to merge two django sites together
6. something about the routing...
7. it is really easy to add users and authentication/sign up to the app!

Where is the bing image search stuff? it was moved to the AngularJS/frontend part
