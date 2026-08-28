---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-a-react-app-by-using-aws-amplify-and-add-authentication-with-amazon-cognito.html
---

# Create a React app by using AWS Amplify and add authentication with Amazon Cognito
<a name="create-a-react-app-by-using-aws-amplify-and-add-authentication-with-amazon-cognito"></a>

*Rishi Singla, Amazon Web Services*

## Summary
<a name="create-a-react-app-by-using-aws-amplify-and-add-authentication-with-amazon-cognito-summary"></a>

This pattern demonstrates how to use AWS Amplify to create a React-based app and how to add authentication to the frontend by using Amazon Cognito. AWS Amplify consists of a set of tools (open source framework, visual development environment, console) and services (web app and static website hosting) to accelerate the development of mobile and web apps on AWS.

## Prerequisites and limitations
<a name="create-a-react-app-by-using-aws-amplify-and-add-authentication-with-amazon-cognito-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ [Node.js](https://nodejs.org/en/download/) and [npm](https://www.npmjs.com/get-npm) installed on your machine

**Product versions**
+ Node.js version 10.x or later (to verify your version, run `node -v` in a terminal window)
+ npm version 6.x or later (to verify your version, run `npm -v` in a terminal window)

## Architecture
<a name="create-a-react-app-by-using-aws-amplify-and-add-authentication-with-amazon-cognito-architecture"></a>

**Target technology stack **
+ AWS Amplify
+ Amazon Cognito

