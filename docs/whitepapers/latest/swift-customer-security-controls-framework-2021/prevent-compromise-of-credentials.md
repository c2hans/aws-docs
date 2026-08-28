---
source_url: https://docs.aws.amazon.com/whitepapers/latest/swift-customer-security-controls-framework-2021/prevent-compromise-of-credentials.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Requirement 4 - Prevent compromise of credentials
<a name="prevent-compromise-of-credentials"></a>

## Password policy
<a name="password-policy"></a>

 [AWS Secrets Manager](https://aws.amazon.com/secrets-manager/) is the recommended service to safely store the passwords that are utilized in the SWIFT secure zone.

 Refer to *Physical and logical password storage* in this document for details on AWS Secrets Manager. It is your responsibility to define the password policy and enforce it.

 To access AWS in a typical enterprise environment, use a federated login to [AWS from the corporate identity provider](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html). In this scenario, the authentication and password policy of the SWIFT operator PC / Accounts is enforced within the corporate security policy.

 You are responsible for configuring operating system level access to EC2 instances. By leveraging AWS Systems Manager Session Manager, you would no longer have to manage passwords for human operators on your EC2 instances. For the service accounts that run applications on the OS, it is your responsibility to maintain the password policy for the users.

## Multi-factor authentication
<a name="multi-factor-authentication"></a>

 Multi-factor authentication (MFA) is mandated for the jump server for accessing the SWIFT secure zone. In the case where AWS Systems Manager Session Manager is utilized for accessing the SWIFT secure zone, you can create an AssumeRole trust policy to enforce MFA when federation is used. Refer to MFA-for-SAML.

 The AWS root user of the AWS account also has access to the SWIFT secure zone using AWS Systems Manager Session Manager by default. You can disable the root user using SCPs to block the root user. Refer to the example, “Block service access for the root user” on the Example service control policies page. You should enable MFA for the root user. Refer to [Enable MFA on the AWS account root user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user_manage_mfa). The following diagram illustrates an example multi-account structure with SWIFT accounts and OU with “Block service access for the root user” SCP applied.

![A diagram depicting an example of a multi-account structure with SWIFT accounts and OU with “Block service access for the root user” SCP applied .](http://docs.aws.amazon.com/whitepapers/latest/swift-customer-security-controls-framework-2021/images/multi-account-structure.jpeg)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
