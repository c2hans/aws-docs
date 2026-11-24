---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/awssupport-validate-fsxwindows-adconfig.html
---

# `AWSSupport-ValidateFSxWindowsADConfig`

 **Description**

 The `AWSSupport-ValidateFSxWindowsADConfig` runbook is used to validate the self-managed Active Directory (AD) configuration of an Amazon FSx for Windows File Server

 **How does it work?**

 The runbook `AWSSupport-ValidateFSxWindowsADConfig` executes the Amazon FSx validation script on the temporary Amazon Elastic Compute Cloud (Amazon EC2) Windows instance launched by the runbook on the Amazon FSx subnet. The script performs multiple checks to validate the network connectivity to self-managed AD/DNS servers and permissions of the Amazon FSx service account. The runbook can validate a failed or misconfigured Amazon FSx for Windows File Server or create a new Amazon FSx for Windows File Server with self-managed AD.

 By default, the runbook creates the Amazon EC2 Windows instance, security group for AWS Systems Manager (SSM) access, AWS Identity and Access Management (IAM) role and policy using CloudFormation on the Amazon FSx subnet. If you want to run the script on an existing Amazon EC2 instance, provide the ID in the parameter `InstanceId`. On successful execution, it deletes the CloudFormation resources. However, to retain the resources, set the `RetainCloudFormationStack` parameter to `true`.

 The CloudFormation template creates an IAM role on your behalf with required permissions to attach to the Amazon EC2 instance to run the Amazon FSx validation script. To specify an existing IAM instance profile for the temporary instance, use the `InstanceProfileName` parameter. The associated IAM role must contain the following permissions:
+ `ec2:DescribeSubnets` and `ec2:DescribeVpcs` permissions and the Amazon Managed Policy `AmazonSSMManagedInstanceCore`.
+ Permissions to get the Amazon FSx service account username and password from Systems Manager by calling the `GetSecretValue` API.
+ Permissions to put object in the Amazon Simple Storage Service (Amazon S3) bucket for the script output.

 **Prerequisites**

 The subnet where the temporary Amazon EC2 instance is created (or the existing instance provided in the `InstanceId` parameter) must allow access to the AWS Systems Manager, AWS Secrets Manager, and Amazon S3 endpoints in order to run the `AmazonFSxADValidation` script using SSM Run Command.

 **AWS Secrets Manager setup**

 The validation script connects to the Microsoft AD domain by retrieving the Amazon FSx service account username and password with a runtime call to Secrets Manager. Follow the steps in [Create an AWS Secrets Manager secret](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html) to create a new Secrets Manager secret. Make sure that the username and password are stored using a key/value pair in the format `{"username":"EXAMPLE-USER","password":"EXAMPLE-PASSWORD"}"`. Refer to [Authentication and access control for AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html) for information about securing access to secrets.

 For more information about the tool, refer to the `TROUBLESHOOTING.md` and `README.md` files in the [AmazonFSxADValidation](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/samples/AmazonFSxADValidation.zip) file.

 **Runbook execution**

 Execute the runbook with Amazon FSx ID or AD parameters. Following is the runbook workflow:
+ Gets the parameters from the Amazon FSx ID or uses the input AD parameters.
+ Creates the temporary validation Amazon EC2 Windows instance on the Amazon FSx subnet, security group for SSM access, IAM role and policy (conditional) using CloudFormation. If the `InstanceId` parameter is specified, it is used.
+ Downloads and executes the validation script on the target Amazon EC2 instance in Amazon FSx primary subnet.
+ Provides the AD validation result code in the automation output. Additionally, the complete script output is uploaded to the Amazon S3 bucket.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-ValidateFSxWindowsADConfig)

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Windows

