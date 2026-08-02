---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/privacy-reference-architecture/global-expansion.html
---

# Strategizing for global expansion
<a name="global-expansion"></a>

**Note**
We would love to hear from you. Please provide feedback on the AWS PRA by taking a [short survey](https://amazonmr.au1.qualtrics.com/jfe/form/SV_cMxJ0MG3jU91Fk2).

[AWS Security Assurance Services](https://aws.amazon.com/professional-services/security-assurance-services/) frequently receives questions regarding architecting for privacy on AWS when expanding globally. Questions revolve around concerns with maintaining compliance with unique privacy requirements, such as data sovereignty obligations or customer contracts, all while avoiding additional costs and operational overhead. Design considerations often include data residency, operator access restriction, resiliency and survivability, and overall independence. For more information, see [Meeting digital sovereignty requirements on AWS](https://d1.awsstatic.com/events/Summits/reinvent2022/SEC205_Meeting-digital-sovereignty-requirements-on-AWS.pdf) (AWS re:Invent 2022 presentation).

The following questions are common, and only you can answer them for your use case:
+ Where does my customers' personal data need to reside?
+ Where is my customer data stored?
+ How and where can personal data cross borders?
+ Does human or service access to data across regions constitute a transfer?
+ How can I be sure that no foreign governments access my customers' personal data?
+ Where can I store my backups and hot or cold sites?
+ To keep data local, should I maintain an AWS landing zone in every region where I provide services? Or can I use an existing AWS Control Tower landing zone?

For data residency requirements, different architecture deployments might work better for different organizations. Some organizations might have requirements that their customers' personal data stay within a specific region. If so, you might be concerned with how to generally comply with regulations while upholding these obligations. No matter the situation, there are multiple considerations when choosing a multi-account deployment strategy.

To define key architecture design components, work closely with your compliance and contract teams to confirm requirements for where, when, and how personal data can cross AWS Regions. Determine what qualifies as data transfer, such as moving, copying, or viewing. In addition, understand whether there are specific resiliency and data protection controls that must be implemented. Do backup and disaster recovery strategies require cross-Region failover? If so, determine which Regions you can use to store your backup data. Determine if there are any requirements for data encryption, such as a specific encryption algorithm or dedicated hardware security modules for key generation. After you align with compliance stakeholders on these topics, start to consider design approaches for your multi-account environment.

The following are three approaches you can use to plan your AWS multi-account strategy, in ascending order of infrastructure segregation:
+ [Central landing zone with managed Regions](#global-expansion-central)
+ [Regional landing zones](#global-expansion-regional)
+ [AWS European Sovereign Cloud](#global-expansion-eea)

It is also important to remember that privacy compliance might not stop at just data sovereignty. Review the rest of this guide to understand possible solutions for many other challenges, such as consent management, data subjects' requests, data governance, and AI bias.

## Central landing zone with managed Regions
<a name="global-expansion-central"></a>

If you want to expand globally but have already established a multi-account architecture in AWS, it's common to want to use the same multi-account landing zone (MALZ) to manage additional AWS Regions. In this configuration, you would continue to operate infrastructure services such as logging, account factory, and general administration from your existing AWS Control Tower landing zone, in the Region where you created it.

For production workloads, you can operate Regional deployments by extending the AWS Control Tower landing zone into a new Region. By doing this, you can extend the AWS Control Tower governance into the new Region. This way, you can keep personal data stores within a specific, managed Region, the data still resides in accounts that benefit from the infrastructure services and AWS Control Tower governance. In AWS Organizations, accounts that contain personal data still roll up under a dedicated Personal Data OU, where all of the data sovereignty guardrails in AWS Control Tower are implemented. In addition, Region-specific workloads are contained in dedicated accounts, rather than establishing production accounts that may contain the same workload in multiple Regions.

This deployment can be the most cost effective, but additional consideration is needed for controlling the flow of personal data across AWS account and Regional boundaries. Consider the following:
+ Logs might contain personal data, so some additional configuration may be required to contain or redact sensitive fields to prevent cross-Region transfer during aggregation. For more information and recommended practices to control log aggregation across Regions, see [Centralized log storage](log-archive-account.md#centralized-log-storage) in this guide.
+ Account for isolation of VPCs and the appropriate bidirectional network traffic flow in the AWS Transit Gateway design. You can limit which Transit Gateway attachments are allowed and approved, and you can limit who or what can change the VPC route tables.
+ You might need to prevent members of your cloud operations team from accessing personal data. For example, application logs that contain customer transaction data may be deemed of higher sensitivity than other log sources. Additional approvals and technical guardrails might be required, such as role-based access control and [attribute-based access control](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html). Also, data might be subject to residency limitations when it comes to access. For example, data in one Region A can only be accessed from within that Region.

The following diagram shows a centralized landing zone with Regional deployments.

![Centralized landing zone with Regional deployments.](http://docs.aws.amazon.com/prescriptive-guidance/latest/privacy-reference-architecture/images/guide-img/a4379862-3434-48e4-8691-64db36363b08/images/9ffce5e7-cc60-486d-bdf5-8373f92555eb.png)

## Regional landing zones
<a name="global-expansion-regional"></a>

Having more than one MALZ can help you achieve stricter compliance requirements by completely isolating workloads that process personal data compared to non-material workloads. AWS Control Tower centralized logging aggregation could be configured by default and therefore simplified. With this approach, you don't need to maintain exceptions for logging with separate streams of logs that require redaction. You could even have a local and dedicated cloud operations team for each MALZ, which limits operator access to local residency.

Many organizations have separate US and EU-based landing zone deployments. Each Regional landing zone has a single, blanket security posture and associated governance for accounts in the Region. For example, encryption of personal data using dedicated HSMs may not be required in workloads in one MALZ, but it might be required in another MALZ.

Although this strategy can scale to meet many current and future requirements, it is important to understand the additional costs and operational overhead associated with maintaining multiple MALZs. For more information, see [AWS Control Tower pricing](https://aws.amazon.com/controltower/pricing/).

The following diagram shows separate landing zones in two Regions.

![Separate landing zones in two Regions.](http://docs.aws.amazon.com/prescriptive-guidance/latest/privacy-reference-architecture/images/guide-img/a4379862-3434-48e4-8691-64db36363b08/images/ba0a7865-d45a-4090-a6be-8e79fe9370af.png)

## AWS European Sovereign Cloud
<a name="global-expansion-eea"></a>

Some organizations require thorough separation of their workloads operating in the European Economic Area (EEA) and workloads operating elsewhere. In this situation, consider the [AWS European Sovereign Cloud](https://aws.eu/). The AWS European Sovereign Cloud is a new, independent cloud for Europe, designed to help customers meet the region's evolving sovereignty needs, including stringent data residency, operational autonomy, and resiliency requirements.

The AWS European Sovereign Cloud is physically and logically separate from existing AWS Regions, all while offering the same security, availability, and performance. Only AWS employees who are located in the EU have control of the operations and support for the AWS European Sovereign Cloud. If you have stringent data residency requirements, the AWS European Sovereign Cloud keeps all metadata that you create (such as the roles, permissions, resource labels, and configurations they use to run AWS) in the EU. The AWS European Sovereign Cloud also features its own billing and usage metering systems.

For this approach, you would use a similar pattern as in the previous section, [Regional landing zones](#global-expansion-regional). However, for services that you provide to European customers, you could deploy a dedicated MALZ in the AWS European Sovereign Cloud.
