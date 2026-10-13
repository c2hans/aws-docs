---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/accelerate-sap-hana-recovery-with-f-sx-for-ontap/introduction.html
---

# Accelerating SAP HANA Backup and Recovery Using Amazon FSx for NetApp ONTAP Snapshots and Commvault
<a name="introduction"></a>

*Shreejesh MV, Amazon Web Services*

Running SAP HANA on AWS requires you to implement backup solutions that meet stringent recovery objectives. As an SAP HANA administrator, you face challenges in three areas: reducing backup overhead on production systems, achieving recovery time and point objectives, and maintaining regulatory compliance.

This guide presents a backup architecture for multi-terabyte SAP HANA databases. The solution conforms to SAP HANA certification requirements and AWS Well-Architected Framework standards.

## Intended audience
<a name="intended-audience"></a>

This guide is intended for SAP Basis administrators, backup and recovery architects, and storage or cloud infrastructure engineers who are responsible for protecting SAP HANA workloads on AWS. You should understand SAP HANA backup and recovery concepts (such as recovery time and point objectives, save points, the backup catalog, and the Backint interface), and be familiar with Amazon FSx for NetApp ONTAP snapshots and Commvault IntelliSnap administration. Working knowledge of AWS multi-account and networking constructs (such as [Amazon VPC](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) and [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html)) is helpful.

## Objectives
<a name="objectives"></a>

By following this guide, you will:
+ Understand a dual-account architecture that isolates SAP HANA backup operations from production.
+ Configure Amazon FSx for NetApp ONTAP service accounts and Commvault IntelliSnap integration for application-consistent snapshots.
+ Set up cross-account snapshot replication with SnapMirror.
+ Implement Backint-based continuous log backups to enable point-in-time recovery.
+ Validate the end-to-end backup and restore workflow against your recovery time objective (RTO) and recovery point objective (RPO) targets.
+ Establish ongoing monitoring, maintenance, and disaster recovery testing for the solution.

### Solution overview
<a name="solution-overview"></a>

This architecture combines [Amazon FSx for NetApp ONTAP](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/getting-started.html)'s native snapshot capabilities with Commvault's automated backup workflow orchestration to deliver:
+ **Recovery time objective (RTO)** under 15 minutes through instant snapshot restoration
+ **Recovery point objective (RPO)** of 5 minutes using continuous log backups via the SAP Backint interface
+ **Minimal production impact** — backup operations are limited to brief database quiescing during snapshot creation
+ **Block-level efficiency — **only changed data blocks are replicated, significantly reducing bandwidth requirements

Central to this design is a dual-account AWS architecture that enforces a hard isolation boundary between production and backup environments. Amazon FSx for NetApp ONTAP's snapshot engine enables near-instantaneous point-in-time copies regardless of database size, while SnapMirror replication transfers only incremental changes to a separate backup account. Commvault IntelliSnap orchestrates the entire workflow, from quiescing SAP HANA, to triggering snapshots, to managing replication, retention, and catalog registration, without manual intervention.

Some AWS services are not available in all AWS Regions. For Region availability, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page in the AWS documentation, and choose the link for the service.

### Attachments
<a name="attachments-1cbb8aa3-6197-4168-8624-86a93eec975a"></a>

To access additional content that is associated with this document, download and unzip the following file:

[attachment.zip](samples/attachment.zip)
