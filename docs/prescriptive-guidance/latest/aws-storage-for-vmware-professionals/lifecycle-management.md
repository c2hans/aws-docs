---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-storage-for-vmware-professionals/lifecycle-management.html
---

# Lifecycle management
<a name="lifecycle-management"></a>

Storage lifecycle management is an aspect of both VMware and AWS environments that focuses on data throughout. This process involves creating, using, maintaining, and eventually retiring or deleting resources. The following table summarizes some lifecycle differences between VMware and AWS.

|
|
| Lifecycle stage | VMware | AWS |
| --- |--- |--- |
| Provisioning | Requires manual creation of datastores and volumes. | Offers on-demand provisioning through S3 (unlimited) and EFS (automatic scaling). EBS provides flexible sizing but requires manual volume creation. |
| Using | Uses storage resource pools and thin provisioning to maximize efficiency. | Offers pay-as-you-go pricing with intelligent tiering (S3) and burst performance (EBS gp2/gp3, EFS). |
| Maintaining | Requires manual optimization, deduplication, and storage using vMotion. | Provides automated lifecycle policies, storage class transitions, and built-in optimization like S3 Intelligent-Tiering. |
| Backing up | Uses VM snapshots and third-party solutions for comprehensive backups. | Offers native backups through EBS snapshots, S3 versioning, and AWS Backup for centralized management across services. |
| Scaling | Scaling requires manual datastore expansion and potential downtime. | Provides automatic scaling (S3, EFS) and elastic EBS volumes without instance interruption. |
| Decommissioning | Requires manual resource cleanup and space reclamation. | Offers automated resource deletion through lifecycle policies and retention rules. |
