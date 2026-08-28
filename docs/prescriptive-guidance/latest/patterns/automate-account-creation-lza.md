---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-account-creation-lza.html
---

# Automate account creation by using the Landing Zone Accelerator on AWS
<a name="automate-account-creation-lza"></a>

*Justin Kuskowski, Joe Behrens, and Nathan Scott, Amazon Web Services*

## Summary
<a name="automate-account-creation-lza-summary"></a>

This pattern explains how to use the [Landing Zone Accelerator on AWS](https://aws.amazon.com/solutions/implementations/landing-zone-accelerator-on-aws/) solution to automatically deploy a new AWS account when an authorized user submits a request. It uses AWS Step Functions to orchestrate a number of AWS Lambda functions. The Lambda functions add the account information to a Git repository, initiate an AWS CodePipeline pipeline, and validate that the necessary AWS resources are provisioned. When the process is complete, the user receives a notification that the account has been created.

Optionally, you can integrate Microsoft Entra ID groups and assign AWS IAM Identity Center permission sets during the account creation process. If your organization is using Microsoft Entra ID as an identity source, this optional feature helps you automatically manage and configure access to the new account.

## Prerequisites and limitations
<a name="automate-account-creation-lza-prereqs"></a>

**Prerequisites**
+ Access to the management account in AWS Organizations
+ AWS Cloud Development Kit (AWS CDK) version 2.118.0 or later, [installed](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html#getting_started_install) and [configured](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html#getting_started_configure)
+ Python version 3.9 or later, [installed](https://www.python.org/downloads/)
+ AWS Command Line Interface (AWS CLI) version 2.13.19 or later, [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
+ Docker version 24.0.6 or later, [installed](https://docs.docker.com/get-started/get-docker/)
+ Landing Zone Accelerator on AWS solution, [deployed](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/deploy-the-solution.html) in the management account
+ (Optional) Microsoft Entra ID and IAM Identity Center, [integrated](https://docs.aws.amazon.com/singlesignon/latest/userguide/idp-microsoft-entra.html)

**Limitations**

The account creation workflow supports sequential executions to deploy a single AWS account. This limitation makes sure that the account creation workflow has successfully completed without having to compete for resources during a parallel run.

## Architecture
<a name="automate-account-creation-lza-architecture"></a>

**Target architecture**

The following image shows the high-level architecture of automating creation of a new AWS account by using the Landing Zone Accelerator on AWS. AWS Step Functions orchestrates the automation. Each task in the Step Functions workflow is performed by one or more AWS Lambda functions.

![Workflow to automate the creation of a new account by using the Landing Zone Accelerator on AWS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/d31abfaa-6854-4923-b896-3b817de9f4d9/images/dfd6503d-a4ed-43df-82d4-082f8153d473.png)

The diagram shows the following workflow:

1. The user requests an account by either running a Python script or by using Amazon API Gateway.

1. The Account Creation Orchestrator workflow starts in AWS Step Functions.

1. The workflow updates the `account-config.yaml` file in the source code repository. It also initiates the Landing Zone Accelerator on AWS pipeline and checks the status of the pipeline. This pipeline creates and sets up the new account. For more information about how this works, see the [Architecture overview](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/architecture-overview.html) for the Landing Zone Accelerator on AWS.

1. (Optional) When the pipeline is complete, the workflow checks whether the group exists in Microsoft Entra ID. If the group doesn’t exist in Microsoft Entra ID, the workflow adds the group to Microsoft Entra ID.

1. The workflow performs additional steps that the Landing Zone Accelerator on AWS solution can't do. The default steps include:
   + Creating an [account alias](https://docs.aws.amazon.com/IAM/latest/UserGuide/console-account-alias.html) in AWS Identity and Access Management (IAM)
   + Attaching [tags](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_tagging.html) to the account in AWS Organizations
   + Creating parameters in [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) based on the tags assigned to the account

1. (Optional) The workflow assigns one or more [permission sets](https://docs.aws.amazon.com/singlesignon/latest/userguide/permissionsetsconcept.html) to the Microsoft Entra ID group that you previously specified. The permission sets allow users in the group to access the new account and allow them to perform the actions you configure.

1. An AWS Lambda function runs QA and validation tests. It validates resource creation, checks that tags have been created, and validates that security resources have been deployed.

1. The workflow releases the account and uses Amazon Simple Email Service (Amazon SES) to notify the user that the process has completed successfully.

For more information about the Step Functions workflow, see *Step Functions workflow diagram* in the [Additional information](#automate-account-creation-lza-additional) section of this pattern.

**Microsoft Entra ID applications**

If you choose to integrate with Microsoft Entra ID, you create the following two applications when you deploy this pattern:
+ An application that is linked to IAM Identity Center and makes sure that Microsoft Entra ID groups are available in IAM Identity Center. In this example, this Microsoft Entra ID application is named `LZA2`.
+ An application that allows a Lambda function to communicate with Microsoft Entra ID and call the [Microsoft Graph APIs](https://learn.microsoft.com/en-us/graph/identity-network-access-overview). In this pattern, this application is named `create_aws_account`.

These applications collect data that is used to sync the Microsoft Entra ID group and assign permission sets.

## Tools
<a name="automate-account-creation-lza-tools"></a>

**AWS services**
+ [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) helps you create, publish, maintain, monitor, and secure REST, HTTP, and WebSocket APIs at any scale. In this pattern, you use API Gateway to check the availability of AWS account names, initiate the AWS Step Functions workflow, and check the status of the Step Functions execution.
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html) is a software development framework that helps you define and provision AWS Cloud infrastructure in code.
+ [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html) helps you set up and govern an AWS multi-account environment, following prescriptive best practices.
+ [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) is a serverless event bus service that helps you connect your applications with real-time data from a variety of sources. For example, AWS Lambda functions, HTTP invocation endpoints using API destinations, or event buses in other AWS accounts. This solution uses an [EventBridge rule](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-rules.html) that starts a Lambda function if the Step Functions workflow state changes to `Failed`, `Timed-out`, or `Aborted`.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) helps you centrally manage single sign-on (SSO) access to all of your AWS accounts and cloud applications.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data. In this pattern, AWS KMS keys are used to encrypt data, such as data stored in Amazon Simple Storage Service (Amazon S3), Lambda environment variables, and data in Step Functions.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) is an account management service that helps you consolidate multiple AWS accounts into an organization that you create and centrally manage.
+ [Amazon Simple Email Service (Amazon SES)](https://docs.aws.amazon.com/ses/latest/dg/Welcome.html) helps you send and receive emails by using your own email addresses and domains. After a new account is successfully created, you receive a notification through Amazon SES.
+ [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) helps you coordinate and manage the exchange of messages between publishers and clients, including web servers and email addresses. If an error occurs during the account creation process, Amazon SNS sends a notification to the email addresses that you configure.
+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) is a serverless orchestration service that helps you combine AWS Lambda functions and other AWS services to build business-critical applications.
+ [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) provides secure, hierarchical storage for configuration data management and secrets management.

**Other tools**
+ [awscurl](https://pypi.org/project/awscurl/0.6/) automates the process of signing AWS API requests and helps you make requests as a standard curl command.
+ [Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/whatis), formerly known as *Azure Active Directory*, is a cloud-based identity and access management service.
+ [Microsoft Graph APIs](https://learn.microsoft.com/en-us/graph/graph-explorer/graph-explorer-overview) help you access data and intelligence in Microsoft cloud services, such as Microsoft Entra and Microsoft 365.

**Code repository**

The code for this pattern is available in the GitHub [lza-account-creation-workflow](https://github.com/aws-samples/lza-account-creation-workflow) repository.

The [lambda\_layer](https://github.com/aws-samples/lza-account-creation-workflow/tree/main/app/lambda_layer) directory contains the following layers, which are referenced in more than one Lambda function:
+ [account\_creation\_helper](https://github.com/aws-samples/lza-account-creation-workflow/tree/main/app/lambda_layer/account_creation_helper) – This layer includes the modules for assuming roles and checking the progress in AWS Service Catalog.
+ [boto3](https://github.com/aws-samples/lza-account-creation-workflow/tree/main/app/lambda_layer/boto3) – This layer includes the [AWS SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) module to make sure that AWS Lambda has the latest version.
+ [identity\_center\_helper](https://github.com/aws-samples/lza-account-creation-workflow/tree/main/app/lambda_layer/identity_center_helper) – This layer supports calls to IAM Identity Center.

The [lambda\_src](https://github.com/aws-samples/lza-account-creation-workflow/tree/main/app/lambda_src) directory contains the following Lambda functions:
+ [AccountTagToSsmParameter](https://github.com/aws-samples/lza-account-creation-workflow/tree/main/app/lambda_src/event/AccountTagToSsmParameter) – This function uses the tags attached to the account in AWS Organizations in order to create parameters in Parameter Store. Each parameter starts with an `/account/tags/` prefix.
+ [AttachPermissionSet](https://github.com/aws-samples/lza-account-creation-workflow/tree/main/app/lambda_src/stepfunction/AttachPermissionSet) – This function adds a permission set to an IAM Identity Center group.
+ [AzureADGroupSync](https://github.com/aws-samples/lza-account-creation-workflow/tree/main/app/lambda_src/stepfunction/AzureADGroupSync) – This function syncs the target Microsoft Entra ID group to IAM Identity Center.
+ [CheckForRunningProcesses](https://github.com/aws-samples/lza-account-creation-workflow/tree/main/app/lambda_src/stepfunction/CheckForRunningProcesses) – This function checks whether the `AWSAccelerator-Pipeline` pipeline is currently running. If the pipeline is running, the function delays the AWS Step Functions workflow.
+ [CreateAccount](https://github.com/aws-samples/lza-account-creation-workflow/tree/main/app/lambda_src/stepfunction/CreateAccount) – This function uses AWS Service Catalog and AWS Control Tower to create the new AWS account.
+ [CreateAdditionalResources](https://github.com/aws-samples/lza-account-creation-workflow/tree/main/app/lambda_src/stepfunction/CreateAdditionalResources) – This function creates the AWS resources that aren't managed by Landing Zone Accelerator or AWS CloudFormation, such as the account alias and AWS Service Catalog tags.
+ [GetAccountStatus](https://github.com/aws-samples/lza-account-creation-workflow/tree/main/app/lambda_src/stepfunction/GetAccountStatus) – This function scans for the provisioned product in AWS Service Catalog to determine if the account creation process has completed.
+ [GetExecutionStatus](https://github.com/aws-samples/lza-account-creation-workflow/tree/main/app/lambda_src/api/GetExecutionStatus) – This function retrieves the status of a running or completed AWS Step Functions execution.
+ [NameAvailability](https://github.com/aws-samples/lza-account-creation-workflow/tree/main/app/lambda_src/api/NameAvailability) – This function checks if an AWS account name already exists in AWS Organizations.
+ [ReturnResponse](https://github.com/aws-samples/lza-account-creation-workflow/tree/main/app/lambda_src/stepfunction/ReturnResponse) – If the account creation was successful, this function returns the ID of the new account. If the account creation was not successful, it returns an error message.
+ [RunStepFunction](https://github.com/aws-samples/lza-account-creation-workflow/tree/main/app/lambda_src/api/RunStepFunction) – This function runs the AWS Step Functions workflow that creates the account.
+ [SendEmailWithSES](https://github.com/aws-samples/lza-account-creation-workflow/tree/main/app/lambda_src/stepfunction/SendEmailWithSES) – This function sends emails to the users who are waiting for the account creation to finish.
+ [ValidateADGroupSyncToSSO](https://github.com/aws-samples/lza-account-creation-workflow/tree/main/app/lambda_src/stepfunction/ValidateAdGroupSyncToSSO) – This function checks if the specified Microsoft Entra ID groups are synced with IAM Identity Center.
+ [ValidateResources](https://github.com/aws-samples/lza-account-creation-workflow/tree/main/app/lambda_src/stepfunction/ValidateResources) – This function validates that all AWS Control Tower customizations have run successfully.

## Best practices
<a name="automate-account-creation-lza-best-practices"></a>

We recommend the following naming conventions for the AWS CDK:
+ Start all parameters with a `p` prefix.
+ Start all conditions with a `c` prefix.
+ Start all resources with an `r` prefix.
+ Start all outputs with an `o` prefix.

## Epics
<a name="automate-account-creation-lza-epics"></a>

### Deploy the IAM roles for validation and tagging
<a name="deploy-the-iam-roles-for-validation-and-tagging"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Prepare the Landing Zone Accelerator on AWS for customization. | 1. In the Landing Zone Accelerator on AWS code repository, create a file named `customizations-config.yaml`. You use this file to define customizations for the core solution. For more information, see [Customizing the solution](https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/customizing-the-solution.html).<br />2. In the `customizations-config.yaml` file, create a section called `cloudFormationStacks`. | AWS DevOps |
| Prepare to deploy the `lza-account-creation-validation` role. | Now, you customize the solution to deploy the `lza-account-creation-validation` IAM role in all accounts other than the management account. This role provides the `ValidateResources` Lambda function with read-only access to the new accounts.1. Download the [account-creation-validation-role.yaml](https://github.com/aws-samples/lza-account-creation-workflow/blob/main/dependencies/account-creation-validation-role.yaml) file from GitHub.<br />2. Save the file to the location that is indicated in the templates section of the `customizations-config.yaml` file.<br />3. Open the `customizations-config.yaml` file.<br />4. In the `cloudFormationStacks` section, add the following code. Update the target AWS Region as needed for your landing zone:<pre>        - deploymentTargets:<br />            organizationalUnits:<br />              - Root<br />            excludedAccounts:<br />              - Management              <br />          description: IAM Role to allow Account Validation<br />          name: lza-account-creation-validation<br />          regions:<br />            - us-east-1<br />          template: cloudformation/account-creation-validation-role.yaml<br />          runOrder: 1 <br />          terminationProtection: true<br />          parameters:<br />            - name: pManagementAccountId<br />              value: "{{ account Management }}"</pre><br />5. Save and close the `customizations-config.yaml` file. | AWS DevOps |
| Prepare to deploy the `account-tagging-to-ssm-parameter-role` role. | Now, you customize the solution to deploy the `account-tagging-to-ssm-parameter-role` IAM role in all accounts other than the management account. This role is used to create the parameters in AWS Systems Manager Parameter Store.1. Download the [account-tagging-to-ssm-parameter-role.yaml](https://github.com/aws-samples/lza-account-creation-workflow/blob/main/dependencies/account-tagging-to-ssm-parameter-role.yaml) file from GitHub.<br />2. Save the file to the location that is indicated in the templates section of the `customizations-config.yaml` file.<br />3. Open the `customizations-config.yaml` file.<br />4. In the `cloudFormationStacks` section, add the following code. Update the target AWS Region as needed for your landing zone:<pre>        - deploymentTargets:<br />            organizationalUnits:<br />              - Root<br />            excludedAccounts:<br />              - Management<br />          description: IAM Role to create SSM Parameters based on Account Tagging<br />          name: lza-account-tagging-to-ssm-parameter<br />          regions:<br />            - us-east-1<br />          template: cloudformation/account-tagging-to-ssm-parameter-role.yaml<br />          runOrder: 1 <br />          terminationProtection: true          <br />          parameters:<br />            - name: pManagementAccountId<br />              value: "{{ account Management }}"</pre><br />5. Save and close the `customizations-config.yaml` file. | AWS DevOps |
| Prepare to deploy the `config-log-validation-role` role. | Now, you customize the solution to deploy the `config-log-validation-role` IAM role in the log archive account. This role allows the `ValidateResources` Lambda function to access the Amazon S3 bucket for logging and access AWS Config rules.1. Download the [config-log-validation-role.yaml](https://github.com/aws-samples/lza-account-creation-workflow/blob/main/dependencies/config-log-validation-role.yaml) file from GitHub.<br />2. Save the file to the location that is indicated in the templates section of the `customizations-config.yaml` file.<br />3. Open the `customizations-config.yaml` file.<br />4. In the `cloudFormationStacks` section, add the following code. Update the target AWS Region as needed for your landing zone:<pre>        - deploymentTargets:<br />            accounts:<br />              - LogArchive<br />          description: IAM Role to validate Config and Logs<br />          name: lza-config-log-validation-role<br />          regions:<br />            - us-east-1<br />          template: cloudformation/config-log-validation-role.yaml<br />          runOrder: 1 <br />          terminationProtection: true          <br />          parameters:<br />            - name: pManagementAccountId<br />              value: "{{ account Management }}"</pre><br />5. Save, close, and commit the changes made to the `customizations-config.yaml` file. | AWS DevOps |

### (Optional) Get data from Microsoft Entra ID
<a name="optional-get-data-from-microsoft-entra-id"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the application that that allows a Lambda function to communicate with Microsoft Entra ID. | 1. In the Microsoft Entra ID admin center, register the `create_aws_account` application. For instructions, see [Register an application](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app) in the Microsoft documentation.<br />2. Follow the instructions in [Update an app's requested permissions](https://learn.microsoft.com/en-us/entra/identity-platform/howto-update-permissions) in the Microsoft documentation to configure the following Microsoft Graph permissions for the `create_aws_account` application:[Application.Read.All](https://learn.microsoft.com/en-us/graph/permissions-reference#applicationreadall)Type: ApplicationAdmin consent required: Yes[AppRoleAssignment.ReadWrite.All](https://learn.microsoft.com/en-us/graph/permissions-reference#approleassignmentreadwriteall)Type: ApplicationAdmin consent required: Yes[Group.ReadWrite.All](https://learn.microsoft.com/en-us/graph/permissions-reference#groupreadwriteall)Type: ApplicationAdmin consent required: Yes[ServicePrincipalEndpoint.Read.All](https://learn.microsoft.com/en-us/graph/permissions-reference#serviceprincipalendpointreadall)Type: ApplicationAdmin consent required: Yes[Synchronization.ReadWrite.All](https://learn.microsoft.com/en-us/graph/permissions-reference#synchronizationreadwriteall)Type: ApplicationAdmin consent required: Yes[User.Read](https://learn.microsoft.com/en-us/graph/permissions-reference#userread)Type: DelegatedAdmin consent required: No | Microsoft Entra ID |
| Retrieve values for the `create_aws_account` application. | Now, you retrieve the values that you need for the `create_aws_account` application.1. In the Microsoft Entra ID admin center, navigate to **App registrations**, and then choose `create_aws_account`.<br />2. In the left pane, choose **Overview**.<br />3. On the **Overview** page, make note of the following values:Application (client) IDDirectory (tenant) ID<br />4. In the left pane, under **Manage**, choose **Certificates & secrets**.<br />5. On the **Certificates & secrets** page, choose the **Client secrets** tab, and then make note of the following values:Client secret valueClient secret ID | Microsoft Entra ID |
| Create the application that integrates Microsoft Entra ID with IAM Identity Center. | In the Microsoft Entra ID admin center, register the `LZA2` application. For instructions, see [Register an application](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app) in the Microsoft documentation. | Microsoft Entra ID |
| Retrieve values for the `LZA2` application. | Now, you retrieve the values that you need for the `LZA2` application.1. In the Microsoft Entra ID admin center, navigate to **Enterprise applications**, and then choose `LZA2`.<br />2. In the left pane, choose **Overview**.<br />3. On the **Overview** page, make note of the following values:NameObject ID<br />4. In the left pane, under **Manage**, choose **Manifest**.<br />5. In the JSON file, in the `appRoles` section, locate the app role named `User`.<br />6. Make note of the `id` value for this app role. | Microsoft Entra ID |
| Create a secret. | 1. In the AWS CLI, enter the following command to create the variables. Use the values that you retrieved for the `create_aws_account` and `LZA2` applications:<pre># Variables for create_aws_account app<br />  TENANT_ID='<Directory ID>'<br />  CLIENT_ID='<Application ID>'<br />  SECRET_ID='<Client secret ID>'<br />  SECRET_VALUE='<Client secret value>'<br /><br /># Variables for LZA2 app<br />  OBJECT_ID='<Object ID>'<br />  APP_ROLE_ID='<App role ID>'<br />  ENTERPRISE_APP_NAME='<Name>'</pre><br />2. Enter the following command to create a secret named `GraphApiSecret` in AWS Secrets Manager:<pre>aws secretsmanager create-secret \<br />  --name GraphApiSecret \<br />  --secret-string "{\"client_id\": \"${CLIENT_ID}\", \"tenant_id\": \"${TENANT_ID}\", \"object_id\": \"${OBJECT_ID}\", \"app_role_id\": \"${APP_ROLE_ID}\", \"secret_value\": \"${SECRET_VALUE}\", \"secret_id\": \"${SECRET_ID}\"}"</pre><br />If you need to update the secret in the future, you can update the variables and run the following command:<pre>aws secretsmanager update-secret \<br />  --secret-id GraphApiSecret \<br />  --secret-string "{\"client_id\": \"${CLIENT_ID}\", \"tenant_id\": \"${TENANT_ID}\", \"object_id\": \"${OBJECT_ID}\", \"app_role_id\": \"${APP_ROLE_ID}\", \"secret_value\": \"${SECRET_VALUE}\", \"secret_id\": \"${SECRET_ID}\"}"</pre> | AWS DevOps |

### Deploy the solution
<a name="deploy-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the source code. | 1. Enter the following command to clone the [lza-account-creation-workflow](https://github.com/aws-samples/lza-account-creation-workflow) repository:<pre>git clone https://github.com/aws-samples/lza-account-creation-workflow</pre><br />2. Enter the following command to navigate into the `config` directory of the cloned repository:<pre>cd lza-account-creation-workflow/config</pre> | DevOps engineer |
| Update the `deploy-config.yaml` file. | 1. Open the `deploy-config.yaml` file.<br />2. Review the template and update the values as needed for deployment in your AWS environment. For example, update values for the following:`accountCreationFailure``accountCompletionFromEmail``ssoLoginUrl``rootEmailPrefix``rootEmailDomain`<br />3. If you're integrating with Microsoft Entra ID, do the following:Set `enableAzureADIntegration` to `true`.For `graphApiSecretName` value, enter the secret that you created previously (`GraphApiSecret`).<br />4. Save and close the `deploy-config.yaml` file. | AWS DevOps |
| Deploy the solution in your AWS environment. | 1. Enter the following command:<pre>cdk bootstrap <account-number>/<Region></pre><br />For more information, see [Bootstrapping](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html) in the AWS CDK documentation.<br />2. Enter the following command to synthesize the CloudFormation template:<pre>cdk synth</pre><br />For more information, see [Configure and perform AWS CDK stack synthesis](https://docs.aws.amazon.com/cdk/v2/guide/configure-synth.html) in the AWS CDK documentation.<br />3. Enter the following command to deploy the solution.<pre>cdk deploy</pre><br />For more information, see [Deploy AWS CDK applications](https://docs.aws.amazon.com/cdk/v2/guide/deploy.html) in the AWS CDK documentation.This solution uses an Amazon S3 bucket to store the source code for this solution. You can use the [upload\_to\_source\_bucket.py](https://github.com/aws-samples/gen-ai-trivia/blob/main/scripts/upload_to_source_bucket.py) script to create an archive of the source code and upload an updated version. | AWS DevOps |

### Option 1 – Create an account using Python
<a name="option-1-create-an-account-using-python"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Identify which arguments to use. | Choose which arguments to use when you run the Python script that initiates the Step Functions workflow. For a complete list of arguments, see the [Additional information](#automate-account-creation-lza-additional) section of this pattern. | AWS DevOps, Python |
| Start the Python script. | 1. Enter the following command to navigate into the cloned repository:<pre>cd lza-account-creation-workflow</pre><br />2. Run the Python script that initiates the Step Functions workflow. The following is an example command that includes sample arguments and values:<pre>python ./run-stepfunction.py \<br />  --account-name "lza-test-01" \<br />  --support-dl "johnsmith@example.com" \<br />  --managed-org-unit "Workloads/Workload-1" \<br />  --purpose "Testing new micro service" \<br />  --force-update true \<br />  --ad-integration "{\"CustomerAccountAdmin\": \"platform-admin\", \"CustomerAccountDev\": \"workload1-app1\"}" \<br />  --bypass-creation true \<br />  --tags APPLICATION=TestingMicroService</pre><br />3. Wait until you receive a notification that the account has been successfully created.If the account creation process fails, Amazon SNS sends a notification to the email addresses that you define in `accountCreationFailure` in the `deploy-config.yaml` file. The account requester is not notified. | DevOps engineer, Python |

### Option 2 – Create an account using API Gateway and awscurl
<a name="option-2-create-an-account-using-api-gateway-and-awscurl"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the variables for awscurl. | 1. Enter the following command to navigate into the source code directory:<pre>cd lza-account-creation-workflow</pre><br />2. Enter the following command to set the AWS access key variables. You can copy the variables from the [AWS access portal](https://docs.aws.amazon.com/singlesignon/latest/userguide/using-the-portal.html) and then paste them into a shell. The following is an example:<pre>export AWS_ACCESS_KEY_ID="<id>"<br />export AWS_SECRET_ACCESS_KEY="<key>"<br />export AWS_SESSION_TOKEN="<token>"</pre><br />3. Enter the following command to set the AWS Region for API calls:<pre>export AWS_REGION=$(aws configure get region)</pre><br />4. Enter the following command to retrieve the API Gateway endpoint from the `lza-account-creation-workflow-application` CloudFormation output:<pre>export API_GATEWAY_ENDPOINT=$(aws cloudformation describe-stacks --stack-name "lza-account-creation-workflow-application" --query 'Stacks[*].Outputs[?OutputKey==`oApiGatewayCreateAccountEndpoint`].OutputValue' --output text)</pre> | AWS DevOps |
| Check name availability. | Enter the following command to verify that the name is available for the AWS account. Replace `<AWS_ACCOUNT_NAME>` with the name of the target account:<pre>awscurl --service execute-api \<br />    --region ${AWS_REGION} \<br />    --access_key ${AWS_ACCESS_KEY_ID} \<br />    --secret_key ${AWS_SECRET_ACCESS_KEY} \<br />    --security_token ${AWS_SESSION_TOKEN} \<br />    -X POST ${API_GATEWAY_ENDPOINT}check_name?account_name=<AWS_ACCOUNT_NAME></pre> | AWS DevOps |
| Run the account creation workflow. | 1. In the root folder of the cloned repository, open the `api_example.json` file.<br />2. Update the parameters with your configuration values:<pre>{<br />    "account_name": "lza-test-01",<br />    "account_email": "johnsmith+lzatest01@example.com",<br />    "support_dl": "johnsmith@example.com",<br />    "managed_org_unit": "Workloads/Workload-1",<br />    "ad_integration": [<br />        {<br />            "PermissionSetName": "CustomerAccountAdmin",<br />            "ActiveDirectoryGroupName": "platform-admin"<br />        },<br />        {<br />            "PermissionSetName": "CustomerAccountDev",<br />            "ActiveDirectoryGroupName": "workload1-app1"<br />        }<br />    ],<br />    "force_update": "true",<br />    "bypass_creation": "false",<br />    "account_tags": [<br />        {<br />            "Key": "Environment",<br />            "Value": "Dev"<br />        }, {<br />            "Key": "DeploymentMethod",<br />            "Value": "ApiGateway"<br />        }<br />    ]<br />}</pre><br />3. Save and close the `api_example.json` file.<br />4. Enter the following command to initiate the Step Functions workflow:<pre>awscurl --service execute-api \<br />    --data @api-example.json \<br />    --region ${AWS_REGION} \<br />    --access_key ${AWS_ACCESS_KEY_ID} \<br />    --secret_key ${AWS_SECRET_ACCESS_KEY} \<br />    --security_token ${AWS_SESSION_TOKEN} \<br />    -X POST ${API_GATEWAY_ENDPOINT}execute</pre><br />5. In the output from the previous command, make note of the Step Functions execution Amazon Resource Name (ARN).<br />6. If you want to check the status of the Step Functions workflow, enter the following command. Replace `<STEP_FUNCTION_EXECUTION_NAME>` with the Step Functions execution ARN or name:<pre>awscurl --service execute-api \<br />  --region ${AWS_REGION} \<br />  --access_key ${AWS_ACCESS_KEY_ID} \<br />  --secret_key ${AWS_SECRET_ACCESS_KEY} \<br />  --security_token ${AWS_SESSION_TOKEN} \<br />  -X GET ${API_GATEWAY_ENDPOINT}get_execution_status?execution=<STEP_FUNCTION_EXECUTION_NAME></pre><br />7. Wait until you receive a notification that the account has been successfully created.If the account creation process fails, Amazon SNS sends a notification to the email addresses that you define in `accountCreationFailure` in the `deploy-config.yaml` file. The account requester is not notified. | AWS DevOps |

### (Optional) Clean up the solution
<a name="optional-clean-up-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Remove objects from the Amazon S3 buckets. | Remove any objects in the following Amazon S3 buckets:+ `lza-account-creation-work-<CDK_UNIQUE_ID>`<br />+ `lza-account-creation-workflow-src-<AWS_REGION>-<AWS_ACCOUNT>`<br />+ `lza-account-creation-workflow-<AWS_REGION>-<AWS_ACCOUNT>` | AWS DevOps |
| Delete the CloudFormation stack. | Enter the following command to delete the CloudFormation stack:<pre>aws cloudformation delete-stack \<br />  --stack-name lza-account-creation-workflow-application<br />aws cloudformation wait stack-delete-complete \<br />  --stack-name lza-account-creation-workflow-application</pre> | AWS DevOps |
| Delete the pipeline. | Enter the following command to delete the `lza-account-creation-workflow-pipeline` pipeline:<pre>cdk destroy lza-account-creation-workflow-pipeline --force</pre> | AWS DevOps |

## Related resources
<a name="automate-account-creation-lza-resources"></a>
+ [Landing Zone Accelerator on AWS](https://aws.amazon.com/solutions/implementations/landing-zone-accelerator-on-aws/) (AWS Solutions Library)
+ [Troubleshooting common AWS CDK issues](https://docs.aws.amazon.com/cdk/v2/guide/troubleshooting.html) (AWS CDK documentation)

## Additional information
<a name="automate-account-creation-lza-additional"></a>

**Step Functions workflow diagram**

The following image shows the states in the Step Functions workflow.

![States in the Step Functions workflow.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/d31abfaa-6854-4923-b896-3b817de9f4d9/images/d93aa7bf-1144-4f25-9488-aacc534a7813.png)

**Arguments**

The following are the arguments that you can use when you run the Python script that initiates the Step Functions workflow.

The following arguments are required:
+ `account-name (-a)` (string) – The name of the new AWS account.
+ `support-dl (-s)` (string) – The email address that receives notification when the account creation process is complete.
+ `managed-org-unit (-m)` (string) – The managed [organizational unit (OU)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_getting-started_concepts.html#organizationalunit) that will contain the new account.

The following arguments are optional:
+ `ad-integration (-ad)` (string dictionary) – The Microsoft Entra ID group and assigned permission set. The following is an example of how to use this argument:

  ```
  --ad-integration "{\"<PermissionSetName>\": \"<EntraIdGroupName>\"}"
  ```
+ `account-email (-e)`** **(string) – The email address for the root user of the new AWS account.
**Note**
If this argument isn't used, an email address will be generated by using the values `rootEmailPrefix` and `rootEmailDomain` from the `configs/deploy-config.yaml` file. If an email address isn't provided, an email address is generated by using the following format: `rootEmailPrefix+accountName@rootEmailDomain`.
+ `region (-r)` (string) – The AWS Region where the Step Functions workflow was deployed. The default value is `us-east-1`.
+ `force-update (-f)` (string Boolean) – Enter `true` to force AWS Service Catalog to update the provisioned product.
+ `bypass-creation (-b)` (string Boolean) – Enter `true` to bypass adding the account to the `accounts-config.yaml` file and bypass running the `AWSAccelerator-Pipeline` pipeline. This argument is typically used to test the account creation workflow process or to run the rest of the Step Functions steps if an error occurs in the `Landing Zone Accelerator` pipeline.
+ `tags (-t)` (string) – Additional tags that you want to add to the AWS account. By default, the following tags are added: `account-name`, `support-dl`, and `purpose`. The following is an example of how to use this argument:

  ```
  --tags TEST1=VALUE1 TEST2=VALUE2
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
