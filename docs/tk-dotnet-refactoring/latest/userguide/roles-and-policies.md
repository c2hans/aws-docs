---
source_url: https://docs.aws.amazon.com/tk-dotnet-refactoring/latest/userguide/roles-and-policies.html
---

AWS .NET Modernization Tools Porting Assistant (PA) for .NET, AWS App2Container (A2C), AWS Toolkit for .NET Refactoring (TR), and AWS Microservice Extractor (ME) for .NET is no longer open to new customers. If you would like to use the service, sign up prior to November 7, 2025. Alternatively use [AWS Transform](https://aws.amazon.com/transform/), which is an agentic AI service developed to accelerate enterprise modernization of .NET.

# AWS roles and managed policies for Toolkit for .NET Refactoring test deployment
<a name="roles-and-policies"></a>

To test your application on AWS using Toolkit for .NET Refactoring, you must have the required permissions. Permissions are required for the following tasks:
+ Containerization of your .NET Core application.
+ Deployment of the ported application to AWS Fargate.

The [AWS managed policies](security-iam-awsmanpol.md) page contains detailed information about the managed policies that you can use with Toolkit for .NET Refactoring.

**Topics**
+ [Manually create roles and policies](#dotnet-refactoring-roles-policies-manual)
+ [Create roles and policies with CloudFormation](#cloudformation-create-roles-policies)
+ [AWS KMS key policy](#dotnet-refactoring-roles-policies-manual-kms)

## Manually create roles and policies
<a name="dotnet-refactoring-roles-policies-manual"></a>

You can manually create the roles and policies required for Toolkit for .NET Refactoring.

### Roles and policies for Toolkit for .NET Refactoring
<a name="dotnet-refactoring-roles-policies-manual-toolkit"></a>

Use the AWS Management Console to create roles and policies to use Toolkit for .NET Refactoring.

1. Navigate to the [AWS Management Console](https://console.aws.amazon.com/console) and search for **IAM**.

1. From the IAM dashboard, create a policy named `refactoringtoolkit-EnablePassRoleAccess` and include the following JSON statement:

------
#### [ JSON ]

****

   ```
   {
     "Version":"2012-10-17",
     "Statement": [
       {
         "Action": [
           "iam:PassRole"
         ],
         "Resource": [
           "arn:aws:iam::048661490019:role/refactoringtoolkit-CodeBuildServiceRole",
           "arn:aws:iam::048661490019:role/refactoringtoolkit-ECSTaskExecutionRole",
           "arn:aws:iam::048661490019:role/refactoringtoolkit-ECSTaskRole"
         ],
         "Effect": "Allow"
       }
     ]
   }
   ```

------

1. Create a policy named `refactoringtoolkit-EnableTelemetryAccess` and include the following JSON statement:

------
#### [ JSON ]

****

   ```
   {
     "Version":"2012-10-17",
     "Statement": [
       {
         "Action": [
           "execute-api:invoke"
         ],
         "Resource": [
           "arn:aws:execute-api:us-east-1:492443789615:3dmmp07yx6/*",
           "arn:aws:execute-api:us-east-1:547614552430:8q2itpfg51/*",
           "arn:aws:execute-api:us-east-1:226975336241:m43z210z43/*",
           "arn:aws:execute-api:us-east-1:651331843990:lqi4wznpac/*",
           "arn:aws:execute-api:us-west-2:930729463547:ml5fgmwiy3/*"
         ],
         "Effect": "Allow",
         "Sid": "EnCorePermission"
       }
     ]
   }
   ```

------

1. Create a role named `refactoringtoolkit-CodeBuildServiceRole` and add an inline policy called `CodeBuildServiceRolePolicy` that includes the following JSON statement:

------
#### [ JSON ]

****

   ```
   {
     "Version":"2012-10-17",
     "Statement": [
       {
         "Action": [
           "logs:CreateLogGroup",
           "logs:CreateLogStream",
           "logs:PutLogEvents"
         ],
         "Resource": "*",
         "Effect": "Allow",
         "Sid": "CloudWatchLogsPolicy"
       },
       {
         "Action": [
           "s3:GetObject",
           "s3:GetObjectVersion",
           "s3:ListBucket"
         ],
         "Resource": "*",
         "Effect": "Allow",
         "Sid": "S3GetObjectPolicy"
       },
       {
         "Action": [
           "s3:GetBucketAcl",
           "s3:GetBucketLocation"
         ],
         "Resource": "*",
         "Effect": "Allow",
         "Sid": "S3BucketIdentity"
       },
       {
         "Action": [
           "ecr:InitiateLayerUpload",
           "ecr:PutImage",
           "ecr:UploadLayerPart",
           "ecr:CompleteLayerUpload",
           "ecr:BatchCheckLayerAvailability",
           "ecr:GetDownloadUrlForLayer"
         ],
         "Resource": "*",
         "Effect": "Allow",
         "Sid": "ECRPushPolicy"
       },
       {
         "Action": [
           "ecr:GetAuthorizationToken"
         ],
         "Resource": "*",
         "Effect": "Allow",
         "Sid": "ECRAuthPolicy"
       }
     ]
   }
   ```

------

1. Create a role named `refactoringtoolkit-ECSTaskRole` and add the `AWSRefactoringToolkitSidecarPolicy` policy.

1. Create a role named `refactoringtoolkit-ECSTaskExecutionRole` and add the `AmazonECSTaskExecutionRolePolicy` policy.

1. Create a role named `refactoringtoolkit-RefactoringToolkitCallerRole` and add the `refactoringtoolkit-EnablePassRoleAccess`, `refactoringtoolkit-EnableTelemetryAccess`, and `AWSRefactoringToolkitFullAccess` policies.

## Create roles and policies with CloudFormation
<a name="cloudformation-create-roles-policies"></a>

Use the CloudFormation template to create roles and policies that you will use for Toolkit for .NET Refactoring.

1. Use the following command to download the CloudFormation template.

   ```
   aws s3 cp s3://aws.portingassistant.dotnet.download/ide.extension.role.creation/aws-refactoringtoolkit-iam-roles.yaml .
   ```

1. Create the required IAM roles in your account. This step uses the `aws-refactoringtoolkit-iam-roles.yaml` file that you downloaded in the previous step. The user that executes the command to create the roles must have the following permissions:
   + `iam:CreateRole`
   + `iam:CreatePolicy`
   + `iam:AttachRolePolicy`

   To create the roles, run the following AWS CLI command:

   ```
   aws cloudformation deploy --stack-name refactoringtoolkit --template-file aws-refactoringtoolkit-iam-roles.yaml --capabilities CAPABILITY_NAMED_IAM
   ```

The following sections provide detailed information about the roles that are created by the CloudFormation template.

**Topics**
+ [Role and policy for the user calling the API](#user-permissions)
+ [Assign a user to the role created by the CloudFormation template](#attach-policies)
+ [Attach the policies to the user](#attach-policies-to-user)
+ [Toolkit for .Net Refactoring caller role](#caller-role)
+ [AWS CodeBuild role](#code-build)
+ [Amazon ECS task execution role](#ecs-task-execution)
+ [Amazon ECS task role](#ecs-task-role)

### Role and policy for the user calling the API
<a name="user-permissions"></a>

The CloudFormation template creates the following policy and role:
+ Policy – `refactoringtoolkit-EnablePassRoleAccess`
+ Policy – `refactoringtoolkit-EnableTelemetryAccess`
+ Role – `refactoringtoolkit-RefactoringToolkitCallerRole`

### Assign a user to the role created by the CloudFormation template
<a name="attach-policies"></a>

The role that was created by the CloudFormation template contains the policies required to use Toolkit for .NET Refactoring. You can assign a user to this role.

To enable a user to assume the role, you need the Amazon Resource Name (ARN) of the user. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *AWS General Reference*.

To allow the user to be assigned a role, you must edit the trust relationship for the `refactoringtoolkit-RefactoringToolkitCallerRole` role. For more information, see [Granting a user permissions to switch roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use_permissions-to-switch.html) in the *AWS Identity and Access Management User Guide*.

Edit the trust relationship to add the principal with the ARN of the user:

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement": {
    "Effect": "Allow",
    "Principal": {
      "AWS": "arn:aws:iam::{{123456789012:user/{{John}}}}",
      "Service": "ec2.amazonaws.com"
    },
    "Action": "sts:AssumeRole"
  }
}
```

------

**Note**
By default, this role has a trust relationship that allows the Amazon EC2 instance to use the role. If you delete the `"Service": "ec2.amazonaws.com"` line, the instance profile will no longer work.

#### Create a new named profile that uses a role
<a name="create-named-profile"></a>

**Important**
The `~/.aws/config` file contains a section for your user profile. In this step, do not edit the section for your user profile. Instead, you will create a new role profile section.

Add the text below to the `~/.aws/config` file to create the `refactoringtoolkit` profile. You can substitute any string for `{{<user_role_profile>}}`, such as `refactoringtoolkit_profile`.

```
[{{<user_role_profile>}}]
role_arn = arn:aws:iam::{{<AWS_account_ID>}}:role/refactoringtoolkit-RefactoringToolkitCallerRole
source_profile = {{<user_profile>}}
```

For information about how to add a role to a profile, see [Using an IAM role in the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-role.html) in the *AWS CLI User Guide for Version 2*. For information about credentials, see [Shared config and credentials files](https://docs.aws.amazon.com/sdkref/latest/guide/file-format.html) in the *AWS SDKs and Tools Reference Guide*.

### Attach the policies to the user
<a name="attach-policies-to-user"></a>

Alternatively, you can attach the policies to a user rather than a role. If you want to do this, you can attach the following policies directly to the user:
+ `AWSRefactoringToolkitFullAccess`
+ `refactoringtoolkit-EnableTelemetryAccess`
+ `refactoringtoolkit-EnablePassRoleAccess`

To provide access, add permissions to your users, groups, or roles:
+ Users and groups in AWS IAM Identity Center:

  Create a permission set. Follow the instructions in [Create a permission set](https://docs.aws.amazon.com//singlesignon/latest/userguide/howtocreatepermissionset.html) in the *AWS IAM Identity Center User Guide*.
+ Users managed in IAM through an identity provider:

  Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](https://docs.aws.amazon.com//IAM/latest/UserGuide/id_roles_create_for-idp.html) in the *IAM User Guide*.
+ IAM users:
  + Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](https://docs.aws.amazon.com//IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.
  + (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](https://docs.aws.amazon.com//IAM/latest/UserGuide/id_users_change-permissions.html#users_change_permissions-add-console) in the *IAM User Guide*.

### Toolkit for .Net Refactoring caller role
<a name="caller-role"></a>

The CloudFormation template creates the following caller role:

```
refactoringtoolkit-RefactoringToolkitCallerRole
```

This role grants Toolkit for .NET Refactoring permissions to do the following:
+ Call the required APIs in AWS.
+ Upload application artifacts and download the resulting artifacts from S3.
+ Build the application into a container image using AWS CodeBuild and store and retrieve the images in Amazon Elastic Container Registry (Amazon ECR).
+ Deploy the application to container services on AWS, such as Amazon Elastic Container Service (Amazon ECS).
+ Optionally, create Amazon VPC resources.
+ Optionally, connect to existing infrastructure, such as Directory Service.

The following policies are attached to the role:
+ `refactoringtoolkit-EnablePassRoleAccess`
+ `refactoringtoolkit-EnableTelemetryAccess`
+ `AWSRefactoringToolkitFullAccess`

To use this role, you must do one of the following:
+ Add it to a named profile in the `~/.aws/config` file. For more information, see [Assign a user to the role created by the CloudFormation template](#attach-policies) in this guide.
+ Use it with an Amazon EC2 instance profile. For more information, see [Install Toolkit for .NET Refactoring](dotnet-refactoring-installation.md) in this guide.

### AWS CodeBuild role
<a name="code-build"></a>

The CloudFormation template creates the following CodeBuild role:

```
refactoringtoolkit-CodeBuildServiceRole
```

AWS CodeBuild uses this role to download application artifacts from S3, build the application container, push to Amazon Elastic Container Registry (Amazon ECR), and create logs in Amazon CloudWatch.

The following policy is attached to the role:

```
CodeBuildServiceRolePolicy
```

Toolkit for .NET Refactoring will automatically use a role with this name.

### Amazon ECS task execution role
<a name="ecs-task-execution"></a>

The CloudFormation template creates the following Amazon ECS task execution role:

```
refactoringtoolkit-ECSTaskExecutionRole
```

This role allows Amazon ECS to pull the application Docker image from Amazon ECR and upload logs.

The following policies are attached to the role:
+ `AmazonECSTaskExecutionRolePolicy`
+ `ECSSecretsPolicy`

Toolkit for .NET Refactoring will automatically use a role with this name.

For more information, see [Amazon ECS task execution IAM role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_execution_IAM_role.html) in the *Amazon ECS User Guide*.

### Amazon ECS task role
<a name="ecs-task-role"></a>

The CloudFormation template creates the following Amazon ECS task role:

```
refactoringtoolkit-ECSTaskRole
```

This role allows your application to authenticate with other AWS services. It is similar to the IAM roles that are used as instance profiles for Amazon EC2 instances. This role is required for test deployment to allow the sidecar to sync files from S3 and for Active Directory to retrieve credentials from AWS Secrets Manager.

The following policy is attached to the role:

```
AWSRefactoringToolkitSidecarPolicy
```

Toolkit for .NET Refactoring will automatically use a role with this name.

For more information, see [IAM roles for tasks](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) in the *Amazon ECS User Guide*.

## AWS KMS key policy
<a name="dotnet-refactoring-roles-policies-manual-kms"></a>

To use Toolkit for .NET Refactoring with an AWS KMS key to encrypt AWS resources, the KMS key policy must include the following statement:

```
{
    "Effect": "Allow",
    "Principal": {
        "Service": "application-transformation.amazonaws.com"
    },
    "Action": [
        "kms:Decrypt",
        "kms:DescribeKey",
        "kms:GenerateDataKey"
    ],
    "Resource": "kmsKeyArn"
}
```

You can create a new KMS key with the previously mentioned policy, or add it to an existing KMS key. For more information, see [Creating a key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-overview.html) and [Changing a key policy](https://docs.aws.amazon.com/kms/latest/developerguide/key-policy-modifying.html) in the *AWS Key Management Service User Guide*.
