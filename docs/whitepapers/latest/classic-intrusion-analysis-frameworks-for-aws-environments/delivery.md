---
source_url: https://docs.aws.amazon.com/whitepapers/latest/classic-intrusion-analysis-frameworks-for-aws-environments/delivery.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Delivery
<a name="delivery"></a>

 During the *Delivery* phase in the intrusion method, attackers transmit their weapon to the intended victim. Some examples of delivery mechanisms include phishing emails, malicious email attachments, and drive-by download sites.

## Control Objective – Detect
<a name="control-objective-detect-2"></a>

 The objective of the *Detect* control in the *Delivery* phase is to “discover or discern the existence, presence, or fact of an intrusion into information systems.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [Amazon GuardDuty](control-name-descriptions.md#amazon-guardduty) <br /> (ID: Sec.Det.1)  |  Detects reconnaissance activity, such as unusual API activity, intra-VPC port scanning, unusual patterns of failed login requests, or unblocked port probing from a known bad IP address.  |
|  [AWS WAF, WAF Managed Rules \+ Automation](control-name-descriptions.md#aws-waf-waf-managed-rules-automation) <br /> (ID: Sec.Inf.2)  |  Malicious sources scan and probe internet-facing web applications for vulnerabilities. They send a series of requests that generate HTTP 4xx error codes. You can use this history to help identify and block malicious source IP addresses.  |
|  [AWS Shield](control-name-descriptions.md#aws-shield) <br /> (ID: Sec.Inf.13)  |  This control defends against most common, frequently occurring network and transport layer DDoS attacks that target your website or applications.  |
|  [Amazon VPC Flow Logs \+ Amazon CloudWatch Alarms](control-name-descriptions.md#amazon-vpc-flow-logs-amazon-cloudwatch-alarms) <br /> (ID: Sec.Det.8)  |  These controls capture and monitor information about the IP traffic going to and from your Amazon VPC.  |
| [Amazon Detective](control-name-descriptions.md#amazon-detective)<br /> (ID: Sec.Det.11)  |  Amazon Detective makes it easy to analyze, investigate, and quickly identify the root cause of potential security issues or suspicious activities. Amazon Detective automatically collects log data from your AWS resources and uses machine learning, statistical analysis, and graph theory to build a linked set of data that enables you to easily conduct faster and more efficient security investigations.  |
|  [AWS IoT Device Defender \+ AWS IoT SiteWise](control-name-descriptions.md#aws-iot-device-defender-aws-iot-sitewise) <br /> (ID: Sec.Det.9)  |  Detects and provides analytics capabilities for anomalous behavior in IoT Things  |
|  [Amazon CloudWatch Logs \+ Amazon Lookout for Metrics](control-name-descriptions.md#amazon-cloudwatch-logs-amazon-lookout-for-metrics) <br /> (ID: Sec.Det.10)  |  Detects and provides analytics capabilities for anomalous behavior in assets and services which send logs to CloudWatch Logs (subject to level of detail of logs being gathered)  |

## Control Objective – Deny
<a name="control-objective-deny-2"></a>

 The objective of the *Deny* control in the *Delivery* phase is to “prevent the adversary from accessing and using critical information, systems, and services.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [Amazon Virtual Private Cloud (VPC)](control-name-descriptions.md#amazon-virtual-private-cloud-amazon-vpc) <br /> (ID: Sec.Inf.3)  |  Amazon VPC can help prevent attackers from scanning network resources during reconnaissance. Amazon VPC Black Hole Routes operate as an allow list or deny list of network reachable assets, before Security Groups or NACLs.  |
|  [Amazon Virtual Private Cloud VPN Gateway \+ AWS Direct Connect](control-name-descriptions.md#amazon-virtual-private-cloud-vpn-gateway-aws-direct-connect) <br /> (ID: Sec.Inf.4)  |  These controls establish private connectivity to multiple Amazon VPCs.  |
|  [Amazon EC2 Security Groups](control-name-descriptions.md#amazon-ec2-security-groups) <br /> (ID: Sec.Inf.5)  |  This control is a virtual firewall that controls inbound and outbound traffic to your network resources and Amazon EC2 instance.  |
|  [Network Access Control Lists](control-name-descriptions.md#network-access-control-lists) <br /> (ID: Sec.Inf.6)  |  This control is a virtual Access Control List that controls inbound and outbound traffic to your network resources and Amazon EC2 instance.  |
|  [AWS Shield](control-name-descriptions.md#aws-shield) <br /> (ID: Sec.Inf.13)  |  This control defends against most common, frequently occurring network and transport layer DDoS attacks that target your website or applications.  |
|  [AWS Identity and Access Management (IAM) \+ IAM Policies and Policies Boundaries](control-name-descriptions.md#aws-identity-and-access-management-iam-iam-policies-and-policies-boundaries) <br /> (ID: Sec.IAM.2)  |  These controls implement strong, least-privilege and need-to-know security principles for both users and services that access your resources.  |
|  [AWS Organizations \+ Service Control Policies (SCPs) \+ AWS Accounts](control-name-descriptions.md#aws-organizations-service-control-policies-scps-aws-accounts) <br /> (ID: Sec.IAM.4)  |  These controls provide strong, least-privilege and need-to-know security principles for both users and services across a multi-account structure. You can control administrators privileges in child accounts.  |
|  [Amazon Simple Storage Service (Amazon S3) Bucket Policies, Object Policies](control-name-descriptions.md#amazon-simple-storage-service-amazon-s3-bucket-policies-object-policies) <br /> (ID: Sec.DP.6)  |  These controls specify access privileges to objects and prevent the upload of that malicious objects into the bucket.  |
|  [Amazon Cognito](control-name-descriptions.md#amazon-cognito) <br /> (ID: Sec.IAM.5)  |  This control provides temporary, limited-privilege AWS credentials to allow access to other AWS services.  |
|  [Amazon EC2: Linux: SELinux – Mandatory Access Control](control-name-descriptions.md#amazon-ec2-linux-selinux-mandatory-access-control) <br /> (ID: Sec.Inf.17)  |  This control is a system policy that cannot be overridden, which mediates access to files, devices, sockets, other processes, and API calls.  |
|  [Amazon EC2 – FreeBSD Trusted BSD – Mandatory Access Control](control-name-descriptions.md#amazon-ec2-freebsd-trusted-bsd-mandatory-access-control) <br /> (ID: Sec.Inf.18)  |  This control is a system policy that cannot be overridden, which mediates access to files, devices, sockets, other processes, and API calls.  |
|  [Amazon EC2 – Linux, FreeBSD – Hardening and Minimization](control-name-descriptions.md#amazon-ec2-linux-freebsd-hardening-and-minimization) <br /> (ID: Sec.Inf.19)  |  These controls disable or remove unused services and packages.  |
|  [Amazon EC2 – Linux – Role-Based Access Control (RBAC) and Discretionary Access Control (DAC)](control-name-descriptions.md#amazon-ec2-linux-role-based-access-control-rbac-and-discretionary-access-control-dac) <br /> (ID: Sec.Inf.23)  |  This control implements least-privilege account profiles.  |
|  [Microsoft Windows Security Baselines](control-name-descriptions.md#microsoft-windows-security-baselines) <br /> (ID: Sec.Inf.24)  |  This control allows you to harden system and user configurations.  |
|  [AWS Physical & Operational Security Policies & Processes](control-name-descriptions.md#aws-physical-operational-security-policies-processes) <br /> (ID: Platform.5)  |  AWS data centers are secure by design and our controls make that possible. We spend countless hours considering potential threats and designing, implementing, and testing controls to ensure the systems, technology, and people we deploy counteract risks.  |
|  [Bottlerocket](control-name-descriptions.md#bottlerocket) <br /> (ID: Sec.Inf.32)  |  This control provides a minimized OS environment capable of running and managing containers, which provides no extraneous listeners or services.  |
|  [AWS Network Firewall](control-name-descriptions.md#aws-network-firewall) <br /> (ID: Sec.Inf.30)  |  Provides deep-packet inspection filtering of VPC network traffic using Suricata-syntax rules  |
|  [AWS Nitro Enclaves](control-name-descriptions.md#aws-nitro-enclaves) <br /> (ID: Sec.DP.5)  |  Provides an isolated execution environment for signed code to handle sensitive data, accessible only by local virtual network socket interface  |
|  [Amazon Simple Email Service (Amazon SES) ](control-name-descriptions.md#amazon-simple-email-service-spam-and-virus-protection)<br /> (ID: Sec.Inf.31)  |  Supports content filtering on inbound and outbound email  |

## Control Objective – Disrupt
<a name="control-objective-disrupt-2"></a>

 The objective of the *Disrupt* control in the *Delivery* phase is to “break or interrupt the flow of information.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [Amazon Virtual Private Cloud (Amazon VPC)](control-name-descriptions.md#amazon-virtual-private-cloud-amazon-vpc) <br /> (ID: Sec.Inf.3)  |  Amazon VPC can help prevent attackers from scanning network resources during reconnaissance. Amazon VPC Black Hole Routes operate as an allow list or deny list of network reachable assets, before Security Groups or NACLs.  |
|  [Amazon EC2 Security Groups](control-name-descriptions.md#amazon-ec2-security-groups) <br /> (ID: Sec.Inf.5)  |  This control is a virtual firewall that controls inbound and outbound traffic to your network resources and Amazon EC2 instance.  |
|  [Network Access Control Lists](control-name-descriptions.md#network-access-control-lists) <br /> (ID: Sec.Inf.6)  |  This control is a virtual Access Control List that controls inbound and outbound traffic to your network resources and Amazon EC2 instance.  |
|  [AWS Shield](control-name-descriptions.md#aws-shield) <br /> (ID: Sec.Inf.13)  |  This control defends against most common, frequently occurring network and transport layer DDoS attacks that target your website or applications.  |
|  [Immutable Infrastructure – Short-Lived Environments](control-name-descriptions.md#immutable-infrastructure-short-lived-environments) <br /> (ID: Ops.2)  |  Rebuilt or refresh your environments periodically to make it more difficult for an attack payload to persist.  |
|  [AWS Network Firewall](control-name-descriptions.md#aws-network-firewall) <br /> (ID: Sec.Inf.30)  |  Provides deep-packet inspection filtering of VPC network traffic using Suricata-syntax rules  |
| [AWS IoT Device Defender \+ AWS IoT SiteWise](control-name-descriptions.md#aws-iot-device-defender-aws-iot-sitewise) <br /> (ID: Sec.Det.9)  |  Detects and provides analytics capabilities and customizable response automation for anomalous behavior in IoT Things  |
| [ Amazon CloudWatch Logs \+ Amazon Lookout for Metrics ](control-name-descriptions.md#amazon-cloudwatch-logs-amazon-lookout-for-metrics)<br /> (ID: Sec.Det.10)  |  Detects and provides analytics capabilities for anomalous behavior in assets and services which send logs to CloudWatch Logs (subject to level of detail of logs being gathered)  |

## Control Objective – Degrade
<a name="control-objective-degrade-2"></a>

 The objective of the *Degrade* control in the *Delivery* phase is to “reduce the effectiveness or efficiency of adversary command and control (C2) or communications systems, and information collection efforts or means.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [Amazon GuardDuty \+ AWS Lambda](control-name-descriptions.md#amazon-guardduty-aws-lambda) <br /> (ID: Sec.IR.1)  |  These controls detect reconnaissance activities and modify security configurations to degrade or block traffic associated with an attack.  |
|  [AWS Shield](control-name-descriptions.md#aws-shield) <br /> (ID: Sec.Inf.13)  |  This control defends against most common, frequently occurring network and transport layer DDoS attacks that target your website or applications.  |
|  [Load Balancing](control-name-descriptions.md#load-balancing) <br /> (ID: Sec.Inf.8)  |  With this control, before an attacker can consistently communicate with your resources, all the instances included in the load-balanced service need to be compromised by the attack. If one or more instances has not been compromised, the load balancer switches to an unaffected instance, which degrades the attack.  |
|  [Immutable Infrastructure - Short-Lived Environments](control-name-descriptions.md#immutable-infrastructure-short-lived-environments) <br /> (ID: Ops.2)  |  Rebuilt or refresh your environments periodically to make it more difficult for an attack payload to persist.  |

## Control Objective – Deceive
<a name="control-objective-deceive-2"></a>

 The objective of the *Deceive* control in the *Delivery* phase is to “cause a person to believe what is not true. MILDEC [military deception] seeks to mislead adversary decision makers by manipulating their perception of reality.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [Honeypot and Honeynet Environments](control-name-descriptions.md#honeypot-and-honeynet-environments) <br /> (ID: Sec.IR.10)  |  These controls help to degrade, detect, and contain attacks.  |
|  [Honeywords and Honeykeys](control-name-descriptions.md#honeywords-and-honeykeys) <br /> (ID: Sec.IR.11)  |  When an attacker attempts to use stolen, false credentials, these controls help to detect and contain the attack, so you can recover faster.  |
|  [AWS WAF \+ AWS Lambda](control-name-descriptions.md#aws-waf-aws-lambda) <br /> (ID: Sec.IR.2)  |  These controls trap endpoints to detect content scrapers and bad bots. When the endpoint is accessed a function adds the source IP address to a blocked list.  |

## Control Objective – Contain
<a name="control-objective-contain-2"></a>

 The objective of the *Contain* control in the *Delivery* phase is the “action of keeping something harmful under control or within limits.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [AWS WAF](control-name-descriptions.md#aws-waf) <br /> (ID: Sec.Inf.1)  |  This control helps to protect your network from common web exploits that could affect application availability, compromise security, or consume excessive resources.  |
|  [Amazon Virtual Private Cloud (Amazon VPC)](control-name-descriptions.md#amazon-virtual-private-cloud-amazon-vpc) <br /> (ID: Sec.Inf.3)  |  Amazon VPC can help prevent attackers from scanning network resources during reconnaissance. Amazon VPC Black Hole Routes operate as an allow list or deny list of network reachable assets, before Security Groups or NACLs.  |
|  [Amazon EC2 Security Groups](control-name-descriptions.md#amazon-ec2-security-groups) <br /> (ID: Sec.Inf.5)  |  This control is a virtual firewall that controls inbound and outbound traffic to your network resources and Amazon EC2 instance.  |
|  [Network Access Control Lists](control-name-descriptions.md#network-access-control-lists) <br /> (ID: Sec.Inf.6)  |  This control is a virtual Access Control List that controls inbound and outbound traffic to your network resources and Amazon EC2 instance.  |
|  [AWS Organizations \+ Service Control Policies (SCPs) \+ AWS Accounts](control-name-descriptions.md#aws-organizations-service-control-policies-scps-aws-accounts) <br /> (ID: Sec.IAM.4)  |  These controls provide strong, least-privilege and need-to-know security principles for both users and services across a multi-account structure. You can control administrators privileges in child accounts.  |
|  [AWS Lambda, Amazon Simple Queue Service (Amazon SQS), AWS Step Functions](control-name-descriptions.md#aws-lambda-amazon-simple-queue-service-amazon-sqs-aws-step-functions) <br /> (ID: Platform.2)  |  These services provide orchestration mechanisms for containment.  |
|  [AWS Nitro Enclaves](control-name-descriptions.md#aws-nitro-enclaves) <br /> (ID: Sec.DP.5)  |  Provides an isolated execution environment for signed code to handle sensitive data, accessible only by local virtual network socket interface  |

## Control Objective – Respond
<a name="control-objective-respond-2"></a>

 The objective of the *Respond* control in the *Delivery* phase is to provide “capabilities that help to react quickly to an adversary’s or others’ IO attack or intrusion.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [AWS Systems Manager State Manager](control-name-descriptions.md#aws-systems-manager-state-manager) <br /> (ID: Sec.Inf.14)  |  This control helps you to define and maintain consistent OS configurations.  |
|  [AWS Partner Offerings – File Integrity Monitoring](control-name-descriptions.md#aws-partner-network-apn-offerings-file-integrity-monitoring) <br /> (ID: Sec.IR.13)  |  These controls help you to maintain the integrity of operating system and application files.  |
|  [AWS WAF \+ AWS Lambda](control-name-descriptions.md#aws-waf-aws-lambda) <br /> (ID: Sec.IR.2)  |  These controls trap endpoints to detect content scrapers and bad bots. When the endpoint is accessed, a function adds the source IP address to a blocked list.  |
|  [Third-Party WAF Integrations](control-name-descriptions.md#third-party-waf-integrations) <br /> (ID: Sec.IR.3)  |  These controls are a complement to AWS WAF.  |
|  [AWS Config Rules](control-name-descriptions.md#aws-config-rules) <br /> (ID: Sec.IR.5)  |  These rules are a configurable set of functions that trigger when an environment configuration change is registered.  |
|  [Amazon CloudWatch Events \+ Lambda](control-name-descriptions.md#amazon-cloudwatch-events-lambda) <br /> (ID: Sec.IR.6)  |  These controls are a configurable set of functions that trigger when an environment configuration change is registered.  |
|  [AWS Managed Services](control-name-descriptions.md#aws-managed-services) <br /> (ID: Ops.3)  |  AWS Managed Services monitors the overall health of your infrastructure resources, and handles the daily activities of investigating and resolving alarms or incidents.  |
| [AWS IoT Device Defender \+ AWS IoT SiteWise](control-name-descriptions.md#aws-iot-device-defender-aws-iot-sitewise) <br /> (ID: Sec.Det.9)  |  Detects and provides analytics capabilities and customizable response automation for anomalous behavior in IoT Things  |
| [ Amazon CloudWatch Logs \+ Amazon Lookout for Metrics \+ Lambda](control-name-descriptions.md#amazon-cloudwatch-logs-amazon-lookout-for-metrics) <br /> (ID: Sec.Det.10)  |  Detects and provides analytics and response capabilities for anomalous behavior in assets and services which send logs to CloudWatch Logs (subject to level of detail of logs being gathered)  |

## Control Objective – Restore
<a name="control-objective-restore"></a>

 The objective of the *Restore* control in the *Delivery* phase is to “bring information and information systems back to their original state.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [AWS Systems Manager State Manager](control-name-descriptions.md#aws-systems-manager-state-manager) <br /> (ID: Sec.Inf.14)  |  This control helps you to define and maintain consistent OS configurations.  |
|  [CloudFormation \+ Service Catalog](control-name-descriptions.md#cloudformation-service-catalog) <br /> (ID: Ops.1)  |  These controls help you to provision your infrastructure in an automated and secure manner. The CloudFormation template file serves as the single source of truth for your cloud environment.  |
|  [Immutable Infrastructure – Short-Lived Environments](control-name-descriptions.md#immutable-infrastructure-short-lived-environments) <br /> (ID: Ops.2)  |  Rebuilt or refresh your environments periodically to make it more difficult for an attack payload to persist.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
