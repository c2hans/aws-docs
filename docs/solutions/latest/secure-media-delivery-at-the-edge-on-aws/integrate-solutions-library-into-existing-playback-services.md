---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/integrate-solutions-library-into-existing-playback-services.html
---

# Integrate solution’s library into existing playback services
<a name="integrate-solutions-library-into-existing-playback-services"></a>

 Another option to add the token generation step into your workflow is to include the solutions’ library into your existing playback services. The library can be used in NodeJS runtimes and is available in the solution’s [source code repository](https://github.com/aws-solutions/secure-media-delivery-at-the-edge). There are no specific requirements or restrictions as to where you should be running your playback API services. Solution’s library contains a set of constructs and methods that interact directly with the specific components created in the base module of the solution. These components provide necessary data for the library to work (like token signing keys) and also accepts the inputs originated from the library calls (like information about session ID to be revoked). Conceptually, this is illustrated in the following diagram.

![Diagram of integrating solution library into existing playback service.](http://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/images/image23.png)

 **Integrating the library into generic environment**

 When integrating the solution’s library in your own generic compute environment in which you manage the application stack, complete the following steps to prepare your environment:

1.  Download the solutions’ library from the solution’s [source code repository](https://github.com/aws-solutions/secure-media-delivery-at-the-edge) available under the `/source/resources/sdk/node/v1/` path.

1.  Copy library’s files `aws-secure-media-delivery.js` and `package.json` into the `aws-secure-media-delivery` folder in your Node.js project folder

1.  Include the library in the `package.json` as a project’s dependency:

   ```
   "dependencies": {
       ...
       "aws-secure-media-delivery": "file:./aws-secure-media-delivery/"
   },
   ```

   And, install the dependencies running `npm install` command.

    In case the project has been already initialized and you want to add library to and existing project, run `npm install –save ./aws-secure-media-delivery`

1.  Import the library in your code:

   ```
   awsSDM = require('aws-secure-media-delivery');
   ```

 Use the library’s methods and constructs as instructed in NodeJS library reference to generate the token and revoke the sessions.

 **Integrating the library into Lambda functions**

 If your existing playback API services are implemented in the AWS environment with the use of Lambda services and you plan to integrate the solution’s library into an existing or new Lambda function, you can simplify the process of installing solution’s library into the NodeJS runtime by leveraging Lambda Layer created by the API module, which already includes the library.

1.  In your Lambda function configuration, under **Layers** select **Add a layer.**

1.  From **Choose a layer,** select **Custom layers**.

1.  From the **Custom layers** list, select the one which starts with **APIGenerateTokeyLayer**, largest version number from the **Version** selector, and choose **Add**.

1.  After adding the layer, you can import the solution’s library directly in your Lambda function code with:

   ```
   awsSDM = require('aws-secure-media-delivery');
   ```

 **Configuring library with the stack**

 After you have successfully added the solution’s library into your environment and imported it into your code, you must provide references to the solution stack that you launched in your AWS account. To allow the library methods to communicate and interact with the solution components deployed from the solution stack, look up the references of these component and provide them when utilizing library methods in your environment. Below are the references you can find in the output tab of the launched solution’s stack in CloudFormation configuration:
+  **Stack Name** – used in Secret class to derive the secrets names in Secrets Manager, where signing keys are stored. Stack name must be provided as an input parameter for the Secret’s constructor.
+  **SecretsPrimarySecret** and **SecretsSecondarySecret** – if you decide to use custom function for retrieving the signing keys from Secrets Manager the values corresponding to these outputs are secrets’ identifiers you can reference when making API calls to Secrets Manager.
+  **SessionRevoke** – a DynamoDB table name which is an entry point for submitting session IDs identified as suspicious one that should be processed for blocking. The name of that table has to be provided as an input parameter for the **initialize** method of Session class.

 Importantly, because solutions’ library interacts directly with AWS components which comprise the solution architecture, IAM permission model applies. When underlying AWS SDK methods are called from the library, there need to be AWS credentials set for the service clients to be able to initiate necessary API calls. Therefore, when running any process that runs the solution’s library code, you must make sure that the right AWS credentials are provided. Depending on the integration model, you have multiple options to ensure the right set of permissions are in use.

 **When using Lambda function**

 The common way for granting the right set of permission for a Lambda function which make API calls to other AWS services is to adjust [https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html) accordingly. If you are unsure and looking for minimal set of permissions for your Lambda function to work with the other elements of the stack, you can copy and include in execution role configuration the same policy as the one attached to the dedicated library’s role. You can find the role’s identifier in CloudFormation output under **RoleARN** key. Navigate to that role definition in IAM settings console and in the **Roles** page, select the role and you will find the policy under the **Permission Policy** tab.

 **When using solution’s library in any environment**

 If you run your playback API services in any generic environment, to be able to use the solution’s library you need to AWS Credentials available in this environment that AWS SDK underpinning solution’s library can assume. For more information about how to manage AWS credentials and profiles in your environment, refer to [Setting Credentials in Node.js](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/setting-credentials-node.html).

 Aside from the standard methods of supplying AWS credentials into NodeJS runtime as outlined in the documentation, the solution’s library also offers the ability to overwrite the permissions assumed in a standard way. When calling the library’s method that initiate service clients for AWS Secrets Manager and DynamoDB table, you can supply an input object in which you can reference specific profile, role, and region used by the underlying client created specifically for library’s operations. The object has following structure:

```
{
  region: [Region for the target service endpoint],
  profile: [Name of the profile, defined in local environment to be used],
  role: [ARN of the role to be assumed through AWS STS]
}
```

 When both profile and role properties are provided, profile takes precedence. Note, that in order to assume the role with the ARN specified, the default set of AWS credentials retrievable from the execution environment needs map to the right set of permissions allowing to perform **sts:AssumeRole** action against the referenced role. We recommend that when you decide to use the role, that you reference the role created when solution is deployed. You can find the created role ARN identifier in CloudFormation output tab of the deployed stack under RoleARN key.

 There are two methods in the solution’s library in which you can provide this object to override the role and target region assumed by AWS SDK through the standard procedure:

 **initSMClient({region: string, role: string, profile: string}) –** in Secrets class as an instance method. It initiates Secrets Manager client to retrieve the signing keys.

 **Session.initialize(revocationTable ,{region: string, role: string, profile: string}) –** in Session class, a class method used to create DynamoDB client which sends the details of the sessions to be revoked.
