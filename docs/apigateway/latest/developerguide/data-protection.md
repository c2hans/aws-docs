---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/data-protection.html
---

# Data protection in Amazon API Gateway

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in Amazon API Gateway. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. You are also responsible for the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).  For information about data protection in Europe, see the [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/).

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
+ Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html) in the *AWS CloudTrail User Guide*.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
+ If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/).

We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with API Gateway or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form text fields used for names may be used for billing or diagnostic logs. If you provide a URL to an external server, we strongly recommend that you do not include credentials information in the URL to validate your request to that server.

## Data protection in API Portal
<a name="data-protection-apiportal"></a>

API Portal stores the following data on your behalf:
+ **API inventory**: for each discovered API, its HTTP method, path, host, port, the ARN and AWS account of the resource that serves it, when it was first and last seen, its visibility and AWS WAF status, and, when AI endpoint identification is enabled, the AI protocols seen in its traffic. Discovery derives this metadata from your resources' configuration and from service traffic logs. API Portal doesn't store request or response bodies.
+ **Security posture findings** for each managed API.
+ **Documentation portal content**: product and page text that you write, API reference pages generated from your API definitions, portal themes, and logos that you upload.

### Encryption at rest
<a name="data-protection-apiportal-at-rest"></a>

API Portal encrypts all stored data at rest, including the API inventory, security posture findings, and documentation portal content, using encryption keys that API Portal manages in AWS KMS.

### Encryption in transit
<a name="data-protection-apiportal-in-transit"></a>

All API Portal endpoints require TLS 1.2 or later. Documentation portals are served over HTTPS through CloudFront.

### Key management
<a name="data-protection-apiportal-keys"></a>

API Portal creates and manages the encryption keys for your data. You can't supply a customer managed AWS KMS key for API Portal resources. API Portal doesn't use your content to improve the service.

When you disable discovery for an account, API Portal stops updating that account's inventory. When an account leaves your organization, its APIs are marked orphaned and are no longer rediscovered. Deleting a managed API, product, or documentation portal deletes the associated data.
