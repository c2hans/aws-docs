---
source_url: https://docs.aws.amazon.com/whitepapers/latest/ransomware-risk-management-on-aws-using-nist-csf/backup.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Backup
<a name="backup"></a>

 The backup capability component establishes the ability to back up and restore each component within the enterprise. The configuration of this component needs to align with the organization’s recovery time objective (RTO) and recovery point objectives (RPO) for a given application or system.

* Table 2 — Backup capability and the associated AWS services *

|  Capability and CSF mapping  |  AWS service  |  AWS service description  |  Function  |  [AWS GovCloud (US)](https://aws.amazon.com/govcloud-us/) available?  |
| --- | --- | --- | --- | --- |
|  Backup <br /> PR.DS-1, PR.IP-3, PR.IP-4, PR.IP-9, PR.IP-10  |  [Amazon EBS Snapshots](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html)  |  [Amazon Elastic Block Store](https://aws.amazon.com/ebs/) (Amazon EBS) provides the ability to create snapshots (backups) of any EBS volume. A snapshot takes a copy of the EBS volume and places it in S3, where it is stored redundantly in multiple Availability Zones.  |  Provides backup and restoration capabilities for systems and immutable storage.  |  Yes  |
|   |  [AWS Backup](https://aws.amazon.com/backup/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc)  |  AWS Backup enables you to centralize and automate data protection across AWS services. AWS Backup offers a cost-effective, fully managed, policy-based service that further simplifies data protection at scale.  |  Provides backup and restoration capabilities for systems, performs periodic backups of in-formation, provides immutable storage.  |  Yes  |
|   |  [CloudEndure Disaster Recovery](https://aws.amazon.com/cloudendure-disaster-recovery/)  |  CloudEndure Disaster Recovery minimizes downtime and data loss by providing fast, reliable recovery into AWS. The solution continuously replicates applications from physical, virtual, or cloud-based infrastructure to a low-cost staging area that is automatically provisioned in any target AWS Region of your choice.  |  Provides backup and restoration capabilities for systems, performs periodic backups of information, and provides immutable storage.  |  Yes  |
|   |  [AWS CodeCommit](https://aws.amazon.com/codecommit/)  |  AWS CodeCommit is a fully-managed source control service that hosts secure GitHub-based repositories.  |  Provides backup and restore capabilities for configuration files.  |  Yes  |

For more information about backup considerations on AWS, refer to [Backup and restore](https://docs.aws.amazon.com/whitepapers/latest/disaster-recovery-workloads-on-aws/disaster-recovery-options-in-the-cloud.html#backup-and-restore) in the *Disaster Recovery of Workloads on AWS: Recovery in the Cloud* whitepaper, and [Back up data](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/back-up-data.html) in the* Reliability Pillar* whitepaper.
