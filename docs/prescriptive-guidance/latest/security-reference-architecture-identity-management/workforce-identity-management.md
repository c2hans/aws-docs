---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-identity-management/workforce-identity-management.html
---

# Workforce identity management
<a name="workforce-identity-management"></a>

|  |
| --- |
| Influence the future of the AWS Security Reference Architecture (AWS SRA) by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_e3XI1t37KMHU2ua). |

Workforce identity management, which is illustrated in the following diagram, refers to managing human access to resources that help build and manage your businesses within your cloud infrastructure and applications. It supports secure provisioning, managing, and removing access, as employees join an organization, move between roles, and leave an organization. Identity administrators can create identities directly in AWS or connect to an external identity provider (IdP) to enable employees to use their corporate credentials to securely access AWS accounts and business applications from one place.

![Workforce identity management on AWS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-identity-management/images/guide-img/1bf8562a-50f2-4dfa-9a24-c4edfe7b936c/images/59bbb59c-bf1b-4487-b9f7-898f95cf21f4.png)

By using AWS IAM Identity Center to manage access to AWS managed applications, you can benefit from new capabilities such as trusted identity propagation from your query application to the AWS data service, and new services such as Amazon Q that provide a continuous user experience as users move from one Amazon Q-enabled service to another. The use of IAM Identity Center for AWS account access prevents the creation and use of IAM users, which have long-term access to resources. Instead, it enables workforce identities to access resources in AWS accounts by using temporary credentials from IAM Identity Center, which is a security best practice. Workforce identity management services let you define fine-grained access control for AWS resources or applications in your multi-account AWS environment based on specific job functions or user attributes. These services also help audit and review user activities within your AWS environment.

AWS offers several several options for workforce identity and access management: IAM Identity Center, IAM SAML federation, and AWS Managed Microsoft AD.
+ [IAM Identity Center](workforce-iam-identity-center.md) is the recommended service for managing workforce access to AWS applications and multiple AWS accounts. You can use this service with an existing identity source, such as Okta, Microsoft Entra ID, or on-premises Active Directory, or by creating users in its directory. IAM Identity Center supplies all AWS services with a shared understanding of your workforce users and groups. AWS managed applications integrate with it, so you do not need to connect your identity source individually to each service, and you can manage and view your workforce access from a central location. You can use IAM Identity Center to manage access to AWS applications while you continue to use your established configuration to access AWS accounts. For new multi-account environments, IAM Identity Center is the recommended service to manage your workforce access to the environment. You can assign permissions consistently across AWS accounts, and your users receive single sign-on access across AWS.
+ An alternate way to grant your workforce access to AWS accounts is by using [IAM SAML 2.0 federation](workforce-iam-federation.md). This involves creating one-to-one trust between your organization's IdP and each AWS account, and isn't recommended for multi-account environments. Inside your organization, you must have an [IdP that supports SAML 2.0](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_saml_3rd-party.html), such as Microsoft Entra ID, Okta, or another compatible SAML 2.0 provider.
+ Another option is to use [Microsoft Active Directory (AD) as a managed service](workforce-aws-managed-ad.md) to run directory-aware workloads in AWS. You can also configure a trust relationship between AWS Managed Microsoft AD in the AWS Cloud and your existing on-premises Microsoft Active Directory, to provide users and groups with access to resources in either domain by using IAM Identity Center.

**Design considerations:**
+ Although this section discusses several services and options, we recommend that you use IAM Identity Center to manage workforce access, because it has advantages over the other two approaches. Later sections discuss the advantages and use cases for individual approaches. A growing number of AWS managed applications require the use of IAM Identity Center. If you are currently using IAM federation, you can enable and use IAM Identity Center with AWS applications without changing your existing configurations.
+ To improve federation resiliency, we recommend that you configure your IdP and AWS federation to support multiple SAML sign-in endpoints. For details, see the AWS blog post [How to use regional SAML endpoints for failover](https://aws.amazon.com/blogs/security/how-to-use-regional-saml-endpoints-for-failover).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