## Tools
<a name="create-a-react-app-by-using-aws-amplify-and-add-authentication-with-amazon-cognito-tools"></a>
+ [Amplify Command Line Interface (CLI)](https://docs.amplify.aws/cli/)
+ [Amplify Libraries](https://docs.amplify.aws/lib/q/platform/react-native/) (open source client libraries)
+ [Amplify Studio](https://docs.amplify.aws/console/) (visual interface)

## Epics
<a name="create-a-react-app-by-using-aws-amplify-and-add-authentication-with-amazon-cognito-epics"></a>

### Install AWS Amplify CLI
<a name="install-aws-amplify-cli"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install the Amplify CLI. | The Amplify CLI is a unified toolchain for creating AWS Cloud services for your React app. To install the Amplify CLI, run:<pre>npm install -g @aws-amplify/cli</pre><br />npm will notify you if a new major version is available. If so, use the following command to upgrade your version of npm:<pre>npm install -g npm@9.8.0</pre><br />where 9.8.0 refers to the version you want to install. | App developer |

### Create a React app
<a name="create-a-react-app"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a React app. | To create a new React app, use the command:<pre>npx create-react-app amplify-react-application</pre><br />where `ampify-react-application` is the name of the app.<br />When the app has been created successfully, you will see the message:<pre>Success! Created amplify-react-application</pre><br />A directory with various subfolders will be created for the React app. | App developer |
| Launch the app on your local machine. | Go to the directory `amplify-react-application` that was created in the previous step and run the command:<pre>amplify-react-application% npm start</pre><br />This launches the React app on your local machine. | App developer |

### Configure the Amplify CLI
<a name="configure-the-amplify-cli"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure Amplify to connect to your AWS account. | Configure Amplify by running the command:<pre>amplify-react-application % amplify configure</pre><br />The Amplify CLI asks you to follow these steps to set up access to your AWS account:1. Sign in to your AWS administrator account.<br />2. Specify the AWS Region you want to use.<br />3. Create an AWS Identity and Access Management (IAM) user with programmatic access, and attach the `AdministratorAccess-Amplify` permissions policy to the user.<br />4. Create and then copy the access key ID and secret access key.<br />5. Enter these details in the terminal.<br />6. Create a profile name or use the default profile.This scenario requires IAM users with programmatic access and long-term credentials, which present a security risk. To help mitigate this risk, we recommend that you provide these users with only the permissions they require to perform the task and that you remove these users when they are no longer needed. Access keys can be updated if necessary. For more information, see [Updating access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey) in the *IAM User Guide*.<br />These steps appear in the terminal as follows.<pre>Follow these steps to set up access to your AWS account:<br />Sign in to your AWS administrator account:<br />https://console.aws.amazon.com/<br />Press Enter to continue<br />Specify the AWS Region<br />? region:  us-east-1<br />Follow the instructions at<br />https://docs.amplify.aws/cli/start/install/#configure-the-amplify-cli<br />to complete the user creation in the AWS console<br />https://console.aws.amazon.com/iamv2/home#/users/create<br />Press Enter to continue<br />Enter the access key of the newly created user:<br />? accessKeyId:  ********************<br />? secretAccessKey:  ****************************************<br />This would update/create the AWS Profile in your local machine<br />? Profile Name:  new<br /><br />Successfully set up the new user.</pre><br />For more information about these steps, see the [documentation](https://docs.amplify.aws/cli/start/install/#configure-the-amplify-cli) in the Amplify Dev Center. | General AWS, App developer |

### Initialize Amplify
<a name="initialize-amplify"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Initialize Amplify. | 1. To initialize Amplify in the new directory, run:<pre>amplify init</pre><br />Amplify prompts you for the project name and configuration parameters<br />2. Specify all parameters, and then press **Y** to initialize the project with the specified configuration.<pre>Project information<br />| Name: amplifyreactproject<br /><br />| Environment: dev<br /><br />| Default editor: Visual Studio Code<br /><br />| App type: javascript<br /><br />| Javascript framework: react<br /><br />| Source Directory Path: src<br /><br />| Distribution Directory Path: build<br /><br />| Build Command: npm run-script build<br /><br />| Start Command: npm run-script start</pre><br />3. Select the profile you created in the previous step. The resources will be deployed into the `dev` environment in the Amplify project you created.<br />4. To confirm that the resources have been created, you can open the [AWS Amplify console](https://console.aws.amazon.com/amplify/home) and view the AWS CloudFormation template that was used to create the resources and the details.<pre>Deploying root stack amplifyreactproject [ ====================-------------------- ] 2/4<br />amplify-amplifyreactproject-d… AWS::CloudFormation::Stack     CREATE_IN_PROGRESS            <br /><br />UnauthRole                     AWS::IAM::Role                 CREATE_COMPLETE                 <br /><br />DeploymentBucket               AWS::S3::Bucket                CREATE_IN_PROGRESS         <br /><br />AuthRole                       AWS::IAM::Role                 CREATE_COMPLETE   </pre> | App developer, General AWS |

### Add authentication to the frontend
<a name="add-authentication-to-the-frontend"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Adding authentication. | You can use the `amplify add <category>` command to add features such as a user login or a backend API. In this step you will use the command to add authentication.<br />Amplify provides a backend authentication service with Amazon Cognito, frontend libraries, and a drop-in Authenticator UI component. Features include user sign-up, user sign-in, multi-factor authentication, user sign-out, and passwordless sign-in. You can also authenticate users by integrating with federated identity providers such as Amazon, Google, and Facebook. The Amplify authentication category integrates seamlessly with other Amplify categories such as API, analytics, and storage, so you can define authorization rules for authenticated and unauthenticated users.1. To configure authentication for your React app, run the command:<pre>amplify-react-application1 % amplify add auth</pre><br />This displays the following information and prompts. You can choose the appropriate configuration depending on your business and security requirements.<pre>Using service: Cognito, provided by: awscloudformation<br /> The current configured provider is Amazon Cognito. <br />Do you want to use the default authentication and security configuration? (Use arrow keys)<br /><br />❯ Default configuration <br /><br />  Default configuration with Social Provider (Federation) <br /><br />  Manual configuration <br /><br />  I want to learn more. </pre><br />2. For a simple example, choose the default configuration and then select the sign-in mechanism for users (in this case, email):<pre>How do you want users to be able to sign in? <br /> Username <br /><br />❯ Email <br /><br />  Phone Number <br /><br />  Email or Phone Number <br /><br />  I want to learn more. </pre><br />3. Bypass the advanced settings to complete adding authentication resources:  <pre>Do you want to configure advanced settings? (Use arrow keys)<br />❯ No, I am done. <br /><br />  Yes, I want to make some additional changes.</pre><br />4. Build your local backend resources and provision them in the cloud:<pre>amplify-react-application1 % amplify push</pre><br />This command makes the appropriate changes to the Congito user pools in your account.<br />5. Press **Y** to configure the `auth` resource by using CloudFormation.<br />This configures the following resources:<pre>UserPool                       AWS::Cognito::UserPool         CREATE_COMPLETE  <br />UserPoolClientWeb              AWS::Cognito::UserPoolClient   CREATE_COMPLETE    <br />UserPoolClientWeb              AWS::Cognito::UserPoolClient   CREATE_COMPLETE            <br />UserPoolClientRole             AWS::IAM::Role                 CREATE_COMPLETE                <br />UserPoolClientLambda           AWS::Lambda::Function          CREATE_COMPLETE  <br />UserPoolClientLambdaPolicy     AWS::IAM::Policy               CREATE_COMPLETE                <br />UserPoolClientLogPolicy        AWS::IAM::Policy               CREATE_IN_PROGRESS                </pre><br />You can also use the [AWS Cognito console](https://console.aws.amazon.com/cognito/home) to view these resources (look for Cognito user pools and identity pools).<br />This step updates the `aws-exports.js` file in the `src` folder for your React app with the Cognito user pool and identity pool configurations. | App developer, General AWS |

### Change the App.js file
<a name="change-the-app-js-file"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Change the App.js file. | In the `src` folder, open and revise the `App.js` file. The modified file should look like this:<pre>{  App.Js File after modifications:<br />import React from 'react';<br />import logo from './logo.svg';<br />import './App.css';<br />import { Amplify } from 'aws-amplify';<br />import { withAuthenticator, Button, Heading } from '@aws-amplify/ui-react';<br />import awsconfig from './aws-exports';<br />Amplify.configure(awsconfig);<br />function App({ signOut }) {<br />  return (<br />      <div><br />      <h1>Thankyou for doing verification</h1><br />      <h2>My Content</h2><br />       <button onClick={signOut}>Sign out</button><br />    </div><br />  );<br />}<br />export default withAuthenticator(App);</pre> | App developer |
| Import React packages. | The `App.js` file imports two React packages. Install these packages by using the command:<pre>amplify-react-application1 % npm install --save aws-amplify @aws-amplify/ui-react</pre> | App developer |

### Launch the React app and check authentication
<a name="launch-the-react-app-and-check-authentication"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Launch the app. | Launch the React app on your local machine:<pre>amplify-react-application1 % npm start</pre> | App developer, General AWS |
| Check authentication. | Check whether the app prompts for authentication parameters. (In our example, we’ve configured email as the sign-in method.)<br />The frontend UI should prompt you for sign-in credentials and provide an option to create an account.<br />You can also configure the Amplify build process to add the backend as part of a continuous deployment workflow. However, this pattern doesn’t cover that option. | App developer, General AWS |

## Related resources
<a name="create-a-react-app-by-using-aws-amplify-and-add-authentication-with-amazon-cognito-resources"></a>
+ [Getting started](https://docs.npmjs.com/getting-started) (npm documentation)
+ [Create a standalone AWS account](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html) (AWS Account Management documentation)
+ [AWS Amplify documentation](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html)
+ [Amazon Cognito documentation](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
