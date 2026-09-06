---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-security-controls/detective-controls.html
---

# Detective controls
<a name="detective-controls"></a>

*Detective controls* are security controls that are designed to detect, log, and alert after an event has occurred. Detective controls are a foundational part of governance frameworks. These guardrails are a second line of defense, notifying you of security issues that bypassed the preventative controls.

For example, you might apply a detective control that detects and notifies you if an Amazon Simple Storage Service (Amazon S3) bucket becomes publicly accessible. While you might have preventative controls in place that disable public access to S3 buckets at the account level and then disable access through SCPs, a threat actor can circumvent these preventative controls by logging in as an administrative user. In these situations, a detective control can alert you to the misconfiguration and potential threat.

Review the following about this type of control:
+ [Objectives](#detective-objectives)
+ [Process](#detective-process)
+ [Use cases](#detective-use-cases)
+ [Technology](#detective-technology)
+ [Business outcomes](#detective-business-outcomes)

## Objectives
<a name="detective-objectives"></a>
+ Detective controls help you improve security operations processes and quality processes.
+ Detective controls help you meet regulatory, legal, or compliance obligations.
+ Detective controls provide security operations teams with visibility to respond to security issues, including advanced threats that bypass the preventative controls.
+ Detective controls can help you identify the appropriate response to security issues and potential threats.

## Process
<a name="detective-process"></a>

You implement detective controls implemented in two phases. First, you set up the system to log events and resource states to a centralized location, such as Amazon CloudWatch Logs. After centralized logging is in place, you analyze those logs to detect anomalies that might indicate a threat. Each analysis is a control that is mapped back to your original requirements and policies. For example, you can create a detective control that searches the logs for a specific pattern and generates an alert if it matches. Detective controls are used by security teams to improve their overall visibility into threats and risks that their system might be exposed to.

## Use cases
<a name="detective-use-cases"></a>

### Detection of suspicious behavior
<a name="detection-of-suspicious-behavior.20b82107-3f6b-5ced-94a3-245446cd17c7"></a>

Detective controls help identify any anomalous activity, such as compromised privileged user credentials or access to or exfiltration of sensitive data. These controls are important reactive factors that can help your company identify and understand the scope of anomalous activity.

### Detection of fraud
<a name="detection-of-fraud.d642f5a1-b775-5714-9849-865f28a3e45c"></a>

These controls help detect and identify a threat inside your company, such as a user who is circumventing policies and performing unauthorized transactions.

### Compliance
<a name="compliance.12454bb3-4b89-5e37-b597-e61e4163b4df"></a>

Detective controls help you meet compliance requirements, such as Payment Card Industry Data Security Standard (PCI DSS), and can help prevent identity theft. These controls can help you discover and protect sensitive information that is subject to regulatory compliance, such as personally identifiable information.

### Automated analysis
<a name="automated-analysis.732bb99e-b430-582c-9f5b-15243f8d4deb"></a>

Detective controls can automatically analyze logs to detect anomalies and other indicators of unauthorized activity.

You can automatically analyze logs from different sources such as AWS CloudTrail logs, [VPC Flow Log](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html), and Domain Name System (DNS) logs, for indications of potentially malicious activity. To help with organization, aggregate security alerts or findings from multiple AWS services to a centralized location.

## Technology
<a name="detective-technology"></a>

A common detective control is implementing one or more monitoring services, which can analyze data sources, such as logs, to identify security threats. In the AWS Cloud, you can analyze sources such as AWS CloudTrail logs, Amazon S3 access logs, and Amazon Virtual Private Cloud (Amazon VPC) flow logs to help detect unusual activity. AWS security services, such as Amazon GuardDuty, Amazon Detective, AWS Security Hub CSPM, and Amazon Macie have built-in monitoring functionalities.

### GuardDuty and Security Hub CSPM
<a name="9999999999999999gdu--and-9999999999999999ash-.4796e478-e7e4-5788-a908-5bca0741b13e"></a>

[AWS Security Hub CSPM](https://docs.aws.amazon.com/guardduty/latest/ug/what-is-guardduty.html) uses threat intelligence, machine learning, and anomaly-detection techniques to continuously monitor your log sources for malicious or unauthorized activity. The dashboard provides insights into the real-time health of your AWS accounts and workloads. You can integrate GuardDuty with [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/what-is-securityhub.html), a cloud security posture management service that checks for adherence to best practices, aggregates alerts, and enables automated remediation. GuardDuty sends findings to Security Hub CSPM as a way to centralize information. You can further integrate Security Hub CSPM with security information and event management (SIEM) solutions to extend monitoring and alerting capabilities for your organization.

### Macie
<a name="9999999999999999mce-.07e72d6f-cc00-50c5-8c68-fd6ae237209d"></a>

[Amazon Macie](https://docs.aws.amazon.com/macie/latest/user/what-is-macie.html) is a fully managed data security and data privacy service that uses machine learning and pattern matching to help discover and protect sensitive data in AWS. The following are some of the detective controls and features available in Macie:
+ Macie inspects bucket inventory and all objects stored in Amazon S3. This information can be presented in a single dashboard view, providing visibility and helping you evaluate bucket security.
+ For discovering sensitive data, Macie uses built-in, managed data identifiers and also supports custom data identifiers.
+ Macie integrates natively with other AWS services and tools. For example, Macie issues findings as Amazon EventBridge events, which are automatically sent to Security Hub CSPM.

The following are best practices for configuring detective controls in Macie:
+ Enable Macie on all accounts. By using the delegated management feature, enable Macie on multiple accounts by using AWS Organizations.
+ Use Macie to evaluate the security posture of the S3 buckets in your accounts. This helps prevent data loss by providing visibility into data location and access. For more information, see [Analyzing your Amazon S3 security posture](https://docs.aws.amazon.com/macie/latest/user/monitoring-s3-inventory.html) (Macie documentation).
+ Automate discovery of sensitive data in your S3 buckets by running and scheduling automated processing and data discovery jobs. This inspects S3 buckets for sensitive data on a regular schedule.

### AWS Config
<a name="9999999999999999cc-.3111e256-1a98-509d-813b-a45c156b9134"></a>

[AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) audits and records the compliance of AWS resources. AWS Config discovers existing AWS resources and generates a full inventory, along with the configuration details of each resource. If there are any configuration changes, it records those changes and provides notification. This can help you detect and roll back unauthorized infrastructure changes. You can use AWS managed rules and can create custom rules.

The following are best practices for configuring detective controls in AWS Config:
+ Enable AWS Config for each member account in the organization and for each AWS Region that contains resources that you want to protect.
+ Set up Amazon Simple Notification Service (Amazon SNS) alerts for any configuration changes.
+ Store configuration data in an S3 bucket and use Amazon Athena to analyze it.
+ Automate the remediation of noncompliant resources by using [Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html), a capability of AWS Systems Manager.
+ Use EventBridge or Amazon SNS to set up notifications about noncompliant AWS resources.

### Trusted Advisor
<a name="9999999999999999aws-ta-.e63fdc04-740d-5325-a967-1ee4ac3c9a86"></a>

[AWS Trusted Advisor](https://docs.aws.amazon.com/awssupport/latest/user/trusted-advisor.html) can be used as a service for detective controls. Through a set of checks, Trusted Advisor identifies areas where you can optimize your infrastructure, improve performance and security, or reduce costs. Trusted Advisor provides recommendations based on AWS best practices that you can follow to improve your services and resources. Business and Enterprise Support plans provide access to all available checks for the [pillars](https://docs.aws.amazon.com/wellarchitected/latest/framework/the-pillars-of-the-framework.html) of the AWS Well-Architected Framework.

The following are best practices for configuring detective controls in Trusted Advisor:
+ Review the check level summary
+ Implement resource-specific recommendations for warning and error states.
+ Check Trusted Advisor frequently to actively review and implement its recommendations.

### Amazon Inspector
<a name="9999999999999999ins-.f22c826c-e291-5555-9386-82cdfc0f0689"></a>

[Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html) is an automated vulnerability management service that, after being enabled, continuously scans your workloads for any unintended network exposure or software vulnerabilities. It contextualizes findings into a risk score that can help you determine next steps, such as remediating or confirming compliance status.

The following are best practices for configuring detective controls in Amazon Inspector:
+ Enable Amazon Inspector on all accounts and integrate it into EventBridge and Security Hub CSPM to configure reporting and notifications for security vulnerabilities.
+ Prioritize remediations and other actions based on the Amazon Inspector risk score.

## Business outcomes
<a name="detective-business-outcomes"></a>

### Less human effort and error
<a name="less-human-effort-and-error.fb26cf3e-6e31-529e-bde8-9b5df7b8056a"></a>

You can achieve automation by using infrastructure as code (IaC). Automating deployment, configuration of monitoring and remediation services and tools reduces the risk of manual errors and reduces the amount of time and effort required to scale these detective controls. Automation helps with the development of security runbooks and reduces manual operations for security analysts. Regular reviews help tune the automation tools and continuously iterate and improve the detective controls.

### Appropriate actions against potential threats
<a name="appropriate-actions-against-potential-threats.104357e1-1271-50f7-8d1d-2ff28818b0bb"></a>

Capturing and analyzing events from logs and metrics is crucial to gaining visibility. This helps analysts act on security events and potential threats to help secure your workloads. Being able to quickly identify which vulnerabilities exist helps analysts take appropriate actions to address and remediate them.

### Better incident response and investigative handling
<a name="better-incident-response-and-investigative-handling.4798f15a-a8f3-5763-92fd-9dc4f6414c98"></a>

Automation of detective control tools can increase the speed of detection, investigation, and recovery. Automated alerting and notifications based on defined conditions enable security analysts to investigate and respond appropriately. These responsive factors can help you identify and understand the scope of anomalous activity.
