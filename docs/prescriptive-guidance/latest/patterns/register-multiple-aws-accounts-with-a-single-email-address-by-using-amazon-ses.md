---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/register-multiple-aws-accounts-with-a-single-email-address-by-using-amazon-ses.html
---

# Register multiple AWS accounts with a single email address by using Amazon SES
<a name="register-multiple-aws-accounts-with-a-single-email-address-by-using-amazon-ses"></a>

*Joe Wozniak and Shubhangi Vishwakarma, Amazon Web Services*

## Summary
<a name="register-multiple-aws-accounts-with-a-single-email-address-by-using-amazon-ses-summary"></a>

This pattern describes how you can decouple real email addresses from the email address that’s associated with an AWS account. AWS accounts require a unique email address to be provided at the time of account creation. In some organizations, the team that manages AWS accounts must take on the burden of managing many unique email addresses with their messaging team. This can be difficult for large organizations that manage many AWS accounts. Additionally, if your email system doesn’t allow *plus addressing* or *sub-addressing* as defined in [Sieve Email Filtering: Subaddress Extension (RFC 5233)](https://datatracker.ietf.org/doc/html/rfc5233)—by adding a plus sign (\+) and an identifier to the end of the local part of the email address, such as `admin+123456789123@example.com`—this pattern can help overcome this limitation.

This pattern provides a unique email address vending solution that enables AWS account owners to associate one email address with multiple AWS accounts. The real email addresses of AWS account owners are then associated with these generated email addresses in a table. The solution handles all incoming email for the unique email accounts, looks up the owner of each account, and then forwards any received messages to the owner.

## Prerequisites and limitations
<a name="register-multiple-aws-accounts-with-a-single-email-address-by-using-amazon-ses-prereqs"></a>

**Prerequisites **
+ Administrative access to an AWS account.
+ Access to a development environment.
+ (Optional) Familiarity with AWS Cloud Development Kit (AWS CDK) workflows and the Python programming language will help you troubleshoot any issues or make modifications.

**Limitations **
+ Overall vended email address length of 64 characters. For details, see [CreateAccount](https://docs.aws.amazon.com/organizations/latest/APIReference/API_CreateAccount.html) in the *AWS Organizations API reference*.

**Product versions**
+ Node.js version 22.x or later
+ Python 3.13 or later
+ Python packages **pip** and **virtualenv**
+ AWS CDK CLI version 2.1019.2 or later
+ Docker 20.10.x or later

## Architecture
<a name="register-multiple-aws-accounts-with-a-single-email-address-by-using-amazon-ses-architecture"></a>

**Target technology stack  **
+ CloudFormation stack
+ AWS Lambda functions
+ Amazon Simple Email Service (Amazon SES) rule and rule set
+ AWS Identity and Access Management (IAM) roles and policies
+ Amazon Simple Storage Service (Amazon S3) bucket and bucket policy
+ AWS Key Management Service (AWS KMS) key and key policy
+ Amazon Simple Notification Service (Amazon SNS) topic and topic policy
+ Amazon DynamoDB table

**Target architecture **

![Target architecture for registering multiple AWS accounts with a single email address](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/1be85b92-69e5-43b2-aeed-27b9509e145e/images/c7ae9d7a-d4e0-412e-97cb-0f3073e012e7.png)

This diagram shows two flows:
+ **Email address vending flow: **In the diagram, the email address vending flow (lower section) begins typically with an account vending solution or outside automation, or is invoked manually. In the request, a Lambda function is called with a payload that contains the needed metadata. The function uses this information to generate a unique account name and email address, stores it in a DynamoDB database, and returns the values to the caller. These values can then be used to create a new AWS account (typically by using AWS Organizations).
+ **Email forwarding flow: **This flow is illustrated in the upper section of the previous diagram. When an AWS account is created by using the account email generated from the email address vending flow, AWS sends various emails, such as account registration confirmation and periodic notifications, to that email address. By following the steps in this pattern, you configure your AWS account with Amazon SES to receive emails for the entire domain. This solution configures forwarding rules that allow Lambda to process all incoming emails, check to see if the `TO` address is in the DynamoDB table, and forward the message to the account owner's email address instead. Using this process gives account owners the ability to associate multiple accounts with one email address.

**Automation and scale**

This pattern uses the AWS CDK to fully automate the deployment. The solution uses AWS managed services that will (or can be configured to) scale automatically to meet your needs. The Lambda functions might require additional configuration to meet your scaling needs. For more information, see [Understanding Lambda function scaling](https://docs.aws.amazon.com/lambda/latest/dg/invocation-scaling.html) in the Lambda documentation.

## Tools
<a name="register-multiple-aws-accounts-with-a-single-email-address-by-using-amazon-ses-tools"></a>

**AWS services**
+ [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell.
+ [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html) is a fully managed NoSQL database service that provides fast, predictable, and scalable performance.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) helps you create and control cryptographic keys to help protect your data.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Simple Email Service (Amazon SES)](https://docs.aws.amazon.com/ses/latest/dg/Welcome.html) helps you send and receive emails by using your own email addresses and domains.
+ [Amazon Simple Notification Service (Amazon SNS)](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) helps you coordinate and manage the exchange of messages between publishers and clients, including web servers and email addresses.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Tools needed for deployment**
+ Development environment with the AWS CLI and IAM access to your AWS account. For details, see the links in the [Related resources](#register-multiple-aws-accounts-with-a-single-email-address-by-using-amazon-ses-resources) section.
+ On your development system, install the following:
  + Git command line tool, available from the [Git downloads website](https://git-scm.com/downloads).
  + The AWS CLI to configure access credentials for the AWS CDK. For more information, see the [AWS CLI documentation](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html).
  + Python version 3.13 or later, available from the [Python downloads website](https://www.python.org/downloads/).
  + UV for Python package management. For installation instructions, see the [UV installation guide](https://docs.astral.sh/uv/getting-started/installation/).
  + Node.js version 22.x or later. For installation instructions, see the [Node.js documentation](https://nodejs.org/en/learn/getting-started/how-to-install-nodejs).
  + AWS CDK CLI version 2.1019.2 or later. For installation instructions, see the [AWS CDK documentation](https://docs.aws.amazon.com/cdk/v2/guide/getting-started.html#getting-started-install).
  + Docker version 20.10.x or later. For installation instructions, see the [Docker documentation](https://docs.docker.com/engine/install/).

**Code **

The code for this pattern is available in the GitHub [AWS account factory email](https://github.com/aws-samples/aws-account-factory-email) repository.

## Epics
<a name="register-multiple-aws-accounts-with-a-single-email-address-by-using-amazon-ses-epics"></a>

### Allocate a target deployment environment
<a name="allocate-a-target-deployment-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Identify or create an AWS account. | Identify an existing or new AWS account to which you have full administrative access, to deploy the email solution. | AWS administrator, Cloud administrator |
| Set up a deployment environment. | Configure an easy to use deployment environment and set up dependencies by following these steps:1. Set up your development environment with the tools listed in the [Tools section](#register-multiple-aws-accounts-with-a-single-email-address-by-using-amazon-ses-tools).<br />2. Clone the GitHub [AWS account factory email](https://github.com/aws-samples/aws-account-factory-email) repository code base to your development environment by using the command:<pre>git clone https://github.com/aws-samples/aws-account-factory-email</pre><br />3. In the `requirements.in` file (in the root of the repository), update the line that starts with `aws-cdk-lib==`  to match the latest version of the AWS CDK. To identify what the latest version is, run `npm view aws-cdk-lib` and look for the keyword "latest:".<br />4. If you made an update to the version in `requirements.in`, run the following command to update the `requirements.txt` file by using UV:<pre>uv pip compile requirements.in -o requirements.txt --python-version 3.13</pre> | AWS DevOps, App developer |

### Set up a verified domain
<a name="set-up-a-verified-domain"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Identify and allocate a domain. | The email forwarding functionality requires a dedicated domain. Identify and allocate a domain or subdomain that you can verify with Amazon SES. This domain should be available to receive incoming email within the AWS account where the email forwarding solution is deployed.<br />Domain requirements:+ The domain should be a standard domain or subdomain.<br />+ The domain should be externally DNS resolvable, because it will be used to receive emails from outside the organization. | Cloud administrator, Network administrator, DNS administrator |
| Verify the domain. | Verify that the identified domain can be used to accept incoming email.<br />Complete the instructions in [Verifying your domain for Amazon SES email receiving](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-verification.html) in the Amazon SES documentation. This will require coordination with the person or team who is responsible for the domain's DNS records. | App developer, AWS DevOps |
| Set up MX records. | Set up your domain with MX records that point to the Amazon SES endpoints in your AWS account and Region. For more information, see [Publishing an MX record for Amazon SES email receiving](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-mx-record.html) in the Amazon SES documentation. | Cloud administrator, Network administrator, DNS administrator |

### Deploy the email vending and forwarding solution
<a name="deploy-the-email-vending-and-forwarding-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Modify the default values in `cdk.json`. | Edit some of the default values in the `cdk.json` file (in the root of the repository) so that the solution will operate correctly after it is deployed.1. Modify the `SES_DOMAIN_NAME` value to match the domain name you verified previously.<br />2. Modify the `ADDRESS_FROM` value to include the same domain that is in `SES_DOMAIN_NAME`. The local part of the address should be determined by your cloud team. This address becomes the `FROM` address for every email that’s forwarded through the solution.<br />3. Modify the `ADDRESS_ADMIN` value to match the email address that any non-matching incoming messages will be forwarded to. This value must be a valid and operating email address. | App developer, AWS DevOps |
| Deploy the email vending and forwarding solution. | 1. Create a Python virtual environment:<pre>uv venv --python 3.13</pre><br />2. Activate the Python virtual environment:<pre>source .venv/bin/activate</pre><br />Or, on the Windows platform, use:<pre>% .venv\Scripts\activate.bat</pre><br />3. Install all Python requirements with no errors:<pre>uv pip install -r requirements.txt</pre><br />4. Synthesize the CloudFormation template:<pre>cdk synth</pre><br />Confirm that there are no errors and that the full CloudFormation template contains the expected output.<br />5. (Optional) If you are deploying the AWS CDK code into the current AWS account or Region for the first time, bootstrap the environment. For more information, see [AWS CDK Bootstrapping ](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html)in the AWS CDK documentation.<pre>cdk bootstrap aws://AWS-ACCOUNT-NUMBER/REGION</pre><br />Replace `AWS-ACCOUNT-NUMBER` and `REGION` with actual values.<br />6. Deploy the solution:<pre>cdk bootstrap<br />cdk deploy</pre><br />The commands should complete without errors. | App developer, AWS DevOps |
| Verify that the solution has been deployed. | Verify that the solution deployed successfully before you begin testing:1. Open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/) and look for a CloudFormation stack that contains the name `AwsMailFwdStack`.<br />2. Confirm that this `AwsMailFwdStack` stack has the following resources:Lambda functionsAmazon SES rule and rule setIAM roles and policiesAmazon S3 bucket and bucket policyAWS KMS key and key policyAmazon SNS topic and topic policyDynamoDB table | App developer, AWS DevOps |

### Verify that email vending and forwarding operate as expected
<a name="verify-that-email-vending-and-forwarding-operate-as-expected"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Verify that the API is working. | In this step, you submit test data to the solution's API and confirm that the solution produces the expected output and that backend operations have been performed as expected.<br />Manually run the **Vend Email** Lambda function by using test input. (For an example, see the [sample\_vend\_request.json file](https://github.com/aws-samples/aws-account-factory-email/blob/main/src/events/sample_vend_request.json).) For `OwnerAddress`, use a valid email address. The API should return an account name and account email with values as expected. | App developer, AWS DevOps |
| Verify that email is being forwarded. | In this step, you send a test email through the system and verify that the email is forwarded to the expected recipient.1. Obtain the account email from the last step.<br />2. Send an email to this address with a test subject and body text.<br />3. Confirm that you received the email at the account owner's email address.<br />4. Confirm that the email you received has a `FROM` address that matches the `ADDRESS_FROM` setting in `cdk.json`.<br />5. Confirm that the received email's subject and body are the same as the original sent message. | App developer, AWS DevOps |

## Troubleshooting
<a name="register-multiple-aws-accounts-with-a-single-email-address-by-using-amazon-ses-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| The system doesn’t forward email as expected. | Verify that your setup is correct:1. You should have completed the [Amazon SES verification process](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/receiving-email-verification.html) for your domain.<br />2. Your domain should be set up properly with MX records pointing to the Amazon SES endpoints in your AWS account and Region. For more information, see [Publishing an MX record for Amazon SES email receiving](https://docs.aws.amazon.com/ses/latest/dg/receiving-email-mx-record.html) in the Amazon SES documentation.<br />After you verify your domain setup, follow these steps:1. Open the [Amazon CloudWatch console](https://console.aws.amazon.com/cloudwatch/) for the account and Region where you deployed the solution, and navigate to CloudWatch log groups in the navigation pane.<br />2. Search the list of log groups for `SesMailForwardLogGroup`.<br />3. Investigate the logs in this group to see if any errors are generated during the email vending and forwarding process. |
| When you try to deploy the AWS CDK stack, you receive an error similar to:<br />"Template format error: Unrecognized resource types"  | In most instances, this error message means that the Region you’re targeting doesn’t have all the available AWS services. If you’re using an Amazon EC2 instance to deploy the solution, you might be targeting a Region that is different from the Region where the instance is running.By default, the AWS CDK deploys to the Region and account that you configured in the AWS CLI.<br />Possible solutions:1. Investigate if all the services needed for this solution (see the [Target technology stack](#register-multiple-aws-accounts-with-a-single-email-address-by-using-amazon-ses-architecture) section earlier in this pattern) are in the AWS Region you are targeting by reviewing [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/).<br />2. If you are using an EC2 instance and targeting a Region that’s different from the Region where your instance is running, make sure to set the `AWS_DEFAULT_REGION` environment variable, or set a Region with the AWS CLI before you deploy the solution. For more information, see the [Configuring environment variables for the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-envvars.html) in the AWS CLI documentation. Alternatively, you can modify the `app.py` file in the root of the repository to include a hard-coded account ID and Region by following the instructions in the [AWS CDK documentation for environments](https://docs.aws.amazon.com/cdk/v2/guide/environments.html). |
| When you deploy the solution, you receive the error message:<br />"Deployment failed: Error: AwsMailFwdStack: SSM parameter /cdk-bootstrap/hnb659fds/version not found. Has the environment been bootstrapped? Please run 'cdk bootstrap'" | If you have never deployed any AWS CDK resources to the AWS account and Region you’re targeting, you will have to first run the `cdk bootstrap` command as the error indicates. If you continue to receive this error after you run the bootstrapping command, you might be trying to deploy the solution to a Region that’s different from the Region where your development environment is running.<br />To solve this problem, set the `AWS_DEFAULT_REGION` environment variable or set a Region with the AWS CLI before you deploy the solution. Alternatively, you can modify the `app.py` file in the root of the repository to include a hard-coded account ID and Region by following the instructions in the [AWS CDK documentation for environments](https://docs.aws.amazon.com/cdk/v2/guide/environments.html). |

## Related resources
<a name="register-multiple-aws-accounts-with-a-single-email-address-by-using-amazon-ses-resources"></a>
+ For help installing the AWS CLI, see [Installing or updating to the latest version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html).
+ For help setting up the AWS CLI with IAM access credentials, see [Configuring settings for the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html).
+ For help with the AWS CDK, see [Getting started with the AWS CDK](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html#getting_started_install).

## Additional information
<a name="register-multiple-aws-accounts-with-a-single-email-address-by-using-amazon-ses-additional"></a>

**Costs**

When you deploy this solution, the AWS account holder might incur costs that are associated with the use of the following services.  It is important for you to understand how these services are billed so you are aware of any potential charges. For pricing information, see the following pages:
+ [Amazon SES pricing](https://aws.amazon.com/ses/pricing/)
+ [Amazon S3 pricing](https://aws.amazon.com/s3/pricing/)
+ [AWS KMS pricing](https://aws.amazon.com/kms/pricing/)
+ [AWS Lambda pricing](https://aws.amazon.com/lambda/pricing/)
+ [Amazon DynamoDB pricing](https://aws.amazon.com/dynamodb/pricing/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
