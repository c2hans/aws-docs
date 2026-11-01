---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/multi-region-architecture.html
---

# Multi-Region Architecture
<a name="multi-region-architecture"></a>

Organizations are increasingly adopting AWS multi-Region security architectures to address critical business, regulatory, and operational requirements. Across the available AWS Regions and Availability Zones, customers in [human capital management (HCM)](https://aws.amazon.com/blogs/apn/adopting-multi-region-architecture-to-support-adp-high-availability-requirements/) sector (active-active high availability), [payment processing](https://aws.amazon.com/blogs/architecture/build-a-multi-region-aws-privatelink-backed-service-with-seamless-failover/) (cross-Region failover for critical payment services to reduce RTO), [financial trading and market data](https://aws.amazon.com/blogs/networking-and-content-delivery/how-lseg-connects-the-world-of-finance-using-aws-cross-region-privatelink-to-transform-global-market-data-access/) (cross-Region access to real-time global market data while meeting regional compliance), and [banking](https://aws.amazon.com/blogs/industries/part-1-bbva-building-a-multi-region-multi-country-global-data-and-ml-platform-at-scale) (multi-country data platform managing 8.4 PB across geographic boundaries) demonstrate the breadth of multi-Region adoption drivers — from resilience and data sovereignty to global performance.

This chapter helps you determine whether an AWS multi-Region approach is necessary for your AWS Security Reference Architecture (AWS SRA) deployment and provides prescriptive recommendations for implementing it.

**Important**
Not every workload requires multi-Region. A well-architected multi-Availability Zone (multi-AZ) deployment within a single Region already provides high availability for most scenarios. The drivers below describe the specific circumstances where extending to multiple AWS Regions becomes necessary.

## Key drivers
<a name="multi-region-architecture-key-drivers"></a>

### Regulatory and compliance requirements
<a name="regulatory-and-compliance-requirements.5c48c841-e823-55c6-b024-62fd7d1bb2ae"></a>

#### Data sovereignty and controlled replication
<a name="data-sovereignty-and-controlled-replication.fb8e8ca0-3021-5164-b147-3c9e4cf1185a"></a>

*Data sovereignty* refers to the legal requirement that data must be stored and processed within specific geographic boundaries. Regulations such as [General Data Protection Regulation](https://aws.amazon.com/compliance/gdpr-center/) (GDPR) in the EU, the [UK Data Protection Act 2018](https://www.legislation.gov.uk/ukpga/2018/12/contents) (UK GDPR post-Brexit), and Germany's [Bundesdatenschutzgesetz](https://www.gesetze-im-internet.de/englisch_bdsg/) (BDSG) impose constraints on where data can reside and how it can be replicated.

A common question arises: *Why does data sovereignty require multi-Region rather than simply operating in the single Region where data is captured?*

The answer lies in the intersection of sovereignty requirements and data resilience mandates. Many regulatory frameworks require not only that data stays within approved jurisdictions, but also that it is replicated for resilience, and that replication must itself remain within approved geographic boundaries. For example:
+ A UK-based financial institution may be required to keep data within the UK and Ireland (`eu-west-1` and `eu-west-2`), but not replicate it to Frankfurt or other EU regions. This creates a multi-Region requirement within a constrained geography.
+ AWS has created [opt-in Regions](https://docs.aws.amazon.com/global-infrastructure/latest/regions/aws-regions.html#regions-opt-in-status) specifically to address data sovereignty. With opt-in Regions, customers must actively opt into a Region to make it possible for their data to be present there, making customer intent explicit. This ensures that customer data only gets replicated to the Regions they specify, with safeguards against unexpected replication to other Regions.
+ For customers requiring stronger sovereignty guarantees, AWS supports client-side encryption as a prerequisite for cross-Region data replication. Even if data were inadvertently replicated to an unintended Region, the cryptographic materials would not exist in that Region, rendering the data unreadable.

These constraints apply across regulated industries:
+ **Healthcare and life sciences** – Healthcare providers and pharmaceutical companies must comply with regional data privacy regulations (such as the Health Insurance Portability and Accountability Act (HIPAA) in the US and GDPR in the EU) that dictate where patient records and clinical data can reside. Electronic health record (EHR) platforms are typically deployed across multiple Availability Zones and multiple Regions within approved jurisdictions.
+ **Financial services** – Financial regulators require institutions to maintain infrastructure across geographically separated locations within approved jurisdictions. This creates a multi-Region requirement where both primary and DR environments must remain within regulatory boundaries.
+ **Automotive** – Connected vehicle platforms must comply with local data storage, sovereignty, and privacy requirements across multiple countries, using geo-location routing to connect millions of vehicles to the closest compliant cloud infrastructure.

#### Audit, compliance, and cross-jurisdictional data protection
<a name="audit--compliance--and-cross-jurisdictional-data-protection.437b129e-c45d-5b26-a949-690bad8532a5"></a>

Organizations operating across multiple jurisdictions must demonstrate to auditors and regulators that they can maintain operations and protect data without violating cross-border data transfer restrictions. This is particularly relevant for European organizations subject to GDPR, where data from EU/EEA citizens must not flow to jurisdictions without adequate data protection frameworks unless specific legal mechanisms are in place.

Multi-Region deployment supports audit and compliance requirements in several ways:
+ **Controlled data boundaries** – By deploying in specific Regions within approved jurisdictions, organizations can demonstrate to auditors that data never leaves the approved geography. AWS services like AWS Config, AWS CloudTrail, and AWS Security Hub provide continuous monitoring and audit trails across Regions.
+ **Cross-border transfer controls** – Organizations prioritize digital sovereignty to ensure data is stored, processed, and managed in specific geographic regions in compliance with local laws. This includes requirements around data residency, control over encryption keys, and ensuring that sensitive information does not leave the designated jurisdiction. AWS helps meet these needs through Region-specific services and customer-managed KMS keys.
+ **Multi-region governance – **Organizations require the flexibility to operate in multiple Regions while maintaining consistent security, monitoring, and governance controls across environments. This includes clear audibility, transparency into data handling practices, and access to compliance documentation and certifications.

### Business continuity (BC) and disaster recovery (DR)
<a name="business-continuity--bc--and-disaster-recovery--dr-.27e92167-bafe-5efc-b20b-a6fa066f776e"></a>

The fundamental question arises: *If a single AWS Region already provides multiple Availability Zones with physical separation, why would I need multi-Region for DR?*

The [AWS Disaster Recovery whitepaper](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/business-continuity-plan-bcp.html) states: "Remember that Availability Zones within an AWS Region are already designed with meaningful distance between them, and careful planning of location, such that most common disasters should only impact one zone and not the others. Therefore, a multi-AZ architecture within an AWS Region may already meet much of your risk mitigation needs."

However, multi-Region becomes necessary when:
+ **Your disaster definition extends beyond a single data center or AZ** – For highly critical workloads, deploying infrastructure across multiple Regions with data replication and continuous backups minimizes business impact.
+ **You need a bounded, predictable recovery time** – An [AWS Architecture blog post](https://aws.amazon.com/blogs/architecture/enhance-the-resilience-of-critical-workloads-by-architecting-with-multiple-aws-regions/) states: "While a single Region supports highly available and resilient applications, distributing workloads across multiple Regions enables a bounded recovery time in the rare event of a disruption to the application." Furthermore, "Each Region has strict logical and physical separation from other Regions. This purposeful design helps avoid service and infrastructure disruptions in one Region affecting another Region. This unique property of Regions can be used to build multi-Region applications with predictable fault domains."
+ **Your RTO/RPO requirements demand it** – The four DR strategies offer different recovery profiles:

|
|
| **Strategy** | **RPO or RTO** | **Cost** | **Use case** |
| --- |--- |--- |--- |
| Backup and restore | Hours | $ | Lower priority workloads |
| Pilot light | Tens of minutes | $ | Core services |
| Warm standby | Minutes | $$ | Business critical services |
| Multi-site active/active | Near real time | $$$ | Mission critical, zero downtime |

### Fault isolation and event containment
<a name="fault-isolation-and-event-containment.a3baa151-68b6-5e9b-890d-6cdde2d55226"></a>

AWS provides isolation at multiple levels:
+ *Account-level isolation* provides resource and security boundaries between workloads. AWS recommends separating workloads using accounts to provide strong isolation boundaries for security, billing, and access.
+ *Availability Zone isolation* helps protect against failures in other Availability Zones within the same Region, protecting against localized disasters, such as power outages or floods.
+ *Region-level isolation* helps protect against failures in other Regions. Each AWS Region is physically and logically separated from other Regions. The physical and logical separation of AWS Regions provides a well-defined fault isolation boundary that you can use to create predictable fault boundaries for your own applications.

Account-level isolation protects against incidents spreading to other accounts within a Region. For example, a misconfiguration in one account does not affect another. However, a Regional disruption affects all accounts operating in that Region. Only Region-level isolation, achieved through multi-Region deployment, protects against disruptions that affect an entire Region.

### Performance and user experience
<a name="performance-and-user-experience.9428e994-8937-5553-9e8e-22aa93c66154"></a>

#### Reduced latency
<a name="reduced-latency.070b61ef-4e98-5167-bc8b-0244f868eafa"></a>

*Latency*, the time it takes for data to travel between a user and the application, is fundamentally constrained by the speed of light across physical distance. A user in Tokyo accessing an application hosted exclusively in `us-east-1` (Virginia) experiences significantly higher latency than one accessing the same application from a Region in Asia Pacific. Multi-Region deployment addresses this by placing compute, storage, and application logic closer to end users.

A single Region, even with multiple Availability Zones, serves users from one geographic location. For applications with a geographically distributed user base, this creates an inherent latency penalty for distant users that cannot be solved within a single Region. Multi-Region deployment, combined with intelligent routing, ensures that each user is served from the nearest infrastructure.

#### Enhanced availability
<a name="enhanced-availability.deeeeed8-cf4e-5d24-879f-35835b70cc2c"></a>

Enhanced availability in a multi-Region context means that users continue to experience uninterrupted service even when an entire AWS Region experiences an impairment. This goes beyond the high availability provided by multi-AZ deployments within a single Region.

A multi-AZ deployment within a single Region protects against the failure of individual Availability Zones. However, if the entire Region experiences a service disruption, all users served by that Region are affected. Multi-Region architectures provide an additional layer of availability by ensuring that if one Region is impaired, traffic is automatically redirected to a healthy Region.

#### Global scale
<a name="global-scale.f2e78c59-7656-5585-b873-2509e1ba10cb"></a>

For organizations serving customers across multiple continents, multi-Region deployment is not just about resilience. It is about delivering a consistent, high-quality experience regardless of where users are located. A single-Region deployment forces a trade-off. Users near the Region experience excellent performance, while users far away experience degraded performance. Multi-Region deployment eliminates this trade-off.

Global scale requires more than just handling high traffic volumes (which can be achieved within a single Region through horizontal scaling). It requires geographic distribution of the application stack so that users in different parts of the world receive comparable response times. This is particularly critical for:
+ Global SaaS platforms where customers expect equivalent service levels across Regions
+ Real-time applications** **(such as gaming, video conferencing, and financial trading) where even small latency differences create unfair or degraded experiences
+ Connected devices and Internet of Things (IoT) (such as connected vehicles and industrial IoT), where millions of devices across geographies need low-latency access to cloud services

## Decision framework for multi-Region deployment
<a name="multi-region-architecture-decision-framework"></a>

To help you decide whether you need multi-Region, consider the following decision framework.

|
|
| Question | If yes | If no |
| --- |--- |--- |
| Do regulations require data replication within approved geographic boundaries? | Multi-Region within approved jurisdictions | Single Region may suffice |
| Does your industry regulator mandate geographically separated DR? | Multi-Region required | Multi-AZ may suffice |
| Must you demonstrate to auditors that data never leaves specific jurisdictions while maintaining DR? | Multi-Region within boundaries | Single Region with multi-AZ |
| Is your RTO requirement under 30 minutes for critical workloads? | Consider warm standby or active/active multi-Region | Pilot light or backup and restore may suffice |
| Does your disaster definition include full regional disruption? | Multi-Region required | Multi-AZ within single Region |
| Do you need protection against correlated regional failures (not just AZ failures)? | Multi-Region required | Multi-AZ provides sufficient isolation |
| Do you serve users across multiple continents with latency-sensitive applications? | Multi-Region active-active recommended | CloudFront edge caching with a single Region may suffice |
| Do you need consistent performance for real-time applications globally? | Full multi-Region active-active | Centralized backend with intelligent routing |

**Important**
For most workloads, a well-architected multi-AZ deployment within a single Region provides sufficient resilience. Each Region's Availability Zones are physically separated and designed so that most common disasters impact only one zone. Multi-Region introduces additional infrastructure management, data synchronization, and application design, along with higher costs from cross-Region data transfer and duplicate infrastructure. Organizations SHOULD NOT adopt a multi-Region architecture by default. Organizations SHOULD adopt multi-Region only when a documented driver (data sovereignty, regulatory DR, fault isolation, or global scale) requires it.

## Multi-Region deployment approach
<a name="multi-region-architecture-deployment-approach"></a>

This section of AWS Security Reference Architecture (AWS SRA) provides holistic guidelines for deploying AWS security services in a multi-account, multi-Region environment. This guidance helps you:
+ Design security service deployments across multiple Regions
+ Understand deployment ordering and dependencies
+ Navigate Regional availability constraints
+ Implement proper delegation models
+ Maintain visibility and protection across your distributed environment

### Foundational prerequisites
<a name="foundational-prerequisites.da707c31-b3de-59c0-b314-e87ad2139c44"></a>

Before expanding to additional Regions, ensure the following prerequisites are met:

|
|
| Prerequisite | Detail (common) | Detail (AWS Control Tower) | Detail (AWS Organizations only) |
| --- |--- |--- |--- |
| Landing zone or organization home Region established | The home region cannot be changed after initial setup. You must explicitly enable and govern additional Regions. | Selected during landing zone setup. Additional Regions are added through `enabledRegions` and enrolled in AWS Control Tower. | Selected during creation of your organization. Each additional Region MUST be explicitly enabled and MUST be under landing zone governance before workloads are deployed to it. |
| Region deny SCPs deployed | Attach at OU level to restrict unauthorized Regions. Define allowed Regions, exempt global services, and exempt break-glass roles. Test in a sandbox OU first. | Apply managed control `CT.MULTISERVICE.PV.1`. Configure `AllowedRegions`, `ExemptedPrincipalARNs`, and `ExemptedActions` parameters. | Create a custom SCP with explicit deny by using the `aws:RequestedRegion` condition key. Define allowed Regions in the `condition` block. |
| Global service exemptions in SCPs | Ensure Region deny SCPs exempt: IAM, AWS Organizations, CloudFront, Route 53, Shield, AWS STS, AWS Support, AWS Budgets, and Cost Explorer. | — | — |
| AWS KMS multi-Region keys replicated | Multi-Region KMS keys must be replicated to every governed Region before enrolling Regions. IAM Identity Center multi-Region replication requires a multi-Region customer-managed KMS key. | — | — |
| AWS Config enabled everywhere | AWS Config recorder must be active in every account and every activated Region, including the management account. | Requires separate sra-config-management-account solution for the management account. | Deploy via CloudFormation StackSets from the management account or a delegated administrator. Include the management account using a separate stack or self-managed stack set. |
| Region deny resource control policies (RCPs) | Deploy RCPs at the OU level to complement SCPs with resource-level Region restrictions. RCPs control what resources can do, not just what principals can do. | Not natively managed by AWS Control Tower. Deploy through Organizations directly or through Customizations for Control Tower (CfCT). | Manage directly in the Organizations console, AWS CLI, or through IaC tools such as CloudFormation |
| SCP management model | Use a deny-list model with `FullAWSAccess` as the default allow. | Do not manually edit CT-managed SCPs. Use CfCT or AFC for custom policies. SCPs have a maximum size of 10,240 characters. | Manage SCPs directly in Organizations console, AWS CLI, or though IaC. Up to 10 SCPs per OU attachment, and 10,240 characters per SCP. |
| Governance automation | Automate SCP/RCP deployment across OUs and Regions. Implement drift detection. | Use CfCT or Landing Zone Accelerator (LZA). AWS Control Tower provides built-in drift detection for managed controls. | Use CloudFormation StackSets, Terraform, or Organizations APIs. Implement custom drift detection via AWS Config rules or AWS Lambda. |

### Operational recommendations
<a name="operational-recommendations.09615bf8-4a02-5540-8983-af6861d26e89"></a>
+ **Deploy one Region at a time, validate before proceeding** – Organizations SHOULD enable one Region at a time and SHOULD validate controls in that Region before enabling the next. This reduces impact scope and simplifies troubleshooting.
+ **Verify service quotas match across all target Regions** – Quotas are per-Region and do not automatically replicate.
+ **Test Region deny SCPs in a sandbox OU** – Misconfigured deny policies can lock out access to existing resources. Always validate in a sandbox OU first.
+ **Automate through CloudFormation StackSets** – Ensures consistent deployment across accounts and Regions by using AWS SRA code library templates.
+ **Implement AWS Config conformance packs per Region** – Provides automated compliance validation in each Region independently.
+ **Establish a runbook for adding new Regions** – Consider dependencies between services
+ **Protect critical configurations via SCPs** – Deny deletion or modification of CloudTrail, AWS Config, IAM Access Analyzer, and KMS keys.
+ **Account for GovCloud gaps** – AWS Security Incident Response and Amazon Macie are absent in GovCloud. Use AWS Systems Manager Incident Manager and manual classification as alternatives.

## Amazon GuardDuty
<a name="multi-region-architecture-guardduty"></a>

[Amazon GuardDuty](https://aws.amazon.com/guardduty/) is a fully managed, continuous security threat detection service for your AWS environment. It uses machine learning, anomaly detection, and integrated threat intelligence to automatically analyze AWS logs and data to identify unauthorized activity, suspicious activity, and potential data exposure. For architectural best practices, refer to the [Amazon GuardDuty](security-tooling.md#tool-guardduty) section in this guide.

### Multi-Region considerations
<a name="multi-region-considerations.0c8419fd-36d8-5a45-b113-8b3541b82ab0"></a>

When working with Amazon GuardDuty you must consider that it is a regional service. This means that for every Region in which you deploy the GuardDuty detector, you MUST do the following actions:

1. Enable GuardDuty in each Region in the management account.

1. Designate the delegate admin to the Security Tooling account (in the Security OU).

1. Ensure that the GuardDuty detector is enabled for all member accounts, foundational data sources are enabled, and protection plans are in place.

When working in multi-Regional deployment in GuardDuty you MUST aggregate all findings in a centralized bucket following AWS best practices. This bucket is deployed in the Log Archive account in the Region selected as primary. To centralize GuardDuty findings, you must set the centralized bucket in each of the detectors of the delegated admin account as the target for the findings.

### Architecture
<a name="architecture.e665b498-64bd-551e-991a-5650c2ee4704"></a>

The following diagrams show the configuration needed for the multi-Region delegated administration set up and the configuration for finding centralization in the primary Region.

The following image shows a multi-Region delegated architecture.

![Multi-Region delegated architecture for GuardDuty.](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/images/guide-img/91d313fc-d5f1-45a8-a5a6-2f4fc7abc93a/images/4eacd5bd-5792-4304-a7a4-c59ef4129634.png)

The following image shows a finding aggregation architecture.

![Finding aggregation architecture for GuardDuty.](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/images/guide-img/91d313fc-d5f1-45a8-a5a6-2f4fc7abc93a/images/a24ca022-690a-4741-9e26-5e995c645eb8.png)

## Amazon Inspector
<a name="multi-region-architecture-inspector"></a>

[Amazon Inspector](https://aws.amazon.com/inspector/) is a fully managed, automated vulnerability management service. It continuously scans AWS workloads for software vulnerabilities (CVEs), unintended network exposures, and insecure configurations. For architectural best practices, refer to the [Amazon Inspector](security-tooling.md#tool-inspector) section in this guide.

### Multi-Region considerations
<a name="multi-region-considerations.b89224e1-5f42-56ff-b93b-3d8f1091acea"></a>

When working with Amazon Inspector, you must consider that it is a Regional service. This means that for every Region in which you deploy workloads, you MUST perform the following actions:

1. Enable Amazon Inspector in each Region in the management account.

1. Designate the delegate admin to the Security Tooling account (in the Security OU).

1. Ensure that Amazon Inspector is enabled for all member accounts and new accounts, and that all scans are activated.

When working in multi-Regional deployment in Amazon Inspector, you must aggregate all findings in a centralized bucket to follow AWS best practices. This bucket is deployed in the Log Archive account in the Region selected as primary. To centralize Amazon Inspector findings, you must create an Amazon EventBridge rule in each of the Regions of the security tooling account to capture all aggregated findings per Region. Rules deployed in non-primary Regions should point to an event bus in the primary Region. This bus serves as an aggregator of all the findings. A final EventBridge rule (aggregator rule) should point to an Amazon Data Firehose in the Log Archive account in the primary Region. This Firehose stream has the centralized logging bucket as a destination. This allows Amazon Inspector to aggregate findings for all Regions and accounts in your AWS organization.

### Architecture
<a name="architecture.daa9209e-e4ab-54c5-9373-cdfc8a986a93"></a>

The following diagram shows the high-level architecture of the delegated administrator configuration and the finding aggregation architecture.

![For Amazon Inspector, the delegated administrator configuration and the finding aggregation architecture.](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/images/guide-img/91d313fc-d5f1-45a8-a5a6-2f4fc7abc93a/images/03899b26-00f4-42af-9ea7-41f30bca2040.png)

## AWS CloudTrail
<a name="multi-region-architecture-cloudtrail"></a>

[AWS CloudTrail](https://docs.aws.amazon.com/cloudtrail/) is a managed governance, compliance, and auditing service. It automatically records and logs every API call made across your AWS account. For architectural best practices, refer to the [AWS CloudTrail](security-tooling.md#tool-cloudtrail) section in this guide.

### Multi-Region considerations
<a name="multi-region-considerations.31083493-526b-5bde-a60c-628d35ddad63"></a>

The [AWS SRA best practices for CloudTrail](checklist.md#checklist-cloudtrail) states that a multi-Region organizational trail should be created and configured to deliver all CloudTrail management events from the management account and all member accounts. With this organizational trail, all managements events in all Regions from all the accounts are captured so there is no additional configuration needed. The organizational trail should be created in the primary Region of your AWS organization.

### Architecture
<a name="architecture.7782e8c4-4f7d-50ae-a575-369854495a70"></a>

The following diagram shows the high-level architecture of the CloudTrail configuration and event aggregation in a multi-account environment for the primary Region.

![CloudTrail configuration and event aggregation in a multi-account environment for the primary Region.](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/images/guide-img/91d313fc-d5f1-45a8-a5a6-2f4fc7abc93a/images/fb0b9cd5-f0d2-4d0b-94cf-540b54f681d3.png)

## AWS Config
<a name="multi-region-architecture-config"></a>

AWS Config provides a detailed view of the configuration of AWS resources in your AWS account. This includes how the resources are related to one another and how they were configured in the past so that you can see how the configurations and relationships change over time. For architectural best practices, refer to the [AWS Config](security-tooling.md#tool-config) section in this guide.

### Multi-Region considerations
<a name="multi-region-considerations.bb1c5bde-d87c-5bdb-9446-28429bfb9ee5"></a>

As described in [AWS](checklist.md#checklist-config)[ SRA best practices for AWS Config](checklist.md#checklist-config), the recorder should be deployed in all accounts and Regions, and the organization aggregator should be configured as multi-Region. With this configuration, AWS Config will track resources from all Regions in all accounts. These recorded changes are aggregated in the organizational aggregator for further analysis. This recorder is deployed in the delegated administrator account for AWS Config, which would be the Security Tooling account.

Additionally, configure AWS Config findings to be aggregated to a centralized bucket in the primary Region in the Logging Account. Each recorder in every account and Region must be configured to use the centralized bucket as the target for config logs.

### Architecture
<a name="architecture.de55e60e-02a3-534b-b795-d2e462ad5132"></a>

The following diagrams show the high-level overview of the delegated administrator, the aggregator, and the recorder log centralization configuration.

Delegated administrator and aggregator configuration:

![Delegated administrator and aggregator configuration for AWS Config.](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/images/guide-img/91d313fc-d5f1-45a8-a5a6-2f4fc7abc93a/images/5c36b9ce-fa93-4b38-b942-babac21a87b5.png)

Log centralization configuration:

![Log centralization configuration for AWS Config.](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/images/guide-img/91d313fc-d5f1-45a8-a5a6-2f4fc7abc93a/images/933e5ef9-fb89-49cb-9767-2c0f22db52e1.png)

## IAM Access Analyzer
<a name="multi-region-architecture-iam-access-analyzer"></a>

[AWS Identity and Access Management Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) is an automated reasoning tool that helps security and operations teams implement the principle of least privilege. It continuously evaluates your AWS environment to identify unintended public or cross-account exposure, map internal access, and pinpoint unused permissions. For architectural best practices, refer to the [IAM Access Analyzer](security-tooling.md#tool-iam-analyzer) section in this guide.

### Multi-Region considerations
<a name="multi-region-considerations.f58110ee-348f-5018-8889-fe6e6a79d2fa"></a>

When working with IAM Access Analyzer, you must consider that it is a Regional service. This means that for every Region in which you deploy workloads, you MUST perform the following actions:

1. Enable IAM Access Analyzer in each Region in the management account.

1. Designate the delegate admin to the Security Tooling account (in the Security OU).

1. Ensure that analyzers (external, internal, and unused) are enabled for all member accounts.

When working in a multi-Region deployment with IAM Access Analyzer, you SHOULD aggregate all findings in a centralized bucket to follow AWS best practices. This bucket is deployed in the Log Archive account in the Region selected as primary. To centralize IAM Access Analyzer findings, you must create an Amazon EventBridge rule in each of the Regions of the Security Tooling account to capture all aggregated findings per Region. Rules deployed in non-primary Regions should point to an event bus in the primary Region. This bus serves as an aggregator of all the findings. A final EventBridge rule (aggregator rule) should point to Amazon Data Firehose in the Log Archive account in the primary Region. This Firehose stream will have the centralized logging bucket as a destination, enabling IAM Access Analyzer finding aggregation for all Regions and accounts in your AWS organization.

### Architecture
<a name="architecture.daa9209e-e4ab-54c5-9373-cdfc8a986a93"></a>

The following diagram shows the high-level architecture of the delegated administrator configuration and the finding aggregation architecture.

![For IAM Access Analyzer, delegated administrator configuration and the finding aggregation architecture.](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/images/guide-img/91d313fc-d5f1-45a8-a5a6-2f4fc7abc93a/images/0a0d8bed-542b-4d01-8a5e-c954df594aa5.png)

## IAM Identity Center
<a name="multi-region-architecture-identity-center"></a>

[AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/) is the recommended service for centrally managing single sign-on (SSO) access to multiple AWS accounts and cloud applications. You can securely connect your existing corporate directory or create users natively, giving your team one portal to access all their assigned resources. For architectural best practices, refer to the [AWS IAM Identity Center](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-identity-management/workforce-iam-identity-center.html) section in the *AWS Security Reference Architecture (AWS SRA) – identity management* guide.

### Multi-Region considerations
<a name="multi-region-considerations.c60278f7-206f-59cb-b055-a9bd1451280d"></a>

IAM Identity Center supports multi-Region by replicating workforce identities, permission sets, and other metadata in your organization instance of IAM Identity Center connected to an external identity provider (IdP), such as Microsoft Entra ID and Okta, from its current primary Region to additional Regions. You can deploy AWS managed applications in your preferred Regions, close to application users and datasets for improved user experience or to meet data residency requirements. Your applications deployed in additional Regions access replicated workforce identities locally for improved performance and reliability. When you replicate your workforce identities to an additional Region, your workforce gets an active AWS access portal endpoint in that Region. This means that in the unlikely event of an IAM Identity Center service disruption in its primary Region, your workforce can still access their AWS accounts through the AWS access portal in an additional Region by using already provisioned permissions. You can continue to manage IAM Identity Center configurations from the primary Region, maintaining centralized control.

Replicating IAM Identity Center to additional AWS Regions provides two key benefits:
+ **Improved resiliency of AWS account access **– Your workforce can access their AWS accounts even if the IAM Identity Center instance experiences a service disruption in its primary Region.
+ **Enhanced flexibility in choosing deployment Regions for AWS managed applications **– You can deploy AWS managed applications in your preferred Regions to meet application data residency requirements and improve performance through proximity to users. Applications deployed in additional Regions can access replicated workforce identities locally for improved performance and reliability.

The replication is asynchronous, meaning that changes in the primary Region are not replicated in real time to the secondary Region.

There are some prerequisites:
+ Multi-Region is only available on organization instances.
+ Your identity source must be an external IdP, such as Okta or the Identity Center directory. Multi-Region is not available for instances using Active Directory.
+ Your instance must be encrypted with a multi-region customer managed KMS key in the same account.
+ Your IdP must support multiple SAML ACS URLs (applies only when using an external IdP).

**Design consideration**:
+ When choosing an additional Region, pick one geographically distant from your primary for maximum resiliency, so if the primary Region experiences a disruption, a distant Region is unlikely to be affected by the same event. If data residency or compliance drives the decision, choose the Region where your regulated datasets live. Where neither constraint applies, choose the Region closest to your users. Before finalizing, confirm that the AWS managed applications your organization uses are available in that Region.

### Architecture
<a name="architecture.ea0a856f-f86e-582c-a26f-abe4e237da85"></a>

[For the multi-Region setup process, refer to the IAM Identity Center documentation](https://docs.aws.amazon.com/singlesignon/latest/userguide/replicate-to-additional-region.html).

## AWS Security Hub
<a name="multi-region-architecture-security-hub"></a>

[AWS Security Hub](https://aws.amazon.com/security-hub/) is a unified cloud security solution that prioritizes your critical security issues and helps you respond at scale. Security Hub detects security issues by automatically correlating and enriching security signals from multiple sources.It serves as a central dashboard to streamline compliance management and automate incident response. For architectural best practices, see [Introduction to AWS Security Hub](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub-v2.html).

### Multi-Region considerations
<a name="multi-region-considerations.d76a2bb8-8ade-5c90-bcbc-53c89a5d0b95"></a>

When working with AWS Security Hub, you must consider that it is a Regional service. This means that for every Region in which you deploy workloads you must perform the following actions:

1. Enable Security Hub in the management account in the home Region.

1. Designate the delegated admin to the Security Tooling account (in the Security OU).

1. Enable Security Hub for all member accounts across all active Regions. Two types of [configurations ](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-v2-da-policy.html)are available: **Policies** and **Deployments**.

1. Configure cross-Region aggregation by designating a home Region and linking all active Regions.

When working in multi-Regional deployment with AWS Organizations integration, Security Hub natively aggregates all findings, resources, and trends from all member accounts and all linked Regions into the delegated administrator's home Region via [cross-Region aggregation](https://docs.aws.amazon.com/securityhub/latest/userguide/security-hub-region-aggregation.html). This means findings, resources and trends from each Region in each member account are sent directly to the delegated administrator's home Region. There is no need for EventBridge rules in each Region to aggregate findings. In addition to new data, Security Hub also replicates updates to data between the linked Regions and the home Region. Updates that occur in a linked Region are replicated to the home Region. Updates that occur in the home Region are replicated back to the linked Region. If there are conflicting updates in the home Region and the linked Region, then the most recent update is used. To centralize findings in a logging bucket to follow AWS best practices, you only need to create a single EventBridge rule in the delegated administrator's home region to capture all aggregated findings. This rule should point to Amazon Data Firehose in the Log Archive account in the primary Region. This Firehose stream has the centralized logging bucket as a destination, enabling Security Hub finding aggregation for all Regions and accounts in your AWS organization.

### Architecture
<a name="architecture.daa9209e-e4ab-54c5-9373-cdfc8a986a93"></a>

The following diagram shows the high-level architecture of the delegated administrator configuration and the finding aggregation architecture.

![For Security Hub, delegated administrator configuration and the finding aggregation architecture.](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/images/guide-img/91d313fc-d5f1-45a8-a5a6-2f4fc7abc93a/images/35385a28-c752-4198-900c-663db5b8d9ec.png)

## AWS Security Hub CSPM
<a name="multi-region-architecture-security-hub-cspm"></a>

AWS Security Hub CSPM continuously audits your AWS environment against security best practices, evaluates compliance, and identifies misconfigurations. For architectural best practices, see What is [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html).

### Multi-Region considerations
<a name="multi-region-considerations.93432731-1261-5545-96fc-7740c08c40d5"></a>

When working with Security Hub CSPM, you must consider that it is a Regional service. This means that for every Region in which you deploy workloads, you MUST perform the following actions:

1. Go to Security Hub CSPM in the management account in the home Region.

1. Designate the delegated admin for Security Hub CSPM to the Security Tooling account (in the Security OU).

1. Enable [central configuration](https://docs.aws.amazon.com/securityhub/latest/userguide/central-configuration-intro.html) from the delegated administrator account. This allows the delegated administrator to configure Security Hub CSPM settings (standards, controls, and enablement) across multiple accounts, OUs, and Regions from the home Region.

1. Create configuration policies from the delegated administrator account to enforce standards and controls across all centrally managed accounts and Regions.

1. Configure cross-Region aggregation in the delegated administrator account by designating a home Region and linking all other active Regions. This aggregates findings, insights, control compliance statuses, and security scores from all linked Regions and all member accounts into the delegated administrator's home Region.

When working in multi-Regional deployment with AWS Organizations integration, Security Hub CSPM natively aggregates all findings from all member accounts and all linked Regions into the delegated administrator's home Region via cross-Region aggregation. Unlike other AWS services, Security Hub CSPM has a built-in cross-Region aggregation feature. This means findings from each Region in each member account are sent directly to the delegated administrator's home Region. There is no intermediate aggregation step in the management account and no need for EventBridge rules in each Region to aggregate findings. To centralize findings in a logging bucket to follow AWS best practices, you only need to create a single Amazon EventBridge rule in the delegated administrator's home Region to capture all aggregated findings. This rule should point to Amazon Data Firehose in the Log Archive account in the primary Region. This Firehose stream has the centralized logging bucket as a destination, enabling Security Hub CSPM finding aggregation for all Regions and accounts in your AWS organization.

### Architecture
<a name="architecture.29eafad6-67d4-5141-825b-eab1aff45f03"></a>

The following diagram shows the high-level architecture of the delegated administrator configuration, cross-Region aggregation, and the finding centralization architecture. has a native cross-Region aggregation feature. All findings from all linked Regions flow natively to the home Region.

![Delegated administrator configuration, cross-Region aggregation, and the finding centralization architecture for Security Hub CSPM.](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/images/guide-img/91d313fc-d5f1-45a8-a5a6-2f4fc7abc93a/images/e0171f79-0263-430d-937f-05ffe64e1bab.png)

## AWS Backup
<a name="multi-region-architecture-backup"></a>

[AWS Backup](https://docs.aws.amazon.com/aws-backup/latest/devguide/whatisbackup.html) is a fully managed, policy-based service that centralizes and automates data protection across AWS services and hybrid environments. It eliminates the need for custom backup scripts or manual processes, allowing you to easily configure backup policies, retention schedules, and compliance monitoring from a single place.

AWS Backup cross-account management provides two distinct delegated capabilities. The first is cross-account jobs monitoring, which is configured in the AWS Backup console and allows the delegated administrator to monitor backup, restore, and copy jobs across all member accounts in the organization. The second is backup policy management, which is configured separately in the AWS Organizations console (delegated administrator for AWS Organizations) and allows the delegated admin to create, modify, delete, attach, and detach backup policies across the organization. To delegate both capabilities to a member account, complete a two-step process: first, register the account in the AWS Backup console, and then delegate policy permissions through the AWS Organizations console.

You MUST delegate the administrator account for monitoring features just in one Region, and it will be activated in all of the active Regions.

### Multi-Region considerations
<a name="multi-region-considerations.8c67c359-baaf-55f7-ac00-43c512488ae2"></a>

In AWS Backup you must consider that some of the resources involved are Regional (like backup plans and vaults), but Organizations backup policies are global. Delegating the administrator account for cross-account monitoring in one Region activates it across all active Regions. For more information, see the [AWS SRA best practices checklist](checklist.md).

### Architecture
<a name="architecture.76c100fe-36d5-5371-a4cc-03289ce8772c"></a>

The following diagram shows a high-level overview of the AWS Backup architecture and deployment for a multi-Region environment.

![AWS Backup architecture and deployment for multiple Regions.](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture/images/guide-img/91d313fc-d5f1-45a8-a5a6-2f4fc7abc93a/images/1d6f6ec9-bc81-499a-8d05-80b0dbe54133.png)

There are two flows:
+ **Deploy AWS Backup vaults** – For this task you can rely on AWS CloudFormation stack sets to deploy AWS Backup vaults in the selected Regions. For more information, see [Managing stacks across accounts and Regions with StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html).
+ **Deploy AWS Backup policies** – AWS Organizations backup policies let you deploy backup plans at scale in all AWS accounts and Regions in your organization. In these backup plans, you set up the main AWS Backup vault and the cross-Region action to the secondary AWS Backup vault. For more information, see [Backup policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_backup.html) in the Organizations documentation.
