---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-directory-service-for-microsoft-ad-well-architected-analysis/performance-efficiency-pillar.html
---

# Performance efficiency pillar
<a name="performance-efficiency-pillar"></a>

The performance efficiency pillar focuses on structured and streamlined allocation of IT and computing resources. The following recommendations can help you meet the** **performance efficiency design principles and architectural best practices for AWS Managed Microsoft AD.

**Key focus areas**
+ Selecting resource types and sizes optimized for workload requirements
+ Monitoring performance
+ Maintaining efficiency as business needs evolve

## Democratize advanced technologies and make their implementation easier for your team
<a name="democratize-advanced-technologies"></a>
+ For data that's configured and deployed through a group policy or home folders and a roaming user profile, use [Amazon FSx for Windows File Server](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/what-is.html).

## Scale globally if needed
<a name="scale-globally"></a>
+ Activate multi-Regional replication when there's a need for users and applications in disperse geographic regions to authenticate against AWS Managed Microsoft AD. For more information, see [Lab 4 – Enable Multi-Region with AWS Managed Microsoft AD](https://catalog.us-east-1.prod.workshops.aws/workshops/b4a4be0e-d4f9-4ff5-af82-ebfb86dbe46a/en-US/2-extending-aws-managed-microsoft-ad/multi) in the Active Directory on AWS Immersion Day Workshop.

## Use serverless architectures
<a name="use-serverless-architectures"></a>
+ Use serverless services, such as AWS Lambda and AWS Secrets Manager, to extend the functionalities of AWS Managed Microsoft AD. For example, serverless products can help users to reset their own passwords. They can also help you obtain temporary credentials for applications without manually provisioning them.

## Test and experiment often
<a name="test-and-experiment-often"></a>
+ Test your infrastructure changes in a test environment before deploying changes to production.
+ Stay up to date on new resources and services and regularly test them in your test environment.

## Consider mechanical sympathy
<a name="consider-mechanical-sympathy"></a>
+ Make a backup of your instance if you decide to manually add an instance to an existing AWS Managed Microsoft AD domain.
+ Use Amazon CloudWatch metrics to generate alarm-based notifications for AWS Managed Microsoft AD. For more information, see [Lab 5 – Create a CloudWatch alarm based on Windows event logs](https://catalog.us-east-1.prod.workshops.aws/workshops/b4a4be0e-d4f9-4ff5-af82-ebfb86dbe46a/en-US/3-aws-managed-microsoft-ad-security-and-compliance/cwa) in the Active Directory on AWS Immersion Day Workshop.

## Improve performance
<a name="improve-performance"></a>
+ Use the Windows DC locator service or the Dynamic DNS (DDNS) service of your AWS Managed Microsoft AD to locate domain controllers (DCs). For more information, see [Enabling clients to locate the next closest domain controller](https://learn.microsoft.com/en-us/windows-server/identity/ad-ds/plan/enabling-clients-to-locate-the-next-closest-domain-controller) in the Microsoft documentation.
+ Use efficient LDAP queries.
+ Automate AWS Managed Microsoft AD scaling based on utilization metrics. For more information, see [How to automate AWS Managed Microsoft AD scaling based on utilization metrics](https://aws.amazon.com/blogs/security/how-to-automate-aws-managed-microsoft-ad-scaling-based-on-utilization-metrics/) on the AWS Blog.
+ Load test before rolling any changes out to production.
+ Choose appropriately sized, dedicated connectivity or a virtual private network (VPN) when you need to establish trust relationships with an on-premises Microsoft Active Directory.
