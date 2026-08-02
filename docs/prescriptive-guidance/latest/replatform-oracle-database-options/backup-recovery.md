---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-oracle-database-options/backup-recovery.html
---

# Backup and recovery
<a name="backup-recovery"></a>

Amazon RDS for Oracle and Amazon RDS Custom for Oracle both provide automatic backup and point-in-time recovery (PITR), which are benefits of managed services. When Multi-AZ deployment is enabled in Amazon RDS for Oracle, backup is automatically taken from the standby instance, and there is no I/O impact to the primary instance.

Amazon RDS Custom for Oracle does not support Multi-AZ deployment, and automatic backup takes place on the primary instance.

|
|
| Backup and recovery options | Amazon RDS for Oracle | Amazon RDS Custom for Oracle |
| --- |--- |--- |
| Automatic backup | Yes | Yes |
| Automatic PITR | Yes | Yes |
| Automatic backup from standby instance | Yes | No |
