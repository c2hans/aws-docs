---
source_url: https://docs.aws.amazon.com/whitepapers/latest/classic-intrusion-analysis-frameworks-for-aws-environments/installation.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Installation
<a name="installation"></a>

 In the *Installation* phase, after vulnerabilities have been successfully exploited, many attackers will attempt to persist undetected in the environment as long as possible, in order to accomplish their objectives. In this phase, attackers will attempt to install tools that allow them to maintain remote access to the victim’s environment.

## Control Objective – Detect
<a name="control-objective-detect-4"></a>

 The objective of the *Detect* control in the *Installation* phase is to “discover or discern the existence, presence, or fact of an intrusion into information systems.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [Amazon GuardDuty](control-name-descriptions.md#amazon-guardduty) <br /> (ID: Sec.Det.1)  |  This control detects reconnaissance activity, such as unusual API activity, intra-VPC port scanning, unusual patterns of failed login requests, or unblocked port probing from a known, bad IP address.  |
|  [Amazon Detective](control-name-descriptions.md#amazon-detective) <br /> (ID: Sec.Det.11)  |  Amazon Detective makes it easy to analyze, investigate, and quickly identify the root cause of potential security issues or suspicious activities. Amazon Detective automatically collects log data from your AWS resources and uses machine learning, statistical analysis, and graph theory to build a linked set of data that enables you to easily conduct faster and more efficient security investigations.  |
| [ Amazon CloudWatch, CloudWatch Logs, CloudTrail \+ Insights, Reporting & Third-Parties](control-name-descriptions.md#amazon-cloudwatch-cloudwatch-logs-cloudtrail-insights-reporting-third-parties)<br /> (ID: Sec.Det.6)  |  These controls monitor, detect, visualize, and receive notifications of attacks, and respond to changes in your AWS resources  |
|  [AWS Security Hub CSPM](control-name-descriptions.md#aws-security-hub) <br /> (ID: Sec.Det.3)  |  This control gives you a comprehensive view of your high-priority security alerts and compliance status across AWS accounts.  |
|  [AWS Security Hub CSPM Partners](control-name-descriptions.md#aws-security-hub-partners) <br /> (ID: Sec.Det.4)  |  AWS Security Hub CSPM APN Partner products are a complement to Amazon GuardDuty.  |
|  [AWS Systems Manager State Manager, AWS Systems Manager Inventory, AWS Config](control-name-descriptions.md#aws-systems-manager-state-manager-aws-systems-manager-inventory-aws-config) <br /> (ID: Sec.Inf.16)  |  When new AWS assets are created, or if malware is installed with a regular package, the AWS Systems Manager Inventory identifies it and sends it to AWS Config for evaluation.  |
|  [Third-Party Security Tools for Containers](control-name-descriptions.md#third-party-security-tools-for-containers) <br /> (ID: Sec.IR.14)  |  This control implements advanced security protection and behavioral security solutions for containers.  |
|  [Third-Party Security Tools for AWS Lambda Functions](control-name-descriptions.md#third-party-security-tools-for-aws-lambda-functions) <br /> (ID: Sec.IR.15)  |  This control implements advanced security protection and behavioral security solutions for Lambda functions.  |
|  [AWS Partner Offerings – Anti-Malware Protection](control-name-descriptions.md#aws-partner-offerings-anti-malware-protection) <br /> (ID: Sec.IR.12)  |  These controls help to detect and block malicious payloads.  |
| [AWS IoT Device Defender \+ AWS IoT SiteWise](control-name-descriptions.md#aws-iot-device-defender-aws-iot-sitewise) <br /> (ID: Sec.Det.9)  |  Detects and provides analytics capabilities and customizable response automation for anomalous behavior in IoT Things  |
| [ Amazon CloudWatch Logs \+ Amazon Lookout for Metrics ](control-name-descriptions.md#amazon-cloudwatch-logs-amazon-lookout-for-metrics)<br /> (ID: Sec.Det.10)  |  Detects and provides analytics capabilities for anomalous behavior in assets and services which send logs to CloudWatch Logs (subject to level of detail of logs being gathered)  |

## Control Objective – Deny
<a name="control-objective-deny-4"></a>

 The objective of the *Deny* control in the *Installation* phase is to “prevent the adversary from accessing and using critical information, systems, and services.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [AWS Identity and Access Management (IAM) \+ IAM Policies and Policies Boundaries](control-name-descriptions.md#aws-identity-and-access-management-iam-iam-policies-and-policies-boundaries) <br /> (ID: Sec.IAM.2)  |  These controls provide strong, least-privilege and need-to-know security principles for both the users and services that can access your resources.  |
|  [AWS Organizations \+ Service Control Policies (SCPs) \+ AWS Accounts](control-name-descriptions.md#aws-organizations-service-control-policies-scps-aws-accounts) <br /> (ID: Sec.IAM.4)  |  These controls provide strong, least-privilege and need-to-know security principles for both users and services across a multi-account structure. You can control administrators privileges in child accounts.  |
|  [Amazon Simple Storage Service (Amazon S3) Bucket Policies, Object Policies](control-name-descriptions.md#amazon-simple-storage-service-amazon-s3-bucket-policies-object-policies) <br /> (ID: Sec.DP.6)  |  These controls manage access to objects and prevent upload of malicious objects into the S3 bucket.  |
|  [Amazon EC2 – Linux, SELinux – Mandatory Access Control](control-name-descriptions.md#amazon-ec2-linux-selinux-mandatory-access-control) <br /> (ID: Sec.Inf.17)  |  This control is a system policy that cannot be overridden, which mediates access to files, devices, sockets, other processes, and API calls.  |
|  [Amazon EC2 – FreeBSD Trusted BSD – Mandatory Access Control](control-name-descriptions.md#amazon-ec2-freebsd-trusted-bsd-mandatory-access-control) <br /> (ID: Sec.Inf.18)  |  This control is a system policy that cannot be overridden, which mediates access to files, devices, sockets, other processes, and API calls.  |
|  [Amazon EC2 – Linux, FreeBSD – Hardening and Minimization](control-name-descriptions.md#amazon-ec2-linux-freebsd-hardening-and-minimization) <br /> (ID: Sec.Inf.19)  |  These controls disable or remove unused services and packages.  |
|  [Amazon EC2 – Windows – User Account Control (UAC)](control-name-descriptions.md#amazon-ec2-windows-user-account-control-uac) <br /> (ID: Sec.Inf.22)  |  UACs make it more difficult for malware to install and run.  |
|  [Amazon EC2 – Linux – Role-Based Access Control (RBAC) and Discretionary Access Control (DAC)](control-name-descriptions.md#amazon-ec2-linux-role-based-access-control-rbac-and-discretionary-access-control-dac) <br /> (ID: Sec.Inf.23)  |  This control implements least-privilege account profiles.  |
|  [Amazon EC2 – Windows – Device Guard](control-name-descriptions.md#amazon-ec2-windows-device-guard) <br /> (ID: Sec.Inf.26)  |  This control specifies which binaries are authorized to run on your server.  |
|  [AWS Partner Offerings – Anti-Malware Protection](control-name-descriptions.md#aws-partner-offerings-anti-malware-protection) <br /> (ID: Sec.IR.12)  |  These controls help to detect and block malicious payloads.  |
|  [Bottlerocket](control-name-descriptions.md#bottlerocket) <br /> (ID: Sec.Inf.32)  |  This control provides a minimized OS environment capable of running and managing containers, which provides no extraneous listeners or services.  |
|  [AWS Nitro Enclaves](control-name-descriptions.md#aws-nitro-enclaves) <br /> (ID: Sec.DP.5)  |  Provides an isolated execution environment for signed code to handle sensitive data, accessible only by local virtual network socket interface  |

## Control Objective – Disrupt
<a name="control-objective-disrupt-4"></a>

 The objective of the *Disrupt* control in the *Installation* phase is to “break or interrupt the flow of information.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [Amazon Simple Storage Service (Amazon S3) Bucket Policies, Object Policies](control-name-descriptions.md#amazon-simple-storage-service-amazon-s3-bucket-policies-object-policies) <br /> (ID: Sec.DP.6)  |  These controls manage access to objects and prevent upload of malicious objects into the S3 bucket.  |
|  [AWS Systems Manager State Manager](control-name-descriptions.md#aws-systems-manager-state-manager) <br /> (ID: Sec.Inf.14)  |  This control helps you to define and maintain consistent OS configurations.  |
|  [Amazon EC2 – Linux, SELinux – Mandatory Access Control](control-name-descriptions.md#amazon-ec2-linux-selinux-mandatory-access-control) <br /> (ID: Sec.Inf.17)  |  This control is a system policy that cannot be overridden, which mediates access to files, devices, sockets, other processes, and API calls.  |
|  [Amazon EC2 – FreeBSD Trusted BSD – Mandatory Access Control](control-name-descriptions.md#amazon-ec2-freebsd-trusted-bsd-mandatory-access-control) <br /> (ID: Sec.Inf.18)  |  This control is a system policy that cannot be overridden, which mediates access to files, devices, sockets, other processes, and API calls.  |
|  [Amazon EC2 – Windows – User Account Control (UAC)](control-name-descriptions.md#amazon-ec2-windows-user-account-control-uac) <br /> (ID: Sec.Inf.22)  |  UACs make it more difficult for malware to install and run.  |
|  [Amazon EC2 – Linux – Role-Based Access Control (RBAC) and Discretionary Access Control (DAC)](control-name-descriptions.md#amazon-ec2-linux-role-based-access-control-rbac-and-discretionary-access-control-dac) <br /> (ID: Sec.Inf.23)  |  This control implements least-privilege account profiles.  |
|  [Amazon EC2 – Windows – Device Guard](control-name-descriptions.md#amazon-ec2-windows-device-guard) <br /> (ID: Sec.Inf.26)  |  This control specifies which binaries are authorized to run on your server.  |
|  [AWS Partner Offerings – File Integrity Monitoring](control-name-descriptions.md#aws-partner-network-apn-offerings-file-integrity-monitoring) <br /> (ID: Sec.IR.13)  |  This control helps to maintain the integrity of operating system and application files.  |
|  [AWS Partner Offerings – Anti-Malware Protection](control-name-descriptions.md#aws-partner-offerings-anti-malware-protection) <br /> (ID: Sec.IR.12)  |  These controls help to detect and block malicious payloads.  |

## Control Objective – Degrade
<a name="control-objective-degrade-4"></a>

 The objective of the *Degrade* control in the *Installation* phase is to “reduce the effectiveness or efficiency of adversary command and control (C2) or communications systems, and information collection efforts or means.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [Load Balancing](control-name-descriptions.md#load-balancing) <br /> (ID: Sec.Inf.8)  |  With this control, before an attacker can consistently communicate with your resources, all the instances included in the load-balanced service need to be compromised by the attack. If one or more instances has not been compromised, the load balancer switches to an unaffected instance, which degrades the attack.  |
|  [AWS Systems Manager State Manager](control-name-descriptions.md#aws-systems-manager-state-manager) <br /> (ID: Sec.Inf.14)  |  This control helps you to define and maintain consistent OS configurations.  |
|  [Amazon EC2 – Linux, FreeBSD – Hardening and Minimization](control-name-descriptions.md#amazon-ec2-linux-freebsd-hardening-and-minimization) <br /> (ID: Sec.Inf.19)  |  These controls disable or remove unused services and packages.  |
|  [Amazon EC2 – Windows – Device Guard](control-name-descriptions.md#amazon-ec2-windows-device-guard) <br /> (ID: Sec.Inf.26)  |  This control specifies which binaries are authorized to run on your server.  |
|  [AWS Partner Offerings – File Integrity Monitoring](control-name-descriptions.md#aws-partner-network-apn-offerings-file-integrity-monitoring) <br /> (ID: Sec.IR.13)  |  This control helps to maintain the integrity of operating system and application files.  |
|  [Immutable Infrastructure – Short-Lived Environments](control-name-descriptions.md#immutable-infrastructure-short-lived-environments) <br /> (ID: Ops.2)  |  These controls rebuild or refresh your environments periodically to make it more difficult for an attack payload to persist.  |

## Control Objective – Deceive
<a name="control-objective-deceive-4"></a>

 The objective of the *Deceive* control in the *Installation* phase is to “cause a person to believe what is not true. MILDEC [military deception] seeks to mislead adversary decision makers by manipulating their perception of reality.”\*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [Honeypot and Honeynet Environments](control-name-descriptions.md#honeypot-and-honeynet-environments) <br /> (ID: Sec.IR.10)  |  These controls help to degrade, detect, and contain attacks.  |
|  [Honeywords and Honeykeys](control-name-descriptions.md#honeywords-and-honeykeys) <br /> (ID: Sec.IR.11)  |  When an attacker attempts to use stolen, false credentials, these controls help to detect and contain the attack, so you can recover faster.  |

## Control Objective– Contain
<a name="control-objective-contain-4"></a>

 The objective of the *Contain* control in the *Installation* phase is the “action of keeping something harmful under control or within limits.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [AWS Organizations \+ Service Control Policies (SCPs) \+ AWS Accounts](control-name-descriptions.md#aws-organizations-service-control-policies-scps-aws-accounts) <br /> (ID: Sec.IAM.4)  |  These controls provide strong, least-privilege and need-to-know security principles for both users and services across a multi-account structure. You can control administrators privileges in child accounts.  |
|  [Amazon EC2 – Linux, SELinux – Mandatory Access Control](control-name-descriptions.md#amazon-ec2-linux-selinux-mandatory-access-control) <br /> (ID: Sec.Inf.17)  |  This control is a system policy that cannot be overridden, which mediates access to files, devices, sockets, other processes, and API calls.  |
|  [Amazon EC2 – FreeBSD Trusted BSD – Mandatory Access Control](control-name-descriptions.md#amazon-ec2-freebsd-trusted-bsd-mandatory-access-control) <br /> (ID: Sec.Inf.18)  |  This control is a system policy that cannot be overridden, which mediates access to files, devices, sockets, other processes, and API calls.  |
|  [Amazon EC2 – Linux – Role-Based Access Control (RBAC) and Discretionary Access Control (DAC)](control-name-descriptions.md#amazon-ec2-linux-role-based-access-control-rbac-and-discretionary-access-control-dac) <br /> (ID: Sec.Inf.23)  |  This control implements least-privilege account profiles.  |
|  [Linux cgroups, namespaces, SELinux](control-name-descriptions.md#linux-cgroups-namespaces-selinux) <br /> (ID: Sec.Inf.25)  |  These controls enforce capability profiles, which prevent running processes from accessing files, network sockets, and other processes.  |
|  [Third-Party Security Tools for Containers](control-name-descriptions.md#third-party-security-tools-for-containers) <br /> (ID: Sec.IR.14)  |  This control implements advanced security protection and behavioral security solutions for containers.  |
|  [Third-Party Security Tools for AWS Lambda Functions](control-name-descriptions.md#third-party-security-tools-for-aws-lambda-functions) <br /> (ID: Sec.IR.15)  |  This control implements advanced security protection and behavioral security solutions for Lambda functions.  |
|  [AWS Container and Abstract Services](control-name-descriptions.md#aws-container-and-abstract-services) <br /> (ID: Platform.1)  |  These controls can help you prevent access to underlying infrastructure by your customers and threat actors, and segregate your service instances.  |
|  [Hypervisor-Level Guest-to-Guest and Guest-to-Host Separation](control-name-descriptions.md#hypervisor-level-guest-to-guest-and-guest-to-host-separation) <br /> (ID: Platform.4)  |  This control leverages the string isolation capabilities of the AWS hypervisor.  |
|  [AWS Nitro Enclaves](control-name-descriptions.md#aws-nitro-enclaves) <br /> (ID: Sec.DP.5)  |  Provides an isolated execution environment for signed code to handle sensitive data, accessible only by local virtual network socket interface.  |

## Control Objective – Respond
<a name="control-objective-respond-4"></a>

 The objective of the *Respond* control in the *Installation* phase is to provide “Capabilities that help to react quickly to an adversary’s or others’ IO attack or intrusion.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [AWS Systems Manager State Manager](control-name-descriptions.md#aws-systems-manager-state-manager) <br /> (ID: Sec.Inf.14)  |  This control helps you to define and maintain consistent OS configurations.  |
|  [AWS Systems Manager State Manager, or Third-Party or OSS File Integrity Monitoring Solutions on Amazon EC2](control-name-descriptions.md#aws-systems-manager-state-manager-or-third-party-or-oss-file-integrity-monitoring-solutions-on-amazon-ec2) <br /> (ID: Sec.Inf.15)  |  This control automates the process of keeping your Amazon EC2 and hybrid infrastructure in a state that you define.  |
|  [AWS Systems Manager State Manager, AWS Systems Manager Inventory, AWS Config](control-name-descriptions.md#aws-systems-manager-state-manager-aws-systems-manager-inventory-aws-config) <br /> (ID: Sec.Inf.16)  |  When new AWS assets are created, or if malware is installed with a regular package, the AWS Systems Manager Inventory identifies it and sends it to AWS Config for evaluation.  |
|  [AWS Partner Offerings – File Integrity Monitoring](control-name-descriptions.md#aws-partner-network-apn-offerings-file-integrity-monitoring) <br /> (ID: Sec.IR.13)  |  This control helps to maintain the integrity of operating system and application files.  |
| [AWS Security Hub CSPM Automated Response and Remediation ](control-name-descriptions.md#aws-security-hub-automated-response-and-remediation)<br /> (ID: Sec IR.7)  |  AWS [Security Hub CSPM Automated Response and Remediation is an add-on solution](https://aws.amazon.com/solutions/implementations/aws-security-hub-automated-response-and-remediation/) that works with [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) to provide a ready-to-deploy architecture and a library of automated playbooks <br /> Refer AWS Security Blog : [How to deploy the AWS Solution for Security Hub CSPM Automated Response and Remediation](https://aws.amazon.com/blogs/security/how-to-deploy-the-aws-solution-for-security-hub-automated-response-and-remediation/)  |

## Control Objective – Restore
<a name="control-objective-restore-2"></a>

 The objective of the *Restore* control in the *Installation* phase is to “bring information and information systems back to their original state.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [AWS Auto Scaling](control-name-descriptions.md#aws-auto-scaling) <br /> (ID: Sec.Inf.9)  |  This control adjusts capacity to maintain steady, predictable performance.  |
|  [AWS Systems Manager State Manager](control-name-descriptions.md#aws-systems-manager-state-manager) <br /> (ID: Sec.Inf.14)  |  This control helps you to define and maintain consistent OS configurations.  |
|  [AWS Partner Offerings – File Integrity Monitoring](control-name-descriptions.md#aws-partner-network-apn-offerings-file-integrity-monitoring) <br /> (ID: Sec.IR.13)  |  This control helps to maintain the integrity of operating system and application files.  |
|  [CloudFormation \+ Service Catalog](control-name-descriptions.md#cloudformation-service-catalog) <br /> (ID: Ops.1)  |  These controls help you to provision your infrastructure in an automated and secure manner. The CloudFormation template file serves as the single source of truth for your cloud environment.  |
|  [Immutable Infrastructure – Short-Lived Environments](control-name-descriptions.md#immutable-infrastructure-short-lived-environments) <br /> (ID: Ops.2)  |  These controls rebuild or refresh your environments periodically to make it more difficult for an attack payload to persist.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
