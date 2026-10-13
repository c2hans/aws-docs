---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/accelerate-sap-hana-recovery-with-f-sx-for-ontap/best-practices.html
---

# Best practices
<a name="best-practices"></a>

## Backup policy design
<a name="backup-policy-design.47b692f3-bf43-52e1-beab-b4da4a782301"></a>
+ **Frequency:** Implement hourly snapshots during business hours and every 4 hours outside business hours. This establishes a maximum snapshot-based RPO of 1 hour and 4 hours respectively. For databases with RPO requirements under 15 minutes, supplement Amazon FSx for NetApp ONTAP snapshots with continuous SAP HANA log backups via the Backint interface. The recovery point depends on log backup completion intervals. Higher transaction rates and lower backup throughput increase recovery time.
+ **Retention:** Retain local snapshots (on production FSx) for 1 to 3 days and remote snapshots (on backup FSx) for 32 days.
+ **Testing:** Include monthly full restore tests in backup policy.

## Performance optimization
<a name="performance-optimization.2dda2511-b93f-56a2-8fc3-63a54488af19"></a>
+ **Parallel processing:** Configure two or more Media Servers for parallel backup operations.
+ **Network optimization:** Use AWS Transit Gateway for replication to Backup account.

## Security hardening
<a name="security-hardening.9529356d-ed79-54ba-bd0c-2cc499659466"></a>
+ **Access control: **Restrict snapshot creation, replication, and restore operations to authorized users. Implement least-privilege IAM policies for backup resources.
+ **Encryption:** All snapshots inherit encryption settings from parent FSx for ONTAP volumes. Data replication using NetApp SnapMirror is encrypted in-transit and remains deduplicated and compressed during transfer.
+ **Audit logging:** All snapshot operations logged in Commvault and Amazon FSx for NetApp ONTAP, providing audit trails for compliance. Enable [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html) logging for all AWS API calls.
+ **Network isolation:** Place backup infrastructure in private subnets with restricted security groups.
+ **Multi-factor authentication (MFA):** Require MFA for Commvault administrative access.

## Disaster recovery planning
<a name="disaster-recovery-planning.6e78bb1a-8661-580e-b856-9a54a21c045f"></a>
+ **Recovery validation testing: **Conduct quarterly disaster recovery drills to confirm your environment meets the defined 15-minute RTO and 5-minute RPO targets.
+ **Documentation:** Maintain runbooks for recovery procedures.
+ **Team training:** Verify the operations team is trained on recovery procedures.
+ **Failover testing:** Test failover to Backup account quarterly.
