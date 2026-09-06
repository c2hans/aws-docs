---
source_url: https://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/module-five.html
---

# Task 5: Add Interactivity to Your Web App
<a name="module-five"></a>

|  |  |
| --- |--- |
| **Time to complete** | 5 minutes  |
| **Services used** | [AWS Amplify](https://amplify/)  |
| **Get help** | [Troubleshooting Amplify](https://docs.amplify.aws/react/build-a-backend/troubleshooting/) <br />[Troubleshooting common issues using Amplify UI](https://ui.docs.amplify.aws/react/getting-started/troubleshooting)  |

## Overview
<a name="overview"></a>

In this task, you will update the website you created in task one to use the Amplify UI component library to scaffold out an entire user authentication flow, allowing users to sign up, sign in, and reset their password and invoke the GraphQL API we created in module three. This will add the ability to display the user’s email that was captured using a serverless function.

## Key concepts
<a name="key-concepts"></a>

**Amplify libraries:** The Amplify libraries allow you to interact with AWS services from a web or mobile application.

## Implementation
<a name="implementation"></a>

### Step 1: Install the Amplify libraries
<a name="install-the-amplify-libraries"></a>

You will need two Amplify libraries for your project. The main **aws-amplify library** contains all of the client-side APIs for connecting your app's frontend to your backend, and the **@aws-amplify/ui-react** library contains framework-specific UI components.
+ Install the libraries

  In a new terminal window, in your projects root folder ( **profilesapp** ), **run** the following command to install the libraries.

  ```
  npm install aws-amplify @aws-amplify/ui-react
  ```
![A terminal window showing the installation of AWS Amplify libraries using npm for a basic web application tutorial. The command 'npm install aws-amplify @aws-amplify/ui-react' is run, and the output indicates successful package installation with zero vulnerabilities found.](http://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/juxz-basic-install-libraries-terminal.png)

### Step 2: Style the App UI
<a name="style-the-app-ui"></a>

You will need two Amplify libraries for your project. The main **aws-amplify library** contains all of the client-side APIs for connecting your app's frontend to your backend, and the **@aws-amplify/ui-react** library contains framework-specific UI components.
+ Modify the CSS

  On your local machine, navigate to the ****profilesapp/src/index.css**** file and **update** it with the following code. Then, **save** the file.

  ```
  :root {
    font-family: Inter, system-ui, Avenir, Helvetica, Arial, sans-serif;
    line-height: 1.5;
    font-weight: 400;

    color: rgba(255, 255, 255, 0.87);

    font-synthesis: none;
    text-rendering: optimizeLegibility;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;

    max-width: 1280px;
    margin: 0 auto;
    padding: 2rem;

  }

  .card {
    padding: 2em;
  }

  .read-the-docs {
    color: #888;
  }

  .box:nth-child(3n + 1) {
    grid-column: 1;
  }
  .box:nth-child(3n + 2) {
    grid-column: 2;
  }
  .box:nth-child(3n + 3) {
    grid-column: 3;
  }
  ```
![A file explorer showing the profilesapp project directory. The src folder is expanded to reveal App.css, App.jsx, an assets folder, main.jsx, and a highlighted index.css file, which is outlined in red. This is commonly used for basic web application tutorials demonstrating file organization in React projects.](http://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/usqfe-basic-index-file-explorer.png)

### Step 3: Implement the UI
<a name="implement-the-ui"></a>

1. Modify the main.jsx file

   On your local machine, navigate to the ****profilesapp/src/main.jsx**** file and **update** it with [this code](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/getting-started/approved/assets/build-basic-web-application-mod-5-tutorial-main-jsx-code.pdf). Then, **save** the file.
   + The code will use the Amplify Authenticator component to scaffold out an entire user authentication flow allowing users to sign up, sign in, reset their password, and confirm sign-in for multifactor authentication (MFA).
![A project directory for 'profilesapp' showing node_modules, public, and src folders, along with files like package.json, README.md, and main.jsx. The file 'main.jsx' is highlighted, illustrating module 5 of a tutorial for building a basic web application.](http://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/yim-basic-main-project-directory.png)

1. Modify the app.jsx file

   **Open** the **profilesapp/src/App.jsx** file, and **update** it with [this code](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/getting-started/approved/assets/build-basic-web-application-mod-5-tutorial-app-jsx-code.pdf). Then, **save** the file.
   + The code starts by configuring the Amplify library with the client configuration file ( **amplify\_outputs.json)** . It then generates a data client using the  **generateClient() ** function. The app will use the data client to get the user’s profile data.
![A project directory structure for a React web application, with the file App.jsx highlighted inside the src folder. The image shows common files such as index.html, package.json, node_modules, and folders like public and assets, useful for tutorials on building basic web applications.](http://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/basic-project-directory-structure-react.png)

1. **Open** a new terminal window, **navigate** to your project's root directory (*profilesapp*), and **run** the following command to launch the app:

   ```
   npm run dev
   ```

1. Select the **Local host link** to open the Vite \+ React application.
![Showing the Vite + React application.](http://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/vite-react.png)

1. Create a new user

   Choose the **Create Account** tab, and use the authentication flow to create a new user by entering your **email address** and a **password**.

   Then, choose **Create Account**.

   You will get a verification code sent to your email. Enter the **verification code** to log in to the app.

   When signed in, the app will display your email address.

1. Push the changes

   In the open terminal window, **run** the following command to push the changes to GitHub:

   ```
   git add .
   git commit -m 'displaying user profile'
   git push origin main
   ```
![Terminal commands and output for adding, committing, and pushing code changes to a Git repository during AWS Amplify Module 5 tutorial for building a basic web application.](http://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/basic-push-changes-eaf-terminal-commands.png)

1. Verify the deployment instance updates

   **Sign in** to the AWS Management console in a new browser window, and **open** the AWS Amplify console at [https://console.aws.amazon.com/amplify/apps](https://console.aws.amazon.com/amplify/apps) .

   AWS Amplify automatically builds your source code and deployed your app at ****https://...amplifyapp.com**** , and on every git push your deployment instance will update. Select the **Visit deployed URL** button to see your web app up and running live.
![The AWS Amplify Console showing the overview page for a web application named 'profilesapp', including deployment status, branch information, and the 'Visit deployed URL' button highlighted.](http://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/basic-console-amplifylong-overview-page.png)
