---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/launch-a-codebuild-project-across-aws-accounts-using-step-functions-and-a-lambda-proxy-function.html
---

# Launch a CodeBuild project across AWS accounts using Step Functions and a Lambda proxy function
<a name="launch-a-codebuild-project-across-aws-accounts-using-step-functions-and-a-lambda-proxy-function"></a>

*Richard Milner-Watts and Amit Anjarlekar, Amazon Web Services*

## Summary
<a name="launch-a-codebuild-project-across-aws-accounts-using-step-functions-and-a-lambda-proxy-function-summary"></a>

This pattern demonstrates how to asynchronously launch an AWS CodeBuild project across multiple AWS accounts by using AWS Step Functions and an AWS Lambda proxy function. You can use the pattern’s sample Step Functions state machine to test the success of your CodeBuild project.

CodeBuild helps you launch operational tasks using the AWS Command Line Interface (AWS CLI) from a fully-managed runtime environment. You can change the behavior of your CodeBuild project at runtime by overriding environment variables. Additionally, you can use CodeBuild to manage workflows. For more information, see [Service Catalog Tools](https://service-catalog-tools-workshop.com/tools.html) on the AWS Workshop website and [Schedule jobs in Amazon RDS for PostgreSQL using AWS CodeBuild and Amazon EventBridge](https://aws.amazon.com/blogs/database/schedule-jobs-in-amazon-rds-for-postgresql-using-aws-codebuild-and-amazon-eventbridge/) on the AWS Database Blog.

## Prerequisites and limitations
<a name="launch-a-codebuild-project-across-aws-accounts-using-step-functions-and-a-lambda-proxy-function-prereqs"></a>

**Prerequisites**
+ Two active AWS accounts: a source account for invoking a Lambda proxy function with Step Functions and a target account for building a remote CodeBuild sample project

**Limitations**
+ This pattern cannot be used to copy [artifacts](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codebuild-project-artifacts.html) between accounts.

## Architecture
<a name="launch-a-codebuild-project-across-aws-accounts-using-step-functions-and-a-lambda-proxy-function-architecture"></a>

The following diagram shows the architecture that this pattern builds.

![Architecture diagram of launching a CodeBuild project across multiple AWS accounts](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/809a5716-56e5-477c-aac6-02243675a2f2/images/857ba3ae-eb9a-4d6b-b73e-e596f41c8cb8.png)

The diagram shows the following workflow:

1. The Step Functions state machine parses the supplied input map and invokes the Lambda proxy function (`codebuild-proxy-lambda`) for each account, Region, and project you defined.

1. The Lambda proxy function uses AWS Security Token Service (AWS STS) to assume an IAM proxy role (`codebuild-proxy-role`), which is associated with an IAM policy (`codebuild-proxy-policy`) in the target account.

1. Using the assumed role, the Lambda function launches the CodeBuild project and returns the CodeBuild job ID. The Step Functions state machine loops and polls the CodeBuild job until receiving a success or failure status.

The state machine logic is shown in the following image.

![Workflow of Step Functions state machine](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/809a5716-56e5-477c-aac6-02243675a2f2/images/4729bbfc-79ad-455d-a85a-b96cce00f432.png)

**Technology stack**
+ AWS CloudFormation
+ CodeBuild
+ IAM
+ Lambda
+ Step Functions
+ X-Ray

## Tools
<a name="launch-a-codebuild-project-across-aws-accounts-using-step-functions-and-a-lambda-proxy-function-tools"></a>
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions.
+ [AWS CloudFormation Designer](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/working-with-templates-cfn-designer-json-editor.html) provides an integrated JSON and YAML editor that helps you view and edit CloudFormation templates.
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) is a fully managed build service that helps you compile source code, run unit tests, and produce artifacts that are ready to deploy.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) is a serverless orchestration service that helps you combine AWS Lambda functions and other AWS services to build business-critical applications.
+ [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) helps you collect data about the requests that your application serves, and provides tools that you can use to view, filter, and gain insights into that data to identify issues and opportunities for optimization.

**Code**

