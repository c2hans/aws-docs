---
source_url: https://docs.aws.amazon.com/whitepapers/latest/classic-intrusion-analysis-frameworks-for-aws-environments/sample-mapping-exercise.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Sample mapping exercise
<a name="sample-mapping-exercise"></a>

AWS services and [AWS Partner Network (APN)](https://aws.amazon.com/partners/) services can be mapped to this courses of action *matrix*(Hutchins, Op.Cit., Page. 5). Performing this mapping exercise can help identify which services, features, and functionality can help organizations detect, deny, disrupt, deceive, contain attacks, as well as respond to them and help recover from them when necessary.

 Using the *installation* phase as an example, you can use the following AWS services and third-party services to help you to detect, deny, disrupt, deceive, contain, respond, and recover during this phase of the intrusion.

## Detect
<a name="detect"></a>

 To help detect attacker activity, use log data from [Amazon CloudWatch](https://aws.amazon.com/cloudwatch), [CloudWatch Logs](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html), [AWS CloudTrail](https://aws.amazon.com/cloudtrail), and [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html), and use reporting tools such as [Amazon OpenSearch Service](https://aws.amazon.com/elasticsearch-service/), [Amazon Quick](https://aws.amazon.com/quicksight) and third-party tools. Key examples are provided in the following table.

 **Table 4: Controls for Detect **

|  Control Name  |  Description  |
| --- | --- |
|  Amazon GuardDuty  |  This control detects reconnaissance activity, such as unusual API activity, intra-VPC port scanning, unusual patterns of failed login requests, or unblocked port probing from a known, bad IP address.  |
|  Amazon Detective  |  Amazon Detective makes it easy to analyze, investigate, and quickly identify the root cause of potential security issues or suspicious activities. Amazon Detective automatically collects log data from your AWS resources and uses machine learning, statistical analysis, and graph theory to build a linked set of data that enables you to easily conduct faster and more efficient security investigations.  |
|  Amazon CloudWatch, CloudWatch Logs, CloudTrail \+ Insights, Reporting & Third-Party Tools  |  These controls monitor, detect, visualize, and receive notifications of attacks, and respond to changes in your AWS resources  |
|  AWS Security Hub CSPM  |  This control gives you a comprehensive view of your high priority security alerts and compliance status across AWS accounts.  |
|  AWS Security Hub CSPM Partners  |  AWS Security Hub CSPM APN Partner products are a complement to Amazon GuardDuty.  |
|  AWS Systems Manager State Manager, AWS Systems Manager Inventory, AWS Config  |  When new AWS assets are created, or if malware is installed with a regular package, the AWS System Manager Inventory identifies it and sends it to AWS Config for evaluation.  |
|  Third-Party Security Tools for Containers  |  This control implements advanced security protection and behavioral security solutions for containers.  |
|  Third-Party Security Tools for AWS Lambda Functions  |  This control implements advanced security protection and behavioral security solutions for Lambda functions.  |
|  AWS Partner Network Offerings – Anti-Malware Protection  |  These controls help to detect and block malicious payloads.  |

## Deny
<a name="deny"></a>

 There are numerous process and technology controls that can help prevent an adversary from accessing and using critical information, systems, and services. A DevSecOps culture and processes that enforce CI/CD static and dynamic security analysis, and immutable, short-lived infrastructures all help mitigate attackers’ efforts in the installation phase of an attack. The following table contains numerous other control examples.

 **Table 5: Controls for Deny **

|  Control Names  |  Descriptions  |
| --- | --- |
|  AWS Identity and Access Management (IAM) \+ IAM Policies and Policies Boundaries  |  These controls can be configured to provide strong, least-privilege and need-to know security principles for both the users and services that can access your resources. IAM privileges are required to either grant or deny privileges for AWS administrators and engineers.  |
|  AWS Organizations \+ Service Control Policies (SCPs) \+ AWS Accounts  |  These controls can be utilized to provide strong, least-privilege and need-to know security principles for both users and services across a multi-account structure. SCPs can be used to deny (but not grant) privileges, overriding the potential privileges granted via IAM. You can control the privileges of all principals in child accounts and organizational units.  |
|  Amazon Simple Storage Service (Amazon S3) Bucket Policies, Object Policies  |  These controls manage access to objects and can prevent upload of objects into the Amazon S3 bucket by malicious actors. Note that there are other AWS services, besides S3, that also have resource policies, such as Amazon Simple Queue Service and Amazon Simple Notification Service.  |
|  Amazon Cognito  |  This control provides temporary, limited-privilege end-user credentials to allow access to appropriate AWS services.  |
|  Bottlerocket  |  This control provides a minimized OS environment capable of running and managing containers, which provides no extraneous listeners or services.  |
|  Amazon EC2 – Linux, Security-Enhanced Linux (SELinux) – Mandatory Access Control  |  This control is a system policy that cannot be overridden, which mediates access to files, devices, sockets, other processes, and API calls.  |
|  Amazon EC2 – FreeBSD Trusted BSD – Mandatory Access Control  |  This control is a system policy that cannot be overridden, which mediates access to files, devices, sockets, other processes, and API calls.  |
|  Amazon EC2 – Linux, FreeBSD – Hardening and Minimization  |  These controls disable or remove unused services and packages.  |
|  Amazon EC2 – Windows – User Account Control (UAC)  |  UACs make it more difficult for malware to install and run.  |
|  Amazon EC2 – Linux – Role-Based Access Control (RBAC) and Discretionary Access Control (DAC)  |  This control implements least-privilege account profiles.  |
|  Amazon EC2 – Windows –Device Guard  |  This control specifies which binaries are authorized to run on your server.  |
|  AWS Partner Network Offerings – Anti-Malware Protection  |  These controls help to detect and block malicious payloads.  |

## Disrupt
<a name="disrupt"></a>

 [AWS Config](https://aws.amazon.com/config) and [AWS Systems Manager State Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state.html) can monitor the configuration of cloud services as well as [Amazon EC2](https://aws.amazon.com/ec2) instances, specify a configuration policy for the instances, and automatically apply updates or configuration changes. This approach can help disrupt post-exploitation changes to systems. The following table contains more examples.

 **Table 6: Controls for Disrupt **

|  Control Names  |  Descriptions  |
| --- | --- |
|  Amazon Simple Storage Service (Amazon S3) Bucket Policies, Object Policies  |  These controls manage access to objects and prevent upload of malicious objects into the Amazon S3 bucket.  |
|  AWS Systems Manager State Manager  |  This control helps you to define and maintain consistent OS configurations.  |
|  Amazon EC2 – Linux, SELinux – Mandatory Access Control  |  This control is a system policy that cannot be overridden, which mediates access to files, devices, sockets, other processes, and API calls.  |
|  Amazon EC2 – FreeBSD Trusted BSD – Mandatory Access Control  |  This control is a system policy that cannot be overridden, which mediates access to files, devices, sockets, other processes, and API calls.  |
|  Amazon EC2 – Windows – User Account Control (UAC)  |  UACs make it more difficult for malware to install and run.  |
|  Amazon EC2 – Linux – Role-Based Access Control (RBAC) and Discretionary Access Control (DAC)  |  This control implements least-privilege account profiles.  |
|  Amazon EC2 – Windows – Device Guard  |  This control specifies which binaries are authorized to run on your server.  |
|  AWS Partner Network Offerings – File Integrity Monitoring  |  This control helps to maintain the integrity of operating system and application files.  |
|  AWS Partner Network Offerings – Anti-Malware Protection  |  These controls help to detect and block malicious payloads.  |

## Degrade
<a name="degrade"></a>

 The objective of the Degrade control in the Installation phase is to negatively impact the attacker’s control, communications, and data collection activities. Some examples of controls that help defenders do this are listed in the following table.

 **Table 7: Controls for Degrade **

|  Control Names  |  Descriptions  |
| --- | --- |
|  [AWS Systems Manager State Manager](control-name-descriptions.md#aws-systems-manager-state-manager)  |  This control helps you to define and maintain consistent OS configurations.  |
|  [Immutable Infrastructure – Short-Lived Environments](control-name-descriptions.md#immutable-infrastructure-short-lived-environments)  |  These controls rebuild or refresh your environments periodically to make it more difficult for an attack payload to persist.  |

## Deceive
<a name="deceive"></a>

 Third-party deception technologies present themselves as part of legitimate infrastructure so that when an attacker attempts to compromise it, they help detect, contain, and recover faster. Integrating honeypots, honeynets, fake credentials, and fake documents into a legitimate IT environment enables organizations to detect attempted unauthorized access to resources and respond and recover rapidly. Examples of third-party companies that offer deception technologies include GuardiCore, PacketViper, and others.

 **Table 8: Controls for Deceive **

|  Control Names  |  Descriptions  |
| --- | --- |
|  Honeypot and Honeynet Environments  |  These controls help to degrade, detect, and contain attacks.  |
|  Honeywords and Honeykeys  |  When an attacker attempts to use stolen, false credentials, these controls help to detect and contain the attack, so you can recover faster.  |

## Contain
<a name="contain"></a>

 As previously noted, the segmented nature of typical cloud networks provides far more containment than traditional datacenter-wide layer 2 networks. Service-oriented architectures and microservices are also containment-oriented, as the compromise of one component can have a limited effect on a large application or system. The code running inside these services should be least-privileged in terms of the power to call cloud APIs, and then only with the temporary, fast-rotating STS credentials of an EC2 role, with VPC Endpoint Policies used to make it impossible to use even those short-lived credentials outside the cloud. All of these [best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) make it difficult for a successful compromise of code inside a service to alter critical cloud configuration settings. Beyond that, with [AWS Organizations](https://aws.amazon.com/organizations), you can create service control policies (SCPs) that centrally control AWS service use across multiple AWS accounts. SCPs put bounds around the permissions that [IAM](https://aws.amazon.com/iam) policies can grant to entities in an account, such as users and roles. For example, SCP policies can be used to allow or deny certain activities so that no principals, not even the *super-user* in a child AWS account can bypass them, thus implementing a form of mandatory access control. This can help contain attackers during the Installation phase. The following table provides more examples of controls that can help contain those that seek unauthorized access.

 **Table 9: Controls for Contain **

|  Control Names  |  Descriptions  |
| --- | --- |
|  AWS Organizations \+ Service Control Policies (SCPs) \+ AWS Accounts  |  These controls strong privilege boundaries (AWS accounts) and, the ability to override privileges at the Organization or organizational unit (OU) level. They allow users to implement least-privilege and need-to know security principles for both users and services across a multi-account structure. You can control all privileges in OUs and child accounts.  |
|  Amazon EC2 – Linux, SELinux – Mandatory Access Control  |  This control is a system policy that cannot be overridden, which mediates access to files, devices, sockets, other processes, and API calls.  |
|  Amazon EC2 – FreeBSD Trusted BSD – Mandatory Access Control  |  This control is a system policy that cannot be overridden, which mediates access to files, devices, sockets, other processes, and API calls.  |
|  Amazon EC2 – Linux – Role-Based Access Control (RBAC) and Discretionary Access Control (DAC)  |  This control implements least-privilege account profiles.  |
|  Linux cgroups, namespaces, SELinux  |  These controls enforce capability profiles, which prevent running processes from accessing files, network sockets, and other processes.  |
|  Third-Party Security Tools for Containers  |  This control implements advanced security protection and behavioral security solutions for containers.  |
|  Third-Party Security Tools for AWS Lambda Functions  |  This control implements advanced security protection and behavioral security solutions for Lambda functions.  |
|  AWS Container and Abstract Services  |  These controls can help you prevent access to underlying infrastructure by your customers and threat actors, and segregate your service instances.  |
|  Hypervisor-Level Guest-to Guest and Guest-to-Host Segregation  |  This control leverages the string isolation capabilities of the AWS hypervisor.  |

## Respond
<a name="respond"></a>

 [AWS Config](https://aws.amazon.com/config) monitors the state of an entire swath of cloud services, and can be configured to alert on any unexpected changes. At the instance level, file integrity monitoring (FIM) and enforcement are controls that help maintain the integrity of operating system files and application files by verifying the current file state and a known good baseline of these files. Some of these solutions can help respond during the Installation phase. Additionally, you can use [AWS Lambda](https://aws.amazon.com/lambda) to automatically execute a function in response to an event to mitigate the threat or stop lateral movement. [AWS Systems Manager State Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-state.html) and some [APN Technology Partners](https://aws.amazon.com/partners/technology/) can monitor file integrity.

 **Table 10: Controls for Respond **

|  Control Names  |  Descriptions  |
| --- | --- |
|  AWS Systems Manager State Manager  |  This control helps you to define and maintain consistent OS configurations.  |
|  AWS Systems Manager State Manager, or Third-Party or OSS File Integrity Monitoring Solutions on Amazon EC2  |  This control automates the process of keeping your Amazon EC2 and hybrid infrastructure in a state that you define.  |
|  AWS Systems Manager State Manager, AWS Systems Manager Inventory, AWS Config  |  When new AWS assets are created, or if malware is installed with a regular package, the AWS System Manager Inventory identifies it and sends it to AWS Config for evaluation.  |
|  AWS Partner Network Offerings – File Integrity Monitoring  |  This control helps to maintain the integrity of operating system and application files.  |
|  AWS Lambda  |  A serverless compute service that lets you run code without provisioning or managing servers, creating workload-aware cluster scaling logic, maintaining event integrations, or managing runtimes.  |

## Restore
<a name="restore"></a>

 During the response to an incident, if a tool automatically shuts down a virtual instance of an operating environment, for example, autoscaling can create a new instance automatically from reference images to replace it, thus helping to restore infrastructure automatically and quickly. See the following table for details.

 **Table 11: Controls for Restore **

|  Control Names  |  Descriptions  |
| --- | --- |
|  AWS Auto Scaling  |  This control adjusts capacity to maintain steady, predictable performance.  |
|  AWS Systems Manager State Manager  |  This control helps you to define and maintain consistent OS configurations.  |
|  AWS Partner Network Offerings – File Integrity Monitoring  |  This control helps to maintain the integrity of operating system and application files.  |
|  CloudFormation \+ Service <br /> Catalog  |  These controls help you to provision your infrastructure in an automated and secure manner. The CloudFormation template file serves as the single source of truth for your cloud environment.  |
|  Immutable Infrastructure – <br /> Short-Lived Environments  |  These controls rebuild or refresh your environments periodically to make it more difficult for an attack payload to persist.  |

 In addition to the services and functionality listed previously, many other AWS and third-party services and functionality are available courses of action in the [Installation](what-is-an-intrusion-method.md#phase-6-installation) phase of the intrusion method. For more information, see the [Installation](installation.md) phase section of [Appendix: Reference Material](appendix-reference-material.md).

 Using multiple services and features to detect, deny, disrupt, degrade, deceive, contain, respond, and recover, in each phase of the intrusion method can make it increasingly difficult for attackers to be successful. Attackers are faced with the challenge of defeating layers of defensive cybersecurity capabilities in each phase of their intrusion methods, in order to be successful.