**Parameters**

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+ `cloudformation:CreateStack`
+ `cloudformation:DeleteStack`
+ `cloudformation:DescribeStackEvents`
+ `cloudformation:DescribeStacks`
+ `ec2:AuthorizeSecurityGroupEgress`
+ `ec2:CreateLaunchTemplate`
+ `ec2:CreateSecurityGroup`
+ `ec2:CreateTags`
+ `ec2:DeleteLaunchTemplate`
+ `ec2:DeleteSecurityGroup`
+ `ec2:DescribeImages`
+ `ec2:DescribeInstances`
+ `ec2:DescribeKeyPairs`
+ `ec2:DescribeLaunchTemplateVersions`
+ `ec2:DescribeLaunchTemplates`
+ `ec2:DescribeSecurityGroups`
+ `ec2:DescribeSubnets`
+ `ec2:RevokeSecurityGroupEgress`
+ `ec2:RunInstances`
+ `ec2:TerminateInstances`
+ `fsx:DescribeFileSystems`
+ `iam:GetInstanceProfile`
+ `iam:PassRole`
+ `s3:GetAccountPublicAccessBlock`
+ `s3:GetBucketAcl`
+ `s3:GetBucketLocation`
+ `s3:GetBucketPolicyStatus`
+ `s3:GetBucketPublicAccessBlock`
+ `s3:GetEncryptionConfiguration`
+ `ssm:DescribeInstanceInformation`
+ `ssm:GetDocument`
+ `ssm:GetParameters`
+ `ssm:ListCommandInvocations`
+ `ssm:ListCommands`
+ `ssm:SendCommand`

 **Example IAM Policy for the Automation Assume Role**

**Note**
This policy assumes that you specify an existing instance profile in the `InstanceProfileName` parameter. The IAM role inside that instance profile must trust `ec2.amazonaws.com` and have the permissions listed for `InstanceProfileName` at the start of this page. If you specify an existing instance in `InstanceId`, the automation doesn't create an instance and doesn't use the instance profile. Before you run the automation, add the tag `CreatedBy` with the value `AWSSupport-ValidateFSxWindowsADConfig` to that instance. The example policy allows `ssm:SendCommand` only on instances with this tag.
If you leave `InstanceProfileName` and `InstanceId` empty, the automation creates an IAM role and instance profile on your behalf, which requires permissions to create and configure IAM resources that this policy doesn't grant.

