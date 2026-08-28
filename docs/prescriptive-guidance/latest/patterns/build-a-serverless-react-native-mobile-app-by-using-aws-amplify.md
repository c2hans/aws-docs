---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-a-serverless-react-native-mobile-app-by-using-aws-amplify.html
---

# Build a serverless React Native mobile app by using AWS Amplify
<a name="build-a-serverless-react-native-mobile-app-by-using-aws-amplify"></a>

*Deekshitulu Pentakota, Amazon Web Services*

## Summary
<a name="build-a-serverless-react-native-mobile-app-by-using-aws-amplify-summary"></a>

This pattern shows how to create a serverless backend for a React Native mobile app by using AWS Amplify and the following AWS services:
+ AWS AppSync
+ Amazon Cognito
+ Amazon DynamoDB

After you configure and deploy the app’s backend by using Amplify, Amazon Cognito authenticates app users and authorizes them to access the app. AWS AppSync then interacts with the frontend app and with a backend DynamoDB table to create and fetch data.

**Note**
This pattern uses a simple "ToDoList" app as an example, but you can use a similar procedure to create any React Native mobile app.

## Prerequisites and limitations
<a name="build-a-serverless-react-native-mobile-app-by-using-aws-amplify-prereqs"></a>

**Prerequisites **
+ An active AWS Account
+ [Amplify Command Line Interface (Amplify CLI)](https://docs.amplify.aws/cli/start/install/), installed and configured
+ XCode (any version)
+ Microsoft Visual Studio (any version, any code editor, any text editor)
+ Familiarity with Amplify
+ Familiarity with Amazon Cognito
+ Familiarity with AWS AppSync
+ Familiarity with DynamoDB
+ Familiarity with Node.js
+ Familiarity with npm
+ Familiarity with React and React Native
+ Familiarity with JavaScript and ECMAScript 6 (ES6)
+ Familiarity with GraphQL

## Architecture
<a name="build-a-serverless-react-native-mobile-app-by-using-aws-amplify-architecture"></a>

The following diagram shows an example architecture for running a React Native mobile app’s backend in the AWS Cloud:

![Workflow for running a React Native mobile app with AWS services.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/c95e0150-5762-4c90-946c-efa3a22913e4/images/5beff5f9-9d14-49dc-a046-b74e5bfbd13f.png)

The diagram shows the following architecture:

1. Amazon Cognito authenticates app users and authorizes them to access the app.

1. To create and fetch data, AWS AppSync uses a GraphQL API to interact with the frontend app and a backend DynamoDB table.

## Tools
<a name="build-a-serverless-react-native-mobile-app-by-using-aws-amplify-tools"></a>

**AWS services**
+ [AWS Amplify](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html) is a set of purpose-built tools and features that helps frontend web and mobile developers quickly build full-stack applications on AWS.
+ [AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/what-is-appsync.html) provides a scalable GraphQL interface that helps application developers combine data from multiple sources, including Amazon DynamoDB, AWS Lambda, and HTTP APIs.
+ [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) provides authentication, authorization, and user management for web and mobile apps.
+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) is a fully managed NoSQL database service that provides fast, predictable, and scalable performance.

**Code**

