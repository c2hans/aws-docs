---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/security.html
---

# Security
<a name="security"></a>

 When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, the virtualization layer, and the physical security of the facilities in which the services operate. For more information about AWS security, visit [AWS Cloud Security](https://aws.amazon.com/security/).

## IAM roles
<a name="iam-roles"></a>

 IAM roles allow customers to assign granular access policies and permissions to services and users on the AWS Cloud. This solution creates IAM roles associated with resources that needs to perform specific actions outlined in previous sections. Permissions defined in the policies created in the solution align with the principle of least privilege access, granting just those permissions that a specific component needs to fulfil its tasks fully. As one of the elements of the architecture is the solution’s library that can be run outside of AWS environment, we recommend using a specific role with the right set of permission to perform the actions against AWS services implemented in the library. You can find a reference to that role in the output section of the deployed CloudFormation stack under the **RoleArn** key.

## Amazon CloudFront
<a name="amazon-cloudfront"></a>

 This solution deploys a demo website [hosted](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html) in an Amazon S3 bucket. To help reduce latency and improve security, this solution includes an Amazon CloudFront distribution with an origin access identity, which is a CloudFront user that provides public access to the solution’s website S3 bucket contents. For more information, refer to [Restricting Access to Amazon S3 Content by Using an Origin Access Identity](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) in the *Amazon CloudFront Developer Guide*. The same CloudFront distribution also interacts with API Gateway endpoint created for managing the access tokens. To maintain good security posture, API Gateway is configured to require AWS IAM authorization for invocation. Therefore, Lambda@Edge function with appropriate IAM permissions is used to sign CloudFront sourced requests. To further improve security of the demo website exposed to the user, a response header policy is attached in the configuration with a set of security headers returned to the viewer, **Strict-Transport-Security**, **X-XSS-Protection**, **X-Content-Type-Options**, **Referrer-Policy**, **X-Frame-Options**, **Content-Security-Policy**.

## Solution’s code library
<a name="solutions-code-library"></a>

 The Secure Media Delivery at the Edge on AWS solution comes with a NodeJS library that was developed to make it easier to integrate solution into your Playback API workflow when adding token generation in it. Functions implemented in this library are built around API calls, made directly against AWS resources – API Gateway endpoint for token-related actions and DynamoDB table to submit the playback sessions that you want to be blocked. To make the API calls for AWS services work, IAM identity with right permission must be assumed when library’s code is run. When run in an AWS environment, you can simply utilize the roles assumed in the context in which library code is initiated – for example, execution role of Lambda functions defined in API module:` [Stack Name]_Generate Token` and `[Stack Name]_SaveManualSession`. If you choose to run your `Playback` API utilizing library provided functions outside an AWS environment, you must still assume the role using a standard approach of credential file, named profiles, or assuming role temporary through AWS Security Token Service; refer to [Setting Credentials in Node.js](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/setting-credentials-node.html). When you interact with the solution classes’, you have an option to refer to a specific profile or Amazon Resource Name (ARN) reference of the role that must be assumed when underlying API calls are made. In this use case, we recommend providing ARN identifier of the dedicated role created specifically for the solution’s library, as it has precisely defined permissions that allow only appropriate actions against specific resources created in the stack. You can find a reference to that role in the output section of deployed CloudFormation stack under **RoleArn** key.

## Signing key protection
<a name="signing-key-protection"></a>

 AWS Secrets Manager is a managed service to securely store and share the secrets based on the IAM defined permissions. A token-based access control mechanism, like the one used in this solution, works on the basis of generating and validating cryptographically created signature, which require a secret key to perform both tasks. AWS Secrets Manager stores the keys used in this solution. The keys are made available only to CloudFront Function and solution library methods, however they are distributed in a different way. CloudFront Functions receive updates with details about the new keys in a push model, when key rotation workflow generates and edits the keys known to CloudFront Function. Solution’s library methods obtain the keys in the pull model by reaching out to AWS Secrets Manager to retrieve the keys when needed. Standard IAM based access model applies where the credentials or role used in the library must translate to appropriate IAM permissions that grant access to the secrets in the deployed stack. This solution has been designed in a way that you do not have to manually define and set keys, instead automation included in the base module addresses that. We recommend leveraging the key rotation mechanism available in the solution to update the signing keys regularly to avoid using the same key for a prolonged period of time.

## API Gateway
<a name="api-gateway"></a>

 HTTP API Gateway is configured to require AWS IAM authorization before the target Lambda functions responsible for token activities are invoked. Therefore, anonymous viewers without appropriate IAM permissions will not be able to make API calls. To successfully integrate other services with the API Gateway endpoint created in the solution, explicit IAM permissions must be granted to the corresponding user or role, allowing to invoke deployed API resource.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Secure Media Delivery at the Edge on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
