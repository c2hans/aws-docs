---
source_url: https://docs.aws.amazon.com/whitepapers/latest/classic-intrusion-analysis-frameworks-for-aws-environments/reconnaissance-post-intrusion.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Reconnaissance – Post-Intrusion
<a name="reconnaissance-post-intrusion"></a>

 Activities in this phase occur after attacker’s intrusion attempts have been successful. Attackers perform reconnaissance inside their victim’s environment in an effort to build a map for themselves, which can then be referenced throughout the attack. These activities could include port scanning, ping sweeps, Windows Management Instrumentation (WMI) queries, and SNMP queries.

## Control Objective – Detect
<a name="control-objective-detect-1"></a>

 The objective of the *Detect* control in the *Reconnaissance Post-Intrusion* phase is to “discover or discern the existence, presence, or fact of an intrusion into information systems.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [Amazon GuardDuty](control-name-descriptions.md#amazon-guardduty) <br /> (ID: Sec.Det.1)  |  This control detects reconnaissance activity, such as unusual API activity, intra-VPC port scanning, unusual patterns of failed login requests, or unblocked port probing from a known, bad IP address.  |
|  [Amazon GuardDuty Partners](control-name-descriptions.md#amazon-guardduty-partners) <br /> (ID: Sec.Det.2)  |  These controls are a complement to Amazon GuardDuty.  |
|  [Amazon CloudWatch, CloudWatch Logs, CloudTrail \+ Insights, Reporting & Third-Parties](control-name-descriptions.md#amazon-cloudwatch-cloudwatch-logs-cloudtrail-insights-reporting-third-parties) <br /> (ID: Sec.Det.6)  |  These controls monitor, detect, visualize, and receive notifications of attacks, and respond to changes in your AWS resources.  |
|  [AWS Security Hub CSPM](control-name-descriptions.md#aws-security-hub) <br /> (ID: Sec.Det.3)  |  This control gives you a comprehensive view of your high-priority security alerts and compliance status across AWS accounts.  |
|  [AWS Security Hub CSPM Partners](control-name-descriptions.md#aws-security-hub-partners) <br /> (ID: Sec.Det.4)  |  AWS Security Hub CSPM APN Partner products are a complement to Amazon GuardDuty.  |
|  [Amazon Detective](control-name-descriptions.md#amazon-detective) <br /> (ID: Sec.Det.11)  |  Amazon Detective makes it easy to analyze, investigate, and quickly identify the root cause of potential security issues or suspicious activities. Amazon Detective automatically collects log data from your AWS resources and uses machine learning, statistical analysis, and graph theory to build a linked set of data that enables you to easily conduct faster and more efficient security investigations.  |
|  [AWS Network Firewall](control-name-descriptions.md#aws-network-firewall) <br /> (ID: Sec.Inf.30)  |  This control detects reconnaissance activity using signature-based detection.  |
|  [Honeywords and Honeykeys](control-name-descriptions.md#honeywords-and-honeykeys) <br /> (ID: Sec.IR.11)  |  When an attacker attempts to use stolen, false credentials, these controls help to detect and contain the attack, so you can recover faster.  |

## Control Objective – Deny
<a name="control-objective-deny-1"></a>

 The objective of the *Deny* control in the *Reconnaissance Post-Intrusion* phase is to “prevent the adversary from accessing and using critical information, systems, and services.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [Amazon Virtual Private Cloud (Amazon VPC)](control-name-descriptions.md#amazon-virtual-private-cloud-amazon-vpc) <br /> (ID: Sec.Inf.3)  |  Amazon VPC can help prevent attackers from scanning network resources during reconnaissance. Amazon VPC Black Hole Routes operate as an allow list or deny list of network reachable assets, before Security Groups or NACLs.  |
|  [AWS Identity and Access Management \+ AWS Organizations](control-name-descriptions.md#aws-identity-and-access-management-aws-organizations) <br /> (ID: Sec.IAM.3)  |  In this context, attackers can't execute <service>:Describe\* API calls without Allow permissions.  |
|  [AWS Certificate Manager \+ Transport Layer Security](control-name-descriptions.md#aws-certificate-manager-transport-layer-security) <br /> (ID: Sec.DP.3)  |  Protecting data in transit denies attackers the ability to capture data in transit during the Reconnaissance phase, unless they are able to impersonate a legitimate endpoint.  |
|  [Network Infrastructure Solutions in the AWS Marketplace](control-name-descriptions.md#network-infrastructure-solutions-in-the-aws-marketplace) <br /> (ID: Sec.Inf.10)  |  Infrastructure solutions in the AWS Marketplace can help deny attackers access to data and infrastructure as they conduct reconnaissance.  |
|  [Reverse Proxy Architecture](control-name-descriptions.md#reverse-proxy-architecture) <br /> (ID: Sec.Inf.11)  |  This control protects your servers from unwanted traffic.  |
|  [Amazon Cognito](control-name-descriptions.md#amazon-cognito) <br /> (ID: Sec.IAM.5)  |  This control provides temporary, limited-privilege AWS credentials to allow access to other AWS services.  |
|  [Bottlerocket](control-name-descriptions.md#bottlerocket) <br /> (ID: Sec.Inf.32)  |  This control provides a minimized OS environment capable of running and managing containers, which provides no extraneous listeners or services.  |
|  [AWS Network Firewall](control-name-descriptions.md#aws-network-firewall) <br /> (ID: Sec.Inf.30)  |  The control blocks network scanning during the reconnaissance phase by blocking network scans and probes utilizing signature based intrusion prevention.  |

## Control Objective – Disrupt
<a name="control-objective-disrupt-1"></a>

 The objective of the *Disrupt* control in the *Reconnaissance Post-Intrusion* phase is to “break or interrupt the flow of information.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [Amazon GuardDuty \+ AWS Lambda](control-name-descriptions.md#amazon-guardduty-aws-lambda) <br /> (ID: Sec.IR.1)  |  These controls detect reconnaissance activities and modify security configurations to block traffic associated with an attack.  |
|  [AWS Network Firewall](control-name-descriptions.md#aws-network-firewall) <br /> (ID: Sec.Inf.30)  |  The control detects reconnaissance activity, blocking network scans and probes utilizing signature based intrusion prevention.  |

## Control Objective – Degrade
<a name="control-objective-degrade-1"></a>

 The objective of the *Degrade* control in the *Reconnaissance Post-Intrusion* phase is to “reduce the effectiveness or efficiency of adversary command and control (C2) or communications systems, and information collection efforts or means.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [Honeypot and Honeynet Environments](control-name-descriptions.md#honeypot-and-honeynet-environments) <br /> (ID: Sec.IR.10)  |  These controls help to degrade, detect, and contain attacks.  |
|  [Honeywords and Honeykeys](control-name-descriptions.md#honeywords-and-honeykeys) <br /> (ID: Sec.IR.11)  |  When an attacker attempts to use stolen, false credentials, these controls help to detect and contain the attack, so you can recover faster.  |

## Control Objective – Deceive
<a name="control-objective-deceive-1"></a>

 The objective of the *Deceive* control in the *Reconnaissance Post-Intrusion* phase is to “cause a person to believe what is not true. MILDEC [military deception] seeks to mislead adversary decision makers by manipulating their perception of reality.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [Honeypot and Honeynet Environments](control-name-descriptions.md#honeypot-and-honeynet-environments) <br /> (ID: Sec.IR.10)  |  These controls help to degrade, detect, and contain attacks.  |
|  [Honeywords and Honeykeys](control-name-descriptions.md#honeywords-and-honeykeys) <br /> (ID: Sec.IR.11)  |  When an attacker attempts to use stolen, false credentials, these controls help to detect and contain the attack, so you can recover faster.  |
|  [Amazon Virtual Private Cloud \+ Automation](control-name-descriptions.md#amazon-virtual-private-cloud-automation) <br /> (ID: Sec.IR.9)  |  These controls save the current security group of the host or instance, then isolate the host using restrictive ingress and egress security group rules.  |

## Control Objective – Contain
<a name="control-objective-contain-1"></a>

 The objective of the *Contain* control in the *Reconnaissance Post-Intrusion* phase is “keeping something harmful under control or within limits.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [Honeypot and Honeynet Environments](control-name-descriptions.md#honeypot-and-honeynet-environments) <br /> (ID: Sec.IR.10)  |  These controls help to degrade, detect, and contain attacks.  |
|  [Honeywords and Honeykeys](control-name-descriptions.md#honeywords-and-honeykeys) <br /> (ID: Sec.IR.11)  |  When an attacker attempts to use stolen, false credentials, these controls help to detect and contain the attack, so you can recover faster.  |
|  [Amazon Virtual Private Cloud \+ Automation](control-name-descriptions.md#amazon-virtual-private-cloud-automation) <br /> (ID: Sec.IR.9)  |  These controls help contain compromised systems by using AWS Command Line Interface (CLI) or software development kits using predefined, restrictive security groups.  |

## Control Objective – Respond
<a name="control-objective-respond-1"></a>

 The objective of the *Respond* control in the *Reconnaissance Post-Intrusion* phase is to provide “capabilities that help to react quickly to an adversary’s or others’ IO attack or intrusion.” \*\*

|  Control Names  |  Descriptions  |
| --- | --- |
|  [AWS WAF, WAF Managed Rules \+ Automation](control-name-descriptions.md#aws-waf-waf-managed-rules-automation) <br /> (ID: Sec.Inf.2)  |  Malicious sources scan and probe internet-facing web applications for vulnerabilities. They send a series of requests that generate HTTP 4xx error codes. You can use this history to help identify and block malicious source IP addresses.  |
|  [Amazon GuardDuty \+ AWS Lambda](control-name-descriptions.md#amazon-guardduty-aws-lambda) <br /> (ID: Sec.IR.1)  |  These controls detect reconnaissance activities and modify security configurations to block traffic associated with an attack.  |
|  [Amazon GuardDuty Partners](control-name-descriptions.md#amazon-guardduty-partners) <br /> (ID: Sec.Det.2)  |  These controls are a complement to Amazon GuardDuty.  |
|  [AWS Security Hub CSPM Partners](control-name-descriptions.md#aws-security-hub-partners) <br /> (ID: Sec.Det.4)  |  AWS Security Hub CSPM APN Partner products are a complement to Amazon GuardDuty.  |
|  [Amazon CloudWatch Events & Alarms \+ Amazon SNS \+ SIEM Solutions](control-name-descriptions.md#amazon-cloudwatch-events-alarms-amazon-sns-siem-solutions) <br /> (ID: Sec.Det.7)  |  These controls help you to monitor, detect, visualize, and receive notifications of attacks, so you can respond to changes in your AWS resources.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
