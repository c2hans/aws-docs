---
source_url: https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/dotnet-refactoring-installation.html
---

AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# Install Toolkit for .NET Refactoring
<a name="dotnet-refactoring-installation"></a>

You can install Toolkit for .NET Refactoring within Microsoft Visual Studio, or the extension is available as part of license included Visual Studio Amazon Machine Images (AMIs) on Amazon EC2.

## Install in Visual Studio
<a name="dotnet-refactoring-installation-vs"></a>

To install the Toolkit for .NET Refactoring extension, open Microsoft Visual Studio and complete the following steps:

1. In Visual Studio, open the **Extensions** menu and select **Manage Extensions**.

1. In the **Manage Extensions** window, search for Toolkit for .NET Refactoring. Select the extension and click **Download**.

1. When the download is complete, Visual Studio prompts you to restart the application. Restart Visual Studio to install the Toolkit for .NET Refactoring extension.

## Install with an AMI on Amazon EC2
<a name="dotnet-refactoring-installation-ami"></a>

If you are using a license included Visual Studio Amazon Machine Image (AMI) on Amazon EC2, you can use the caller role (`refactoringtoolkit-RefactoringToolkitCallerRole`) directly, without providing user credentials or editing configuration files. For more information about AMIs, see [User-based subscriptions in AWS License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/user-based-subscriptions.html) in the *AWS License Manager User Guide*.

The CloudFormation template creates an instance profile named `refactoringtoolkit-Ec2InstanceProfile`. For more information about the CloudFormation template, see [Create roles and policies with CloudFormation](roles-and-policies.md#cloudformation-create-roles-policies) in this guide.

You can launch an Amazon EC2 instance with an IAM role through the AWS Management Console or AWS CLI.

**Launch an Amazon EC2 instance in the AWS Management Console**

1. Launch an instance. For more information, see [Quickly launch an instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-instance-wizard.html#liw-quickly-launch-instance) in the *Amazon Elastic Compute Cloud User Guide for Linux Instances*.

1. Expand **Advanced details**, and in the **IAM instance profile **field, select `refactoringtoolkit-Ec2InstanceProfile`.

**Launch an EC2 instance with AWS CLI**

Use AWS CLI to launch an instance that uses the instance profile. For more information, see [ run-instances](https://docs.aws.amazon.com/cli/latest/reference/ec2/run-instances.html) in the *AWS CLI Command Reference.*

The code below is an example command that illustrates how to launch an EC2 instance with the instance profile:

```
aws ec2 run-instances \
    --image-id ami-11aa22bb \
    --iam-instance-profile Name="s3access-profile" \
    --key-name my-key-pair \
    --security-groups my-security-group \
    --subnet-id subnet-1a2b3c4d
```

For more information about instance profiles, see [Using instance profiles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2_instance-profiles.html) in the *AWS Identity and Access Management User Guide*. For more information about using IAM roles with Amazon EC2 instances, see [Using an IAM role to grant permissions to applications running on Amazon EC2 instances](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_switch-role-ec2.html) in the *AWS Identity and Access Management User Guide*. For information about retrieving credentials from instance metadata, see [Retrieve security credentials from instance metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html#instance-metadata-security-credentials) in the *Amazon Elastic Compute Cloud User Guide for Linux Instances*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for NET Refactoring. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query tk-dotnet-refactoring` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
