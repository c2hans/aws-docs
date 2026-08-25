---
source_url: https://docs.aws.amazon.com/decision-guides/latest/decision-guides/identity-on-aws-how-to-choose.html
---

# Choosing an AWS identity service
<a name="identity-on-aws-how-to-choose"></a>

**Taking the first step**

|  |  |
| --- |--- |
| **Time to read** |  10 minutes  |
| **Purpose** | Help determine which AWS identity service is the best fit for your organization. |
| **Last updated** | August 15, 2025 |

## Introduction
<a name="intro"></a>

 Identity and access management helps ensure that only authenticated and authorized users can access only the cloud resources that they need to perform their tasks, and that they can do it in a secure and compliant way.

![Diagram showing identity, authentication, and authorization.](http://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/understand-identity-services.png)

As shown in the preceding diagram, identity is the unique identification of an entity, authentication is the process of verifying the identity, and authorization is the process of determining what the authenticated entity is allowed to do.

 AWS offers multiple services that help you manage access to your resources on AWS. These include the following:

|  |  |
| --- |--- |
| **Services covered** |  +  [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.htm) <br />+  [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) <br />+  [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) <br />+  [AWS Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html) <br />+  [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html) <br />+  [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html) <br />+  [Amazon Verified Permissions](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html)   |

 Though there are similarities between some identity services, these services address different scenarios. This decision guide helps you get started and choose the right AWS identity service for your use case.

## Understand AWS identity and access management
<a name="understand"></a>

 Understanding the foundations of IAM can help you meet your needs.

Principals, including human users, workloads, federated users, and assumed roles, access AWS services by using APIs. All AWS compute environments deliver credentials that applications use to sign their API calls and request access to AWS services. API requests are authenticated and authorized by a system of identities (such as IAM roles), actions (IAM policies), and resources that are defined in IAM. Every AWS customer configures these to use AWS APIs. IAM roles are identities with temporary and conditional permissions to perform scoped actions on AWS resources. IAM policies define the actions that IAM roles can perform on specific AWS resources.

By carefully crafting IAM policies, you can ensure that the permissions available to an IAM role allow access only to the resources needed to fulfill a task: a concept known as *least privilege*.

## Consider criteria for choosing an AWS identity service
<a name="consider"></a>

 Choosing the right AWS services depends on your needs, and on the following considerations:
+ **Who requires access** - you and your workforce, a machine and your workloads, or the applications you build.
+ **What they want to access** - AWS accounts; AWS applications and services, and the data in them; or data in the applications you build.
+ **Where they want to access it from** - from within AWS, from your on-premises environment, from another cloud environment, or from AWS IoT devices.

## Choose which AWS identity services to use
<a name="choose"></a>

The following table helps you find recommended AWS services for your use cases. For best results, consider the additional services and capabilities recommended for your objective.

| I am a... | I want to... | AWS identity service | Additional services and capabilities to consider |
| --- | --- | --- | --- |
| Cloud/Identity administrator | Make it easier for my team to grant and audit access to AWS applications, such as Amazon Q and Amazon SageMaker AI. | [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) | [Trusted identity propagation in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-overview.html)<br />[AWS Lake Formation](https://docs.aws.amazon.com/singlesignon/latest/userguide/tip-tutorial-lf.html)<br />[Amazon S3 Access Grants](https://docs.aws.amazon.com/singlesignon/latest/userguide/tip-tutorial-s3.html) |
| Cloud/Identity administrator | Make it easier for the owners of my organization's data to grant data access by workforce user or group. | [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) | [Trusted identity propagation in IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/trustedidentitypropagation-overview.html)<br />[AWS Lake Formation](https://docs.aws.amazon.com/singlesignon/latest/userguide/tip-tutorial-lf.html)<br />[Amazon S3 Access Grants](https://docs.aws.amazon.com/singlesignon/latest/userguide/tip-tutorial-s3.html) |
| Cloud/Identity administrator<br />OR<br />Developer | Configure workforce access to AWS accounts and the resources in them, such as Amazon S3 buckets. | [IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)<br />[Federation with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html#id_roles_providers_iam) | [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/what-is-control-tower.html)<br />[Centralize root access for member accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-enable-root-access.html)<br />[Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html) |
| Cloud/Identity administrator | Run Active Directory dependent workloads in AWS. | [AWS Directory Service for Microsoft Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html), also known as AWS Managed Microsoft AD | [Integrations with AWS services and applications](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html) |
| Cloud/Identity administrator | Join my AWS workloads to my on-premises Microsoft Active Directory Domain Services. | [AWS Directory Service for Microsoft Active Directory](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/directory_microsoft_ad.html), also known as AWS Managed Microsoft AD | [Integrations with AWS services and applications](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html) |
| Cloud/Identity administrator | Configure the access of my workloads to AWS resources. | [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) | [AWS Resource Access Manager](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) |
| Cloud/Identity administrator | Establish a data perimeter to enforce my organization's security requirements. | [IAM permissions guardrails using data perimeters](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_data-perimeters.html) | [Data perimeters on AWS](https://aws.amazon.com/identity/data-perimeters-on-aws/) |
| Cloud/Identity administrator | Verify which IAM roles and users within my organization have access to critical AWS resources. | [IAM Access Analyzer internal access analysis](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html#what-is-access-analyzer-internal-access-analysis) |  |
| Cloud/Identity administrator | Analyze and refine permissions to drive towards least privilege. | [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) |  |
| Cloud/Identity administrator | Grant on-premises workloads access to AWS. | [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html)<br />(requires PKI, the ability to issue and manage certificates) |  |
| Cloud/Identity administrator | Grant an IoT device access to AWS. | [AWS IoT Device Management](https://docs.aws.amazon.com/iot/latest/developerguide/iot-thing-management.html) |  |
| Developer | Grant code in any external-to-AWS cloud environment access to AWS. | [AWS Security Token Service`AssumeRoleWithWebIdentity`](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRoleWithWebIdentity.html) | [Temporary security credentials in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp.html)<br />[AWS Security Token Service CLI V2 Reference](https://docs.aws.amazon.com/cli/latest/reference/sts/) |
| Developer | Perform service-to-service authentication and authorization in my application running solely in AWS. | [Amazon VPC Lattice](https://docs.aws.amazon.com/vpc-lattice/latest/ug/what-is-vpc-lattice.html) | [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) with [AWS Signature Version 4 authentication](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_sigv.html)<br />[AWS PrivateLink](https://docs.aws.amazon.com/vpc/latest/privatelink/what-is-privatelink.html) |
| Developer | Perform service-to-service authentication and authorization in my application with components in various cloud environments. | [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/federation-endpoints-oauth-grants.html) | [Amazon Verified Permissions](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html) |
| Developer | Enable your customers to access your AI application and manage the identities of AI agents. | [Amazon Bedrock AgentCore Identity](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/identity.html) | [Amazon Bedrock AgentCore](https://aws.amazon.com/bedrock/agentcore/) |
| Developer | Build and manage IoT device software on AWS. | [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html) |  |
| Developer | Build an authentication mechanism into my own application. | [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html) |  |
| Developer | Build an authorization mechanism into an application. | [Amazon Verified Permissions](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html) |  |

## Use AWS identity services
<a name="use"></a>

### For you and your workforce
<a name="for-your-workforce"></a>

#### IAM Identity Center
<a name="for-your-workforce-identity-center"></a>

IAM Identity Center helps you configure the single sign-on experience of your employees from your existing identity provider to user-facing AWS applications, such as Amazon Q and Amazon SageMaker AI, and to the AWS Management Console, including any AWS accounts that are assigned to your employees. With a single connection of your identity provider, you can scale your use of AWS applications as much as your business requires, and offer a continuous user experience across applications.

With IAM Identity Center, AWS applications such as Amazon Q can provide your users with personalized experiences, such as a dashboard showing what a user was working on when they last signed in. Data service owners, such as an Amazon Redshift administrator, can define permissions and audit access to data in AWS by the users in your directory. AWS data and analytics services can recognize your employees by their directory identities. For more information, see [Application access](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-applications.html) in the AWS IAM Identity Center User Guide.

An [*organization instance*](https://docs.aws.amazon.com/singlesignon/latest/userguide/organization-instances-identity-center.html) of IAM Identity Center can help you manage your workforce access to AWS accounts as well. It lets you assign permissions to users and provision the permissions to multiple accounts from a central place. For more information, see [AWS account access](https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-accounts.html) in the AWS IAM Identity Center User Guide.

#### Federation with IAM
<a name="federation-with-iam"></a>

You can also use IAM to federate workforce users through your identity provider to specific AWS accounts. Users assume IAM roles to perform scoped actions on the AWS resources in the account. You can federate with an identity provider that provides identity information using either OpenID Connect (OIDC) or SAML 2.0. For more information, see [Identity providers and federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html).

### For your workloads
<a name="for-your-workloads"></a>

#### IAM
<a name="for-your-workloads-iam"></a>

IAM lets your workload assume IAM roles with temporary security credentials to use AWS APIs and perform scoped actions on AWS resources. For example, they let workloads run code on compute services such as Amazon EC2 or Lambda. For more information, see [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) in the IAM User Guide.

#### IAM Access Analyzer
<a name="for-your-workloads-access-analyzer"></a>

IAM Access Analyzer guides you to least privilege by providing features to set, verify, and refine permissions. It helps you implement your access management strategy by analyzing external, internal, and unused access, and validating that your IAM policies match your specified security standards. Use IAM Access Analyzer to do the following:
+ [Generate least-privilege policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html) based on access activity
+ [Validate that your policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-checks-validating-policies.html) match IAM best practices and your security standards
+ Verify who can access what and [detect unintended public and cross-account access](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-concepts.html#access-analyzer-work-with-findings-external)
+ [Verify internal access to critical resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-concepts.html#access-analyzer-work-with-findings-internal) by identifying which IAM roles and users within your AWS organization have access to critical resources such as Amazon S3 buckets, Amazon DynamoDB tables, and Amazon RDS snapshots.
+ Refine permissions by [identifying unused access](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-concepts.html#access-analyzer-work-with-findings-unused) in your IAM policies

The following image shows the IAM Access Analyzer dashboard with external and internal access findings.

![Dashboard showing external and internal access findings in IAM Access Analyzer](http://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/analyzer-findings-01.png)

The following image shows unused access findings in the IAM Access Analyzer dashboard.

![Dashboard showing unused access findings analysis with 100 active findings, including 40 unused roles, 15 unused credentials, and 45 unused permissions.](http://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/unused-access-analyzer-dashboard.png)

#### IAM Roles Anywhere
<a name="for-your-workloads-iam-roles-anywhere"></a>

IAM Roles Anywhere extends the capabilities of IAM to on-premises and hybrid cloud workloads. Use it to get temporary security credentials and to use the same IAM policies and IAM roles that you use for AWS workloads.

#### AWS Directory Service
<a name="for-your-workloads-ad"></a>

AWS Directory Service for Microsoft Active Directory, also known as AWS Managed Microsoft AD, is a highly available, fully managed Microsoft Active Directory (AD) service. It extends your on-premises Microsoft AD configurations to AWS so that your Microsoft Windows on-premises workloads can communicate with your AWS resources. Using AWS Managed Microsoft AD, you can join to your domain AWS resources such as Amazon EC2 instances, Amazon WorkSpaces managed desktops, and Amazon RDS for Microsoft SQL Server.

### For the applications you build
<a name="for-your-applications"></a>

#### Amazon Cognito
<a name="for-your-applications-cognito"></a>

Amazon Cognito helps your developers implement customer identity and access management (CIAM) in the web and mobile applications that they develop. It is a scalable service they can use in your applications to manage users, authenticate, and authorize their access. In addition to CIAM, Amazon Cognito supports service-to-service authentication and authorization within your applications. It scales to millions of users across devices, and processes more than 100 billion authentications per month.

#### Verified Permissions
<a name="for-your-applications-verified-permissions"></a>

Verified Permissions is a fully managed authorization service, which uses the easy-to-understand [Cedar policy language](https://www.cedarpolicy.com/en) for fine-grained permissions. Authorization decisions are verified formally by using automated reasoning. With Verified Permissions, developers can externalize authorization, align it with [Zero Trust principles](https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-zero-trust-architecture/zero-trust-principles.html), and centralize policy management. Security and audit teams can better analyze and audit who has access to what within your applications.

The following image shows an example of permissions policy details from Verified Permissions and to whom the policy grants access.

![An AWS policy configuration showing a permission that allows SalesTeam members to maintain customer account data.](http://docs.aws.amazon.com/decision-guides/latest/decision-guides/images/customer-data-policy.png)

## Explore other AWS services
<a name="explore"></a>

This section suggests additional services you should consider.
+ [AWS Control Tower](https://aws.amazon.com/controltower) - Lets you set up a well-architected, multi-account AWS environment based on security and compliance best practices, and to manage it at scale.
+ [AWS Resource Access Manager](https://aws.amazon.com/ram) - Helps you share your resources across AWS accounts.
+ [Amazon VPC Lattice](https://aws.amazon.com/vpc/lattice) - Lets you connect, secure, and monitor services and resources for your application.
+ [Amazon API Gateway](https://aws.amazon.com/api-gateway) - Lets you create, publish, maintain, monitor, and secure REST, HTTP, and WebSocket APIs.
+ [AWS IoT Device Management](https://aws.amazon.com/iot-device-management) - Lets you onboard, organize, and manage Internet of Things (IoT) devices.
+ [AWS IoT Greengrass](https://aws.amazon.com/greengrass) - Lets you build, deploy, and manage IoT device software.

## Additional resources
<a name="resources"></a>

 User guides with specific deployment guidance for AWS identity services:
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.htm)
  + [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)
  + [IAM federation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers.html#id_roles_providers_iam)
  + [AWS STS API Reference](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html)
+ [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
+ [IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html)
  + [Policy generation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html)
  + [Policy validation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-checks-validating-policies.html)
  + [Unused permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-concepts.html#access-analyzer-work-with-findings-unused)
  + [External access](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-concepts.html#access-analyzer-work-with-findings-external)
  + [Internal access](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-concepts.html#access-analyzer-work-with-findings-internal)
+ [AWS Directory Service](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/what_is.html)
+ [IAM Roles Anywhere](https://docs.aws.amazon.com/rolesanywhere/latest/userguide/introduction.html)
+ [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/what-is-amazon-cognito.html)
+ [Amazon Verified Permissions](https://docs.aws.amazon.com/verifiedpermissions/latest/userguide/what-is-avp.html)

 AWS Security Blog posts with use case specific guidance:
+ [How to use AWS managed applications with IAM Identity Center (Amazon Q)](https://aws.amazon.com/blogs/security/how-to-use-aws-managed-applications-with-iam-identity-center/)
+ [Cloud infrastructure entitlement management in AWS](https://aws.amazon.com/blogs/security/cloud-infrastructure-entitlement-management-in-aws/)
+ [Customize the scope of IAM Access Analyzer unused access analysis](https://aws.amazon.com/blogs/security/customize-the-scope-of-iam-access-analyzer-unused-access-analysis/)
+ [Use IAM roles to connect GitHub actions to actions in AWS](https://aws.amazon.com/blogs/security/use-iam-roles-to-connect-github-actions-to-actions-in-aws/)
+ [Planning for your IAM Roles Anywhere deployment](https://aws.amazon.com/blogs/security/planning-for-your-iam-roles-anywhere-deployment/)
+ [How to monitor, optimize, and secure Amazon Cognito machine-to-machine authorization](https://aws.amazon.com/blogs/security/how-to-monitor-optimize-and-secure-amazon-cognito-machine-to-machine-authorization/)
+ [How to support OpenID AuthZEN requests with Amazon Verified Permissions](https://aws.amazon.com/blogs/security/how-to-support-openid-authzen-requests-with-amazon-verified-permissions/)
+ [Approaches for authenticating external applications in a machine-to-machine scenario](https://aws.amazon.com/blogs/security/approaches-for-authenticating-external-applications-in-a-machine-to-machine-scenario/)
+ [Blog Post Series: Establishing a Data Perimeter on AWS](https://aws.amazon.com/identity/data-perimeters-blog-post-series/)
+ [Verify internal access to critical AWS resources with new IAM Access Analyzer capabilities](https://aws.amazon.com/blogs/aws/verify-internal-access-to-critical-aws-resources-with-new-iam-access-analyzer-capabilities/)
