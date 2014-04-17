Commands:

1) Install Gensim:

easy_install numpy
easy_install scipy
easy_install -U gensim


2) Install LSHash:

pip install lshash


3) Run the project:
In src folder type the below commands -

To parse the input tweet file -
python --parse parser.py <tweets_file>   

To create the dictionary which is mapping of word with its unique ID -
python --dict parser.py <tweets_file>   

To create corpus which contains vector form of all tweets -
python --corp parser.py <tweets_file>   

To detect subevent given the corpus file -
python --sub parser.py <tweets_file>   

To detect subevents as well as creating summary for each subevent -
python --all parser.py <tweets_file>   


Note :: First four command should be executed in that order only. The last command will execute the entire project and hence it is the preferred command.
