---
source_url: https://docs.aws.amazon.com/vpn/latest/clientvpn-admin/data-protection.html
---

# Data protection in AWS Client VPN
<a name="data-protection"></a>

The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in AWS Client VPN. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. You are also responsible for the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).  For information about data protection in Europe, see the [General Data Protection Regulation (GDPR) Center](https://aws.amazon.com/compliance/gdpr-center/).

For data protection purposes, we recommend that you protect AWS account credentials and set up individual users with AWS IAM Identity Center or AWS Identity and Access Management (IAM). That way, each user is given only the permissions necessary to fulfill their job duties. We also recommend that you secure your data in the following ways:
+ Use multi-factor authentication (MFA) with each account.
+ Use SSL/TLS to communicate with AWS resources. We require TLS 1.2 and recommend TLS 1.3.
+ Set up API and user activity logging with AWS CloudTrail. For information about using CloudTrail trails to capture AWS activities, see [Working with CloudTrail trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-trails.html) in the *AWS CloudTrail User Guide*.
+ Use AWS encryption solutions, along with all default security controls within AWS services.
+ Use advanced managed security services such as Amazon Macie, which assists in discovering and securing sensitive data that is stored in Amazon S3.
+ If you require FIPS 140-3 validated cryptographic modules when accessing AWS through a command line interface or an API, use a FIPS endpoint. For more information about the available FIPS endpoints, see [Federal Information Processing Standard (FIPS) 140-3](https://aws.amazon.com/compliance/fips/).

We strongly recommend that you never put confidential or sensitive information, such as your customers' email addresses, into tags or free-form text fields such as a **Name** field. This includes when you work with Client VPN or other AWS services using the console, API, AWS CLI, or AWS SDKs. Any data that you enter into tags or free-form text fields used for names may be used for billing or diagnostic logs. If you provide a URL to an external server, we strongly recommend that you do not include credentials information in the URL to validate your request to that server.

## Encryption in transit
<a name="encryption-in-transit"></a>

AWS Client VPN provides secure connections from any location using Transport Layer Security (TLS) 1.2 or later.

## Internetwork traffic privacy
<a name="internetwork-traffic-privacy"></a>

**Enabling internetwork access**
You can enable clients to connect to your VPC and other networks through a Client VPN endpoint. For more information and examples, see [Scenarios and examples for Client VPN](how-it-works.md#scenario).

**Restricting access to networks**
You can configure your Client VPN endpoint to restrict access to specific resources in your VPC. For user-based authentication, you can also restrict access to parts of your network, based on the user group that accesses the Client VPN endpoint. For more information, see [Restrict access to your network using Client VPN](how-it-works.md#scenario-restrict).

**Authenticating clients**
Authentication is implemented at the first point of entry into the AWS Cloud. It is used to determine whether clients are allowed to connect to the Client VPN endpoint. If authentication succeeds, clients connect to the Client VPN endpoint and establish a VPN session. If authentication fails, the connection is denied and the client is prevented from establishing a VPN session.
Client VPN offers the following types of client authentication:
+ [Active Directory authentication](ad.md) (user-based)
+ [Mutual authentication](mutual.md) (certificate-based)
+ [Single sign-on (SAML-based federated authentication)](federated-authentication.md) (user-based)
