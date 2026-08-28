---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-aws-managed-services-outcomes/ams-operational-excellence.html
---

# Using AWS Managed Services to achieve operational excellence
<a name="ams-operational-excellence"></a>

AWS Managed Services (AMS) helps you manage the operations of your AWS infrastructure. Whether you're starting with a single-account or multi-account landing zone, AMS can help you adopt AWS at scale and operate efficiently and securely. The proactive, preventative, and detective capabilities in AMS are designed to reduce risk and improve reliability without constraining agility, allowing your organization to prioritize innovation, such as new features and bug fixes. The operational capabilities of AMS include 24/7/365 proactive monitoring and remediation, incident detection and management, security management, patching, backup, and cost optimization. AMS helps you implement operational best practices and provides specialized automations, skills, and experience. For more information, see [AWS Managed Services features](https://aws.amazon.com/managed-services/features/accelerate-operations-plan/).

AMS acts as an extended operating partner. It can help you effectively manage your cloud infrastructure and security operations. This reduces the amount of time your IT operations teams spends performing operational tasks. This allows your team to focus on higher level activities for your applications, fast-tracking the development process to deliver new features to your customers. The following AMS features can help accelerate cloud adoption by reducing the load on internal cloud operations teams:
+ [Security](#security)
+ [Compliance](#compliance)
+ [Proactive incident management](#incident-management)
+ [Automation and automatic remediation](#automation)
+ [Deep AWS expertise](#aws-expertise)
+ [Cost optimization](#cost-optimization)
+ [Timely updates](#patching)
+ [Cloud native](#cloud-native)
+ [Ongoing governance](#governance)
+ [No vendor lock-in](#pay-as-you-go)

## Security
<a name="security"></a>

Security is critical to every company, and it is a key pillar in the AWS Well-Architected Framework. Security best practices at AWS are designed to help protect your organization's data, systems, and assets in the cloud. Logging, monitoring, identity and access management, and encryption are examples of security controls that you can put in place to help protect your cloud resources. A *security control* is a technical or administrative guardrail that prevents, detects, or reduces the ability of a threat actor to exploit a security vulnerability.

AMS continuously helps mitigate cloud operating risks by using AWS best practices and AWS services. Prescriptive, preventative, detective, and responsive security controls are built in. AMS deploys and monitors more than 200 managed guardrails and security checks through AWS services such as [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) and [Amazon GuardDuty](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html). AMS can also automatically remediate findings and noncompliant resources. The AMS response processes align to the National Institute of Standards and Technology (NIST) Cybersecurity Framework (CSF) standards.

For example, GuardDuty is a continuous security monitoring service for your AWS environment. It uses machine learning and threat intelligence feeds, such as lists of malicious IP addresses and domains, to identify potentially unauthorized or anomalous behavior. When you subscribe to AMS, GuardDuty is enabled to monitor your accounts for any sign of compromise, such as unusual access behavior, unauthorized infrastructure deployments, or unusual API calls. For example, GuardDuty detects if a user in your account issues an API call to reduce the password strength requirements in a password policy.

AMS monitors GuardDuty findings 24/7/365. AMS investigates the findings with security experts and collaborates with you to remediate or contain the issue. For more information, see [Proactive incident management](#incident-management) in this guide.

In addition, AMS provides advanced tooling such as [Trusted Remediator](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/trusted-remediator.html), which automates the remediation of security findings from AWS Trusted Advisor checks. Trusted Remediator creates recommendations when Trusted Advisor checks indicate opportunities for you to close security gaps for your AWS accounts. With Trusted Remediator, you can address security recommendations in a safe, standardized way that uses established best practices.

For more information about how AMS can help secure your infrastructure and data in the AWS Cloud, see [Security management](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sec.html) in the AMS documentation.

## Compliance
<a name="compliance"></a>

AMS offers an accelerated path to help you meet compliance requirements. AMS complies with many industry standards, including:
+ Center for Internet Security (CIS)
+ Payment Card Industry Data Security Standard (PCI DSS)
+ Health Insurance Portability and Accountability Act (HIPAA)
+ Health Information Trust Alliance Common Security Framework (HITRUST CSF)
+ Moderate-impact and high-impact FedRAMP workloads

You can accelerate the journey toward many compliance frameworks and other industry frameworks that require similar controls. For example, because AMS complies with PCI DSS, its default infrastructure for security, logging, and auditing helps your organization achieve PCI DSS compliance faster.

To meet industry standards and frameworks, AMS maintains and deploys a library of AWS Config rules to your account. These rules evaluate whether your AWS accounts comply with standards for security and operational integrity. AWS Config continuously tracks configuration changes for your resources. If a change violates the conditions of any rule, AMS reports its findings. According to the severity of the violation, you can configure AMS to automatically remediate the violation. For more information about how AMS uses AWS Config to help protect your accounts, see [Configuration compliance](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-sec-compliance.html) in the AMS documentation.

## Proactive incident management
<a name="incident-management"></a>

With 24/7/365 monitoring, AMS can proactively detect and notify you about critical incidents. It uses a *follow-the-sun* model, in which issues are handled and passed between more than seven geographical locations in different time zones in order to provide continual service. Many of these incidents could result in downtime for critical business functions if not addressed in a timely manner. AMS also performs trend analysis for repeated incidents, in order to help identify and investigate the root cause. The AMS incident management model can drastically reduce mean time to response and mean time to resolution (MTTR) for your organization because the findings have already been identified and reviewed by AWS experts.

## Automation and automatic remediation
<a name="automation"></a>

AMS scales through automation and standardization. Automation and automatic remediation reduce manual errors, drive efficiencies, and improve application reliability. AMS takes an automation-first approach to operations in order to provide consistency, speed, accuracy, and high-quality outcomes. These automations include centralized patching, monitoring, alerting, backing up, restoring, or remediating an issue. For more information about automatic remediation, see [AMS automatic remediation of alerts](https://docs.aws.amazon.com/managedservices/latest/userguide/auto-remediation.html). Through continuous improvement mechanisms, AMS helps resolve complex problems and provides ongoing operational efficiency for all AMS subscribers, globally, regardless of enterprise size or segment. Automating remediation actions reduces the need for staff involvement, which reduces costs and improves consistency and reliability. For example, if an Amazon Elastic Compute Cloud (Amazon EC2) instance is approaching a defined threshold, such as 95%, of its storage capacity, AMS automatically either compresses known logs or extends the underlying disk and file system to help avoid downtime. AMS operations teams would also work with you to identify the root cause to help prevent similar issues in future.

## Deep AWS expertise
<a name="aws-expertise"></a>

AMS operations and delivery teams have deep expertise in operating AWS services and in extending and upskilling your cloud operations and governance capabilities. By using the AMS operational capabilities and experience, you can minimize the number of cloud operations resources your organization requires and scale the business without adding more resources. AMS provides service-level agreements (SLAs) for incident response and restoration, backed by service credits. Because AMS is part of broader AWS Support coverage, AMS has direct access to AWS service experts who can resolve complex technical issues, which can also drastically reduce MTTR.

## Cost optimization
<a name="cost-optimization"></a>

AMS Cloud Service Delivery Managers (CSDMs) make regular recommendations to help you optimize AWS resources and cloud operations. They use various cost optimization tools and services, such as AWS Trusted Advisor, AWS Compute Optimizer, and AWS Well-Architected Tool. AMS can implement required changes at scale by using the [Operations on Demand](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/ops-on-demand.html) feature. Using AMS commonly results in annual operational cost savings that can significantly offset the cost of AMS itself.

Because AMS provides hands-on keyboard services to manage AWS infrastructure, AMS can actually perform cost-optimization changes, such as changing the instance types for underutilized instances. AMS is equipped with advanced cost-efficient features, such as AMS Resource Scheduler, and it has over 20 standard savings patterns that you can use to meet short-term and long-term savings objectives. For more information, see [Cost optimization with AMS Resource Scheduler](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-resource-scheduler.html) in the AMS documentation.

In addition, AMS provides advanced tooling such as [Trusted Remediator](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/trusted-remediator.html), which automates the remediation of cost optimization findings from Trusted Advisor checks. Trusted Remediator creates recommendations when Trusted Advisor checks identify opportunities for you to fix cost leakages, which reduces the overall total cost of ownership (TCO). With Trusted Remediator, you can address security recommendations in a safe, standardized way that uses established best practices.

## Timely updates
<a name="patching"></a>

Through patch orchestration, AMS offers automated operating-system (OS) patching across all AWS accounts and AWS Regions to keep infrastructure up-to-date. This results in timely updates for critical security patches from operating system vendors to reduce security vulnerabilities and help secure the infrastructure. If there is a patch failure, AMS tries to remediate it, and if necessary to preserve smooth operations, it restores the instance from a prepatch backup. You can also use AMS on-demand patching to address zero-day exploits. For more information, see [Patch management](https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/acc-patching.html) in the AMS documentation.

## Cloud native
<a name="cloud-native"></a>

AMS uses cloud-native AWS services for all its automation and tooling to efficiently and cost effectively monitor and manage AWS infrastructure. For example, to perform patch automation, AMS uses a combination of AWS Systems Manager, AWS Lambda, and Amazon Simple Notification Service (Amazon SNS). If you decide to unsubscribe from AMS and your cloud operations team takes over infrastructure and security management, your team doesn't need to upskill to learn any third-party products. You can view all changes and operations that AMS performs in your AWS account.

For more information about how AMS uses cloud-native AWS services to achieve operational excellence for some of its key operational capabilities, see [AMS reference architecture diagrams](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/AWS-managed-services-for-operational-excellence-ra.pdf).

## Ongoing governance
<a name="governance"></a>

AMS augments a Cloud Center of Excellence (CCoE) team by providing ongoing governance related to security, performance, reliability, cost, and overall operational excellence. In addition to self-serve reports, you have designated resources, a Cloud Service Delivery Managers (CSDM) and a Cloud Architect (CA), who act as extended team members who provide ongoing guidance. Through business reviews, they provide deep insights into key operational risks and metrics by using tools such as [AWS Cost Explorer](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html), [AWS Cost and Usage Report](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html), and [AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/). These resources work with you to identify and implement potential improvements. AMS helps offload undifferentiated tasks from your CCoE team, which results in a leaner team that can focus on improving application design and modernization instead of routine governance activities.

## No vendor lock-in
<a name="pay-as-you-go"></a>

Unlike many other service providers, AMS has a month-to-month, pay-as-you-go model, similar to most other AWS services. Cloud operations teams can learn from AMS automation and governance. Over time, as they upskill through experience with AMS, teams can improve their own IT operational practices and eventually take over infrastructure and security management and operations. Because AMS uses only cloud-native AWS services, subscribing to AMS doesn't require commitment to any third-party contracts or licensing.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
