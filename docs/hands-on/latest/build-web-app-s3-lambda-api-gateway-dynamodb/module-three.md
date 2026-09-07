---
source_url: https://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/module-three.html
---

# Task 3: Create a Data Table
<a name="module-three"></a>

|  |  |
| --- |--- |
| **Time to complete** | 5 minutes  |
| **Services used** | [AWS Amplify](https://aws.amazon.com/amplify/) <br />[AWS AppSync](https://aws.amazon.com/appsync/)  |
| **Get help** | [Troubleshooting Amplify](https://docs.amplify.aws/react/build-a-backend/troubleshooting/) <br />[Learn about Data](https://docs.amplify.aws/react/how-amplify-works/)  |

## Overview
<a name="overview"></a>

In this task, you will create a data model to persist data using a GraphQL API and Amazon DynamoDB.  Additionally, you will use AWS Identity and Access Management (IAM) authorization to securely give our services the required permissions to interact with each other. You will also allow the Lambda function you created in the previous task to use the GraphQL API to write to your newly created DynamoDB table using an IAM policy.

## Key concepts
<a name="key-concepts"></a>

**Amplify backend:** Amplify Gen 2 uses a full stack TypeScript developer experience (DX) for defining backends. Simply author app requirements like data models, business logic, and auth rules in TypeScript. Amplify automatically configures the correct cloud resources and deploys them to per-developer cloud sandbox environments for fast, local iteration.

## Implementation
<a name="implementation"></a>

### Step 1: Set up Amplify Data
<a name="set-up-amplify-data"></a>

1. Update the resource file

   On your local machine, navigate to the **amplify/data/resource.ts** file and **update** it with the code in [this file](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/getting-started/approved/assets/build-basic-web-app-tutorial-mod-3-resource-ts.pdf). Then, **save** the file.
   + This code will define the schema for the UserProfile data model using a per-owner authorization rule allow.owner() to restrict the expense record’s access to the creator of the record
   + It also uses the field profileOwner to track the ownership, and configures the authorization rule to allow the postConfirmation resource.
   + Granting access to resources creates environment variables for your function, such as the GraphQL API endpoint.
![The project folder structure in a web application tutorial, highlighting the 'resource.ts' TypeScript file within the 'data' and 'post-confirmation' directories under 'amplify/auth'.](https://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/uhi-basic-module-resource-file-bad-feefc.png)

1. Deploy sandbox

   **Open** a new terminal window, **navigate** to your app's root folder (**profilesapp**), and **run** the following command to deploy cloud resources into an isolated development space so you can iterate fast.

   ```
   npx ampx sandbox
   ```
![A terminal showing the 'npx ampx sandbox' command and options for starting sandbox mode for Amplify backend deployments. The image is part of an AWS Amplify tutorial for deploying web apps using sandbox environments.](https://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/ozuy-sandbox-terminal-ampx-command-options.png)

1. View confirmation message

   Once the cloud sandbox has been fully deployed, your terminal will display a **confirmation message**.
![A Mac terminal showing AWS Amplify profiles app configuration, CloudFormation stack ARN output, and sandbox deployment status. The console displays environment variables and completion messages for deploying an Amplify app using Node.js and AWS services.](https://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/mac-terminal-amplifylong-profiles.png)

1. Verify outputs file is added to your project

   Verify that the **amplify\_outputs.json** file was **generated and added** to your project.
![A file explorer showing the folder structure of a React project named 'profilesapp' with the file 'amplify_outputs.json' highlighted. This file is located in the root directory and is used for AWS Amplify configuration outputs.](https://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/file-explorer-folder-structure-react.png)

1. Generate GraphQL client code

   **Open** a new terminal window, **navigate** to your app's root folder(**profilesapp**), and **run** the following command to generate the GraphQL client code to call your data backend.
**Note**
You will need to **update** the following command to use the path to the **post-confirmation** folder that you created in the previous step. For example: **npx ampx generate graphql-client-code --out** ****amplify/auth/post-confirmation******/graphql.**

   ```
   npx ampx generate graphql-client-code --out <path-to-post-confirmation-handler-dir>/graphql
   ```

   Amplify will create the folder **amplify/auth/post-confirmation/graphql** where you will find the client code to connect to the GraphQL API.
![A directory structure for a project named 'profilesapp,' focusing on the 'amplify/auth/post-confirmation/graphql' folder, which contains TypeScript files: API.ts, mutations.ts, queries.ts, and subscriptions.ts. This image is used in Module 3 of a tutorial on building a basic web application, illustrating GraphQL integration in the project.](https://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/basic-module-graphql-fafff-directory.png)

### Step 2: Modify Lambda function to connect to the API
<a name="modify-lambda-function-to-connect-to-the-api"></a>
+ Modify the handler file

  On your local machine, navigate to the **amplify/auth/post-confirmation/handler.ts** file and **replace** the code with the code in [this file](https://d1.awsstatic.com/onedam/marketing-channels/website/aws/en_US/getting-started/approved/assets/build-basic-web-app-tutorial-mod-3-handler-ts.pdf). Then, **save** the file.

  This code configures the Amplify using the env variables and sets the authorization to use IAM. It then generates a data client using the generateClient() function. Finally, it uses the data client to create a user profile by setting the email and owner based on the attributes of the signed-up user.
![The folder structure of a web application project with the 'handler.ts' file highlighted in the 'amplify/auth/post-confirmation/graphql' directory, used in Module 3 of the Build a Basic Web Application tutorial.](https://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/urx-basic-module-handler-dffec-folder.png)

## Conclusion
<a name="conclusion"></a>

You have created a data table and configured a GraphQL API to persist data in an Amazon DynamoDB database. Then, you updated the Lambda function to use the API.
