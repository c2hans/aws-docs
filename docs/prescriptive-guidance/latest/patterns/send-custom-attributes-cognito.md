---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/send-custom-attributes-cognito.html
---

# Send custom attributes to Amazon Cognito and inject them into tokens
<a name="send-custom-attributes-cognito"></a>

*Carlos Alessandro Ribeiro and Mauricio Mendoza, Amazon Web Services*

## Summary
<a name="send-custom-attributes-cognito-summary"></a>

Sending custom attributes to an Amazon Cognito authentication process can provide additional context to an application, enable more granular access controls, and make it easier to manage user profiles and authentication requirements. These features are useful in a wide range of applications and scenarios, and they can help you improve the overall security and functionality of an application.

This pattern shows how to send custom attributes to an Amazon Cognito authentication process when an application needs to provide additional context to the [access token](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-the-access-token.html) or [identity (ID) token](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-the-id-token.html). You use the Node.js as the backend application. The application authenticates a user from an Amazon Cognito [user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html) and passes custom attributes that are needed for token generation. You can use [AWS Lambda triggers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-working-with-lambda-triggers.html) for Amazon Cognito to customize your authentication process without major code customization or significant effort.

**Important**
The code and samples in this pattern are not recommended for production workloads because they are intended for demonstration purposes only. For production workloads, additional configuration is required on the client side. Use this pattern as a reference for pilot or proof-of-concept purposes only.

