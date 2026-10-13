---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/accelerate-sap-hana-recovery-with-f-sx-for-ontap/deployment-model.html
---

# Deployment model
<a name="deployment-model"></a>

## Dual-account deployment model
<a name="dual-account-deployment-model.3942d46f-ac11-55a1-aa10-4bb3d1a036b2"></a>

The architecture isolates backup and production workloads using separate AWS accounts, enabling performant, secure, and scalable SAP HANA backups through Amazon FSx for NetApp ONTAP and Commvault IntelliSnap:

**Production account:** Hosts SAP HANA on Amazon EC2 instances with primary Amazon FSx for NetApp ONTAP storage. Commvault IntelliSnap Agents coordinate application-consistent backups via ONTAP snapshots.

**Backup account:** Contains CommServe, Media Servers, Access Nodes, and secondary Amazon FSx for NetApp ONTAP instance receiving SnapMirror copies. Isolating backup operations in a dedicated account prevents backup jobs from consuming production compute or network resources.

**Network connectivity: **Connect your production and backup accounts over AWS Transit Gateway, which gives you the required bandwidth for large backups, supporting up to 100 Gbps per direction (100 Gbps ingress and 100 Gbps egress) per VPC attachment per Availability Zone**.** As an example, when you back up a 20 TB database with a 10% daily change rate, you transfer 2 TB of incremental data, and completing this within a 15-minute window requires approximately 18.6 Gbps. To ensure your backup traffic stays within provisioned limits, you should monitor the Transit Gateway CloudWatch metrics BytesIn and BytesOut for real-time bandwidth utilization, enabling you to set proactive alerts and plan capacity to maintain your backup service level agreements (SLAs).

**Account isolation: **[AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) roles in production account lack access to backup resources**.** Backup operations are restricted to their dedicated VPC, preventing backup jobs from impacting SAP HANA performance or accessing production data.

**Independent scaling:** Backup infrastructure (Media Servers, Amazon FSx for NetApp ONTAP storage) operates independently. It scales independently of Production capacity and peak workload schedules.

**Regional deployment flexibility:** Single-region deployment reduces latency and cost for SAP HANA workloads. Cross-region deployment enables disaster recovery through Amazon FSx for NetApp ONTAP SnapMirror replication between AWS regions.

### Amazon FSx for NetApp ONTAP snapshots integration with Commvault
<a name="amazon-f-sx-for-net-app-ontap-snapshots-integration-with-commvault"></a>

Amazon FSx for NetApp ONTAP integrates with Commvault through:

**Snapshot orchestration:** Commvault orchestrates snapshot creation through IntelliSnap Agents. When a backup policy triggers, Commvault communicates with the agent. The agent coordinates with Amazon FSx for NetApp ONTAP to create snapshots.

**Automatic registration:** Snapshots created through integration automatically register in the HANA backup catalog. This enables HANA recovery tools to recognize them as valid recovery points.

**SnapMirror management: **Commvault automatically initiates replication for newly created snapshots to the Backup account Amazon FSx for NetApp ONTAP**.**

**Metadata tracking:** All snapshot metadata is tracked centrally. This includes creation time, size, retention period, and replication status.

**Policy-based automation:** Backup policies define snapshot frequency, retention, and replication parameters. These are enforced automatically without manual intervention.

#### Block-level delta efficiency
<a name="block-level-delta-efficiency"></a>

Block-level delta efficiency transfers only changed blocks during replication, reducing data transfer overhead in proportion to the database change rate:

**Initial baseline replication:** The first snapshot is replicated to the Backup account. This establishes the initial copy on backup Amazon FSx for NetApp ONTAP.

**Incremental transfers:** Subsequent snapshots transfer only the changed blocks rather than the full database. For a 10TB database with 10GB hourly changes, only 10GB (1%) transfers, reducing bandwidth consumption by 99%.

**Storage efficiency:** SnapMirror deduplicates and compresses changed blocks, further reducing backup storage consumption.

**Frequent backup intervals**: Amazon FSx for NetApp ONTAP's snapshot architecture supports frequent snapshot intervals, which can lower the achievable RPO for SAP HANA workloads. Snapshots themselves are near-instantaneous, but SnapMirror replication schedules can be set as frequently as every 5 minutes. Choose the replication interval carefully based on your RPO and RTO targets and on performance and bandwidth considerations, because more frequent replication increases the volume of incremental data transferred. For more information, see [Replicating your data using NetApp SnapMirror](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/scheduled-replication.html) in the Amazon FSx for NetApp ONTAP documentation.

#### Snapshot lifecycle management
<a name="snapshot-lifecycle-management"></a>

Commvault manages snapshot lifecycle:

##### Creation
<a name="creation.e3d34b88-4c4a-5677-8100-5a76067ecce0"></a>

Creates snapshots at scheduled intervals per backup policy. For example, hourly during business hours and every 4 hours otherwise.

##### Replication
<a name="replication.8a842018-0278-5d82-8e2a-61010edf113d"></a>

SnapMirror replicates the snapshot to the backup account asynchronously. Replication latency scales with incremental data volume and network throughput, directly influencing the achieved RPO.

##### Retention
<a name="retention.d3db06d6-324d-5951-b8c6-0da62db77128"></a>

The system retains snapshots per policy, for example, 24 hourly, 7 daily, and 4 weekly snapshots. Older snapshots are deleted.

##### Expiration
<a name="expiration.2eeb118b-8704-5f44-9529-4ea87002c3c3"></a>

Snapshots reaching retention expiration are automatically deleted. This applies to both production and backup Amazon FSx for NetApp ONTAP.

##### Archival
<a name="archival.fe1f4c58-a949-5e2d-b9aa-f1faf441e832"></a>

Before deletion, older snapshots are archived to Amazon S3 for long-term retention. Lifecycle policies transition them to cheaper storage classes.

Recovery from Amazon FSx for NetApp ONTAP snapshots follows these steps:

1. **Snapshot selection:** Identify the desired recovery point from available snapshots in the Commvault catalog. Review creation time and metadata.

1. **Volume cloning:** The selected snapshot is cloned to create a new volume with recovered data. Cloning is instantaneous and uses ONTAP's space-efficient cloning technology.

1. **Mount to target:** The cloned volume is mounted to a recovery location. This can be a test system, alternate HANA instance, or recovery environment.

1. **Data validation:** Validate recovered data before confirming recovery. HANA performs consistency checks on the recovered dataset.

1. **Cleanup: **Delete cloned volumes after recovery to manage storage costs.** **This can be automated or manual.
