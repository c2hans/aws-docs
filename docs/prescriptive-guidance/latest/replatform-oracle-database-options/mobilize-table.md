---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-oracle-database-options/mobilize-table.html
---

# Mobilize phase comparison table
<a name="mobilize-table"></a>

Based on the thorough analysis, Amazon RDS for Oracle and Amazon RDS Custom for Oracle are similar in many ways but different in some areas.

The following table lists the key differences between Amazon RDS for Oracle and Amazon RDS Custom for Oracle. The table provides you with a comprehensive summary for the entire evaluation process to help you make a final decision.

|
|
| Feature | Amazon RDS for Oracle | Amazon RDS Custom for Oracle |
| --- |--- |--- |
| License Included (SE2 only) | Yes | No |
| Version | 19c<br />21c | 12.1.0.2<br />12.2.0.1<br />18c<br />19c |
| Multi-tenant supported version | 19c, 21c | 19c |
| Single-tenant configuration | Yes | No |
| Number of PDBs per CDB in EE | Up to 30 | No restriction |
| AWS Region | [Most](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html#Concepts.RegionsAndAvailabilityZones.Regions) | [Limited](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RDS_Fea_Regions_DB-eng.Feature.RDSCustom.html#Concepts.RDS_Fea_Regions_DB-eng.Feature.RDSCustom.ora) |
| DB instance class | [Most](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Oracle.Concepts.InstanceClasses.html#Oracle.Concepts.InstanceClasses.Supported) | [Limited](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-oracle-feature-support.html#custom-reqs-limits.instances) |
| CPU scalability | License Included model | Not available |
| Storage type | All | gp2, gp3, io1 |
| Maximum throughput per instance | 16,000 MiB/s | 4,000 MiB/s |
| Automatic storage scaling | Yes | No |
| Access to operating system | No | Yes |
| Access to built-in Oracle users (for example, `SYS`, `SYSTEM`) | No | Yes |
| Automatic operating system patching | Yes | No |
| Automatic Oracle Database patching | Yes | No |
| Automatic Oracle Database minor-version upgrade | Yes | No |
| Automatic backup from standby database | Yes | No |
| Multi-AZ deployment | Yes | No |
| Standby replication | Synchronous | Asynchronous or synchronous |
| AWS managed automatic failover | Yes | No |
| AWS managed cross-Region read replica | Yes | No |
| Modification of AWS managed read replica | No | Yes |
| Creation of self-managed read replica | No | Yes |
| Enhanced Monitoring | Yes | No |
| Performance Insights | Yes | No |