## Prerequisites and limitations
<a name="send-custom-attributes-cognito-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ Permissions to create and manage Amazon Cognito user pools and AWS Lambda functions
+ AWS Command Line Interface (AWS CLI), [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
+ An integrated development environment (IDE) that supports Node.js
+ Node.js version 18 or later, [installed](https://nodejs.org/en/download/)
+ npm version 8 or later, [installed](https://docs.npmjs.com/getting-started)
+ TypeScript, [installed](https://www.typescriptlang.org/download/)

**Limitations**
+ This pattern is not applicable for application integration through the Client Credentials authentication flow.
+ The pre-token generation trigger can add or change only some attributes of the access token and identity token. For more information, see [Pre token generation Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-token-generation.html) in the Amazon Cognito documentation.

## Architecture
<a name="send-custom-attributes-cognito-architecture"></a>

**Target architecture**

The following diagram shows the target architecture for this pattern. It also shows how the Node.js application might work with a backend to update databases. However, the backend database updates are outside the scope of this pattern.

![A Node.js application issuing an access token with custom attributes to an Amazon Cognito user pool.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/9f0855e6-77f9-48c2-846e-f9c317127e1f/images/8c52c88b-8954-4b4c-aed3-fd8c22f84c1d.png)

The diagram shows the following workflow:

1. The Node.js application issues an access token with custom attributes to the Amazon Cognito user pool.

1. The Amazon Cognito user pool initiates the pre-token generation Lambda function, which customizes the access and ID tokens.

1. The Node.js application makes an API call through Amazon API Gateway.

**Note**
The other architectural components shown in this architecture are for example only and are out of scope for this pattern.

**Automation and scale**

You can automate the provisioning of Amazon Cognito user pools, AWS Lambda functions, database instances, and other resources by using [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html), the [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html), [HashiCorp Terraform](https://www.terraform.io/docs), or any supported infrastructure as code (IaC) tool. If you want to scale your deployments, use continuous integration and continuous delivery (CI/CD) pipelines, which help prevent errors associated with manual deployments.

## Tools
<a name="send-custom-attributes-cognito-tools"></a>

**AWS services**
+ [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) helps you create, publish, maintain, monitor, and secure REST, HTTP, and WebSocket APIs at any scale.
+ [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) provides authentication, authorization, and user management for web and mobile apps.
+ [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) is a fast and scalable container management service that helps you run, stop, and manage containers on a cluster.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS SDK for JavaScript](https://docs.aws.amazon.com/sdk-for-javascript/v3/developer-guide/welcome.html) provides a JavaScript API for AWS services. You can use it to build libraries or applications for Node.js or the browser.

**Other tools**
+ [Node.js](https://nodejs.org/en/docs/) is an event-driven JavaScript runtime environment that is designed for building scalable network applications.
+ [npm](https://docs.npmjs.com/about-npm) is a software registry that runs in a Node.js environment and is used to share or borrow packages and manage deployment of private packages.

## Best practices
<a name="send-custom-attributes-cognito-best-practices"></a>

We recommend that you implement the following best practices:
+ **Secrets and sensitive data** – Do not store secrets or sensitive data within the application. Use an external system that the application can pull the data from, such as [AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html), [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html), or [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html).
+ **Standardized deployment** – Use CI/CD pipelines to deploy your applications. You can use services such as [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) and [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html).
+ **Token expiration** – Set a short expiration date for the access token.
+ **Use a secure connection** – All communication between the client application and the backend should be encrypted by using SSL/TLS. Use [AWS Certificate Manager (ACM)](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) to generate and manage SSL/TLS certificates, and use [Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) or [Elastic Load Balancing ](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html)to handle SSL/TLS termination.
+ **Validate user input** – Make sure that all user input is validated to prevent injection attacks and other security vulnerabilities. Use input validation libraries and services such as Amazon API Gateway and [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html#waf-intro) to prevent common attack vectors.
+ **Use IAM roles** – Use [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) roles to control access to AWS resources and make sure that only authorized users have access. Follow the principle of least privilege and make sure that each user has only the necessary permissions to perform their role.
+ **Use a password policy** – Configure a password policy that meets your security requirements, such as minimum length, complexity, and expiration. Use Secrets Manager or AWS Systems Manager Parameter Store to store and manage passwords securely.
+ **Enable multi-factor authentication (MFA)** – Enable MFA for all users to provide an additional layer of security and reduce the risk of unauthorized access. Use [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) or Amazon Cognito to enable MFA and other authentication methods.
+ **Store sensitive information securely** – Store sensitive information, such as passwords and access tokens, securely by using [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) or other encryption services.
+ **Use strong authentication methods** – To increase the security of the authentication process, use strong authentication methods, such as biometric authentication or multi-factor authentication.
+ **Monitor for suspicious activity** – Use [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) and other monitoring tools to monitor for suspicious activity and potential security threats. Set up automated alerts for unusual activity, and use [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) or [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html) to detect potential threats.
+ **Regularly review and update security policies** – Regularly review and update your security policies and procedures to make sure that they meet your changing security requirements and best practices. Use AWS Config to track and audit changes to your security policies and procedures.
+ **Automated sign-up** – Do not enable automated sign-up to an Amazon Cognito user pool. For more information, see [Reduce risks of user sign-up fraud and SMS pumping with Amazon Cognito user pools](https://aws.amazon.com/blogs/security/reduce-risks-of-user-sign-up-fraud-and-sms-pumping-with-amazon-cognito-user-pools/) (AWS blog post).

For additional best practices, see [Security best practices for Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-security-best-practices.html) in the Amazon Cognito documentation.

## Epics
<a name="send-custom-attributes-cognito-epics"></a>

### Set up the AWS resources
<a name="set-up-the-aws-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a user pool. | 1. In a CLI terminal, enter the following command to create an Amazon Cognito user pool:<pre>aws cognito-idp create-user-pool \<br />   --pool-name <MyUserPool></pre><br />2. Enter the following command to create a client ID and secret that will be used with the SDK for JavaScript:<pre>aws cognito-idp create-user-pool-client \<br />   --user-pool-id <UserPoolID>  \<br />   --client-name <MyNewClient> \<br />   --no-generate-secret \<br />   --explicit-auth-flows "USER_PASSWORD_AUTH" "ADMIN_NO_SRP_AUTH"</pre>For more information and instructions for how to set up a user pool in the AWS Management Console, see [Getting started with user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/getting-started-user-pools.html) and [Add more features and security options to your user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-next-steps.html).To reduce costs, use the Essentials plan or Lite plan to test this pattern. For more information, see [Amazon Cognito pricing](https://aws.amazon.com/cognito/pricing/). | App developer, AWS DevOps |
| Add a user to the user pool. | Enter the following command to create one user in the Amazon Cognito user pool:<pre>aws cognito-idp sign-up \<br />   --client-id <ClientID> \<br />   --username <jane@example.com> \<br />   --password <PASSWORD> \<br />   --user-attributes Name="email",Value="<jane@example.com>" Name="name",Value="<Jane>"</pre> | App developer, AWS DevOps |
| Add the app client to the user pool. | 1. Navigate to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/).<br />2. Choose **User pools**.<br />3. Choose the user pool that you created previously.<br />4. Under **Define your application**, choose the **Application type** that best fits the application scenario that you want to create authentication and authorization services for.<br />5. In **Name your application**, enter a descriptive name or proceed with the default name.<br />6. Under **Add a return URL**, enter a redirect path to your application for after users complete authentication.<br />7. Choose **Create your application**. You can set up the advanced options after you create your app client. | AWS systems administrator, AWS administrator, AWS DevOps, App developer |
| Create a Lambda trigger for pre-token generation. | 1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions) of the Lambda console.<br />2. Choose **Create function**.<br />3. Select **Author from scratch**.<br />4. In the **Basic information** pane, for **Function name**, enter `myPreTokenGenerationLambdaFunction`.<br />5. For **Runtime**, choose **Node.js 22**.<br />6. Leave **architecture** set to **x86\_64**.<br />7. Choose **Create function**.<br />8. On the **Code** tab, under **Code Source**, enter the sample Lambda function from the [Additional resources](#send-custom-attributes-cognito-additional) section of this pattern. This Lambda function injects the custom attributes into the ID token and access token. | AWS DevOps, App developer |
| Customize the user pool workflow. | 1. Navigate to the [Amazon Cognito console](https://console.aws.amazon.com/cognito/).<br />2. Choose **User pools**.<br />3. Choose the user pool that you created previously.<br />4. In the left navigation pane, under **Authentication**, choose **Extensions**.<br />5. Choose **Add Lambda trigger**.<br />6. Add or edit a **Pre token generation trigger**.<br />7. For **Trigger type**, choose **Authentication**.<br />8. Under **Authentication**, choose **Pre token generation trigger**.<br />9. For **Assign Lambda function**, choose `myPreTokenGenerationLambdaFunction`.<br />10. Choose **Add Lambda trigger**.<br />11. Choose a **Trigger event version** of **Basic features \+ access token customization for user identities** or **Basic features \+ access token customization for user and machine identities**. This setting updates the request parameters that Amazon Cognito sends to your function to include fields for access token customization.For more information, see [Customizing user pool workflows with Lambda triggers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-working-with-lambda-triggers.html) in the Amazon Cognito documentation. | AWS DevOps, App developer |

### Create the Node.js application
<a name="create-the-node-js-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Node.js application. | 1. In a terminal, enter the following commands:<pre>mkdir my-app<br />cd my-app<br />npm init -y<br />npm install --save-dev typescript<br />npm i --save-dev @types/node<br />npm i amazon-cognito-identity-js<br />npx tsc --init<br />mkdir src<br />touch src/index.ts</pre><br />2. Modify the `package.json` file to include the TypeScript compilation scripts:<pre>"scripts": {<br />  "start": "node src/index.js",<br />  "build": "tsc"<br />},</pre> | App developer |
| Implement the authentication logic. | 1. Open the `index.ts` file.<br />2. Paste the sample Typescript provided in the [Additional resources](#send-custom-attributes-cognito-additional) section of this pattern.<br />3. Save and close the `index.ts` file.You can create your own TypeScript file or modify the sample provided as needed for your use case. | App developer |
| Configure the environment variables and configuration file. | In a terminal, enter the following commands to create the environment variables:<pre>export USERNAME="<COGNITO_USER_NAME>"<br />export PASSWORD="<COGNITO_USER_PASSWORD>"<br />export USER_POOL_ID="<COGNITO_USER_ID>"<br />export CLIENT_ID="<COGNITO_CLIENT_ID>"</pre>Do not hardcode secrets or expose your credentials. | App developer |
| Run the application. | Enter the following commands to run the application and confirm that it is working:<pre>npm run build<br />npm start</pre> | App developer |
| Confirm that the custom attributes are injected into the tokens. | Use the debugging features for your IDE to view the access and ID tokens. Confirm that the custom attributes were added. For sample tokens, see the [Additional information](#send-custom-attributes-cognito-additional) section of this pattern. | App developer |

## Troubleshooting
<a name="send-custom-attributes-cognito-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Invalid client ID when trying to authenticate the user | This error typically occurs when you are using a client ID with a generated client secret. You must create a client ID without a secret attached to it. For more information, see [Application-specific settings with app clients](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-client-apps.html). |

## Related resources
<a name="send-custom-attributes-cognito-resources"></a>
+ [Customizing user pool workflows with Lambda triggers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools-working-with-aws-lambda-triggers.html) (Amazon Cognito documentation)
+ [Pre token generation Lambda trigger](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-token-generation.html) (Amazon Cognito documentation)
+ [CognitoIdentityProviderClient](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/cognito-identity-provider/) (AWS SDK for JavaScript documentation)
+ [cognito-idp](https://awscli.amazonaws.com/v2/documentation/api/2.0.34/reference/cognito-idp/index.html#cli-aws-cognito-idp) (AWS CLI documentation)

## Additional information
<a name="send-custom-attributes-cognito-additional"></a>

**Sample TypeScript file**

The following code sample is a TypeScript file that invokes the authentication process by using an AWS SDK to send custom attributes to Amazon Cognito:

```
import * as AmazonCognitoIdentity from "amazon-cognito-identity-js";

const userPoolId: string = process.env.USER_POOL_ID ?? '';
const clientId: string = process.env.CLIENT_ID ?? '';

const poolData = {
  UserPoolId: userPoolId,
  ClientId: clientId
};
const userPool = new AmazonCognitoIdentity.CognitoUserPool(poolData);

export const loginWithCognitoSDK = function (userName: string, password: string) {
  const authenticationDetails = new AmazonCognitoIdentity.AuthenticationDetails({
    Username: userName,
    Password: password,
    ClientMetadata: {
        customGroup: "MyCustomGroup",
        customApplicationData: "Custom data from a custom application"
    }
  });
  const userData = {
    Username: userName,
    Pool: userPool
  };

  const cognitoUser = new AmazonCognitoIdentity.CognitoUser(userData);

  // Authenticate the user using the authenticationDetails object
  cognitoUser.authenticateUser(authenticationDetails, {
    onSuccess: function (result: any) {},
    onFailure: function (err: any) {},
  });
}
loginWithCognitoSDK(process.env.USERNAME ?? '', process.env.PASSWORD ?? '');
```

The sample uses the `AuthenticationDetails` model from the SDK for JavaScript to provide the username, password, and the `ClientMetadada`. After the authentication in Amazon Cognito, the client metadata can be retrieved from the access and ID tokens.

**Sample Lambda function**

The following code sample is a Lambda function that is linked to the [Pre-Generation Token](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools-working-with-aws-lambda-triggers.html) from Amazon Cognito. It helps you customize the access token and ID token that Amazon Cognito uses. The tokens are passed through the integrations between your architecture. This sample includes a custom claim attribute called `customApplicationData` and a custom group name called `MyCustomGroup`:

```
export const handler = async(event, context, callback) => {
    event.response = {
        claimsOverrideDetails: {
            claimsToAddOrOverride: { customApplicationData: event.request.clientMetadata.customApplicationData },
            groupOverrideDetails: { groupsToOverride: [event.request.clientMetadata.customGroup] }
        }
    };
    callback(null, event);
};
```

**Sample access token**

You can decode the access token to visualize the custom attributes that were added. The following is a sample access token:

```
{
  "sub": "6daf331f-4451-48b4-abde-774579299204",
  "cognito:groups": [
    "MyCustomGroup"
  ],
  "iss": "https://cognito-idp.<REGION>.amazonaws.com/<USERPOOL_ID>",
  "client_id": "<YOUR_CLIENT_ID>",
  "origin_jti": "acff7e91-09f9-4fde-8eec-38b0f8c47cdc",
  "event_id": "c5113a9c-1f01-435b-9b73-a5cd3e88514e",
  "token_use": "access",
  "scope": "aws.cognito.signin.user.admin",
  "auth_time": 1677979246,
  "exp": 1677982846,
  "iat": 1677979246,
  "jti": "5c9c2708-a871-4428-bd9b-18ad261bea90",
  "username": "<USER_NAME>"
}
```

**Sample ID token**

You can decode the access token to visualize the custom attributes that were added. The following is a sample access token:

```
{
  "sub": "6daf331f-4451-48b4-abde-774579299204",
  "cognito:groups": [
    "MyCustomGroup"
  ],
  "iss": "https://cognito-idp.<REGION>.amazonaws.com/<USERPOOL_ID>",
  "cognito:username": "<USER_NAME>",
  "origin_jti": "acff7e91-09f9-4fde-8eec-38b0f8c47cdc",
  "customApplicationData": "Custom data from a custom application",
  "aud": "<YOUR_CLIENT_ID>",
  "event_id": "c5113a9c-1f01-435b-9b73-a5cd3e88514e",
  "token_use": "id",
  "auth_time": 1677979246,
  "exp": 1677982846,
  "iat": 1677979246,
  "jti": "f7ca006b-f25b-44d2-a7a4-6e6423f4201f",
  "email": "<USER_EMAIL>"
}
```
