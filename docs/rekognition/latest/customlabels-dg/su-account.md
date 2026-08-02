---
source_url: https://docs.aws.amazon.com/rekognition/latest/customlabels-dg/su-account.html
---

# Step 1: Create an AWS account
<a name="su-account"></a>

In this step, you create an AWS account, create an administrative user, and learn about granting programmatic access to the AWS SDK.

**Topics**
+ [Sign up for an AWS account](#sign-up-for-aws)
+ [Programmatic access](#su-sdk-programmatic-access)

## Sign up for an AWS account
<a name="sign-up-for-aws"></a>

To get started with AWS, you need an AWS account. For information about creating an AWS account, see [Getting started with an AWS account](https://docs.aws.amazon.com//accounts/latest/reference/getting-started.html) in the *AWS Account Management Reference Guide*.

## Programmatic access
<a name="su-sdk-programmatic-access"></a>

Users need programmatic access if they want to interact with AWS outside of the AWS Management Console. The way to grant programmatic access depends on the type of user that's accessing AWS.

To grant users programmatic access, choose one of the following options.

****

| Which user needs programmatic access? | To | By |
| --- | --- | --- |
| IAM | (Recommended) Use console credentials as temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.[See the AWS documentation website for more details](http://docs.aws.amazon.com/rekognition/latest/customlabels-dg/su-account.html) |
| Workforce identity<br />(Users managed in IAM Identity Center) | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.[See the AWS documentation website for more details](http://docs.aws.amazon.com/rekognition/latest/customlabels-dg/su-account.html) |
| IAM | Use temporary credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions in [Using temporary credentials with AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html) in the IAM User Guide. |
| IAM | (Not recommended)Use long-term credentials to sign programmatic requests to the AWS CLI, AWS SDKs, or AWS APIs. | Following the instructions for the interface that you want to use.[See the AWS documentation website for more details](http://docs.aws.amazon.com/rekognition/latest/customlabels-dg/su-account.html) |
