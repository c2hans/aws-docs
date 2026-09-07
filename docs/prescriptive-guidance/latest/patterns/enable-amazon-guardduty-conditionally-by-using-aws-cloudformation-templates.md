---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/enable-amazon-guardduty-conditionally-by-using-aws-cloudformation-templates.html
---

# Enable Amazon GuardDuty conditionally by using AWS CloudFormation templates
<a name="enable-amazon-guardduty-conditionally-by-using-aws-cloudformation-templates"></a>

*Ram Kandaswamy, Amazon Web Services*

## Summary
<a name="enable-amazon-guardduty-conditionally-by-using-aws-cloudformation-templates-summary"></a>

[AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html), an infrastructure as code (IaC) tool, helps you to manage AWS resources through template-based deployments. CloudFormation is typically used to manage AWS resources. Using it to enable AWS services, such as [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html), can present unique challenges. GuardDuty is a threat detection service that continuously monitors your AWS accounts for malicious activity and unauthorized behavior. Unlike typical resources that can be created multiple times, GuardDuty is a service that needs to be enabled once per account and AWS Region. Traditional CloudFormation conditions support only static value comparisons, which makes it difficult to check the current state of services such as GuardDuty. If you attempt to enable GuardDuty through CloudFormation in an account where it's already active, the stack deployment fails. This can create operational challenges for DevOps teams that are managing multi-account environments.

This pattern introduces a solution to this challenge. It uses CloudFormation custom resources that are backed by [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) functions to perform dynamic state checks. The conditional logic enables GuardDuty only if it isn’t already enabled. It uses the stack outputs to record the GuardDuty status for future reference.

By following this pattern, you can automate GuardDuty deployments across your AWS infrastructure while maintaining clean, predictable CloudFormation stack operations. This approach is particularly valuable for organizations that are:
+ Managing multiple AWS accounts through IaC
+ Implementing security services at scale
+ Requiring idempotent infrastructure deployments
+ Automating security service deployments

