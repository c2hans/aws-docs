---
source_url: https://docs.aws.amazon.com/sdkref/latest/guide/access.html
---

# Authentication and access using AWS SDKs and tools
<a name="access"></a>

When you develop an AWS SDK application or use AWS tools to use AWS services, you must establish how your code or tool authenticates with AWS. You can configure programmatic access to AWS resources in different ways, depending on the environment the code runs in and the AWS access available to you.

The options below are a part of the [credential provider chain](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html#credentialProviderChain). This means that by configuring your shared AWS `config` and `credentials` files accordingly, your AWS SDK or tool will automatically discover and use that method of authentication.

## Choose a method to authenticate your application code
<a name="authDecisionTree"></a>

Choose a method to authenticate the calls made to AWS by your application.

### Are you running code INSIDE an AWS service (such as Amazon EC2, Lambda, Amazon ECS, Amazon EKS, CodeBuild)?
<a name="a"></a>

If your code runs on AWS, credentials can be made automatically available to your application. For example, if your application is hosted on Amazon Elastic Compute Cloud, and there is an IAM role associated with that resource, the credentials are automatically made available to your application. Likewise, if you use Amazon ECS or Amazon EKS containers, the credentials set for the IAM role can be automatically obtained by the code running inside the container through the SDK's [credential provider chain](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html#credentialProviderChain).

#### Is your code in an Amazon Elastic Compute Cloud instance?
<a name="a1"></a>

[Using IAM roles to authenticate applications deployed to Amazon EC2](access-iam-roles-for-ec2.md) – Use IAM roles to securely run your application on an Amazon EC2 instance.

#### Is your code in an AWS Lambda function?
<a name="a2"></a>

Lambda creates an execution role with minimal permissions when you [create a Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html). The AWS SDK or tool then automatically uses the IAM role attached to the Lambda at runtime, via the Lambda execution environment.

#### Is your code in Amazon Elastic Container Service (on Amazon EC2 or AWS Fargate for Amazon ECS)?
<a name="a3"></a>

Use IAM Role for Task. You must [create a task role](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-iam-roles.html) and specify that role in your [Amazon ECS task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definitions.html). The AWS SDK or tool then automatically uses the IAM role assigned to the task at runtime, via the Amazon ECS metadata.

#### Is your code in Amazon Elastic Kubernetes Service?
<a name="a4"></a>

We recommend you use [Amazon EKS Pod Identities](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html).

Note: If you feel that [IAM roles for service accounts](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) (IRSA) might better suit your unique needs, see [Comparing EKS Pod Identity and IRSA](https://docs.aws.amazon.com/eks/latest/userguide/service-accounts.html#service-accounts-iam) in the **Amazon EKS User Guide**.

#### Is your code running in AWS CodeBuild
<a name="a5"></a>

See [Using identity-based policies for CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/auth-and-access-control-iam-identity-based-access-control.html).

#### Is your code in another AWS service?
<a name="a6"></a>

See the dedicated guide for your AWS service. When you run code on AWS, the SDK [credential provider chain](https://docs.aws.amazon.com/sdkref/latest/guide/standardized-credentials.html#credentialProviderChain) can automatically obtain and refresh credentials for you.

### Are you creating mobile applications or client-based web applications?
<a name="b"></a>

If you are creating mobile applications or client-based web applications that require access to AWS, build your app so that it requests temporary AWS security credentials dynamically by using web identity federation.

With web identity federation, you don't need to create custom sign-in code or manage your own user identities. Instead, app users can sign in using a well-known external identity provider (IdP), such as Login with Amazon, Facebook, Google, or any other OpenID Connect (OIDC)-compatible IdP. They can receive an authentication token, and then exchange that token for temporary security credentials in AWS that map to an IAM role with permissions to use the resources in your AWS account.

To learn how to configure this for your SDK or tool, see [Assuming a role with web identity or OpenID Connect to authenticate AWS SDKs and tools](access-assume-role-web.md).

For mobile applications, consider using Amazon Cognito. Amazon Cognito acts as an identity broker and does much of the federation work for you. For more information, see [Using Amazon Cognito for mobile apps](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc_cognito.html) in the *IAM User Guide*.

### Are you developing and running the code LOCALLY?
<a name="c"></a>

We recommend [Using console credentials to authenticate AWS SDKs and tools](access-login.md).

After a quick browser-based authentication flow, AWS automatically generates temporary credentials that work across local development tools like the AWS CLI, AWS Tools for PowerShell and AWS SDKs.

#### If you use Identity Center for AWS account access
<a name="idc"></a>

Use IAM Identity Center to authenticate AWS SDK and tools if you already have access to AWS accounts and/or need to manage access for your workforce. As a security best practice, we recommend using AWS Organizations with IAM Identity Center to manage access across all your AWS accounts. You can create users in IAM Identity Center, use Microsoft Active Directory, use a SAML 2.0 identity provider (IdP), or individually federate your IdP to AWS accounts. To check if your Region supports IAM Identity Center, see [Using IAM Identity Center to authenticate AWS SDK and tools](access-sso.md)IAM Identity Center endpoints and quotas in the Amazon Web Services General Reference.

#### If you are looking for other ways to authenticate
<a name="owa"></a>

Create a least-privileged IAM user with permissions to `sts:AssumeRole` into your target role. Then configure your profile to assume a role using a `source_profile` set up for that user.

You can also use temporary IAM credentials via environment variables or the shared AWS credentials file. See Using short-term credentials to authenticate AWS SDKs and tools.

Note: In sandbox or learning environments only, you can consider Using long-term credentials to authenticate AWS SDKs and tools.

### Is this code running on-premise or in a hybrid/on-demand VM (such as server that reads from or writes to Amazon S3, or Jenkins deploying to the cloud)?
<a name="d"></a>

#### Are you using X.509 client certificates?
<a name="d1"></a>

Yes: See [Using IAM Roles Anywhere to authenticate AWS SDKs and tools](access-rolesanywhere.md). You can use IAM Roles Anywhere to obtain temporary security credentials in IAM for workloads such as servers, containers, and applications that run outside of AWS. To use IAM Roles Anywhere, your workloads must use X.509 certificates.

#### Can the environment securely connect to a federated identity provider (such as Microsoft Entra or Okta) to request temporary AWS credentials?
<a name="d2"></a>

##### Yes: Use [Process credential provider](feature-process-credentials.md)
<a name="d2a"></a>

Use [Process credential provider](feature-process-credentials.md) to retrieve credentials automatically at runtime. These systems might use a helper tool or plugin to obtain the credentials, and might assume an IAM role behind the scenes using `sts:AssumeRole`.

##### No: Use temporary credentials injected via AWS Secrets Manager
<a name="d2b"></a>

Use temporary credentials injected via AWS Secrets Manager. For options to obtain short-lived access keys, see [Request temporary security credentials](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_request.html) in the *IAM User Guide*. For options on storing these temporary credentials, see [AWS access keys](feature-static-credentials.md).

You can use these credentials to securely retrieve broader application permissions from [Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html), where your production secrets or long-lived role-based credentials can be stored.

### Are you using a third-party tool not in AWS?
<a name="e"></a>

Use the documentation written by your third-party provider for best guidance on obtaining credentials.

#### If your third-party has not provided documentation, can you inject temporary credentials securely?
<a name="e1"></a>

Yes: Use environment variables and temporary AWS STS credentials.

No: Use static access keys stored in encrypted secret manager (last resort).

## Authentication methods
<a name="authOptions"></a>

**Authentication methods for code running within an AWS environment **

If your code runs on AWS, credentials can be made automatically available to your application. For example, if your application is hosted on Amazon Elastic Compute Cloud, and there is an IAM role associated with that resource, the credentials are automatically made available to your application. Likewise, if you use Amazon ECS or Amazon EKS containers, the credentials set for the IAM role can be automatically obtained by the code running inside the container through the SDK's credential provider chain.
+ [Using IAM roles to authenticate applications deployed to Amazon EC2](access-iam-roles-for-ec2.md) – Use IAM roles to securely run your application on an Amazon EC2 instance.
+  You can programmatically interact with AWS using IAM Identity Center in the following ways:
  + Use [AWS CloudShell](https://docs.aws.amazon.com/cloudshell/latest/userguide/) to run AWS CLI commands from the console.
  + To try cloud-based collaboration space for software development teams, consider using [Amazon CodeCatalyst](https://docs.aws.amazon.com/codecatalyst/latest/userguide/welcome.html).

**Authentication through a web-based identity provider - Mobile or client-based web applications**

If you are creating mobile applications or client-based web applications that require access to AWS, build your app so that it requests temporary AWS security credentials dynamically by using web identity federation.

With web identity federation, you don't need to create custom sign-in code or manage your own user identities. Instead, app users can sign in using a well-known external identity provider (IdP), such as Login with Amazon, Facebook, Google, or any other OpenID Connect (OIDC)-compatible IdP. They can receive an authentication token, and then exchange that token for temporary security credentials in AWS that map to an IAM role with permissions to use the resources in your AWS account.

To learn how to configure this for your SDK or tool, see [Assuming a role with web identity or OpenID Connect to authenticate AWS SDKs and tools](access-assume-role-web.md).

For mobile applications, consider using Amazon Cognito. Amazon Cognito acts as an identity broker and does much of the federation work for you. For more information, see [Using Amazon Cognito for mobile apps](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc_cognito.html) in the *IAM User Guide*.

**Authentication methods for code running locally (not in AWS) **
+ [Using console credentials to authenticate AWS SDKs and tools](access-login.md) – This feature works with both AWS Command Line Interface and Tools for PowerShell and gives you refreshable credentials that work across local development tools like the AWS CLI, Tools for PowerShell and AWS.
+ [Using IAM Identity Center to authenticate AWS SDK and tools](access-sso.md) – As a security best practice, we recommend using AWS Organizations with IAM Identity Center to manage access across all your AWS accounts. You can create users in AWS IAM Identity Center, use Microsoft Active Directory, use a SAML 2.0 identity provider (IdP), or individually federate your IdP to AWS accounts. To check if your Region supports IAM Identity Center, see [AWS IAM Identity Center endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/sso.html) in the *Amazon Web Services General Reference*.
+ [Using IAM Roles Anywhere to authenticate AWS SDKs and tools](access-rolesanywhere.md) – You can use IAM Roles Anywhere to obtain temporary security credentials in IAM for workloads such as servers, containers, and applications that run outside of AWS. To use IAM Roles Anywhere, your workloads must use X.509 certificates.
+  [Assuming a role with AWS credentials to authenticate AWS SDKs and tools](access-assume-role.md) – You can assume an IAM role to temporarily access AWS resources that you might not have access to otherwise.
+  [Using AWS access keys to authenticate AWS SDKs and tools](access-users.md) – Other options that might be less convenient or might increase the security risk to your AWS resources.

**More information about access management**

The *IAM User Guide* has the following information about securely controlling access to AWS resources:
+ [IAM Identities (users, user groups, and roles)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id.html) – Understand the basics of identities in AWS.
+ [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) – Security recommendations to follow when developing AWS applications according to the [shared-responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/).

The *Amazon Web Services General Reference* has foundational basics on the following:
+ [Understanding and getting your AWS credentials](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html) – Access key options and management practices for both console and programmatic access.

**IAM Identity Center trusted identity propagation (TIP) plugin to access AWS services**
+ [Using the TIP plugin to access AWS services](access-tip.md) – If you are creating an application for Amazon Q Business or other service that supports trusted identity propagation, and are using the AWS SDK for Java or the AWS SDK for JavaScript, you can use the TIP plugin for a streamlined authorization experience.

## AWS Builder ID
<a name="bid"></a>

Your AWS Builder ID complements any AWS accounts you might already own or want to create. While an AWS account acts as a container for AWS resources you create and provides a security boundary for those resources, your AWS Builder ID represents you as an individual. You can sign in with your AWS Builder ID to access developer tools and services such as Amazon Q and Amazon CodeCatalyst.
+ [Sign in with AWS Builder ID](https://docs.aws.amazon.com/signin/latest/userguide/sign-in-aws_builder_id.html) in the *AWS Sign-In User Guide* – Learn how to create and use an AWS Builder ID and learn what the Builder ID provides.
+ [CodeCatalyst concepts - AWS Builder ID](https://docs.aws.amazon.com/codecatalyst/latest/userguide/concepts.html#sign-in-concept) in the *Amazon CodeCatalyst User Guide* – Learn how CodeCatalyst uses an AWS Builder ID.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for none. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdkref` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
