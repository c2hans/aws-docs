---
source_url: https://docs.aws.amazon.com/whitepapers/latest/ransomware-risk-management-on-aws-using-nist-csf/event-detection.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Event detection
<a name="event-detection"></a>

 The Event Detection component provides the ability to detect security events as they happen, to trigger the appropriate responses, and to provide information about the incident to the security team.

* Table 5 — Event detection capability and the associated AWS services *

|  Capability and CSF mapping  |  AWS service  |  AWS service description  |  Function  |  [AWS GovCloud (US)](https://aws.amazon.com/govcloud-us/) available?  |
| --- | --- | --- | --- | --- |
|  Event Detection <br /> DE.AE-3, DE.CM-1, DE.CM-4, DE.CM-5, DE.CM-7  |  [Amazon GuardDuty](https://aws.amazon.com/guardduty/)  |  Amazon GuardDuty is a threat detection service that continuously monitors for malicious activity and unauthorized behavior to protect your AWS accounts, workloads, and data stored in S3.  |  This control detects reconnaissance activity, such as unusual API activity, intra-VPC port scanning, unusual patterns of failed login requests, or unblocked port probing from a known, bad IP address.  |  Yes  |
|   |  [Amazon Macie](https://aws.amazon.com/macie/)  |  Amazon Macie is a fully managed data security and data privacy service that uses machine learning (ML) and pattern matching to discover and protect your sensitive data in AWS.  |  This control discovers and protects sensitive data using ML and pattern matching.  |  No  |
|   |  [AWS Network Firewall](https://aws.amazon.com/network-firewall/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc)  |  AWS Network Firewall is a high availability, managed network firewall service for your virtual private cloud (VPC). It enables you to easily deploy and manage stateful inspection, intrusion prevention and detection, and web filtering to help protect your virtual networks on AWS. Network Firewall automatically scales with your traffic, ensuring high availability with no additional customer investment in security infrastructure.  |  This control detects reconnaissance activity using signature-based detection.  |  Yes  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