## Prerequisites and limitations
<a name="enable-amazon-guardduty-conditionally-by-using-aws-cloudformation-templates-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An AWS Identity and Access Management (IAM) role that has permissions to create, update, and delete CloudFormation stacks
+ AWS Command Line Interface (AWS CLI), [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html#getting-started-install-instructions) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)

**Limitations**

If GuardDuty has been manually disabled for an AWS account or AWS Region, this pattern does not enable GuardDuty for that target account or Region.

## Architecture
<a name="enable-amazon-guardduty-conditionally-by-using-aws-cloudformation-templates-architecture"></a>

**Target technology stack**

The pattern uses CloudFormation for infrastructure as code (IaC). You use a CloudFormation custom resource backed by a Lambda function to achieve the dynamic service-enablement capability.

**Target architecture**

The following high-level architecture diagram shows the process of enabling GuardDuty by deploying a CloudFormation template:

![Using a CloudFormation stack to enable GuardDuty in an AWS account.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/3abd7cb7-0937-41fe-8eaa-79aedb182732/images/71624052-eebc-474a-9aa3-8606d87fc51d.png)

1. You deploy a CloudFormation template to create a CloudFormation stack.

1. The stack creates an IAM role and a Lambda function.

1. The Lambda function assumes the IAM role.

1. If GuardDuty is not already enabled on the target AWS account, the Lambda function enables it.

**Automation and scale**

You can use the AWS CloudFormation StackSet feature to extend this solution to multiple AWS accounts and AWS Regions. For more information, see [Working with AWS CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) in the CloudFormation documentation.

## Tools
<a name="enable-amazon-guardduty-conditionally-by-using-aws-cloudformation-templates-tools"></a>
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions.
+ [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) is a continuous security monitoring service that analyzes and processes logs to identify unexpected and potentially unauthorized activity in your AWS environment.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.

## Epics
<a name="enable-amazon-guardduty-conditionally-by-using-aws-cloudformation-templates-epics"></a>

### Create the CloudFormation template and deploy the stack
<a name="create-the-cfnshort-template-and-deploy-the-stack"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Store the code in Amazon S3. | 1. Copy the Python code in the [Additional information](#enable-amazon-guardduty-conditionally-by-using-aws-cloudformation-templates-additional) section of this pattern.<br />2. Paste the code in a text editor.<br />3. Save the file as `index.py`.<br />4. Upload the file to an Amazon Simple Storage Service (Amazon S3) bucket. For instructions, see [Uploading objects](https://docs.aws.amazon.com/AmazonS3/latest/userguide/upload-objects.html) in the Amazon S3 documentation. | AWS DevOps |
| Create the CloudFormation template. | 1. Open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/home). <br />2. In the left navigation pane, choose **Infrastructure Composer**.<br />3. If you don’t see a blank canvas, create a new project.<br />4. Drag and drop an AWS Lambda function onto the canvas.<br />5. In the template view, validate that a Lambda function and a log group are present.<br />6. Modify the `Runtime` of the Lambda function to the latest version of Python.<br />7. Validate that the `Handler` property has value of `index.lambda_handler.`<br />8. Configure the `CodeUri` property to be the Amazon S3 location where you uploaded the Python code. An example value is `s3://amzn-s3-demo-bucket/key-name`.<br />9. Add a `Policies` property for the resource. Follow security best practices to provide least privilege access permissions that allow CloudFormation and GuardDuty actions. For example, you could use the `AWSLambdaExecute` managed policy for logs and a custom `iam:CreateServiceLinkedRole` for GuardDuty.<br />10. Add custom resource definition to the snippet by navigating to the template view.<pre>CheckResourceExist:<br />    Type: 'Custom::LambdaCustomResource'<br />    Properties:<br />      ServiceToken: !GetAtt Function.Arn</pre><br />11. Save the template as `sample.yaml`. | AWS DevOps |
| Create the CloudFormation stack. | 1. In the AWS CLI, enter the following command. This creates a new CloudFormation stack using the `sample.yaml` file. For more information, see [Creating a stack](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-cli-creating-stack.html) in the CloudFormation documentation.<pre>aws cloudformation create-stack \<br />--stack-name guardduty-cf-stack \<br />--template-body file://sample.yaml</pre><br />2. Confirm the following value appears in the AWS CLI, indicating that the stack has been successfully created. The amount of time required to create the stack can vary.<pre>"StackStatus": "CREATE_COMPLETE",</pre> | AWS DevOps |
| Validate that GuardDuty is enabled for the AWS account. | 1. Sign in to the AWS Management Console and open the [GuardDuty console](https://console.aws.amazon.com/guardduty/).<br />2. Verify that the GuardDuty service is enabled. | Cloud administrator, AWS administrator |
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

## Additional information
<a name="enable-amazon-guardduty-conditionally-by-using-aws-cloudformation-templates-additional"></a>

**Python code**

```
import boto3
import os
import json
from botocore.exceptions import ClientError
import cfnresponse
guardduty=boto3.client('guardduty')
cfn=boto3.client('cloudformation')
def lambda_handler(event, context):
    print('Event: ', event)
    if 'RequestType' in event:
      if event['RequestType'] in ["Create","Update"]:
          enabled=False
          try:
            response=guardduty.list_detectors()
            if "DetectorIds" in response and len(response["DetectorIds"])>0:
              enabled="AlreadyEnabled"
            elif "DetectorIds" in response and len(response["DetectorIds"])==0:
              cfn_response=cfn.create_stack(
                StackName='guardduty-cfn-stack',
                TemplateBody='{ "AWSTemplateFormatVersion": "2010-09-09",    "Description": "Guard duty creation template",    "Resources": { "IRWorkshopGuardDutyDetector": {  "Type": "AWS::GuardDuty::Detector",    "Properties": {   "Enable": true  }   } } }'
                )
              enabled="True"
          except Exception as e:
              print("Exception: ",e)
          responseData = {}
          responseData['status'] = enabled
          cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData, "CustomResourcePhysicalID" )
      elif event['RequestType'] == "Delete":
          cfn_response=cfn.delete_stack(
                  StackName='guardduty-cfn-stack')
          cfnresponse.send(event, context, cfnresponse.SUCCESS, {})
```