The code for the sample application that’s used in this pattern is available in the GitHub [aws-amplify-react-native-ios-todo-app](https://github.com/aws-samples/aws-amplify-react-native-ios-todo-app) repository. To use the sample files, follow the instructions in the** Epics** section of this pattern.

## Epics
<a name="build-a-serverless-react-native-mobile-app-by-using-aws-amplify-epics"></a>

### Create and run your React Native app
<a name="create-and-run-your-react-native-app"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up a React Native development environment.  | For instructions, see [Setting up the development environment](https://reactnative.dev/docs/next/environment-setup) in the React Native documentation. | App developer |
| Create and run the ToDoList React Native mobile app in iOS Simulator. | 1. Create a new React Native mobile app project directory in in your local environment by running the following command in a new terminal window:<br />`npx react-native init ToDoListAmplify`<br />2. Navigate to the project’s root directory by running the following command:<br />`cd ToDoListAmplify`<br />3. Run the app by running the following command:<br />`npx react-native run-ios` | App developer |

### Initialize a new backend environment for the app
<a name="initialize-a-new-backend-environment-for-the-app"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the backend services needed to support the app in Amplify.  | 1. In your local environment, run the following command from the project’s root directory (**ToDoListAmplify**):<br />`amplify init`<br />2. A prompt appears that asks you to provide information about the app. Enter the required information based on your use case. Then, press **Enter**.For the ToDoList app setup used in this pattern, apply the following example configuration.<br />**Example React Native Amplify app configuration settings**<pre>? Name: ToDoListAmplify<br /><br />? Environment: dev<br /><br />? Default editor: Visual Studio Code<br /><br />? App type: javascript<br /><br />? Javascript framework: react-native<br /><br />? Source Directory Path: src<br /><br />? Distribution Directory Path: /<br /><br />? Build Command: npm run-script build<br /><br />? Start Command: npm run-script start<br /><br />? Select the authentication method you want to use: AWS profile<br /><br />? Please choose the profile you want to use: default</pre><br />For more information, see [Create a new Amplify backend](https://docs.amplify.aws/lib/project-setup/create-application/q/platform/js/#create-a-new-amplify-backend) in the Amplify Dev Center documentation.The `amplify init` command provisions the following resources by using [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html): + AWS Identity and Access Management (IAM) roles for authenticated and unauthenticated users (**Auth Role** and **Unauth Role**)<br />+ An Amazon Simple Storage Service (Amazon S3) bucket for deployment (for this pattern’s example app, **Amplify-meta.json**)<br />+ A backend environment in [Amplify Hosting](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html) | App developer |

### Add Amazon Cognito authentication to your Amplify React Native app
<a name="add-amazon-cognito-authentication-to-your-amplify-react-native-app"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Amazon Cognito authentication service. | 1. In your local environment, run the following command from the project’s root directory (**ToDoListAmplify**):<br />`amplify add auth`<br />2. A prompt appears that asks you to provide information about the authentication service’s configuration settings. Enter the required information based on your use case. Then, press **Enter**.For the ToDoList app setup used in this pattern, apply the following example configuration.<br />**Example authentication service configuration settings**<pre>? Do you want to use the default authentication and security configuration? \ <br />Default configuration<br /> <br />? How do you want users to be able to sign in? \ <br />Username <br /><br />? Do you want to configure advanced settings? \ <br />No, I am done</pre>The `amplify add auth` command creates the necessary folders, files, and dependency files in a local folder (**amplify**) within the project’s root directory. For the ToDoList app setup used in this pattern, the **aws-exports.js** is created for this purpose. | App developer |
| Deploy the Amazon Cognito service to the AWS Cloud. | 1. From the project’s root directory, run the following Amplify CLI command:<br />`amplify push`<br />2. A prompt to confirm deployment appears. Enter **Yes**. Then, press **Enter**.To see the deployed services in your project, go to the Amplify console by running the following command:`amplify console` | App developer |
| Install the required Amplify libraries for React Native and the CocoaPods dependencies for iOS. | 1. Install the required Amplify open-source client libraries by running the following command from the project’s root directory:<br />`npm install aws-amplify aws-amplify-react-native \ amazon-cognito-identity-js @react-native-community/netinfo \ @react-native-async-storage/async-storage`<br />2. Install the required CocoaPods dependencies for iOS by running the following command:<br />`npx pod-install` | App developer |
| Import and configure the Amplify service. | In the app’s entry point file (for example,** App.js**), import and load the Amplify service’s configuration file by entering the following lines of code:<pre>import Amplify from 'aws-amplify'<br />import config from './src/aws-exports'<br />Amplify.configure(config)</pre>If you receive an error after importing the Amplify service in the app’s entry point file, stop the app. Then, open XCode and select the **ToDoListAmplify.xcworkspace** from the project’s iOS folder and run the app. | App developer |
| Update your app's entry point file to use the withAuthenticator Higher-order component (HOC). | The `withAuthenticator` HOC provides sign-in, sign-up, and forgot password workflows in your app by using only a few lines of code. For more information, see [Option 1: Use pre-build UI components](https://docs.amplify.aws/lib/auth/getting-started/q/platform/js/#option-1-use-pre-built-ui-components) in the Amplify Dev Center. Also, [Higher-order components](https://reactjs.org/docs/higher-order-components.html) in the React documentation.1. In the app’s entry point file (for example, **App.js**), import the `withAuthenticator` HOC by entering the following lines of code:<br />`import { withAuthenticator } from 'aws-amplify-react-native'`<br />2. Export the withAuthenticator HOC by entering the following code:<br />`export default withAuthenticator(App)`**withAuthenticator HOC code example**<pre>import Amplify from 'aws-amplify'<br />import config from './src/aws-exports'<br />Amplify.configure(config)<br />import { withAuthenticator } from 'aws-amplify-react-native';<br /><br /><br />const App = () => {<br />  return null;<br />};<br /><br /><br />export default withAuthenticator(App);</pre>In iOS Simulator, the app shows the login screen that’s provided by the Amazon Cognito service. | App developer |
| Test the authentication service setup. | In iOS Simulator, do the following:1. Create a new account in the app by using a real email address. A verification code is then sent to the registered email.<br />2. Verify the account set up by using the code that you receive in the verification email.<br />3. Enter the username and password that you created. Then, choose **Sign In**. A welcome screen appears.  You can also open the [Amazon Cognito console](https://console.aws.amazon.com/cognito/) and check if a new user has been created in the **Identity Pool** or not. | App developer |

### Connect an AWS AppSync API and DynamoDB database to the app
<a name="connect-an-aws-appsync-api-and-dynamodb-database-to-the-app"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an AWS AppSync API and DynamoDB database. | 1. Add an AWS AppSync API to your app and automatically provision a DynamoDB database by running the following Amplify CLI command from the project’s root directory:<br />`amplify add api`<br />2. A prompt appears that asks you to provide information about the API and database configuration settings. Enter the required information based on your use case. Then, press **Enter**. The Amplify CLI opens the GraphQL schema file in your text editor. For the ToDoList app setup used in this pattern, apply the following example configuration.<br />**Example API and database configuration settings**<pre>? Please select from one of the below mentioned services: \ <br />GraphQL <br /><br />? Provide API name: todolistamplify<br /><br />? Choose the default authorization type for the API \ <br />Amazon Cognito User Pool<br /><br />Do you want to use the default authentication and security configuration<br /><br />? Default configuration How do you want users to be able to sign in? \ <br />Username<br /><br />Do you want to configure advanced settings? \ <br />No, I am done.<br /><br />? Do you want to configure advanced settings for the GraphQL API \ <br />No, I am done.<br /><br />? Do you have an annotated GraphQL schema? \ <br />No<br /><br />? Choose a schema template: \ <br />Single object with fields (e.g., "Todo" with ID, name, description)<br /><br />? Do you want to edit the schema now? \ <br />Yes</pre><br />**Example GraphQL schema**<pre> type Todo @model {<br />   id: ID!<br />   name: String!<br />   description: String<br />}</pre> | App developer |
| Deploy the AWS AppSync API. | 1. In the project’s root directory, run the following Amplify CLI command:<br />`amplify push`<br />2. A prompt appears that asks you to provide more information about the API and database configuration settings. Enter the required information based on your use case. Then, press **Enter**. Your app can now interact with the AWS AppSync API. For the ToDoList app setup used in this pattern, apply the following example configuration.<br />**Example AWS AppSync API configuration settings**The following configuration creates the GraphQL API in AWS AppSync and a **Todo** table in Dynamo DB.<pre> ? Are you sure you want to continue? Yes<br />? Do you want to generate code for your newly created GraphQL API Yes<br />? Choose the code generation language target javascript<br />? Enter the file name pattern of graphql queries, mutations and subscriptions src/graphql/**/*.js<br />? Do you want to generate/update all possible GraphQL operations - \ <br />queries, mutations and subscriptions Yes<br />? Enter maximum statement depth \<br />[increase from default if your schema is deeply nested] 2</pre> | App developer |
| Connect the app's frontend to the AWS AppSync API. | To use the example ToDoList app provided in this pattern, copy the code from the **App.js** file in the [aws-amplify-react-native-ios-todo-app](https://github.com/aws-samples/aws-amplify-react-native-ios-todo-app) GitHub repository. Then, integrate the example code into your local environment.<br />The example code provided in the repository’s **App.js** file does the following:+ Shows the form for creating a **ToDo Item** with **Title **and **Description** fields<br />+ Displays the list of to-do items (**Title** and **Description**)<br />+ Posts and fetches data by using `aws-amplify` methods | App developer |

## Related resources
<a name="build-a-serverless-react-native-mobile-app-by-using-aws-amplify-resources"></a>
+ [AWS Amplify](https://aws.amazon.com/amplify/)
+ [Amazon Cognito](https://aws.amazon.com/cognito/)
+ [AWS AppSync](https://aws.amazon.com/appsync/)
+ [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
+ [React](https://reactjs.org/) (React documentation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
