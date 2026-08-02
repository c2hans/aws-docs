---
source_url: https://docs.aws.amazon.com/whitepapers/latest/classic-intrusion-analysis-frameworks-for-aws-environments/prioritizing-control-implementations.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Prioritizing Control Implementations
<a name="prioritizing-control-implementations"></a>

 Organizations often want to know where to start if they want to implement a classic intrusion analysis framework. This section describes two ways that you can use the control number associated with each control listed in the [Appendix: Reference Material](appendix-reference-material.md) section to prioritize control implementations. Control numbers can be aligned with the [AWS Cloud Adoption Framework](https://aws.amazon.com/professional-services/CAF/) (AWS CAF) or can be used to prioritize implementations based on control coverage. Each of these approaches are discussed.

 Each unique control included in the [*Appendix: Reference Material*](appendix-reference-material.md) section has a unique control number assigned to it. For example, the following example table, the control number is *Sec.IAM.2*.

 **Control number example**

|  Control Names  |  Descriptions  |
| --- | --- |
|  [AWS Identity and Access Management (IAM) \+ IAM Policies and Policies Boundaries](control-name-descriptions.md#aws-identity-and-access-management-iam-iam-policies-and-policies-boundaries) <br /> (ID: Sec.IAM.2)  |  These controls provide strong, least-privilege and need-to-know security principles for both the users and services that can access your resources.  |

 The same control number appears in each place in the intrusion method analysis framework that the associated control is used. For example, each appearance of the *Amazon Simple Storage Service (Amazon S3) Bucket Policies, Object Policies* control in the method analysis framework includes the Sec.DP.6 control number. The control numbers are based on the AWS CAF. The guidance and current recommendations provided by the AWS CAF help you build a comprehensive approach to cloud computing across your organization, and throughout your IT lifecycle. Using the AWS CAF helps you realize measurable business benefits from cloud adoption faster and with less risk.

 The AWS CAF organizes guidance into six areas of focus, known as *perspectives*. Each perspective covers distinct responsibilities owned or managed by functionally related stakeholders. In general, the Business, People, and Governance Perspectives focus on business capabilities, while the Platform, Security, and Operations Perspectives focus on technical capabilities.

![This image shows the AWS CAF perspectives](http://docs.aws.amazon.com/whitepapers/latest/classic-intrusion-analysis-frameworks-for-aws-environments/images/aws-caf-perspectives.png)

 **AWS CAF perspectives**

 For a full explanation of the AWS CAF, see [AWS Cloud Adoption Framework](https://aws.amazon.com/professional-services/CAF/).

 Numerous controls listed in *this paper* are from the AWS CAF Security perspective. To help you with your implementation, you can use the AWS CAF Security Epics. The Security Epics consist of groups of user stories (use cases and abuse cases) that you can work on during sprints. Each of these epics has multiple iterations that address increasingly complex requirements and layering in robustness. Although we advise the use of Agile methodologies, the epics can also be treated as general work streams or topics that help in prioritizing and structuring delivery using any other framework. Some CAF perspectives, such as the Operations and Platform perspectives, do not have epics.

![This image shows the AWS CAF security epics.](http://docs.aws.amazon.com/whitepapers/latest/classic-intrusion-analysis-frameworks-for-aws-environments/images/aws-caf-security-epics.png)

 **AWS CAF Security Epics**

## Control Number Format
<a name="control-number-format"></a>

 The format of the control numbers is:

 <*CAF perspective*>.<*CAF perspective epic*>.<*sequential\_number>*

 The *CAF perspective epic* only applies to AWS CAF perspectives that have epics, such as the Security perspective.

 Some examples of control numbers:
+  Sec.IAM.1 – CAF Security Perspective, Identity & Access Management Epic, control 1
+  Sec.Det.1 – CAF Security Perspective, Detective Security Epic, control 1
+  Sec.DP.3 – CAF Security Perspective, Data Protection Epic, control 3
+  Sec.Inf.11 – CAF Security Perspective, Infrastructure Security Epic, control 11
+  Sec.IR.5 – CAF Security Perspective, Incident Response Epic, control 5
+  Platform.1 – CAF Platform Perspective, control 1
+  Ops.2 – CAF Operations Perspective, control 2

## Prioritize Controls with the Control Number and AWS CAF
<a name="prioritize-controls-with-the-control-number-and-aws-caf"></a>

 Organizations that use AWS CAF to build a comprehensive approach to cloud computing across their organization and have also decided to implement some or all of the controls described in this paper, can use the tables in this section to cross-reference their efforts. This table makes it easy to identify which intrusion method controls can be implemented as organizations perform sprints associated with AWS CAF perspectives and epics.

 For example, when an organization plans to work on the *Detective Controls Epic*, the table shows them that when they implement the controls listed under that epic, they will also be enabling other capabilities as part of their intrusion analysis strategy.

 This approach can help organizations prioritize which intrusion method controls to implement as part of a broader AWS CAF strategy.

 **Table 12 – Controls Mapped to AWS Cloud Adoption Framework (AWS CAF) **

<table>
<thead>
  <tr><th> Control ID </th><th> Control Name </th></tr>
</thead>
<tbody>
  <tr><td colspan="2"> Security Perspective – Identity and Access Management (IAM) Epic </td></tr>
  <tr><td> Sec.IAM.1 </td><td> AWS Identity and Access Management (IAM) Roles  </td></tr>
  <tr><td> Sec.IAM.2 </td><td> AWS Identity and Access Management (IAM) \+ IAM Policies and Policy Boundaries </td></tr>
  <tr><td> Sec.IAM.3 </td><td> AWS Identity and Access Management (IAM) \+ AWS Organizations </td></tr>
  <tr><td> Sec.IAM.4 </td><td> AWS Organizations \+ Service Control Policies (SCPs) \+ AWS Accounts </td></tr>
  <tr><td> Sec.IAM.5 </td><td> Amazon Cognito </td></tr>
  <tr><td> </td><td> </td></tr>
  <tr><td colspan="2"> Security Perspective – Detective Controls Epic </td></tr>
  <tr><td> Sec.Det.1 </td><td> Amazon GuardDuty </td></tr>
  <tr><td> Sec.Det.2 </td><td> Amazon GuardDuty Partners </td></tr>
  <tr><td> Sec.Det.3 </td><td> AWS Security Hub CSPM </td></tr>
  <tr><td> Sec.Det.4 </td><td> AWS Security Hub CSPM Partners </td></tr>
  <tr><td> Sec.Det.5 </td><td> AWS Config </td></tr>
  <tr><td> Sec.Det.6 </td><td> Amazon CloudWatch, CloudWatch Logs, CloudTrail \+ Insights, Reporting & Third Parties </td></tr>
  <tr><td> Sec.Det.7 </td><td> Amazon CloudWatch Events & Alarms \+ Amazon SNS \+ SIEM Solutions </td></tr>
  <tr><td> Sec.Det.8 </td><td> Amazon VPC Flow Logs \+ CloudWatch Alarms or other analytics tools  </td></tr>
  <tr><td> Sec.Det.9 </td><td> AWS IoT Device Defender \+ AWS IoT SiteWise </td></tr>
  <tr><td> Sec.Det.10 </td><td> Amazon CloudWatch Logs \+ Amazon Lookout for Metrics </td></tr>
  <tr><td> Sec.Det.11 </td><td> Amazon Detective </td></tr>
  <tr><td colspan="2"> Security Perspective – Infrastructure Security Epic </td></tr>
  <tr><td> Sec.Inf.1 </td><td> AWS WAF </td></tr>
  <tr><td> Sec.Inf.2 </td><td> AWS WAF, WAF Managed Rules \+ Automation </td></tr>
  <tr><td> Sec.Inf.3 </td><td> Amazon Virtual Private Cloud (Amazon VPC) </td></tr>
  <tr><td> Sec.Inf.4 </td><td> AWS Direct Connect </td></tr>
  <tr><td> Sec.Inf.5 </td><td> Amazon EC2 Security Groups </td></tr>
  <tr><td> Sec.Inf.6 </td><td> Network Access Control Lists (NACLs) </td></tr>
  <tr><td> Sec.Inf.7 </td><td> Outbound Proxy Partners </td></tr>
  <tr><td> Sec.Inf.8 </td><td> Load Balancing </td></tr>
  <tr><td> Sec.Inf.9 </td><td> AWS Auto Scaling </td></tr>
  <tr><td> Sec.Inf.10 </td><td> Network infrastructure solutions in the AWS Marketplace </td></tr>
  <tr><td> Sec.Inf.11 </td><td> Reverse Proxy architecture </td></tr>
  <tr><td> Sec.Inf.12 </td><td> Amazon EC2 Forward Proxy Servers </td></tr>
  <tr><td> Sec.Inf.13 </td><td> AWS Shield </td></tr>
  <tr><td> Sec.Inf.14 </td><td> AWS Systems Manager State Manager  </td></tr>
  <tr><td> Sec.Inf.15 </td><td> AWS Systems Manager State Manager, or Third-Party or OSS File Integrity Monitoring Solutions on Amazon EC2 </td></tr>
  <tr><td> Sec.Inf.16 </td><td> AWS Systems Manager State Manager, AWS Systems Manager Inventory, AWS Config </td></tr>
  <tr><td> Sec.Inf.17 </td><td> Amazon EC2 – Linux, SELinux – Mandatory Access Control </td></tr>
  <tr><td> Sec.Inf.18 </td><td> Amazon EC2 – FreeBSD Trusted BSD – Mandatory Access Control </td></tr>
  <tr><td> Sec.Inf.19 </td><td> Amazon EC2 – Linux, FreeBSD – Hardening and Minimization </td></tr>
  <tr><td> Sec.Inf.20 </td><td> Amazon EC2 – Linux, Windows, FreeBSD – Address Space Layout Randomization (ASLR) </td></tr>
  <tr><td> Sec.Inf.21 </td><td> Amazon EC2 – Linux, Windows, FreeBSD – Data Execution Prevention (DEP) </td></tr>
  <tr><td> Sec.Inf.22 </td><td> Amazon EC2 – Windows – User Account Control (UAC) </td></tr>
  <tr><td> Sec.Inf.23 </td><td> Amazon EC2 – Linux – Role-Based Access Control (RBAC) and Discretionary Access Control (DAC) </td></tr>
  <tr><td> Sec.Inf.24 </td><td> Microsoft Windows Security Baselines </td></tr>
  <tr><td> Sec.Inf.25 </td><td> Linux cgroups, namespaces, SELinux  </td></tr>
  <tr><td> Sec.Inf.26 </td><td> Amazon EC2 – Windows – Device Guard </td></tr>
  <tr><td> Sec.Inf.27 </td><td> AWS Lambda Partners </td></tr>
  <tr><td> Sec.Inf.28 </td><td> Container Partners – Security </td></tr>
  <tr><td> Sec.Inf.29 </td><td> AWS Partner Offerings – Behavioral Monitoring, Response Tools and Services  </td></tr>
  <tr><td> Sec.Inf.30 </td><td> AWS Network Firewall </td></tr>
  <tr><td> Sec.Inf.31 </td><td> Amazon Simple Email Service (Amazon SES) </td></tr>
  <tr><td> Sec.Inf.32 </td><td> Bottlerocket </td></tr>
  <tr><td colspan="2"> Security Perspective - Data Protection Epic </td></tr>
  <tr><td> Sec.DP.1 </td><td> AWS Key Management Service (KMS) \+ AWS CloudHSM </td></tr>
  <tr><td> Sec.DP.2 </td><td> AWS KMS Key Policies </td></tr>
  <tr><td> Sec.DP.3 </td><td> AWS Certificate Manager \+ Transport Layer Security (TLS) </td></tr>
  <tr><td> Sec.DP.4 </td><td> AWS Partner Offerings – SQL Behavioral Analytics Proxies </td></tr>
  <tr><td> Sec.DP.5 </td><td> AWS Nitro Enclaves </td></tr>
  <tr><td> Sec.DP.6 </td><td> Amazon Simple Storage Service (Amazon S3) Bucket Policies, Object Policies </td></tr>
  <tr><td> Sec.DP.7 </td><td> AWS Secrets Manager </td></tr>
  <tr><td colspan="2"> Security Perspective - Incident Response Epic </td></tr>
  <tr><td> Sec.IR.1 </td><td> Amazon GuardDuty \+ AWS Lambda </td></tr>
  <tr><td> Sec.IR.2 </td><td> AWS WAF \+ AWS Lambda </td></tr>
  <tr><td> Sec.IR.3 </td><td> Third-Party WAF Integrations  </td></tr>
  <tr><td> Sec.IR.4 </td><td> Amazon GuardDuty \+ AWS Lambda \+ AWS WAF, Security Groups, NACLs </td></tr>
  <tr><td> Sec.IR.5 </td><td> AWS Config Rules  </td></tr>
  <tr><td> Sec.IR.6 </td><td> Amazon CloudWatch Events \+ Lambda  </td></tr>
  <tr><td> Sec.IR.7 </td><td> AWS Security Hub CSPM Automated Response and Remediation </td></tr>
  <tr><td> Sec.IR.8 </td><td> Amazon CloudWatch Logs \+ Amazon Lookout for Metrics \+ Lambda </td></tr>
  <tr><td> Sec.IR.9 </td><td> Amazon Virtual Private Cloud (Amazon VPC) \+ automation </td></tr>
  <tr><td> Sec.IR.10 </td><td> Honeypot and Honeynet Environments </td></tr>
  <tr><td> Sec.IR.11 </td><td> Honeywords and Honeykeys </td></tr>
  <tr><td> Sec.IR.12 </td><td> AWS Partner Offerings – Anti-Malware Protection </td></tr>
  <tr><td> Sec.IR.13 </td><td> AWS Partner Offerings – File Integrity Monitoring  </td></tr>
  <tr><td> Sec.IR.14 </td><td> Third-Party Security Tools for Containers </td></tr>
  <tr><td> Sec.IR.15 </td><td> Third-Party Security Tools for AWS Lambda Functions </td></tr>
  <tr><td colspan="2"> Platform Perspective </td></tr>
  <tr><td> Platform.1 </td><td> AWS Container and Abstract Services  </td></tr>
  <tr><td> Platform.2 </td><td> AWS Lambda, Amazon Simple Queue Service (Amazon SQS), AWS Step Functions  </td></tr>
  <tr><td> Platform.3 </td><td> Amazon Simple Email Service </td></tr>
  <tr><td> Platform.4 </td><td> Hypervisor-Level Guest-to-Guest and Guest-to-Host Separation  </td></tr>
  <tr><td> Platform.5 </td><td> AWS physical and operational security policies and processes </td></tr>
  <tr><td colspan="2"> Operations Perspective </td></tr>
  <tr><td> Ops.1 </td><td> CloudFormation \+ Service Catalog </td></tr>
  <tr><td> Ops.2 </td><td> Immutable Infrastructure – Short-Lived Environments </td></tr>
  <tr><td> Ops.3 </td><td> AWS Managed Services  </td></tr>
  <tr><td> Ops.4 </td><td> AWS DR Solutions </td></tr>
</tbody>
</table>

## Prioritize Controls Based on Control Coverage
<a name="prioritize-controls-based-on-control-coverage"></a>

 Another way to leverage the unique control numbers, is to identify which controls provide the greatest level of coverage, and potentially provided the biggest ROI.

 For example, the following table shows that by implementing control *Sec.IR.15*, (Third-Party Security Tools for AWS Lambda Functions), it can potentially help detect, deny, disrupt, contain, and respond in the Exploitation phase of an attack. This mapping helps identify the benefits of enabling that one control, which provides significant Infrastructure Security capability coverage in multiple places in the intrusion method analysis framework.

 **Table 13 – Example of an AWS Cloud Adoption Framework (AWS CAF) security control appearing multiple times in a Courses of Action Matrix**

![This image shows an example of AWS CAF appearing multiple times in a courses of action matrix.](http://docs.aws.amazon.com/whitepapers/latest/classic-intrusion-analysis-frameworks-for-aws-environments/images/aws-caf-in-courses-of-action-matrix.png)

 The following table shows each place in the *courses of action matrix* that each control number appears. You can use the control number for each control to help you prioritize your control implementations. For example, notice that control *Sec.Det.1* (Amazon GuardDuty) can provide Detection capabilities in all phases of the intrusion method analysis framework (except Exploit Development).

 **Table 14 – Controls Mapped to the Intrusion Method **

|   |  Detect  |  Deny  |  Disrupt  |  Degrade  |  Deceive  |  Contain  |  Respond  |  Restore  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  Recon – Pre-Intrusion  |  Sec.Det.1 <br /> Sec.Det.2 <br /> Sec.Inf.2 <br /> Sec.Det.6 <br /> Sec.Det.3 <br /> Sec.Det.4 <br /> Sec.Inf.30 <br /> Sec.Det.11 <br /> Sec.IR.10  |  Sec.Inf.3 <br /> Sec.IAM.3 <br /> Sec.DP.3 <br /> Sec.Inf.10 <br /> Sec.Inf.2 <br /> Sec.Inf.4 <br /> Sec.Inf.30  |  Sec.IR.1 <br /> Sec.Inf.30  |  Sec.IR.10 <br /> Sec.IR.11  |  Sec.IR.10 <br /> Sec.IR.11 <br /> Sec.IR.2  |  Sec.IR.10 <br /> Sec.IR.11  |  Sec.Inf.2 <br /> Sec.IR.1 <br /> Sec.Det.2 <br /> Sec.Det.4 <br /> Sec.Det.7  |  —  |
|  Recon – Post-Intrusion  |  Sec.Det.1 <br /> Sec.Det.2 <br /> Sec.Det.6 <br /> Sec.Det.3 <br /> Sec.Det.4 <br /> Sec.Inf.30 <br /> Sec.Det.11 <br /> Sec.IR.10 <br /> Sec.IR.11  |  Sec.Inf.3 <br /> Sec.IAM.3 <br /> Sec.DP.3 <br /> Sec.Inf.11 <br /> Sec.Inf.11 <br /> Sec.IAM.5 <br /> Sec.Inf.30 <br /> Sec.Inf.32  |  Sec.IR.1 <br /> Sec.Inf.30  |  Sec.IR.10 <br /> Sec.IR.11  |  Sec.IR.10 <br /> Sec.IR.11 <br /> Sec.IR.9  |  Sec.IR.10 <br /> Sec.IR.11 <br /> Sec.IR.9  |  Sec.Inf.2 <br /> Sec.IR.1 <br /> Sec.Det.2 <br /> Sec.Det.4 <br /> Sec.Det.7  |  —  |
|  Exploit Development  |  —  |  —  |  —  |  —  |  —  |  —  |  —  |  —  |
|  Delivery  |  Sec.Det.1 <br /> Sec.Inf.2 <br /> Sec.Inf.13 <br /> Sec.Det.8 <br /> Sec.Det.9 <br /> Sec.Det.10 <br /> Sec.Det.11  |  Sec.Inf.3 <br /> Sec.Inf.4 <br /> Sec.Inf.5 <br /> Sec.Inf.6 <br /> Sec.Inf.13 <br /> Sec.IAM.2 <br /> Sec.IAM.4 <br /> Sec.IAM.5 <br /> Sec.Inf.17 <br /> Sec.Inf.18 <br /> Sec.Inf.19 <br /> Sec.Inf.23 <br /> Sec.Inf.24 <br /> Platform.5 <br /> Sec.Inf.30 <br /> Sec.Inf.31 <br /> Sec.Inf.32 <br /> Sec.DP.5 <br /> Sec.DP.6  |  Sec.Inf.3 <br /> Sec.Inf.5 <br /> Sec.Inf.6 <br /> Sec.Inf.13 <br /> Ops.2 <br /> Sec.Inf.30 <br /> Sec.Det.9 <br /> Sec.Det.10  |  Sec.IR.1 <br /> Sec.Inf.13 <br /> Sec.Inf.8 <br /> Ops.2  |  Sec.IR.10 <br /> Sec.IR.11 <br /> Sec.IR.2  |  Sec.Inf.1 <br /> Sec.Inf.3 <br /> Sec.Inf.5 <br /> Sec.Inf.6 <br /> Sec.IAM.4 <br /> Sec.Inf.25 <br /> Platform.1 <br /> Platform.2 <br /> Platform.4 <br /> Sec.DP.5  |  Sec.Inf.14 <br /> Sec.IR.13 <br /> Sec.IR.2 <br /> Sec.IR.3 <br /> Sec.IR.5 <br /> Sec.IR.6 <br /> Sec.IR.7 <br /> Ops.3 <br /> Sec.Det.9 <br /> Sec.Det.10  |  Sec.Inf.14 <br /> Ops.1 <br /> Ops.2  |
|  Exploitation  |  Sec.Det.1 <br /> Sec.Det.9 <br /> Sec.Det.10 <br /> Sec.Det.11 <br /> Sec.Inf.2 <br /> Sec.Inf.3 <br /> Sec.Det.5 <br /> Sec.IR.14 <br /> Sec.IR.15 <br /> Sec.IR.12 <br /> Sec.Inf.27 <br /> Sec.Inf.28  |  Sec.IAM.1 <br /> Sec.DP.7 <br /> Sec.Inf.17 <br /> Sec.Inf.18 <br /> Sec.Inf.19 <br /> Sec.Inf.20 <br /> Sec.Inf.21 <br /> Sec.Inf.22 <br /> Sec.Inf.23 <br /> Sec.Inf.24 <br /> Sec.IR.14 <br /> Sec.IR.15 <br /> Sec.IR.12 <br /> Sec.Inf.27 <br /> Sec.Inf.28 <br /> Sec.Inf.32 <br /> Platform.3 <br /> Sec.DP.1 <br /> Sec.DP.5 <br /> Sec.DP.6  |  Sec.Inf.2 <br /> Sec.DP.7 <br /> Sec.Inf.17 <br /> Sec.Inf.18 <br /> Sec.Inf.20 <br /> Sec.Inf.21 <br /> Sec.Inf.22 <br /> Sec.Inf.23 <br /> Sec.IR.14 <br /> Sec.IR.15 <br /> Sec.IR.12 <br /> Sec.Inf.30 <br /> Ops.2 <br /> Sec.DP.5 <br /> Sec.DP.6  |  Sec.IR.1 <br /> Sec.Inf.1 <br /> Sec.Inf.9 <br /> Sec.Inf.30 <br /> Ops.2  |  Sec.IR.10 <br /> Sec.IR.11 <br /> Sec.IR.2  |  Sec.IAM.1 <br /> Sec.IAM.4 <br /> Sec.Inf.17 <br /> Sec.Inf.18 <br /> Sec.Inf.19 <br /> Sec.Inf.23 <br /> Sec.Inf.25 <br /> Sec.IR.14 <br /> Sec.IR.15 <br /> Platform.1 <br /> Platform.4 <br /> Sec.DP.5  |  Sec.Det.2 <br /> Sec.Det.11 <br /> Sec.IR.14 <br /> Sec.IR.15 <br /> Sec.Inf.29 <br /> Ops.3 <br /> Sec.IR.7  |  Sec.Inf.9 <br /> Sec.Inf.14 <br /> Sec.IR.13 <br /> Ops.1 <br /> Ops.2  |
|  Installation  |  Sec.Det.1 <br /> Sec.Det.6 <br /> Sec.Det.3 <br /> Sec.Det.4 <br /> Sec.Det.9 <br /> Sec.Det.10 <br /> Sec.Det.11 <br /> Sec.Inf.16 <br /> Sec.IR.14 <br /> Sec.IR.15 <br /> Sec.IR.12  |  Sec.IAM.2 <br /> Sec.IAM.4 <br /> Sec.IAM.5 <br /> Sec.Inf.17 <br /> Sec.Inf.18 <br /> Sec.Inf.22 <br /> Sec.Inf.23 <br /> Sec.Inf.26 <br /> Sec.Inf.32 <br /> Sec.IR.12 <br /> Sec.DP.5 <br /> Sec.DP.6  |  Sec.Inf.14 <br /> Sec.Inf.17 <br /> Sec.Inf.18 <br /> Sec.Inf.22 <br /> Sec.Inf.23 <br /> Sec.Inf.26 <br /> Sec.IR.13 <br /> Sec.IR.12 <br /> Sec.DP.6  |  Sec.Inf.8 <br /> Sec.Inf.14 <br /> Sec.Inf.19 <br /> Sec.Inf.26 <br /> Sec.IR.13 <br /> Ops.2  |  Sec.IR.10 <br /> Sec.IR.11  |  Sec.IAM.4 <br /> Sec.Inf.17 <br /> Sec.Inf.18 <br /> Sec.Inf.23 <br /> Sec.Inf.25 <br /> Sec.IR.14 <br /> Sec.IR.15 <br /> Platform.1 <br /> Platform.4 <br /> Sec.DP.5  |  Sec.Inf.14 <br /> Sec.Inf.15 <br /> Sec.Inf.16 <br /> Sec.IR.13 <br /> Sec IR.7  |  Sec.Inf.10 <br /> Sec.Inf.14 <br /> Sec.IR.13 <br /> Ops.1 <br /> Ops.2  |
|  Command and Control  |  Sec.Det.1 <br /> Sec.Det.6 <br /> Sec.Det.3 <br /> Sec.Det.4 <br /> Sec.Det.11 <br /> Sec.Inf.8 <br /> Sec.Inf.12 <br /> Sec.IR.14 <br /> Sec.IR.15  |  Sec.IAM.2 <br /> Sec.IAM.4 <br /> Sec.IAM.5 <br /> Sec.Inf.3 <br /> Sec.Inf.5 <br /> Sec.Inf.6 <br /> Sec.IR.14 <br /> Sec.IR.15  |  Sec.Inf.3 <br /> Sec.Inf.5 <br /> Sec.Inf.6 <br /> Sec.IR.14 <br /> Sec.IR.15 <br /> Sec.IR.1 <br /> Sec.IR.4 <br /> Ops.2  |  Sec.IR.1 <br /> Sec.IR.4 <br /> Ops.2  |  Sec.IR.10  |  Sec.IAM.2 <br /> Sec.IAM.4 <br /> Sec.Inf.3 <br /> Sec.Inf.5 <br /> Sec.Inf.6 <br /> Sec.Inf.25 <br /> Sec.Inf.30 <br /> Platform.1 <br /> Platform.2 <br /> Platform.4  |  Sec.IR.14 <br /> Sec.IR.15 <br /> Sec.Inf.29 <br /> Sec.IR.1 <br /> Ops.3  |  Sec.Inf.9 <br /> Sec.Inf.14 <br /> Sec.IR.13 <br /> Ops.1 <br /> Ops.2 <br /> Ops.4  |
|  Actions on Objectives  |  Sec.Det.1 <br /> Sec.Det.6 <br /> Sec.Det.3 <br /> Sec.Det.4 <br /> Sec.Det.11 <br /> Sec.Inf.8 <br /> Sec.Inf.13 <br /> Sec.IR.14 <br /> Sec.IR.15 <br /> Sec.DP.4  |  Sec.IAM.2 <br /> Sec.IAM.4 <br /> Sec.IAM.5 <br /> Sec.Inf.17 <br /> Sec.Inf.18 <br /> Sec.Inf.23 <br /> Sec.IR.14 <br /> Sec.IR.15 <br /> Sec.DP.1 <br /> Sec.DP.2  |  Sec.IAM.2 <br /> Sec.Inf.17 <br /> Sec.Inf.18 <br /> Sec.Inf.23 <br /> Sec.IR.14 <br /> Sec.IR.15 <br /> Sec.IR.5 <br /> Ops.2  |  Sec.IAM.2 <br /> Sec.Inf.9 <br /> Sec.Inf.17 <br /> Sec.Inf.18 <br /> Sec.Inf.23 <br /> Sec.DP.4  |  Sec.IR.10  |  Sec.IAM.2 <br /> Sec.IAM.4 <br /> Sec.Inf.3 <br /> Sec.Inf.5 <br /> Sec.Inf.6 <br /> Sec.Inf.25 <br /> Platform.1 <br /> Platform.4  |  Sec.IR.14 <br /> Sec.IR.15 <br /> Sec.Inf.29 <br /> Sec.IR.1 <br /> Ops.3 <br /> Sec IR.7  |  Sec.Inf.9 <br /> Sec.IR.13 <br /> Ops.1 <br /> Ops.4  |

**Note**
\*\*Defined in the 2006 version of JP 3-13, as documented in Mitre, "Characterizing Effects on the Cyber Adversary, A Vocabulary for Analysis and Assessment", https://www.mitre.org/sites/default/files/publications/characterizing-effects-cyber-adversary-13-4173.pdf
