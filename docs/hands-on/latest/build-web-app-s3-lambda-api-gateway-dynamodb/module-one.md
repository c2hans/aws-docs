---
source_url: https://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/module-one.html
---

# Task 1: Create a Web App
<a name="module-one"></a>

|  |  |
| --- |--- |
| **Minimum time to complete** | 5 minutes  |
| **Services used** | [AWS Amplify](https://aws.amazon.com/amplify)  |
| **Requires** | A [GitHub account](https://github.com/) <br />GitHub [SSH connection](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) <br />[Nodejs](https://nodejs.org/en/download) and [npm](https://www.npmjs.com/)  |
| **Get help** | [Troubleshooting Amplify](https://docs.amplify.aws/react/build-a-backend/troubleshooting/) <br />[How Amplify works](https://docs.amplify.aws/react/how-amplify-works/)  |

## Overview
<a name="overview"></a>

AWS Amplify offers a Git-based CI/CD workflow for building, deploying, and hosting single-page web applications or static sites with backends. When connected to a Git repository, Amplify determines the build settings for both the frontend framework and any configured backend resources, and automatically deploys updates with every code commit.

In this task, you will start by creating a new React application and pushing it to a GitHub repository. You will then connect the repository to AWS Amplify web hosting and deploy it to a globally available content delivery network (CDN) hosted on an **amplifyapp.com** domain.

## Key concepts
<a name="key-concepts"></a>

**React Application:** React is a JavaScript library that enables developers to quickly build performant single-page applications.

**Git:** Git is a version control system that allows developers to store files, maintain and update relationships between files and directories, and track versions and changes to the files.

## Implementation
<a name="implementation"></a>

### Step 1: Create a new React application
<a name="create-a-new-react-application"></a>

1. Create the app

   In a new terminal or command line window, **run** the following command to use Vite to create a React application:

   ```
   npm create vite@latest profilesapp -- --template react
   cd profilesapp
   npm install
   npm run dev
   ```
![The resource creation interface.](http://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/create-the-app.png)

1. View the app

   In the terminal window, select and open the **Local link** to view the Vite \+ React application.
![The resource creation interface.](http://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/resource-creation-interface-1.png)

### Step 2: Install the Amplify packages
<a name="install-the-amplify-packages"></a>

1. Open GitHub

   Sign in to GitHub at [https://github.com/](https://github.com/).
![The navigation interface.](http://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/basic-navigation-interface.png)

1. Start repository

   In the Start a new repository section, make the following selections:
   + For **Repository name**, enter **profilesapp**, and choose the **Public** radio button.
   + Then select, **Create a new repository**.
![The resource creation interface.](http://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/resource-creation-interface-2.png)

1. Push the app to GitHub

   Open a new terminal window, navigate to your projects root folder (profilesapp), and run the following commands to initialize a git and push of the application to the new GitHub repo:
**Note**
Replace the SSH GitHub URL in the command with your GitHub URL.

   ```
   git init
   git add .
   git commit -m "first commit"
   git remote add origin git@github.com:<your-username>/profilesapp.git
   git branch -M main
   git push -u origin main
   ```

### Step 3: Initialize a GitHub repository
<a name="initialize-a-github-repository"></a>

1. Create an Amplify project

   **Open** a new terminal window, **navigate** to your app's root folder (**profilesapp**), and **run** the following command:

   ```
   npm create amplify@latest -y
   ```
![The resource creation interface.](http://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/resource-creation-interface-3.png)

1. View the project directory

   Running the previous command will scaffold a lightweight Amplify project in the app’s directory.
![File directory view showing a "profilesapp" folder with subfolders "amplify," "auth," and "data," containing TypeScript files and configuration files.](http://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/ptbhu-project-file-directory-view.png)

1. Push the changes to the repository

   In your terminal window, **run** the following command to push the changes to GitHub:

   ```
   git add .
   git commit -m 'installing amplify'
   git push origin main
   ```
![Interface element requiring manual review.](http://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/push-to-repo.png)

### Step 4: Deploy your app with AWS Amplify
<a name="deploy-your-app-with-aws-amplify"></a>

In this step, you will connect the GitHub repository you just created to AWS Amplify. This will enable you to build and deploy your app on AWS.

1. Create a new Amplify app

   **Sign in** to the AWS Management console in a new browser window, and open the AWS Amplify console at [https://console.aws.amazon.com/amplify/apps](https://console.aws.amazon.com/amplify/apps).

   Choose **Create new app**.
![The resource creation interface.](http://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/resource-creation-interface-4.png)

1. Choose GitHub as your Git provider

   On the **Start building with Amplify** page, for **Deploy your app**, select **GitHub**, and select **Next**.
![The selection interface.](http://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/selection-interface.png)

1. Add repository and branch

   When prompted, **authenticate** with GitHub. You will be automatically redirected back to the Amplify console. Choose the **repository** and **main branch** you created earlier. Then select **Next**.
![The resource creation interface.](http://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/resource-creation-interface-5.png)

1. Review build settings

   Leave the default **build settings**, and select **Next**.
![The review and confirmation interface.](http://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/confirmation-interface.png)

1. Deploy the app

   Review the inputs selected, and choose **Save and deploy**.
![Interface element requiring manual review.](http://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/interface-1.png)

1. Monitor build status

   AWS Amplify will now **build** your source code and **deploy** your app at **https://...amplifyapp.com**, and on every git push your deployment instance will update.

   It may take up to 5 minutes to deploy your app.
![Interface element requiring manual review.](http://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/interface-2.png)

1. View the deployed app

   Once the build completes, select the **Visit deployed URL** button to see your web app up and running live.
![The interface controls and buttons.](http://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/interface-controls-buttons.png)

## Conclusion
<a name="conclusion"></a>

You have deployed a React application in the AWS Cloud by integrating with GitHub and using AWS Amplify. With AWS Amplify, you can continuously deploy your application in the Cloud and host it on a globally available CDN.
