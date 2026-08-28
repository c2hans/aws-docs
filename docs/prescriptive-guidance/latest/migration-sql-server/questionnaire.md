---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-sql-server/questionnaire.html
---

# Appendix: SQL Server database migration questionnaire
<a name="questionnaire"></a>

Use the questionnaire in this section as a starting point to gather information for the assessment and planning phases of your migration project.

General information

1. What is the name of your SQL Server instance?

1. What is the version of your SQL Server instance?

1. What is the edition of your SQL Server database: Standard, Developer, or Enterprise?

1. What is the database type (OLTP, DW, reporting, batch processing)?

1. How many databases do you have on the SQL Server instance?

1. What is the size of your database?

1. What is the database collation?

1. What is the time zone of the database?

1. What are the average and maximum I/O transactions per second (TPS)?

1. What is the IOPS (on average and maximum) for this database for read/write operations?

1. How many transaction logs do you generate per hour (with average and maximum size)?

1. Does the database have linked servers pointing to other databases?

1. What are the SLA requirements for your database?

1. What is the RTO and RPO requirements for your database?

1. How much database downtime can you allow for migration purposes?

1. Do you have any compliance, regulatory, or auditing requirements?

1. What tool do you use to monitor your SQL Server databases?

Infrastructure

1. What is the hostname of the database?

1. What is the operating system used for this database?

1. How many CPU cores does the server have?

1. What is the memory size on the server?

1. Is the database on a virtualized machine or a physical server?

1. Are you using local storage?

1. Do you use network-attached storage (NAS) or storage area network (SAN) storage types?

1. Do you have a cluster or single instances?

Database backups

1. How do you back up your database?  How often?

1. What is your retention period for transaction logs and backups?

1. Where do you store your backup?

Database features

1. Do you use automatic tuning for your SQL Server instance?

1. Do you use parallel-indexed operations?

1. Do you use partitioned table parallelism features?

1. Do you use table and index partitioning?

Database security

1. Do you use dynamic data masking?

1. Do you use security features such as Transparent Database Encryption (TDE)?

1. Do you use server or database audits?

1. Do you use advanced compression?

Database high availability and disaster recovery

1. What are your high availability requirements?

1. Do you use transactional replication?

1. Do you use peer-to-peer transactional replication?

1. What type of high availability solutions (for example, failover clustering, Always On availability groups, database mirroring) do you use for your SQL Server environment?

1. Where are your primary and standby database regions?

1. What do you use as a disaster recovery solution (for example, log shipping, Always On availability groups, a SAN-based virtualized environment)?

1. Do you use a Domain Name System (DNS) alias for database connectivity?

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
