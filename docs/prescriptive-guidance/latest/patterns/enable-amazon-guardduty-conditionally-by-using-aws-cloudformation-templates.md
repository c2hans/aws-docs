---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/enable-amazon-guardduty-conditionally-by-using-aws-cloudformation-templates.html
---

# Enable Amazon GuardDuty conditionally by using AWS CloudFormation templates

*Ram Kandaswamy, Amazon Web Services*

## Summary
<a name="enable-amazon-guardduty-conditionally-by-using-aws-cloudformation-templates-summary"></a>

[Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) is a threat detection service that continuously monitors your AWS accounts for unauthorized activity and anomalous behavior. GuardDuty supports only one detector for each AWS account and AWS Region. If an AWS CloudFormation template declares a GuardDuty detector in an account and Region where GuardDuty is already enabled, creating the detector fails, and by default the stack rolls back. In multi-account environments, GuardDuty is often already enabled in some accounts, for example manually, by another team, or through AWS Organizations. As a result, you can't reliably deploy a single template across all accounts. CloudFormation conditions can't prevent this failure, because they compare only static values, such as parameters, and can't check whether a detector already exists.

This pattern prevents that failure. A CloudFormation custom resource backed by an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) function checks for an existing detector when you deploy the stack, and it creates a detector only if none exists. The same template deploys successfully whether or not GuardDuty is already enabled, and a stack output records whether GuardDuty was already enabled or the stack enabled it. You generate the function code and the template by using prompts with an AI coding assistant, such as Kiro, and you validate the generated code before you deploy it.

This approach is particularly valuable for organizations that are:
+ Managing multiple AWS accounts through infrastructure as code (IaC)
+ Implementing security services at scale
+ Requiring idempotent infrastructure deployments
+ Automating security service deployments

