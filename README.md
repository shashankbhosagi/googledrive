# Google DRIVE api 

## Step1. Create a service account on google 

- Go to google cloud console, and create a project and select that project.
- Then in top left corner click on sidebar icon and navigate to `IAM & Admin`

![IAM admin click](assets/image-11.png)

- Again in sidebar look for `Service Account`

![side bar service acc](assets/image-9.png)

- In top bar click on `Create Serivce Account`

![click on create sa](assets/image-10.png)

- Fillin the details

![create account](assets/image.png)

- for step 2 and 3 during creation directly click Done as they are optional
- It should Look like this 

![account created](assets/image-1.png)

- Click on three dots in above image, and go to manage keys

![keys](assets/image-2.png)

- Click on add key drop down and click on create key

![add key](assets/image-3.png)

- Select json and save the key in a secure location as you will not be able to download it again

Now account has been created with the key !!

## Step2. Install required libraries

```bash
pip install google-api-python-client
```

## Step3. Get parent folder id from google drive 

- Go to drive.google.com, and create a folder

![folder create](assets/image-4.png)

- Go to google cloud consle and inside service account and copy the email.

![copy email](assets/image-5.png)

- Share the folder with that email and give editior access

![share folder](assets/image-6.png)


## Step4. Run the code app.py 

- To run the app, you must first copy the folder id of the shared folder

![folder id](assets/image-7.png)

- Paste it in variable PARENT_FOLDER_ID

- Run the code

```bash
python3 app.py
```
- Output must be like this

![output](assets/image-8.png)


#### Note: The key you downloaded must be in same folder as your app.py and the key should be renamed to `service_account.json`

Enjoi !