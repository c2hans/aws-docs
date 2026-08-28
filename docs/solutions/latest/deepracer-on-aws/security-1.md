---
source_url: https://docs.aws.amazon.com/solutions/latest/deepracer-on-aws/security-1.html
---

# Security
<a name="security-1"></a>

When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, the virtualization layer, and the physical security of the facilities in which the services operate. For more information about security on AWS, visit [AWS Cloud Security](https://aws.amazon.com/security/)

## Security best practices
<a name="security-best-practices"></a>

DeepRacer on AWS is designed with security best practices in mind. However, the security of a solution differs based on your specific use case. The following are additional recommendations to enhance the security posture of DeepRacer on AWS.

### Use a dedicated account for deployment
<a name="use-a-dedicated-account-for-deployment"></a>

We strongly recommend using a dedicated account that’s separate from any production workloads for deploying and hosting DeepRacer on AWS. This separation helps prevent mixing different levels of data sensitivity, and reduces the potential blast radius in the event of a security incident.

### Activate Ubuntu Pro to apply ESM patches
<a name="activate-ubuntu-pro-to-apply-esm-patches"></a>

See [Mitigate OS vulnerabilities with Ubuntu Pro](#mitigate-vulns-with-ubuntu-pro).

## Infrastructure security
<a name="infrastructure-security"></a>

### Console UI
<a name="console-ui"></a>

This solution deploys a web console [hosted](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html) in an Amazon S3 bucket. To enhance security and reduce latency, the solution configures an Amazon CloudFront distribution with an origin access control (OAC). This OAC provides controlled public access to the solution’s website bucket contents, ensuring that users can only access the web console through CloudFront and not directly from S3. For more information, see [Restricting access to an Amazon S3 origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) in the *Amazon CloudFront Developer Guide*.

The CloudFront distribution is configured to only accept HTTPS requests. If an HTTP request is received, it will redirect it to HTTPS to promote encryption in-transit.

CloudFront activates additional security mitigations to append HTTP security headers to each viewer response. For additional details, please see [Adding or removing HTTP headers in CloudFront responses](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/adding-response-headers.html).

This solution uses the default CloudFront certificate, which has a minimum supported security protocol of TLS v1.0. To enforce the use of TLS v1.2 or TLS v1.3, you must use a custom SSL certificate instead of the default CloudFront certificate. For more information, refer to [How do I configure my CloudFront distribution to use an SSL/TLS certificate](https://aws.amazon.com/premiumsupport/knowledge-center/install-ssl-cloudfront/).

### Authentication and authorization
<a name="authentication-and-authorization"></a>

This solution uses Amazon Cognito and several other services for managing authentication and authorization. Authentication is handled by an Amazon Cognito user pool, which is configured with three user pool groups, one for each user type (i.e. admins, race facilitators, and racers). The AWS Amplify Auth plugin is used for authenticating users from the console and managing sessions.

Each user pool group has a dedicated IAM role mapped to it using rule-based role mapping in the identity pool. These roles define what resources a user in a given user pool group can or cannot access.

Authorization is handled via the issuance of temporary credentials from an Amazon Cognito identity pool, based on the role associated with their user pool group. These credentials are assumed by the user upon successful authentication into the console, and are used for signing requests to the back-end. When a request is received by the API, an IAM authorizer is used to authorize the request before proxying it to the appropriate Lambda function for servicing.

### Identity and access management
<a name="identity-and-access-management"></a>

AWS Identity and Access Management (IAM) roles are used to grant specific permissions to various resources that comprise DeepRacer on AWS. The following IAM roles are created:

1. Lambda execution roles: Allows AWS Lambda functions to access other AWS services such as Amazon S3, Amazon DynamoDB, and Amazon CloudWatch Logs.

1. SageMaker execution role: Allows SageMaker AI training jobs to access necessary resources like ECR images and S3 buckets.

1. Step Functions execution roles: Permits Step Functions to invoke Lambda functions and manage SageMaker jobs.

1. API Gateway execution roles: Enables Amazon API Gateway to invoke AWS Lambda functions in response to requests.

1. User roles: Allows for granular access control to be applied by user type.

These roles follow the principle of least privilege, granting only the permissions necessary for each component to perform its functions.

### Log retention and monitoring
<a name="log-retention-and-monitoring"></a>

By default, DeepRacer on AWS retains all security-relevant logs for 10 years, which aligns with AWS security best practices. Security-relevant logs include logs emitted by AWS Lambda functions that support API services as well as authentication and authorization services. All other logs are retained for 2 years. You can customize the log retention period for one or more logs through the CloudWatch Logs console.

All logs are encrypted at-rest using AWS KMS customer-managed keys.

### Amazon API Gateway
<a name="amazon-api-gateway"></a>

This solution deploys an Amazon API Gateway REST API and uses the default API endpoint and SSL certificate. The default API endpoint supports TLSv1 security policy. It is recommended to use the TLS\_1\_2 security policy to enforce TLSv1.2\+ with your own custom domain name and custom SSL certificate.

For more information:
+  [Choose a security policy for your custom domain in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-custom-domain-tls-version.html)
+  [Custom domain name for public REST APIs in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html)

## AWS CloudTrail
<a name="aws-cloudtrail"></a>

AWS CloudTrail is not automatically enabled by DeepRacer on AWS. AWS recommends enabling CloudTrail to monitor API calls and administrative actions in your account.

### Amazon DynamoDB
<a name="amazon-dynamodb"></a>

All user data stored in Amazon DynamoDB is encrypted at-rest using customer managed keys (CMK) stored in AWS KMS.

### AWS Key Management System
<a name="aws-key-management-system"></a>

This solution creates one KMS Customer Managed Key (CMK) for the purpose of log encryption.

### AWS Lambda functions
<a name="aws-lambda-functions"></a>

By default, all AWS Lambda functions that are configured by this solution use the most recent, stable version of the language runtime. No sensitive data or secrets are logged. Service interactions are carried out with the least required privilege. Roles that define these privileges are not shared between functions.

### Amazon SageMaker
<a name="amazon-sagemaker"></a>

This solution uses the Amazon SDK to create Amazon SageMaker training jobs. These training jobs are responsible for servicing requests from users to train models, evaluate models, and simulate models in a competition.

### Amazon S3
<a name="amazon-s3"></a>

This solution deploys S3 buckets with default S3 bucket security configurations. For encryption of objects at rest, consider using customer managed CMKs instead of the default key for encrypting objects. Customer managed keys are recommended for customers who want full control over the lifecycle and usage of their keys.

It’s a best practice to use modern encryption protocols for data in transit. To enforce the use of TLS version 1.2 or later for connections to S3, update your bucket’s security policy.

It is recommended that S3 server access logging provides detailed records for the requests that are made to a bucket. [Amazon S3 server access logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html) provides detailed records for the requests made to the bucket. S3 Access Logs can be enabled and saved in another S3 bucket.

For more information:
+  [Using server-side encryption with customer-provided keys (SSE-C)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerSideEncryptionCustomerKeys.html)
+  [How do I enforce TLS 1.2 or later for my S3 buckets?](https://repost.aws/knowledge-center/s3-enforce-modern-tls)
+  [Security best practices for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/security-best-practices.html)

### AWS Web application firewall (WAF)
<a name="aws-web-application-firewall-waf"></a>

The solution deploys AWS WAF to protect against common web exploits and bot traffic. It includes rules to mitigate against common vulnerabilities and allows for custom rule creation.

## Data protection
<a name="data-protection"></a>

DeepRacer on AWS uses an Amazon DynamoDB table and Amazon S3 buckets for storing models, profiles, training and evaluation outputs, and other assets uploaded to or generated by the solution. The following data protection settings are configured by default to mitigate against loss of data, unauthorized access, and other issues:
+ For the **table**, point-in-time recovery is enabled with a backup recovery period of 35 days, allowing for the table to be rolled back seamlessly in the event of a data issue. In addition, the table is configured to be retained in the event of a stack deletion or update-replace event. Data is also encrypted at rest using an AWS managed key.
+ For the model storage and upload **buckets**, bucket encryption, logging, and versioning are enabled by default. Access logging is also configured and all public access is blocked.

## Vulnerability analysis and management
<a name="vuln-analysis"></a>

DeepRacer on AWS and its dependencies are continuously monitored by AWS for security vulnerabilities. Customers may choose to use Amazon Inspector or other automated vulnerability management product for monitoring their deployments.

### Mitigate OS vulnerabilities with Ubuntu Pro
<a name="mitigate-vulns-with-ubuntu-pro"></a>

DeepRacer on AWS uses a container image that is based on Ubuntu 24.04 and it is possible for Common Vulnerabilities and Exposures “CVEs” to appear. Customers may at their sole option, obtain an [Ubuntu Pro 24.04](https://ubuntu.com/pro) license which may provide additional security assurance and follow the provided instructions linked below to modify the solution to use Ubuntu Pro 24.04 as the operating system for applicable containers.

Choosing to obtain and use Ubuntu Pro 24.04 is solely at the customer’s option and is not required to use any features of DeepRacer on AWS. Obtaining the Ubuntu Pro 24.04 license may only provide access to patched versions of core Ubuntu packages and may not provide access to patched versions of third-party or open-source dependencies. Use of Ubuntu Pro 24.04 may reduce the number of CVEs reported against core packages by providing access to patched versions and does not guarantee a reduction of CVEs at any given time.

Customers are solely responsible for securing and complying with any Ubuntu Pro 24.04 licenses and AWS is not responsible for any licensing or support of Ubuntu Pro 24.04. For instructions on implementing Ubuntu Pro 24.04, please see below.

#### Activating Ubuntu Pro
<a name="activating-ubuntu-pro"></a>

To take advantage of ESM patches offered by Ubuntu Pro, please follow the procedure outlined below which will activate Ubuntu Pro on the SageMaker image that has been deployed for you by DeepRacer on AWS.

 **Prerequisites**
+ A laptop or cloud workstation that has access to the AWS account where DeepRacer on AWS is deployed
+ Installed copies of Docker and the AWS CLI
+ A valid Ubuntu Pro token

 **Procedure**

1. Log in to access the ECR repositories in your AWS account:

   ```
   aws ecr get-login-password --region $REGION | \
     docker login --username AWS --password-stdin $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com
   ```

1. Pull the image from the remote repository to your local machine:

   ```
   docker pull $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$REPOSITORY_NAME\:$IMAGE_VERSION
   ```

1. Create a temporary Dockerfile with Ubuntu Pro activation commands:

   ```
   cat << EOF > Dockerfile.ubuntu-pro
   FROM $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$REPOSITORY_NAME\:$IMAGE_VERSION

   # Install ubuntu-advantage-tools and attach token
   RUN apt-get update && \
       apt-get install -y ubuntu-advantage-tools && \
       ua attach $UBUNTU_PRO_TOKEN && \
       apt-get update && \
       apt full-upgrade -y && \
       apt-get clean && \
       rm -rf /var/lib/apt/lists/*
   EOF
   ```

1. Build a new image with Ubuntu Pro activated:

   ```
   docker build -t $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$REPOSITORY_NAME\:$IMAGE_VERSION -f Dockerfile.ubuntu-pro .
   ```

1. Push the new image back to your ECR repository:

   ```
   docker push $ACCOUNT_ID.dkr.ecr.$REGION.amazonaws.com/$REPOSITORY_NAME\:$IMAGE_VERSION
   ```

## Uploaded artifacts
<a name="uploaded-artifacts"></a>

DeepRacer on AWS allows users to upload models downloaded from other instances to promote portability and allow submission of externally-trained models to races. All artifacts that are uploaded to DeepRacer on AWS are thoroughly scanned and validated using functions that are isolated from the rest of your AWS account using a VPC with least privilege permissions. Only after an artifact package passes these validations is it allowed to be stored in the system.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DeepRacer on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