In the following example, replace {{111122223333}} with your AWS account ID, {{FSxValidationInstanceProfile}} with the name of the instance profile that you pass in `InstanceProfileName`, and {{FSxValidationInstanceRole}} with the name of the IAM role inside that instance profile:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "ActionsWithoutResourceLevelPermissions",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstances",
                "ec2:DescribeImages",
                "ec2:DescribeKeyPairs",
                "ec2:DescribeLaunchTemplates",
                "ec2:DescribeLaunchTemplateVersions",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeSubnets",
                "fsx:DescribeFileSystems",
                "ssm:DescribeInstanceInformation",
                "ssm:ListCommandInvocations",
                "ssm:ListCommands"
            ],
            "Resource": "*"
        },
        {
            "Sid": "CloudFormationStack",
            "Effect": "Allow",
            "Action": [
                "cloudformation:CreateStack",
                "cloudformation:DeleteStack",
                "cloudformation:DescribeStackEvents",
                "cloudformation:DescribeStacks"
            ],
            "Resource": "arn:aws:cloudformation:*:{{111122223333}}:stack/AWSSupport-ValidateFSxWindowsADConfig-*"
        },
        {
            "Sid": "ReadRunbookAttachment",
            "Effect": "Allow",
            "Action": "ssm:GetDocument",
            "Resource": "arn:aws:ssm:*:*:document/AWSSupport-ValidateFSxWindowsADConfig"
        },
        {
            "Sid": "ReadWindowsAmiParameter",
            "Effect": "Allow",
            "Action": "ssm:GetParameters",
            "Resource": "arn:aws:ssm:*::parameter/aws/service/ami-windows-latest/*"
        },
        {
            "Sid": "CreateTaggedLaunchTemplate",
            "Effect": "Allow",
            "Action": "ec2:CreateLaunchTemplate",
            "Resource": "arn:aws:ec2:*:{{111122223333}}:launch-template/*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/CreatedBy": "AWSSupport-ValidateFSxWindowsADConfig"
                }
            }
        },
        {
            "Sid": "CreateTaggedSecurityGroup",
            "Effect": "Allow",
            "Action": "ec2:CreateSecurityGroup",
            "Resource": "arn:aws:ec2:*:{{111122223333}}:security-group/*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/CreatedBy": "AWSSupport-ValidateFSxWindowsADConfig"
                }
            }
        },
        {
            "Sid": "CreateSecurityGroupInVpc",
            "Effect": "Allow",
            "Action": "ec2:CreateSecurityGroup",
            "Resource": "arn:aws:ec2:*:{{111122223333}}:vpc/*"
        },
        {
            "Sid": "RunInstancesWithAmazonImage",
            "Effect": "Allow",
            "Action": "ec2:RunInstances",
            "Resource": "arn:aws:ec2:*::image/*",
            "Condition": {
                "StringEquals": {
                    "ec2:Owner": "amazon"
                }
            }
        },
        {
            "Sid": "RunInstancesResources",
            "Effect": "Allow",
            "Action": "ec2:RunInstances",
            "Resource": [
                "arn:aws:ec2:*:{{111122223333}}:key-pair/*",
                "arn:aws:ec2:*:{{111122223333}}:launch-template/*",
                "arn:aws:ec2:*:{{111122223333}}:network-interface/*",
                "arn:aws:ec2:*:{{111122223333}}:security-group/*",
                "arn:aws:ec2:*:{{111122223333}}:subnet/*",
                "arn:aws:ec2:*:{{111122223333}}:volume/*"
            ]
        },
        {
            "Sid": "RunTaggedInstance",
            "Effect": "Allow",
            "Action": "ec2:RunInstances",
            "Resource": "arn:aws:ec2:*:{{111122223333}}:instance/*",
            "Condition": {
                "StringEquals": {
                    "aws:RequestTag/CreatedBy": "AWSSupport-ValidateFSxWindowsADConfig"
                }
            }
        },
        {
            "Sid": "TagOnCreateOnly",
            "Effect": "Allow",
            "Action": "ec2:CreateTags",
            "Resource": [
                "arn:aws:ec2:*:{{111122223333}}:instance/*",
                "arn:aws:ec2:*:{{111122223333}}:launch-template/*",
                "arn:aws:ec2:*:{{111122223333}}:network-interface/*",
                "arn:aws:ec2:*:{{111122223333}}:security-group/*",
                "arn:aws:ec2:*:{{111122223333}}:volume/*"
            ],
            "Condition": {
                "StringEquals": {
                    "ec2:CreateAction": [
                        "CreateLaunchTemplate",
                        "CreateSecurityGroup",
                        "RunInstances"
                    ]
                }
            }
        },
        {
            "Sid": "ManageTaggedResources",
            "Effect": "Allow",
            "Action": [
                "ec2:AuthorizeSecurityGroupEgress",
                "ec2:DeleteLaunchTemplate",
                "ec2:DeleteSecurityGroup",
                "ec2:RevokeSecurityGroupEgress",
                "ec2:TerminateInstances"
            ],
            "Resource": [
                "arn:aws:ec2:*:{{111122223333}}:instance/*",
                "arn:aws:ec2:*:{{111122223333}}:launch-template/*",
                "arn:aws:ec2:*:{{111122223333}}:security-group/*"
            ],
            "Condition": {
                "StringEquals": {
                    "aws:ResourceTag/CreatedBy": "AWSSupport-ValidateFSxWindowsADConfig"
                }
            }
        },
        {
            "Sid": "ReadInstanceProfile",
            "Effect": "Allow",
            "Action": "iam:GetInstanceProfile",
            "Resource": "arn:aws:iam::{{111122223333}}:instance-profile/{{FSxValidationInstanceProfile}}"
        },
        {
            "Sid": "AllowPassRoleToEC2",
            "Effect": "Allow",
            "Action": "iam:PassRole",
            "Resource": "arn:aws:iam::{{111122223333}}:role/{{FSxValidationInstanceRole}}",
            "Condition": {
                "StringEquals": {
                    "iam:PassedToService": "ec2.amazonaws.com"
                }
            }
        },
        {
            "Sid": "SSMSendCommand",
            "Effect": "Allow",
            "Action": "ssm:SendCommand",
            "Resource": "arn:aws:ssm:*::document/AWS-RunPowerShellScript"
        },
        {
            "Sid": "SSMSendCommandOnlyFsxInstance",
            "Effect": "Allow",
            "Action": "ssm:SendCommand",
            "Resource": "arn:aws:ec2:*:{{111122223333}}:instance/*",
            "Condition": {
                "StringLike": {
                    "ssm:resourceTag/CreatedBy": [
                        "AWSSupport-ValidateFSxWindowsADConfig"
                    ]
                }
            }
        },
        {
            "Sid": "CheckResultsBucket",
            "Effect": "Allow",
            "Action": [
                "s3:GetBucketAcl",
                "s3:GetBucketLocation",
                "s3:GetBucketPolicyStatus",
                "s3:GetBucketPublicAccessBlock",
                "s3:GetEncryptionConfiguration"
            ],
            "Resource": "arn:aws:s3:::{{amzn-s3-demo-bucket}}"
        },
        {
            "Sid": "S3AccountPublicAccessBlock",
            "Effect": "Allow",
            "Action": "s3:GetAccountPublicAccessBlock",
            "Resource": "*"
        }
    ]
}
```

 **Instructions**

Follow these steps to configure the automation:

1. Navigate to [`AWSSupport-ValidateFSxWindowsADConfig`](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-ValidateFSxWindowsADConfig/description) in Systems Manager under Documents.

1. Select **Execute automation.**

1. To validate self-managed AD with an existing failed or misconfigured Amazon FSx, enter the following parameters:
   + **AutomationAssumeRole (Optional):**

     The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user who starts this runbook.
   + **FSxId (Conditional):**

     The Amazon FSx for Windows File Server ID. This is required to validate existing failed or misconfigured Amazon FSx.
   + **SecretArn (Required):**

     The ARN of your Secrets Manager secret containing the Amazon FSx service account username and password. Make sure that the username and password are stored using a key/value pair in the format `{"username":"EXAMPLE-USER","password":"EXAMPLE-PASSWORD"}`. The CloudFormation stack creates the validation instance with permissions to perform `GetSecretValue` to this ARN.
   + **FSxSecurityGroupId (Required):**

     The security group ID for the Amazon FSx for Windows File Server.
   + **BucketName (Required):**

     The Amazon S3 bucket to upload the validation results to. Make sure that the bucket is configured with server-side encryption (SSE) and the bucket policy does not grant unnecessary read/write permissions to parties that do not need to access the logs. Also make sure that the Amazon EC2 Windows instance has necessary access to the Amazon S3 bucket.
![Input parameters form with fields for instance ID, IAM role, S3 bucket, secrets ARN, and FSx configuration.](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/images/awssupport-validate-fsxwindows-adconfig_input_parameters1.png)

1. To validate self-managed AD configuration for a new Amazon FSx creation, enter the following parameters:
   + **AutomationAssumeRole (Optional):**

     The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf. If no role is specified, Systems Manager Automation uses the permissions of the user who starts this runbook.
   + **SecretArn (Required):**

     The ARN of your Secrets Manager secret containing the Amazon FSx service account username and password. Make sure that the username and password are stored using a key/value pair in the format `{"username":"EXAMPLE-USER","password":"EXAMPLE-PASSWORD"}`. The CloudFormation stack creates the validation instance with permissions to perform `GetSecretValue` to this ARN.
   + **FSxSecurityGroupId (Required):**

     The security group ID for the Amazon FSx for Windows File Server.
   + **BucketName (Required):**

     The Amazon S3 bucket to upload the validation results to. Make sure that the bucket is configured with server-side encryption (SSE) and the bucket policy does not grant unnecessary read/write permissions to parties that do not need to access the logs. Also make sure that the Amazon EC2 Windows instance has necessary access to the Amazon S3 bucket.
   + **FSxPreferredSubnetId (Conditional):**

     The Amazon FSx for Windows File Server preferred subnet.
   + **DomainName (Conditional):**

     The fully qualified domain name of your self-managed Microsoft AD domain.
   + **DnsIpAddresses (Conditional):**

     A list of up to two DNS server or domain controller IP addresses in your self-managed AD domain. For up to two IPs, enter them separated by a comma.
   + **FSxAdminsGroup (Conditional):**

     The Amazon FSx for Windows File Server delegated file system administrators group. By default, this is `Domain Admins`.
   + **FSxOrganizationalUnit (Conditional):**

     The Organizational Unit (OU) within which you want to join your file system. Provide the distinguished path name of the OU. Example: `OU=org,DC=example,DC=com`.
![Configuration parameters for Amazon FSx including domain name, subnet IDs, and admin groups.](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/images/awssupport-validate-fsxwindows-adconfig_input_parameters2.png)

1. Select **Execute.**

1. The automation initiates.

1. The document performs the following steps:
   + **CheckBucketPublicStatus (aws:executeScript):**

     Checks if the target Amazon S3 bucket potentially grants read and/or write public access to its objects.
   + **BranchOnInputParameters (aws:branch):**

     Branches on the provided input parameters such as Amazon FSx ID or Amazon FSx parameters.
   + **AssertFileSystemTypeIsWindows (aws:assertAwsResourceProperty):**

     If Amazon FSx ID is provided, validates the file system type is Amazon FSx for Windows File Server.
   + **GetValidationInputs (aws:executeScript):**

     Returns the self-managed Microsoft AD configuration required by the CloudFormation template to create the Amazon EC2 instance.
   + **BranchOnInstanceId (aws:branch):**

     Branches on the provided input `InstanceId`. If `InstanceId` is provided, the validation script runs on the target Amazon EC2 instance from automation `step:RunValidationScript`.
   + **CreateEC2InstanceStack (aws:createStack):**

     Creates the Amazon EC2 instance in the preferred subnet using CloudFormation where the `AmazonFSxADValidation` tool will be executed
   + **DescribeStackResources (aws:executeAwsApi):**

     Describes the CloudFormation stack to get the temporary Amazon EC2 instance ID.
   + **WaitForEC2InstanceToBeManaged (aws:waitForAwsResourceProperty):**

     Waits until the Amazon EC2 instance is managed by Systems Manager in order to run the validation script using SSM Run Command.
   + **GetAmazonFSxADValidationAttachment (aws:executeAwsApi):**

     Gets the `AmazonFSxADValidation` tool URL from the runbook attachments.
   + **RunValidationScript (aws:runCommand):**

     Runs the `AmazonFSxADValidation` tool on the temporary Amazon EC2 instance and stores the result in the Amazon S3 bucket specified in the `BucketName` parameter.
   + **DescribeErrorsFromStackEvents (aws:executeScript):**

     Describes the CloudFormation stack events if the runbooks fails to create the stack.
   + **BranchOnRetainCloudFormationStack (aws:branch):**

     Branches on the `RetainCloudFormationStack` and `InstanceId` parameters to determine if the CloudFormation stack should be deleted.
   + **DeleteCloudFormationStack (aws:deleteStack):**

     Deletes the CloudFormation stack.

1. After completed, review the Outputs section for the results of the execution:
![Outputs section showing validation script results with one InvalidCredentials error.](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/images/awssupport-validate-fsxwindows-adconfig_outputs.png)

   The runbook will upload the results of the validation script execution to the Amazon S3 bucket.

 **References**

Systems Manager Automation
+ [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/documents/AWSSupport-ValidateFSxWindowsADConfig/description)
+ [Run an automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-working-executing.html)
+ [Setting up an Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-setup.html)
+ [Support Automation Workflows landing page](https://aws.amazon.com/premiumsupport/technology/saw/)

AWS service documentation
+ [What is Amazon FSx for Windows File Server?](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html)
+ [Validating self-managed AD configuration for Amazon FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/validate-ad-config.html)
