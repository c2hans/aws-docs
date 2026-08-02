---
source_url: https://docs.aws.amazon.com/whitepapers/latest/classic-intrusion-analysis-frameworks-for-aws-environments/actions-on-objectives.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Actions on Objectives
<a name="actions-on-objectives"></a>

 At in the *Actions* phase of the intrusion, the attackers are now in a position to achieve their objectives. Objectives can include data theft, compromising data integrity, destroying data and infrastructure, disrupting operations, and perpetrating attacks on other victims.

## Control Objective – Detect
<a name="control-objective-detect-6"></a>

 The objective of the *Detec*t control in the *Actions* phase is to “discover or discern the existence, presence, or fact of an intrusion into information systems.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [Amazon GuardDuty](control-name-descriptions.md#amazon-guardduty) <br /> (ID: Sec.Det.1)  |  This control detects reconnaissance activity, such as unusual API activity, intra-VPC port scanning, unusual patterns of failed login requests, or unblocked port probing from a known, bad IP address.  |
|  [Amazon Detective](control-name-descriptions.md#amazon-detective) <br /> (ID: Sec.Det.11)  |  Amazon Detective makes it easy to analyze, investigate, and quickly identify the root cause of potential security issues or suspicious activities. Amazon Detective automatically collects log data from your AWS resources and uses machine learning, statistical analysis, and graph theory to build a linked set of data that enables you to easily conduct faster and more efficient security investigations.  |
|  [Amazon CloudWatch, CloudWatch Logs, CloudTrail \+ Insights, Reporting & Third Parties](control-name-descriptions.md#amazon-cloudwatch-cloudwatch-logs-cloudtrail-insights-reporting-third-parties) <br /> (ID: Sec.Det.6)  |  These controls help you to monitor, detect, visualize, receive notifications, and respond to changes in your AWS resources.  |
|  [AWS Security Hub CSPM](control-name-descriptions.md#aws-security-hub) <br /> (ID: Sec.Det.3)  |  This control gives you a comprehensive view of your high-priority security alerts and compliance status across AWS accounts.  |
|  [AWS Security Hub CSPM Partners](control-name-descriptions.md#aws-security-hub-partners) <br /> (ID: Sec.Det.4)  |  AWS Security Hub CSPM APN Partner products are a complement to Amazon GuardDuty.  |
|  [Outbound Proxy Partners](control-name-descriptions.md#outbound-proxy-partners) <br /> (ID: Sec.Inf.8)  |  Because it is an intermediary for requests, this control can detect malicious traffic before it reaches your network.  |
|  [AWS EC2 Forward Proxy Servers](control-name-descriptions.md#amazon-ec2-forward-proxy-servers) <br /> (ID: Sec.Inf.12)  |  Because it is in intermediary for requests, this control can detect malicious traffic before it reaches your network.  |
|  [Third-Party Security Tools for Containers](control-name-descriptions.md#third-party-security-tools-for-containers) <br /> (ID: Sec.IR.14)  |  This control implements advanced security protection and behavioral security solutions for Containers.  |
|  [Third-Party Security Tools for AWS Lambda Functions](control-name-descriptions.md#third-party-security-tools-for-aws-lambda-functions) <br /> (ID: Sec.IR.15)  |  This control implements advanced security protection and behavioral security solutions for Lambda functions.  |
|  [AWS Partners Offerings – SQL Behavioral Analytics Proxies](control-name-descriptions.md#aws-partners-offerings-sql-behavioral-analytics-proxies) <br /> (ID: Sec.DP.4)  |  These controls detect unauthorized actions on SQL applications.  |

## Control Objective – Deny
<a name="control-objective-deny-6"></a>

 The objective of the *Deny* control in the *Actions* phase is to “prevent the adversary from accessing and using critical information, systems, and services.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [AWS Identity and Access Management (IAM) \+ IAM Policies and Policies Boundaries](control-name-descriptions.md#aws-identity-and-access-management-iam-iam-policies-and-policies-boundaries) <br /> (ID: Sec.IAM.2)  |  These controls provide strong, least-privilege and need-to-know security principles for both the users and services that can access your resources.  |
|  [AWS Organizations \+ Service Control Policies (SCPs) \+ AWS Accounts](control-name-descriptions.md#aws-organizations-service-control-policies-scps-aws-accounts) <br /> (ID: Sec.IAM.4)  |  These controls provide strong, least-privilege and need-to-know security principles for both users and services across a multi-account structure. You can control administrators privileges in child accounts.  |
|  [Amazon Cognito](control-name-descriptions.md#amazon-cognito) <br /> (ID: Sec.IAM.5)  |  This control provides temporary, limited-privilege AWS credentials to allow access to other AWS services.  |
|  [Amazon EC2 – Linux, SELinux – Mandatory Access Control](control-name-descriptions.md#amazon-ec2-linux-selinux-mandatory-access-control) <br /> (ID: Sec.Inf.17)  |  This control is a system policy that cannot be overridden, which mediates access to files, devices, sockets, other processes, and API calls.  |
|  [Amazon EC2 – FreeBSD Trusted BSD – Mandatory Access Control](control-name-descriptions.md#amazon-ec2-freebsd-trusted-bsd-mandatory-access-control) <br /> (ID: Sec.Inf.18)  |  This control is a system policy that cannot be overridden, which mediates access to files, devices, sockets, other processes, and API calls.  |
|  [Amazon EC2 – Linux – Role-Based Access Control (RBAC) and Discretionary Access Control (DAC)](control-name-descriptions.md#amazon-ec2-linux-role-based-access-control-rbac-and-discretionary-access-control-dac) <br /> (ID: Sec.Inf.23)  |  This control implements least-privilege account profiles.  |
|  [Third-Party Security Tools for Containers](control-name-descriptions.md#third-party-security-tools-for-containers) <br /> (ID: Sec.IR.14)  |  This control implements advanced security protection and behavioral security solutions for Containers.  |
|  [Third-Party Security Tools for AWS Lambda Functions](control-name-descriptions.md#third-party-security-tools-for-aws-lambda-functions) <br /> (ID: Sec.IR.15)  |  This control implements advanced security protection and behavioral security solutions for Lambda functions.  |
|  [AWS Key Management Service (AWS KMS) \+ AWS CloudHSM](control-name-descriptions.md#aws-key-management-service-aws-kms-aws-cloudhsm) <br /> (ID: Sec.DP.1)  |  These controls prevent attackers from exfiltrating clear text data that has been encrypted.  |
|  [AWS KMS Key Policies](control-name-descriptions.md#aws-kms-key-policies) <br /> (ID: Sec.DP.2)  |  This control implements strong access control policies for encryption keys.  |

## Control Objective – Disrupt
<a name="control-objective-disrupt-6"></a>

 The objective of the *Disrupt* control in the *Actions* phase is to “break or interrupt the flow of information.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [AWS Identity and Access Management (IAM) \+ IAM Policies and Policies Boundaries](control-name-descriptions.md#aws-identity-and-access-management-iam-iam-policies-and-policies-boundaries) <br /> (ID: Sec.IAM.2)  |  These controls provide strong, least-privilege and need-to-know security principles for both the users and services that can access your resources.  |
|  [Amazon EC2 – Linux, SELinux – Mandatory Access Control](control-name-descriptions.md#amazon-ec2-linux-selinux-mandatory-access-control) <br /> (ID: Sec.Inf.17)  |  This control is a system policy that cannot be overridden, which mediates access to files, devices, sockets, other processes, and API calls.  |
|  [–Amazon EC2 – FreeBSD Trusted BSD – Mandatory Access Control](control-name-descriptions.md#amazon-ec2-freebsd-trusted-bsd-mandatory-access-control) <br /> (ID: Sec.Inf.18)  |  This control is a system policy that cannot be overridden, which mediates access to files, devices, sockets, other processes, and API calls.  |
|  [Amazon EC2 – Linux – Role-Based Access Control (RBAC) and Discretionary Access Control (DAC)](control-name-descriptions.md#amazon-ec2-linux-role-based-access-control-rbac-and-discretionary-access-control-dac) <br /> (ID: Sec.Inf.23)  |  This control implements least-privilege account profiles.  |
|  [Third-Party Security Tools for Containers](control-name-descriptions.md#third-party-security-tools-for-containers) <br /> (ID: Sec.IR.14)  |  This control implements advanced security protection and behavioral security solutions for Containers.  |
|  [Third-Party Security Tools for AWS Lambda Functions](control-name-descriptions.md#third-party-security-tools-for-aws-lambda-functions) <br /> (ID: Sec.IR.15)  |  This control implements advanced security protection and behavioral security solutions for Lambda functions.  |
|  [AWS Config Rules](control-name-descriptions.md#aws-config-rules) <br /> (ID: Sec.IR.5)  |  These rules are a configurable set of functions that trigger when an environment configuration change is registered.  |
|  [–Immutable Infrastructure – Short-Lived Environments](control-name-descriptions.md#immutable-infrastructure-short-lived-environments) <br /> (ID: Ops.2)  |  These controls rebuild or refresh your environments periodically to make it more difficult for an attack payload to persist.  |

## Control Objective – Degrade
<a name="control-objective-degrade-6"></a>

 The objective of the *Degrade* control in the *Actions* phase is to “reduce the effectiveness or efficiency of adversary command and control (C2) or communications systems, and information collection efforts or means.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [AWS Identity and Access Management (IAM) \+ IAM Policies and Policies Boundaries](control-name-descriptions.md#aws-identity-and-access-management-iam-iam-policies-and-policies-boundaries) <br /> (ID: Sec.IAM.2)  |  These controls provide strong, least-privilege and need-to-know security principles for both the users and services that can access your resources.  |
|  [Load Balancing](control-name-descriptions.md#load-balancing) <br /> (ID: Sec.Inf.8)  |  With this control, before an attacker can consistently communicate with your resources, all the instances included in the load-balanced service need to be compromised by the attack. If one or more instances has not been compromised, the load balancer switches to an unaffected instance, which degrades the attack.  |
|  [Amazon EC2 – Linux, SELinux – Mandatory Access Control](control-name-descriptions.md#amazon-ec2-linux-selinux-mandatory-access-control) <br /> (ID: Sec.Inf.17)  |  This control is a system policy that cannot be overridden, which mediates access to files, devices, sockets, other processes, and API calls.  |
|  [Amazon EC2 – FreeBSD Trusted BSD – Mandatory Access Control](control-name-descriptions.md#amazon-ec2-freebsd-trusted-bsd-mandatory-access-control) <br /> (ID: Sec.Inf.18)  |  This control is a system policy that cannot be overridden, which mediates access to files, devices, sockets, other processes, and API calls.  |
|  [Amazon EC2 – Linux – Role-Based Access Control (RBAC) and Discretionary Access Control (DAC)](control-name-descriptions.md#amazon-ec2-linux-role-based-access-control-rbac-and-discretionary-access-control-dac) <br /> (ID: Sec.Inf.23)  |  This control implements least-privilege account profiles.  |
|  [AWS Partners Offerings – SQL Behavioral Analytics Proxies](control-name-descriptions.md#aws-partners-offerings-sql-behavioral-analytics-proxies) <br /> (ID: Sec.DP.4)  |  These controls detect unauthorized actions on SQL applications.  |

## Control Objective – Deceive
<a name="control-objective-deceive-6"></a>

 The objective of the *Deceive* control in the *Actions* phase is to “cause a person to believe what is not true. MILDEC [military deception] seeks to mislead adversary decision makers by manipulating their perception of reality.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [Honeypot and Honeynet Environments](control-name-descriptions.md#honeypot-and-honeynet-environments) <br /> (ID: Sec.IR.10)  |  These controls help to degrade, detect, and contain attacks.  |

## Control Objective – Contain
<a name="control-objective-contain-6"></a>

 The objective of the *Contain* control in the *Actions* phase is “keeping something harmful under control or within limits.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [AWS Identity and Access Management (IAM) \+ IAM Policies and Policies Boundaries](control-name-descriptions.md#aws-identity-and-access-management-iam-iam-policies-and-policies-boundaries) <br /> (ID: Sec.IAM.2)  |  These controls provide strong, least-privilege and need-to-know security principles for both the users and services that can access your resources.  |
|  [AWS Organizations \+ Service Control Policies (SCPs) \+ AWS Accounts](control-name-descriptions.md#aws-organizations-service-control-policies-scps-aws-accounts) <br /> (ID: Sec.IAM.4)  |  These controls provide strong, least-privilege and need-to-know security principles for both users and services across a multi-account structure. You can control administrators privileges in child accounts.  |
|  [Amazon Virtual Private Cloud (VPC)](control-name-descriptions.md#amazon-virtual-private-cloud-amazon-vpc) <br /> (ID: Sec.Inf.3)  |  Amazon VPC can help prevent attackers from scanning network resources during reconnaissance. Amazon VPC Black Hole Routes operate as an allow list or deny list of network reachable assets, before Security Groups or NACLs.  |
|  [Amazon EC2 Security Groups](control-name-descriptions.md#amazon-ec2-security-groups) <br /> (ID: Sec.Inf.5)  |  This control is a virtual firewall that controls inbound and outbound traffic to your network resources and Amazon EC2 instance.  |
|  [Network Access Control Lists](control-name-descriptions.md#network-access-control-lists) <br /> (ID: Sec.Inf.6)  |  This control is a virtual Access Control List that controls inbound and outbound traffic to your network resources and Amazon EC2 instance.  |
|  [Linux cgroups, namespaces, SELinux](control-name-descriptions.md#linux-cgroups-namespaces-selinux) <br /> (ID: Sec.Inf.25)  |  These controls enforce capability profiles, which prevent running processes from accessing files, network sockets, and other processes.  |
|  [AWS Container and Abstract Services](control-name-descriptions.md#aws-container-and-abstract-services) <br /> (ID: Platform.1)  |  These controls can help you prevent access to underlying infrastructure by your customers and threat actors, and segregate your service instances.  |
|  [Hypervisor-Level Guest-to-Guest and Guest-to-Host Separation](control-name-descriptions.md#hypervisor-level-guest-to-guest-and-guest-to-host-separation) <br /> (ID: Platform.4)  |  This control leverages the string isolation capabilities of the AWS hypervisor.  |

## Control Objective – Respond
<a name="control-objective-respond-6"></a>

 The objective of the *Respond* control in the *Actions* phase is to provide “Capabilities that help to react quickly to an adversary’s or others’ IO attack or intrusion.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [Third-Party Security Tools for Containers](control-name-descriptions.md#third-party-security-tools-for-containers) <br /> (ID: Sec.IR.14)  |  This control implements advanced security protection and behavioral security solutions for Containers.  |
|  [Third-Party Security Tools for AWS Lambda Functions](control-name-descriptions.md#third-party-security-tools-for-aws-lambda-functions) <br /> (ID: Sec.IR.15)  |  This control implements advanced security protection and behavioral security solutions for Lambda functions.  |
|  [AWS Partner Offerings – Behavioral Monitoring, Response Tools and Services](control-name-descriptions.md#aws-partner-offerings-behavioral-monitoring-response-tools-and-services) <br /> (ID: Sec.Inf.29)  |  These controls provide insight into the threats in your environment.  |
|  [Amazon GuardDuty \+ AWS Lambda](control-name-descriptions.md#amazon-guardduty-aws-lambda) <br /> (ID: Sec.IR.1)  |  These controls detect reconnaissance activities and modify security configurations to block traffic associated with an attack.  |
|  [AWS Managed Services](control-name-descriptions.md#aws-managed-services) <br /> (ID: Ops.3)  |  AWS Managed Services monitors the overall health of your infrastructure resources, and handles the daily activities of investigating and resolving alarms or incidents.  |
|  AWS Security Hub CSPM Automated Response and Remediation <br /> (ID: Sec IR.7)  |  AWS [Security Hub CSPM Automated Response and Remediation is an add-on solution](https://aws.amazon.com/solutions/implementations/aws-security-hub-automated-response-and-remediation/) that works with [AWS Security Hub CSPM](https://aws.amazon.com/security-hub/) to provide a ready-to-deploy architecture and a library of automated playbooks <br /> Refer to the AWS Security Blog : [How to deploy the AWS Solution for Security Hub CSPM Automated Response and Remediation](https://aws.amazon.com/blogs/security/how-to-deploy-the-aws-solution-for-security-hub-automated-response-and-remediation/)  |

## Control Objective – Restore
<a name="control-objective-restore-4"></a>

 The objective of the *Restore* control in the *Actions* phase is to “bring information and information systems back to their original state.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [AWS Auto Scaling](control-name-descriptions.md#aws-auto-scaling) <br /> (ID: Sec.Inf.9)  |  This control adjusts capacity to maintain steady, predictable performance.  |
|  [AWS Partner Offerings – File Integrity Monitoring](control-name-descriptions.md#aws-partner-network-apn-offerings-file-integrity-monitoring) <br /> (ID: Sec.IR.13)  |  This control helps to maintain the integrity of operating system and application files.  |
|  [CloudFormation \+ Service Catalog](control-name-descriptions.md#cloudformation-service-catalog) <br /> (ID: Ops.1)  |  These controls help you to provision your infrastructure in an automated and secure manner. The CloudFormation template file serves as the single source of truth for your cloud environment.  |
|  [AWS DR Options](control-name-descriptions.md#aws-dr-options) <br /> (ID: Ops.4)  |  These controls can help you rapidly recover your IT infrastructure and data.  |