## Prerequisites and limitations
<a name="enable-amazon-guardduty-conditionally-by-using-aws-cloudformation-templates-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ Permissions to create, update, and delete AWS CloudFormation stacks and [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/) roles.
+ AWS Command Line Interface (AWS CLI), [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#getting-started-install-instructions) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
+ An AI coding assistant, such as Kiro.
+ The following validation tools, installed: cfn-lint, Checkov, and Bandit.

**Limitations**
+ If GuardDuty is suspended in an AWS account or Region, its detector still exists. This pattern reports the status as AlreadyEnabled and doesn't resume monitoring. To resume monitoring, enable GuardDuty in the GuardDuty console or by using the aws guardduty update-detector command.
+ If you disabled GuardDuty in an AWS account or Region, GuardDuty deleted its detector and findings. This pattern creates a new detector. This pattern doesn't restore findings from before you disabled GuardDuty.
+ If the stack output shows Created, deleting the stack also deletes the GuardDuty detector and turns off threat detection in that Region. If the output shows AlreadyEnabled, deleting the stack doesn't change GuardDuty.
+ Generated code varies by AI model and version. Review and validate the generated code before you deploy it.
+ CloudFormation limits inline Lambda code in a template (using the `ZipFile` property) to a 4 MB zip file.

<a name="limitations-replace"></a>

## Architecture
<a name="enable-amazon-guardduty-conditionally-by-using-aws-cloudformation-templates-architecture"></a>

**Target technology stack**

The pattern uses CloudFormation for infrastructure as code (IaC). You use a CloudFormation custom resource backed by a Lambda function to achieve the dynamic service-enablement capability.

**Target architecture**

The following high-level architecture diagram shows the process of enabling GuardDuty by deploying a CloudFormation template:

![Using a CloudFormation stack to enable GuardDuty in an AWS account.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/3abd7cb7-0937-41fe-8eaa-79aedb182732/images/71624052-eebc-474a-9aa3-8606d87fc51d.png)

1. You deploy a CloudFormation template to create a CloudFormation stack.

1. The stack creates an IAM role, a Lambda function, and a custom resource that invokes the function.

1. The Lambda function checks whether a GuardDuty detector exists in the account and Region.

1. If no detector exists, the function creates a separate stack, guardduty-cfn-stack, that contains the GuardDuty detector.

1. The function returns the GuardDuty status, which the stack shows as an output.

**Automation and scale**

You can use the AWS CloudFormation StackSet feature to extend this solution to multiple AWS accounts and AWS Regions. For more information, see [Working with AWS CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) in the CloudFormation documentation.

## Tools
<a name="enable-amazon-guardduty-conditionally-by-using-aws-cloudformation-templates-tools"></a>
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions.
+ [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) is a continuous security monitoring service that analyzes and processes logs to identify unexpected and potentially unauthorized activity in your AWS environment.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ Kiro is an agentic AI engineering system available through an [**IDE**](https://kiro.dev/ide/), [**CLI**](https://kiro.dev/cli/), [**web interface**](https://kiro.dev/web/), [**mobile app**](https://kiro.dev/mobile/), and [**Kiro Crew**](https://kiro.dev/crew/) that helps developers and teams build software more efficiently. (Recommended)
+ cfn-lint checks CloudFormation templates for syntax errors and property values that aren't valid. (Recommended)
+ Checkov is a static analysis tool that scans infrastructure as code for security and compliance misconfigurations. (Recommended)
+ Bandit is a static analysis tool that finds common security issues in Python code. (Recommended)

## Best practices
<a name="enable-amazon-guardduty-conditionally-by-using-aws-cloudformation-templates-best-practices"></a>
+ Review the generated code and confirm that it meets every requirement in the prompt before you deploy it.
+ Grant the Lambda function's role only the permissions that the function needs, scoped to the specific stack, log group, account, and Region.
+ Don't log the full custom resource event. It contains a presigned URL that anyone can use to send a response to AWS CloudFormation.
+ Deploy the stack in a test account first, and confirm that both stack creation and stack deletion complete successfully.
+ Use the GuardDutyStatus stack output to identify the accounts and Regions where this stack enabled GuardDuty.

## Epics
<a name="enable-amazon-guardduty-conditionally-by-using-aws-cloudformation-templates-epics"></a>

### Create the CloudFormation template and deploy the stack
<a name="create-the-cfnshort-template-and-deploy-the-stack"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Generate Python code using Kiro or another AI coding assistant | Use the following prompt, or a similar one, to generate the code. Save the file as index.py.<br />`Write a minimal Python AWS Lambda function for a CloudFormation custom resource. The code is embedded inline in the template (Code.ZipFile), so use the cfnresponse module. Handler: index.lambda_handler. It enables Amazon GuardDuty in the current Region only if no detector exists.`+ `Create: if guardduty.list_detectors() returns a detector, respond Status=AlreadyEnabled. Otherwise create a stack named guardduty-cfn-stack with one AWS::GuardDuty::Detector (Enable: true) and respond Status=Created.`<br />+ `Update: change nothing. Respond Status=AlreadyEnabled if a detector exists, otherwise Status=NotEnabled.`<br />+ `Delete: delete only guardduty-cfn-stack, and succeed if it doesn't exist.`<br />+ `The function timeout is 15 minutes. Wait for each stack operation to complete, but stop waiting in time to send a response before the function times out.`<br />+ `Always respond with PhysicalResourceId "guardduty-enablement".`<br />+ `Send exactly one response per invocation. On any error, send FAILED with the error message.`<br />+ `Don't log the event; it contains a presigned URL.` | AWS DevOps |
| Generate an AWS CloudFormation template | In the same AI coding assistant session, enter the following prompt. If you use a new session, provide index.py with the prompt. Save the template as sample.yaml.<br />`Write a CloudFormation template in YAML that deploys the Lambda function in index.py and invokes it as a custom resource.`+ `AWS::Lambda::Function with the code from index.py inline in Code.ZipFile, handler index.lambda_handler, the latest supported Python runtime, and Timeout 900.`<br />+ `An IAM role for the function, without RoleName. Attach a customer managed policy (AWS::IAM::ManagedPolicy) that grants only: guardduty:ListDetectors and guardduty:CreateDetector; guardduty:DeleteDetector on detectors in this account and Region; cloudformation:CreateStack, DeleteStack, and DescribeStacks on the guardduty-cfn-stack stack; iam:CreateServiceLinkedRole only for guardduty.amazonaws.com; and write access to the function's own log group.`<br />+ `A custom resource named CheckResourceExist whose ServiceToken is the function ARN.`<br />+ `An output named GuardDutyStatus that returns the custom resource's Status attribute.`<br />+ `Use AWS::Partition, AWS::Region, and AWS::AccountId instead of hard-coded values.` | AWS DevOps |
| Validate code and template | `cfn-lint sample.yaml`<br />`checkov -f sample.yaml --framework cloudformation`<br />`bandit index.py`<br />Resolve all errors and findings, and then save the updated files. |  |
| Create the CloudFormation stack. | 1. In the AWS CLI, enter the following command. This creates a new CloudFormation stack using the `sample.yaml` file. For more information, see [Creating a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-cli-creating-stack.html) in the CloudFormation documentation.<pre>aws cloudformation create-stack \<br />--stack-name guardduty-cf-stack \<br />--template-body file://sample.yaml</pre><br />2. Confirm the following value appears in the AWS CLI, indicating that the stack has been successfully created. The amount of time required to create the stack can vary.<pre>"StackStatus": "CREATE_COMPLETE",</pre> | AWS DevOps |
| Validate that GuardDuty is enabled for the AWS account. | 1. Sign in to the AWS Management Console and open the [GuardDuty console](https://console.aws.amazon.com/guardduty/). Verify that the GuardDuty service is enabled.<br />2. You can also use the AWS CLI to verify that Amazon GuardDuty is enabled:<br />`DETECTOR_ID=$(aws guardduty list-detectors \`<br />` --query "DetectorIds[0]" --output text)`<br />`aws guardduty get-detector \`<br />` --detector-id "$DETECTOR_ID" \`<br />` --query Status --output text` | Cloud administrator, AWS administrator |
| Configure additional accounts or Regions. | As needed for your use case, use the CloudFormation StackSet feature to extend this solution to multiple AWS accounts and AWS Regions. For more information, see [Working with AWS CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) in the CloudFormation documentation. | Cloud administrator, AWS administrator |

## Related resources
<a name="enable-amazon-guardduty-conditionally-by-using-aws-cloudformation-templates-resources"></a>

**References**
+ [AWS CloudFormation documentation](https://docs.aws.amazon.com/cloudformation/index.html)
+ [AWS Lambda resource type reference](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/AWS_Lambda.html)
+ [CloudFormation resource type: AWS::IAM::Role](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-iam-role.html)
+ [CloudFormation resource type: AWS::GuardDuty::Detector ](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-guardduty-detector.html)
+ [Four ways to retrieve any AWS service property using AWS CloudFormation](https://aws.amazon.com/blogs/mt/four-ways-to-retrieve-any-aws-service-property-using-aws-cloudformation-part-1/) (blog post)

**Tutorials and videos**
+ [Simplify Your Infrastructure Management Using AWS CloudFormation](https://www.youtube.com/watch?v=1h-GPXQrLZw) (Tutorial)
+ [Use Amazon GuardDuty and AWS Security Hub CSPM to secure multiple accounts](https://www.youtube.com/watch?v=Rg2ZzAAi1nY) (AWS re:Invent 2020)
+ [Best practices for authoring AWS CloudFormation](https://www.youtube.com/watch?v=bJHHQM7GGro) (AWS re:Invent 2019)
+ [Threat Detection on AWS: An Introduction to Amazon GuardDuty](https://www.youtube.com/watch?v=czsuZXQvD8E) (AWS re:Inforce 2019)