The sample code for this pattern is available in the GitHub [Cross Account CodeBuild Proxy](https://github.com/aws-samples/cross-account-codebuild-proxy) repository. This pattern uses the AWS Lambda Powertools for Python library to provide logging and tracing functionality. For more information on this library and its utilities, see [Powertools for AWS Lambda (Python)](https://docs.powertools.aws.dev/lambda/python/latest/).

## Best practices
<a name="launch-a-codebuild-project-across-aws-accounts-using-step-functions-and-a-lambda-proxy-function-best-practices"></a>

1. Adjust the wait time values in the Step Function state machine to minimize polling requests for job status. Use the expected execution time for the CodeBuild project.

1. Adjust the `MaxConcurrency` property of the map in Step Functions to control how many CodeBuild projects can run in parallel.

1. If required, review the sample code for production readiness. Consider what data might be logged by the solution and whether the default Amazon CloudWatch encryption is sufficient.

## Epics
<a name="launch-a-codebuild-project-across-aws-accounts-using-step-functions-and-a-lambda-proxy-function-epics"></a>

### Create the Lambda proxy function and associated IAM role in the source account
<a name="create-the-lambda-proxy-function-and-associated-iam-role-in-the-source-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Record the AWS account IDs. | AWS account IDs are required to set up access across accounts.<br />Record the AWS account ID for your source and target accounts. For more information, see [Finding your AWS account ID](https://docs.aws.amazon.com/IAM/latest/UserGuide/console_account-alias.html#FindingYourAWSId) in the IAM documentation. | AWS DevOps |
| Download the AWS CloudFormation templates. | 1. Download the `sample_target_codebuild_template.yaml` AWS CloudFormation template from the [GitHub repository](https://github.com/aws-samples/cross-account-codebuild-proxy) for this pattern.<br />2. Download the `codebuild_lambda_proxy_template.yaml` AWS CloudFormation template from the [GitHub repository](https://github.com/aws-samples/cross-account-codebuild-proxy) for this pattern.In the AWS CloudFormation templates, `<SourceAccountId>` is the AWS account ID for the source account, and `<TargetAccountId>` is the AWS account ID for the target account. | AWS DevOps |
| Create and deploy the AWS CloudFormation stack. | 1. Sign in to the AWS Management Console for your source account, open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/), and then choose **Stacks**.<br />2. Choose **Create Stack **and then choose **With new resources (standard)**.<br />3. For **Template source**, choose **Upload a template file**.<br />4. For **Upload a template** file, choose** file**, and then choose your downloaded `codebuild_lambda_proxy_template.yaml` file. Choose **Next**.<br />5. For **Stack name**, enter a name for the stack (for example, `codebuild-lambda-proxy`).<br />6. Replace the `crossAccountTargetRoleArn` parameter with your `<TargetAccountId>` (for example, `<arn:aws:iam::123456789012:role/proxy-lambda-codebuild-role>`). : You aren’t required to update the default value for the** **`targetCodeBuildProject` parameter.<br />7. Choose **Next**, accept the default stack creation options, and then chose **Next**.<br />8. Choose the **I acknowledge that AWS CloudFormation might create IAM resources with custom names **check box, and then choose **Create stack**.You must create the AWS CloudFormation stack for the proxy Lambda function before creating any resources in target accounts. When you create a trust policy in a target account, the IAM role is translated from the role name to an internal identifier. This is why the IAM role must already exist. | AWS DevOps |
| Confirm the creation of the proxy function and state machine. | 1. Wait for the AWS CloudFormation stack to reach **CREATE\_COMPLETE **status. This should take less than one minute.<br />2. Open the [AWS Lambda console](https://console.aws.amazon.com/lambda/), choose **Functions**, and then find the `lambda-proxy-ProxyLambda-<GUID>`** **function.<br />3. Open the [AWS Step Functions console](https://console.aws.amazon.com/states/), choose **state machines**, and then find the `sample-crossaccount-codebuild-state-machine` state machine. | AWS DevOps |

### Create an IAM role in the target account and launch a sample CodeBuild project
<a name="create-an-iam-role-in-the-target-account-and-launch-a-sample-codebuild-project"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create and deploy the AWS CloudFormation stack. | 1. Sign in to the AWS Management Console for your target account, open the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/), and then choose **Stacks**.<br />2. Choose **Create Stack** and then choose **With new resources (standard)**.<br />3. For **Template source**, choose **Upload a template file**.<br />4. For **Upload a template** file, choose **Choose file**, and then choose the `sample_target_codebuild_template.yaml` file. Choose **Next**.<br />5. For **Stack name**, enter a name for the stack (for example: `sample-codebuild-stack`).<br />6. Replace the `crossAccountSourceRoleArn` parameter with your `<SourceAccountId>` (for example, `<arn:aws:iam::123456789012:role/codebuild-proxy-lambda-role>`).<br />7. Choose **Next**, accept the default stack creation options, and then choose **Next**.<br />8. Choose the **I acknowledge that AWS CloudFormation might create IAM resources with custom names **check box, and then choose **Create stack**. | AWS DevOps |
| Verify the creation of the sample CodeBuild project.  | 1. Wait for the AWS CloudFormation stack to reach **CREATE\_COMPLETE** status. This should take less than one minute.<br />2. Open the [AWS CodeBuild console](https://console.aws.amazon.com/codesuite/codebuild/start) and then find the `sample-codebuild-project`** **project. | AWS DevOps |

### Test the cross-account Lambda proxy function
<a name="test-the-cross-account-lambda-proxy-function"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Launch the state machine. | 1. Sign in to the AWS Management Console for your source account, open the [AWS Step Functions console](https://console.aws.amazon.com/states/), and then choose **State machines**.<br />2. Choose the `sample-crossaccount-codebuild-state-machine` state machine and then choose **Start execution**.<br />3. In the **Input** editor, enter the following JSON, and replace `<TargetAccountID>` with the AWS account ID of the account that contains the CodeBuild project.<pre>{<br />  "crossAccountTargetRoleArns": [<br />    {<br />      "arn": "arn:aws:iam::<TargetAccountID>:role/proxy-lambda-codebuild-role",<br />      "region": "eu-west-1",<br />      "codeBuildProject": "sample-codebuild-project",<br />      "SampleValue1": "Value1",<br />      "SampleValue2": "Value2"<br />    }<br />  ]<br />}</pre>The key-value pairs are passed as environment variables from the function in the source account to the CodeBuild project in the target account.<br />4. Choose **Start execution**.<br />5. On the **Details** tab of the state machine page, check if** Execution Status** is set to **Succeeded**. This confirms that your state machine is running. **Note**: It can take around 30 seconds for the state machine to reach **Succeeded** status.<br />6. To see the output and input of a step in the state machine, expand that step in the **Execution event history** section. For example, expand the **Lambda - CodeBuild Proxy – Start **step. The output includes details on the overridden environment variables, the original payload, and the CodeBuild job ID. | AWS DevOps |
| Validate the environment variables. | 1. Sign in to the AWS Management Console for your target account.<br />2. Open the [AWS CodeBuild console](https://console.aws.amazon.com/codebuild/), expand **Build**, and then choose **Build projects**.<br />3. Choose the `sample-codebuild-project`** **project, and then choose **View details**.<br />4. On the **Build history **tab, choose the most recent build of the project, and then choose **View logs**.<br />5. In the log output, verify that the environment variables printed to STDOUT match the environment variables from the Step Functions sample state machine. | AWS DevOps |

## Troubleshooting
<a name="launch-a-codebuild-project-across-aws-accounts-using-step-functions-and-a-lambda-proxy-function-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Step Functions execution is taking longer than expected. | Adjust the `MaxConcurrency` property of the map in the Step Function state machine to control how many CodeBuild projects can run in parallel. |
| The execution of the CodeBuild jobs is taking longer than expected. | 1. Adjust the wait time values in the Step Functions state machine to minimize polling requests for job status. Use the expected execution time for the CodeBuild project.<br />2. Consider whether CodeBuild is the appropriate tool to be using. For example, the time required to initialize a CodeBuild job can be significantly longer than AWS Lambda. If high throughput and fast completion times are a requirement, consider migrating the business logic to AWS Lambda and using a fan-out architecture. |
