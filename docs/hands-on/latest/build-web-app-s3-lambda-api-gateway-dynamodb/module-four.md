---
source_url: https://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/module-four.html
---

# Task 4: Link a Serverless Function to a Web App
<a name="module-four"></a>

|  |  |
| --- |--- |
| **Minimum time to complete** | 10 minutes  |
| **Services used** | [AWS Amplify](https://aws.amazon.com/amplify/)  |
| **Get help** | [Troubleshooting Amplify](https://docs.amplify.aws/react/build-a-backend/troubleshooting/) <br />[Learn about Auth](https://docs.amplify.aws/react/build-a-backend/auth/)  |

## Overview
<a name="overview"></a>

In this task, you will update the Amplify Auth resources to use the Lambda function you created in the previous module as an Amazon Cognito post confirmation invocation. When the user completes the sign up, the function will use the GraphQL API and capture the user’s email into the DynamoDB table.

## Key concepts
<a name="key-concepts"></a>

**Lambda invocation:** The type of event that will make a Lambda (serverless) function run. This can be another AWS service or an external input.

## Implementation
<a name="implementation"></a>

### Step 1: Set up Amplify Auth
<a name="set-up-amplify-auth"></a>

By default, your auth resource is configured allowing the user to sign up using email, but you need to update the resource to invoke the previously created postConfirmation function.

1. Update the resource file

   On your local machine, navigate to the **amplify/auth/resource.ts** file and **update** it with the following code. Then, **save** the file.

   ```
   import { defineAuth } from '@aws-amplify/backend';
   import { postConfirmation } from './post-confirmation/resource';
   export const auth = defineAuth({
     loginWith: {
       email: true,
     },
     triggers: {
       postConfirmation
     }
   });
   ```
![The resource creation interface.](http://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/resource-creation-interface.png)

1. Start the sandbox, if necessary

   The sandbox will automatically get updated and redeployed once the file is updated. If the sandbox is not running, you can run the following command in a new terminal window to start it.

   ```
   npx ampx sandbox
   ```

1. View the confirmation message

   Once the cloud sandbox has been fully deployed, your terminal will display a **confirmation message**.
![Interface element requiring manual review.](http://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/interface-interface-element.png)

1. View the file

   The **amplify\_outputs.json** file will be **generated/updated** and **added** to your **profilesapp** project.
![Interface element requiring manual review.](http://docs.aws.amazon.com/hands-on/latest/build-web-app-s3-lambda-api-gateway-dynamodb/images/interface.png)

## Conclusion
<a name="conclusion"></a>

You used Amplify to configure auth and configured the Lambda function to be invoked when the user signs in to the app.
