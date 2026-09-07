---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/privacy-reference-architecture/network-account.html
---

# Infrastructure OU – Network account
<a name="network-account"></a>

**Note**
We would love to hear from you. Please provide feedback on the AWS PRA by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_cMxJ0MG3jU91Fk2).

In the Network account, you manage the networking between your virtual private clouds (VPCs) and the broader internet. In this account, you can implement broad disclosure control mechanisms by using AWS WAF, use AWS Resource Access Manager (AWS RAM) to share VPC subnets and AWS Transit Gateway attachments, and use Amazon CloudFront to support targeted service usage. For more information about this account, see the [AWS Security Reference Architecture (AWS SRA)](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/network.html). The following diagram illustrates the AWS security and privacy services that are configured in the Network account.

![AWS services deployed in the Network account in the Infrastructure organizational unit.](https://docs.aws.amazon.com/prescriptive-guidance/latest/privacy-reference-architecture/images/guide-img/a4379862-3434-48e4-8691-64db36363b08/images/ff33f539-9a1b-49f9-8650-f67ed1e347f2.png)

This section provides more detailed information about the following AWS services that are used in this account:
+ [Amazon CloudFront](#cloudfront)
+ [AWS Resource Access Manager](#aws-ram-network)
+ [AWS Transit Gateway](#transit-gateway)
+ [AWS WAF](#aws-waf)

## Amazon CloudFront
<a name="cloudfront"></a>

[Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/Introduction.html) supports geographic restrictions for frontend applications and file hosting. CloudFront can deliver content through a worldwide network of data centers that are called *edge locations*. When a user requests content that you're serving with CloudFront, the request is routed to the edge location that provides the lowest latency. For more information about how this service is used in a security context, see the [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/network.html#network-cf).

Your privacy program might currently support compliance with specific regional laws. If your workload is scoped to provide services only to customers who reside only within these regions, you might implement technical measures that prevent usage from other regions. You can use CloudFront geographic restrictions to prevent users in specific geographic locations from accessing content that you are distributing through a CloudFront distribution. For more information and configuration options for geographic restrictions, see [Restricting the geographic distribution of your content](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/georestrictions.html) in the CloudFront documentation.

You can also configure CloudFront to generate access logs that contain detailed information about every user request that CloudFront receives. For more information, see [Configuring and using standard logs (access logs)](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html) in the CloudFront documentation. Finally, if CloudFront is configured to cache content at a series of edge locations, you might consider where caching occurs. For some organizations, cross-Regional caching might be subject to cross-border data transfer requirements.

## AWS Resource Access Manager
<a name="aws-ram-network"></a>

[AWS Resource Access Manager (AWS RAM)](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) helps you securely share your resources across AWS accounts to reduce operational overhead and provide visibility and auditability. With AWS RAM, organizations can restrict which AWS resources can be shared with other AWS accounts in their organization or with third-party accounts. For more information, see [Shareable AWS resources](https://docs.aws.amazon.com/ram/latest/userguide/shareable.html). In the Network account, you can use AWS RAM to share VPC subnets and transit gateway connections. If you use AWS RAM to share a data plane connection with another AWS account, you might consider establishing processes to check that the connections are made to preapproved AWS Regions and adhere to your data residency requirements.

In addition to sharing VPCs and transit gateway connections, AWS RAM can be used to share resources that don't support IAM resource-based policies. For a workload hosted in the [Personal Data OU](personal-data-account.md), you can use AWS RAM to access personal data that is located in a separate AWS account. For more information, see [AWS Resource Access Manager](personal-data-account.md#aws-ram-pd-account) in the *Personal Data OU – PD Application account* section.

## AWS Transit Gateway
<a name="transit-gateway"></a>

If you want to deploy AWS resources that collect, store, or process personal data in AWS Regions that align with your organizational data residency requirements and you have the appropriate technical safeguards, consider implementing guardrails to prevent unapproved cross-border data flows on the control and data planes. On the control plane, you can limit Region usage and, as a result, cross-Region data flows by using IAM and service control policies.

There are multiple options for controlling cross-Region data flows on the data plane. For example, you can use route tables, VPC peering, and AWS Transit Gateway attachments. [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html) is a central hub that connects virtual private clouds (VPCs) and on-premises networks. As a part of your larger AWS landing zone, you can consider the various ways data can traverse AWS Regions, including out through internet gateways, through direct VPC-to-VPC peering, and through inter-Region peering with AWS Transit Gateway. For example, you can do the following in AWS Transit Gateway:
+ Confirm that the east-west and north-south connections between your VPCs and on-premises environments are aligned with your privacy requirements.
+ Configure VPC settings according to your privacy requirements.
+ Use a service control policy in AWS Organizations and IAM policies to help prevent modifications to your AWS Transit Gateway and Amazon Virtual Private Cloud (Amazon VPC) configurations. For a sample service control policy, see [Restrict changes to VPC configurations](restrict-changes-vpc-configurations.md) in this guide.

## AWS WAF
<a name="aws-waf"></a>

To help prevent unintended disclosure of personal data, you can deploy a defense-in-depth approach for your web applications. You can build input validation and rate limiting into your application, but AWS WAF can serve as another line of defense. [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/what-is-aws-waf.html) is a web application firewall that helps you monitor HTTP and HTTPS requests that are forwarded to your protected web application resources. For more information about how this service is used in a security context, see the [AWS Security Reference Architecture](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/network.html#network-waf).

With AWS WAF, you can define and deploy rules that inspect for specific criteria. The following activities might be associated with unintended disclosure of personal data:
+ Traffic from unknown or malicious IP addresses or geographical locations
+ Open Worldwide Application Security Project (OWASP) [Top 10 attacks](https://owasp.org/www-project-top-ten/), including exfiltration-related attacks such as SQL injection
+ High rates of requests
+ General bot traffic
+ Content scrapers

You can deploy AWS WAF [rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-groups.html) that are managed by AWS. Some managed rule groups for AWS WAF can be used to detect threats to privacy and personal data, for example:
+ [SQL database](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-use-case.html#aws-managed-rule-groups-use-case-sql-db) – This rule group contains rules designed to block request patterns associated with exploitation of SQL databases, such as SQL injection attacks. Consider this rule group if your application interfaces with a SQL database.
+ [Known bad inputs](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-baseline.html#aws-managed-rule-groups-baseline-known-bad-inputs) – This rule group contains rules designed to block request patterns that are known to be invalid and are associated with exploitation or discovery of vulnerabilities.
+ [Bot Control](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-bot.html) – This rule group contains rules designed to manage requests from bots, which can consume excess resources, skew business metrics, cause downtime, and perform malicious activities.
+ [Account takeover prevention (ATP)](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-atp.html) – This rule group contains rules designed to prevent malicious account takeover attempts. This rule group inspects the login attempts sent to your application's login endpoint.
