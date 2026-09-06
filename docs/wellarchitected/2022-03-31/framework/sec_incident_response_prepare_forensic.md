---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sec_incident_response_prepare_forensic.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC10-BP03 Prepare forensic capabilities
<a name="sec_incident_response_prepare_forensic"></a>

 It’s important for your incident responders to understand when and how the forensic investigation fits into your response plan. Your organization should define what evidence is collected and what tools are used in the process. Identify and prepare forensic investigation capabilities that are suitable, including external specialists, tools, and automation. A key decision that you should make upfront is if you will collect data from a live system. Some data, such as the contents of volatile memory or active network connections, will be lost if the system is powered off or rebooted.

Your response team can combine tools, such as AWS Systems Manager, Amazon EventBridge, and AWS Lambda, to automatically run forensic tools within an operating system and VPC traffic mirroring to obtain a network packet capture, to gather non-persistent evidence. Conduct other activities, such as log analysis or analyzing disk images, in a dedicated security account with customized forensic workstations and tools accessible to your responders.

Routinely ship relevant logs to a data store that provides high durability and integrity. Responders should have access to those logs. AWS offers several tools that can make log investigation easier, such as Amazon Athena, Amazon OpenSearch Service (OpenSearch Service), and Amazon CloudWatch Logs Insights. Additionally, preserve evidence securely using Amazon Simple Storage Service (Amazon S3) Object Lock. This service follows the WORM (write-once- read-many) model and prevents objects from being deleted or overwritten for a defined period. As forensic investigation techniques require specialist training, you might need to engage external specialists.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Identify forensic capabilities: Research your organization's forensic investigation capabilities, available tools, and external specialists.
+  [Automating Incident Response and Forensics ](https://youtu.be/f_EcwmmXkXk)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [How to automate forensic disk collection in AWS](https://aws.amazon.com/blogs/security/how-to-automate-forensic-disk-collection-in-aws/)
