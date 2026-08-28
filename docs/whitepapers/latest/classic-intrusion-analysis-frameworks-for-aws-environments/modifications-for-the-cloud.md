---
source_url: https://docs.aws.amazon.com/whitepapers/latest/classic-intrusion-analysis-frameworks-for-aws-environments/modifications-for-the-cloud.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Modifications for the cloud
<a name="modifications-for-the-cloud"></a>

 The AWS approach extends the courses of action available to defenders so that organizations can leverage the inherent benefits of the cloud and the mitigations provided by AWS.

 The courses of action have been modified in the following ways:
+  Destroy is replaced with *respond*.

   Security teams need to plan for successful intrusions to be prepared to respond effectively and efficiently, should an intrusion ever occur. AWS provides customers with response capabilities that help reduce the time, effort, damage, and costs associated with intrusion attempts.
+  *Contain* is added to the courses of action.

   Containing attackers that successfully penetrate an IT environment is a prudent course of action. Preventing lateral movement and the credential theft and reuse attacks typically associated with lateral movement, will reduce potential damage and speed recovery. AWS provides several controls that customers can use to help contain attackers. For more information, see *[Appendix: Reference Material](appendix-reference-material.md).*
+  *Restore* is added to the matrix.

   In the scenario where every course of action that an organization has implemented fails across every phase of the intrusion method, restoring data and infrastructure as quickly as possible will be important to restoring business as usual. The AWS Cloud provides a number of powerful service features that allow the rapid restoration of data, such as point-in-time restore for databases, and object locking (immutability) and versioning for [Amazon S3](https://aws.amazon.com/s3).

 AWS also supports many conventional disaster recovery (DR) architectures from *pilot light* environments that may be suitable for small customer workload data center failures to *hot standby* environments that enable rapid failover at scale. With data centers in AAWS Regions all around the world, AWS provides a set of cloud-based disaster recovery services designed to provide rapid recovery of your IT infrastructure and data, such as [CloudEndure Disaster Recovery](https://aws.amazon.com/cloudendure-disaster-recovery/).

 **Table 2: Modified courses of action matrix **

|  Phase  |  Detect  |  Deny  |  Disrupt  |  Degrade  |  Deceive  |  Contain  |  Respond  |  Restore  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  Reconnaissance: pre-intrusion  |   |   |   |   |   |   |   |   |
|  Reconnaissance: post-intrusion  |   |   |   |   |   |   |   |   |
|  Exploit development  |   |   |   |   |   |   |   |   |
|  Delivery  |   |   |   |   |   |   |   |   |
|  Exploitation  |   |   |   |   |   |   |   |   |
|  Installation  |   |   |   |   |   |   |   |   |
|  Command and Control  |   |   |   |   |   |   |   |   |
|  Actions on Objectives  |   |   |   |   |   |   |   |   |

 The following table lists definitions of the courses of action included in the matrix. All of the following definitions are based on definitions published in [Characterizing Effects on the Cyber Adversary, A Vocabulary for Analysis and Assessment](https://www.mitre.org/sites/default/files/publications/characterizing-effects-cyber-adversary-13-4173.pdf).

**Note**
Defined in 2006 version of JP 3-13, as documented in Mitre, "Characterizing Effects on the Cyber Adversary, A Vocabulary for Analysis and Assessment", https://www.mitre.org/sites/default/files/publications/characterizing-effects-cyber-adversary-13-4173.pdf

 **Table 3: Courses of action definitions**

|  Action  |  Definition  |
| --- | --- |
|  Detect  |  To discover or discern the existence, presence, or fact of an intrusion into information systems.  |
|  Deny  |  To prevent the adversary from accessing and using critical information, systems, and services.  |
|  Disrupt  |  To break or interrupt the flow of information.  |
|  Degrade  |  To reduce the effectiveness or efficiency of adversary command and control (C2) or communications systems, and information collection efforts or means.  |
|  Deceive  |  To cause a person to believe what is not true. MILDEC [military deception] seeks to mislead adversary decision makers by manipulating their perception of reality.  |
|  Contain  |  The action of keeping something harmful under control or within limits.  |
|  Respond  |  To react quickly to an adversary’s or another’s IO attack or intrusion.  |
|  Restore  |  To bring information and information systems back to their original state.  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
