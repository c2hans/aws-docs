---
source_url: https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/using-aws-services-to-strengthen-compliance-and-governance.html
---

# Using AWS Services to Strengthen Compliance and Governance
<a name="using-aws-services-to-strengthen-compliance-and-governance"></a>

To meet regulatory obligations such as those under the GDPR, organizations must combine technical, operational, and organizational safeguards. AWS provides a suite of services that help customers implement and manage these safeguards across multi-account cloud environments. The following sections explain how specific AWS services can support key areas of a security and compliance strategy:
+ [**AWS Control Tower**](https://aws.amazon.com/controltower/) – for setting up and governing secure multi-account environments with built-in guardrails.
+ [**AWS Security Hub**](https://aws.amazon.com/security-hub/) – for centralized visibility into security and compliance findings.
+ [**Amazon ****GuardDuty**](https://aws.amazon.com/guardduty/) – for intelligent threat detection and analysis of activity logs.
+ [**Amazon Inspector**](https://aws.amazon.com/inspector/) – for automated vulnerability management and security assessments.
+ [**Amazon ****EventBridge**](https://aws.amazon.com/eventbridge/) (formerly CloudWatch Events) – for triggering automated responses to events and incidents.
+ [**AWS Organizations**](https://aws.amazon.com/organizations/) – for centralized policy management across multiple accounts.
+ [**AWS Systems Manager**](https://aws.amazon.com/systems-manager/) – for operational visibility, automation, and patch compliance.
+ [**AWS Security Lake**](https://aws.amazon.com/security-lake/) – for aggregating and analyzing security data at scale.
+ [**AWS Audit Manager**](https://aws.amazon.com/audit-manager/) – for automating evidence collection and managing audit frameworks.
+ [**AWS Trusted Advisor**](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) – for continuous checks and recommendations across security domains.
+ [**Amazon Macie**](https://aws.amazon.com/macie) – for sensitive data discovery and protection across S3 buckets.

## AWS Control Tower
<a name="aws-control-tower"></a>

[AWS Control Tower](https://aws.amazon.com/controltower/) provides a method to set up and govern a new, secure, multi-account AWS environment. It automates the setup of a landing zone, which is a multi-account environment that is based on best practices blueprints and enables governance using guardrails that you can choose from a pre-packaged list. Guardrails implement governance rules for security, compliance, and operations.

AWS Control Tower provides identity management using [AWS IAM Identity Center](https://aws.amazon.com/iam/identity-center/) (IAM Identity Center) default directory and enables cross-account audit using IAM Identity Center and IAM. It also centralizes logs coming from CloudTrail and AWS Config logs, which are stored in Amazon S3.

## AWS Security Hub
<a name="aws-security-hub"></a>

[AWS Security Hub](https://aws.amazon.com/security-hub/) is another service that supports centralization and can improve visibility into an organization. Security Hub centralizes and prioritizes security and compliance findings from across AWS accounts and services, such as [Amazon GuardDuty](https://aws.amazon.com/guardduty/) and [Amazon Inspector](https://aws.amazon.com/inspector/), and can be integrated with security software from third-party partners to help you analyze security trends and identify the highest priority security issues.

AWS Security Hub Cloud Security Posture Management ([AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html)) provides you with a comprehensive view of your security state in AWS and helps you assess your AWS environment against security industry standards and best practices.

## Amazon GuardDuty
<a name="amazon-guardduty"></a>

[Amazon GuardDuty](https://aws.amazon.com/guardduty/) is an intelligent threat detection service that can help customers more accurately and easily monitor and protect their AWS accounts, workloads, and data stored in Amazon S3. GuardDuty analyzes billions of events across your AWS accounts from several sources, including [AWS CloudTrail Management Events](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.html), [Amazon S3 CloudTrail Events](https://docs.aws.amazon.com/AmazonS3/latest/userguide/cloudtrail-logging-s3-info.html), [Amazon Virtual Private Cloud Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html), and DNS logs. For example, it detects unusual API calls, suspicious outbound communications to known malicious IP addresses, or possible data theft using DNS queries as the transport mechanism. GuardDuty is able to provide more accurate findings by leveraging machine learning-powered threat intelligence and third-party security partners. GuardDuty Malware Protection helps you detect the potential presence of malware by scanning the [Amazon Elastic Block Store](https://aws.amazon.com/ebs/) (Amazon EBS) volumes that are attached to the [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2) instances and container workloads. You can include or exclude specific Amazon EC2 instances and container workloads at the time of scanning. You also have an option to retain the snapshots of Amazon EBS volumes attached to the Amazon EC2 instances or container workloads.

## Amazon Inspector
<a name="amazon-inspector"></a>

[Amazon Inspector](https://aws.amazon.com/inspector/) is an automated security assessment service that helps improve the security and compliance of applications deployed on Amazon EC2 instances. Amazon Inspector automatically assesses applications for exposure, vulnerabilities, and deviations from best practices. After performing an assessment, Amazon Inspector produces a detailed list of security findings prioritized by level of severity.

## Amazon EventBridge
<a name="amazon-eventbridge"></a>

[Amazon EventBridge](https://aws.amazon.com/eventbridge/) was formerly called Amazon CloudWatch Events. EventBridge is a serverless service that uses events to connect application components together, making it easier for you to build scalable event-driven applications. Event-driven architecture is a style of building loosely-coupled software systems that work together by emitting and responding to events. Event-driven architecture can help you boost agility and build reliable, scalable applications.

By creating rules in Amazon EventBridge, you can respond automatically to AWS Security Hub CSPM findings. Security Hub CSPM sends findings as events to EventBridge in near-real time. You can write simple rules to indicate which events you are interested in and what automated actions to take when an event matches a rule. Security Hub CSPM automatically sends all new findings and all updates to existing findings to EventBridge as EventBridge events. You can also create custom actions that allow you to send selected findings and insight results to EventBridge.

## AWS Organizations
<a name="aws-organizations"></a>

[AWS Organizations](https://aws.amazon.com/organizations/) helps you centrally manage and govern complex environments. It enables you to control access, compliance, and security in a multi-account environment. AWS Organizations supports Service Control Policies (SCPs), which define the AWS service actions available to use with specific accounts or Organizational Units (OUs) within an organization.

## AWS Systems Manager
<a name="aws-systems-manager"></a>

[AWS Systems Manager](https://aws.amazon.com/systems-manager/) provides you visibility and control of your infrastructure on AWS. You can view operational data from multiple AWS services from a unified console and automate operational tasks across them. You can have information about recent API activities, resource configuration changes, operational alerts, software inventory, and patch compliance status. Using the integration with other AWS services, you can also take action on resources depending on your operational needs, to help make your environment compliant.

For example, by integrating Amazon Inspector with AWS Systems Manager, security assessments are simplified and automated, because you can install Amazon Inspector agent automatically using Amazon Elastic Compute Cloud Systems Manager when an Amazon EC2 instance is launched. You can also perform automatic remediations for Amazon Inspector findings by using Amazon EC2 System Manager and Lambda functions.

## AWS Security Lake
<a name="aws-security-lake"></a>

[AWS Security Lake](https://aws.amazon.com/security-lake/) provides a comprehensive solution for centralizing security data across your entire organization. It automatically centralizes security data from cloud, on-premises, and custom sources into a purpose-built data lake stored in your account. The service adopts the Open Cybersecurity Schema Framework (OCSF), enabling standardized security data collection and normalization across diverse sources, including AWS services, third-party security solutions, and custom applications. This standardization simplifies security analysis and reporting across your organization. Security Lake automatically creates a copy of your security data in your account's S3 bucket using a column-based Apache Parquet format, optimizing for both storage cost and query performance. The service integrates seamlessly with popular analytics tools like [Amazon Athena](https://aws.amazon.com/athena/), [Amazon OpenSearch](https://aws.amazon.com/opensearch-service/), and [Amazon Quick Sight](https://aws.amazon.com/quicksight/), as well as third-party security information and event management (SIEM) solutions. This integration enables security teams to perform more efficient investigations, generate compliance reports, and conduct threat hunting across their entire security data landscape. By providing a unified view of security data, Security Lake helps organizations meet GDPR requirements for continuous monitoring, incident detection, and demonstrable compliance through comprehensive security data management.

## AWS Audit Manager
<a name="aws-audit-manager"></a>

[AWS Audit Manager](https://aws.amazon.com/audit-manager/) helps simplify the continuous auditing of AWS usage, making it easier to assess risk and compliance with regulations, industry standards, and company policies. It automatically collects and organizes relevant evidence across AWS accounts and services, mapping it to the controls required for common frameworks such as GDPR, HIPAA, and ISO 27001. The service provides pre-built frameworks that can be customized to align with your organization's specific requirements, while also supporting the creation of custom frameworks for unique compliance obligations. Audit Manager continuously monitors your AWS resource usage and compliance activities, maintaining an audit-ready posture by collecting relevant evidence in the form of configurations, user activity, and compliance results. This evidence is organized into assessments that help demonstrate your compliance posture during audits. The service integrates with other AWS security and compliance tools, including [AWS Security Hub](https://aws.amazon.com/security-hub/), [AWS Config](https://aws.amazon.com/config/), and [AWS CloudTrail](https://aws.amazon.com/cloudtrail/), to provide a comprehensive view of your compliance status. For organizations managing GDPR compliance, [AWS Audit Manager](https://aws.amazon.com/audit-manager/) can help demonstrate ongoing compliance through automated evidence collection and control monitoring, supporting both periodic formal audits and continuous compliance assessments. This automation significantly reduces the manual effort typically required for audit preparation and evidence collection, while providing a centralized view of compliance across your AWS environment.

## AWS Trusted Advisor
<a name="aws-trusted-advisor"></a>

[AWS Trusted Advisor](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) provides real-time guidance to help customers follow AWS best practices for security, cost optimization, performance, reliability, and service limits. From a security management perspective, Trusted Advisor continuously inspects your AWS environment and provides actionable recommendations across multiple security dimensions. It checks for open access ports, overly permissive permissions, unencrypted data storage, unmanaged encryption keys, and other potential security vulnerabilities. For organizations managing GDPR compliance, Trusted Advisor's security checks are particularly valuable in identifying gaps in data protection measures, such as detecting public S3 buckets that might expose personal data or highlighting IAM configurations that could lead to unauthorized access. The service integrates with [AWS Organizations](https://aws.amazon.com/organizations/) to provide a consolidated view of recommendations across multiple accounts, and works in conjunction with [AWS Security Hub](https://aws.amazon.com/security-hub/) to surface security findings. Through the [AWS Health API](https://docs.aws.amazon.com/health/latest/APIReference/Welcome.html), customers can programmatically access [Trusted Advisor's](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/) recommendations and automate responses to security findings. Enterprise and Business Support customers receive access to the full set of Trusted Advisor checks and can utilize [AWS Config](https://aws.amazon.com/config/) rules based on Trusted Advisor best practices, enabling automated, continuous security assessment and remediation across their AWS infrastructure.

## Amazon Macie
<a name="amazon-macie"></a>

[Amazon Macie](https://aws.amazon.com/macie) plays a crucial role in centralized security management by providing automated sensitive data discovery and security assessment across your AWS environment. Using machine learning and pattern matching, Macie automatically discovers and classifies sensitive data such as personally identifiable information (PII), financial data, healthcare information, and credentials stored in Amazon S3 buckets. For GDPR compliance, Macie is particularly valuable as it can identify specific categories of personal data, including European-specific data types such as European tax identification numbers, identity card numbers, and passport information. The service performs continuous analysis of data access patterns and user behavior to detect potential data security risks, such as unencrypted sensitive data or buckets with public access. Macie integrates seamlessly with [AWS Organizations](https://aws.amazon.com/organizations/) for multi-account management and [AWS Security Hub](https://aws.amazon.com/security-hub/) for centralized findings, enabling organization-wide sensitive data discovery and protection. Through its integration with [AWS EventBridge](https://aws.amazon.com/eventbridge/), Macie can trigger automated workflows for remediation actions when it discovers security risks. The service maintains detailed logs of all findings and provides customizable alerts, helping organizations demonstrate their ongoing data protection efforts and respond promptly to potential data privacy incidents. Macie's findings can also be exported to [Amazon Security Lake](https://aws.amazon.com/security-lake/) for long-term analysis and correlation with other security data, providing a comprehensive view of data security posture across the organization.
