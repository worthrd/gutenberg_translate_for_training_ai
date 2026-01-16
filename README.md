**Project Gurenberg Child Stories Translator for Azure AI Training**

This project translates prject gutenberg know child stories to Turkish for trainin data. 

> You need to specify AZURE deployed model properties for translate in .env file :  
>> *  AZURE_API_KEY
>> *  AZURE_ENDPOINT
>> *  AZURE_API_VERSION

If you want to translate another languege you have to change firs parameter in the message array **azure_client.py** to desired language. It is for Turkish
Also need to change **prompt.py** text for desired language translate

**Run project** 

1. docker compuse up --build
2. When ecerything is ok, you can http://localhost:5555 for running task. Translate is long process so it is divide sub tasks by using celery
3. You can stop anytime if you staisfy generated result in outpu folder. (docker-compose down -v)
4. To make single file (JSONL) run ``python combine_json_to_jsonl.py`` 
