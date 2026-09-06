---
source_url: https://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/module-two.html
---

# Task 2: Build a Serverless Function
<a name="module-two"></a>

|  |  |
| --- |--- |
| **Time to complete** | 5 minutes  |
| **Services used** | [AWS Lambda](https://aws.amazon.com/lambda/) <br />[AWS Amplify](https://aws.amazon.com/amplify/)  |
| **Requires** | A text editor. Here are a few free ones: +  [Atom](https://atom.io/)  <br />+  [Notepad\+\+](https://notepad-plus-plus.org/)  <br />+  [Sublime](https://www.sublimetext.com/)  <br />+  [Vim](https://www.vim.org/)  <br />+  [Visual Studio Code](https://code.visualstudio.com/)   |
| **Get help** | [Learn more about functions](https://docs.amplify.aws/react/build-a-backend/functions/)  |

## Overview
<a name="overview"></a>

Now that you have a React web app, you will use AWS Amplify and AWS Lambda to configure a serverless function. This function is invoked after a signed-up user confirms their user account. AWS Lambda is a compute service that runs your code in response to events and automatically manages the compute resources, making it the fastest way to turn an idea into a modern, production, serverless applications.

## Key concepts
<a name="key-concepts"></a>

**Serverless function:** Piece of code that will be executed by a compute service, on demand.

## Implementation
<a name="implementation"></a>

### Step 1: Set up an Amplify Function
<a name="set-up-an-amplify-function"></a>

1. Create files

   On your local machine, navigate to the **profilesapp/amplify/auth** folder.

   **Create** a new folder inside the **amplify/auth** folder and name it ****post-confirmation****.

   **Create** the files named **resource.ts** and **handler.ts** inside the folder.
![A sample file structure for a basic web application tutorial, showing folders such as amplify, auth, and data, with TypeScript files like handler.ts and resource.ts highlighted under post-confirmation in the auth folder.](http://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/basic-file-structure-ace-sample-folders.png)

1. Update the resources file

   **Update** the **amplify/auth/post-confirmation/resource.ts** file with the following code to define the **postConfirmation** function. Then, **save** the file.

   ```
   import { defineFunction } from '@aws-amplify/backend';
   export const postConfirmation = defineFunction({
     name: 'post-confirmation',
   });
   ```
![The file structure for a web application project, highlighting the update to 'resource.ts' in the amplify/auth/post-confirmation directory. Used in the 'Build a Basic Web Application' tutorial.](http://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/basic-update-resource-file-structure.png)

1. Update the handler file

   **Update** the **amplify/auth/post-confirmation/handler.ts **file with the following code to define the function’s handler. Then, **save** the file.

   ```
   import type { PostConfirmationTriggerHandler } from "aws-lambda";
   export const handler: PostConfirmationTriggerHandler = async (event) => {
     return event;
   };
   ```
![The folder structure of a web application project, highlighting the 'handler.ts' file in the 'amplify/auth/post-confirmation' directory. This illustrates the step to update the handler file as part of building a basic web application tutorial.](http://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/fmpdokb-basic-update-handler-file-folder.png)

## Conclusion
<a name="conclusion"></a>

You have defined a Lambda function using Amplify.
