---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-best-practices-for-manufacturing-ot/secure-manufacturing-data.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Secure manufacturing data
<a name="secure-manufacturing-data"></a>

Securing and protecting manufacturing data demands a holistic approach. Some key pillars to protect data within OT and cloud environments are: encryption in transit, encryption at rest, access controls, data classification, and monitoring/auditing data access. The following figure highlights some of these best practices.
+  **Encrypt data in transit and at rest** — Examine the data flow patterns to ensure data is encrypted in transit. Follow the recommendations of securing the connections to the cloud and to network resources as discussed in the sections above. Use secure protocols for network resources and choose strongest possible encryption. Ensure the data is also encrypted at rest; for example, use disk encryption with computing resources like edge gateways.

The encryption techniques for cloud resources may vary based on each AWS service. Consider service documentation to ensure encryption in transit and rest is properly configured for the service. For example, the following figure depicts data stored in S3 bucket is encrypted at rest and is encrypted in transit.
+  **Apply access controls using least privilege principle and monitor/audit data access** — Apply data access controls of OT resources on both data sources and data consumers. On data sources, the access controls should be applied at application, OS and Active Directory level to restrict access to known entities and only for the needed resources. Data consumers should also be configured with a unique identity and should only be allowed to communicate and access the intended data sources. If data consumers are AWS services (Kinesis Streams, S3 buckets), IAM access policy and resource policy can be used.

Access controls should also be applied at the connectivity layer using security appliances such as firewalls or [data diodes](https://en.wikipedia.org/wiki/Unidirectional_network) (unidirectional network devices).

Physical security of network resources should be considered when planning access controls for OT. Physical access to computing hardware, network infrastructure and security appliances should be strictly controlled and limited to only a few approved personnel.

Control measures to manage end of lifecycle for compute and storage should also be considered. Ensure the data is sanitized as per [NIST media sanitization guidelines](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-88r1.pdf) at the end of the lifecycle.

Follow the monitoring best practices guidelines discussed in this document, and ensure that data usage and data access monitoring is part of the overall monitoring plan. Configure automated rules to analyze monitoring data in real time, to send alerts or take automated actions.

For resources in the cloud, physical security of resources in the cloud is the responsibility of AWS in the shared responsibility model. However, the customer has the responsibility of securing connection to the cloud and securing the workloads running in the cloud. AWS offers various access controls and monitoring/auditing mechanisms to help customers secure their workloads running in the cloud. These mechanisms may vary by each service; use the service documentation to ensure access controls are properly applied for cloud resources.
+  **Use resiliency features of the edge and agent software to prevent real time data loss** — Data loss prevention is also an important element to consider in data security. Design the data collection with resiliency in mind. Use features such as “store and forward” in edge and agent software to protect against intermittent data loss. AWS IoT Greengrass, for example, provides [stream manager](https://docs.aws.amazon.com/greengrass/latest/developerguide/stream-manager.html) to locally store data streams in case of intermittent connectivity. It also provides other [resiliency features](https://docs.aws.amazon.com/greengrass/latest/developerguide/disaster-recovery-resiliency.html) such persistent sessions with AWS IoT core and message queue for cloud targets.
+  **Use cloud for backup and business continuity** — Ensuring effective data backup and disaster recovery strategies is critical to ensure data and systems can be available even in the case of an adverse event at the local facility.

Cloud is an attractive target for [backup and restore use cases](https://aws.amazon.com/backup-restore/use-cases/) as it provides virtually unlimited, durable, and cost-effective storage. Amazon S3 and Amazon Glacier are the primary targets for storing backup data. They provide highly durable, flexible, scalable, and secure service to store backup data. Many third-party services offer built-in cloud connectors to send data to the cloud.

Ensuring business continuity requires a more careful consideration on how quickly and efficiently the systems can be restored in case of system failures, server corruptions, or cyber-attacks. With AWS, [CloudEndure Disaster Recovery](https://aws.amazon.com/cloudendure-disaster-recovery/) can be used to minimize downtime and data loss for on-premises physical and virtual servers, and databases. CloudEndure can continuously replicate machines into a low-cost staging area in AWS Cloud. It also provides fail-back capability to on-premise after the failover.

For manufacturing, some low latency workloads may not be able run in cloud even for a shorter duration during disruption. As such disaster recovery plans should include consideration for running on-premises workload on a separate on-premises infrastructure (such as [AWS Snowball Edge Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/whatisedge.html) or [AWS Outposts](https://aws.amazon.com/outposts/)).

![A diagram showing secure manufacturing data.](http://docs.aws.amazon.com/whitepapers/latest/security-best-practices-for-manufacturing-ot/images/secure-manufacturing-data.png)

* Secure manufacturing data *

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
