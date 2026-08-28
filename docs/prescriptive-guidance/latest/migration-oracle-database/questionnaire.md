---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/questionnaire.html
---

# Appendix: Oracle migration questionnaire
<a name="questionnaire"></a>

Use the questionnaire in this section as a starting point to gather information for the assessment and planning phases of your migration project. You can [download this questionnaire](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-oracle-database/samples/oracle-database-migration-questionnaire.zip) in Microsoft Excel format and use it to record your information.

## General information
<a name="q-general"></a>

1. What is the name of your Oracle database?

1. What is the version of your Oracle database?

1. What is the edition of the database: Standard or Enterprise?

1. What is the size of your database?

1. What is the database character set?

1. What is the time zone of the database?

1. What are the average and maximum I/O transactions per second (TPS)?

1. What is the IOPS (on average and maximum) for this database for read/write operations?

1. What is the redo log generation per hour (on average and maximum) per day?

1. How many schemas do you plan to migrate?

1. What is the size of each schema?

1. How many big tables (over 100 GB) do you have per schema?

1. Can you archive the tables that don't need to migrate?

1. What is the size of system global areas (SGAs) and program global areas (PGAs) or Automatic Memory Management (AMM) usage, in megabytes?

1. How many tables have LOBs? What is the maximum size of the LOBs?

1. Do all your tables with LOBs have primary keys?

1. Do you have database links that point to other databases?

1. What are the SLA requirements for your database?

1. What are the RTO and RPO requirements for your database?

1. How much database downtime can you allow for migration purposes?

1. Do you have any compliance, regulatory, or auditing requirements?

## Infrastructure
<a name="q-infrastructure"></a>

1. What is the hostname of the database?

1. What is the operating system used for this database?

1. How many CPU cores does the server have?

1. What is the memory size on the server?

1. Are you using local storage?

1. Do you use network-attached storage (NAS) or storage area network (SAN) storage types?

1. Do you have a RAC database? If yes, how many nodes does it have?

1. Do you use partitioning features?

1. Do you use Oracle Spatial?

1. Do you have a multi-tenant database?

## Database backups
<a name="q-backup"></a>

1. How do you back up your database?  How often?

1. What is your retention period for archive logs and backups?

1. Do you use backups to clone your database?

1. Where do you store your backup?

## Database security
<a name="q-security"></a>

1. Do you use Oracle Database Vault?

1. Do you use data masking?

1. Do you use Secure Sockets Layer (SSL)?

1. Do you use Oracle Advanced Security features such as Transparent Data Encryption (TDE)?

1. Do you use Oracle Advanced Compression?

## Database high availability and disaster recovery
<a name="q-ha-dr"></a>

1. What are your high availability requirements?

1. Do you use Oracle Data Guard?  Where are your primary and standby database regions?

1. Do you use Oracle Active Data Guard?

1. Do you use a Domain Name System (DNS) alias for database connectivity?

1. Do you use replication tools such as Oracle GoldenGate, Quest SharePlex, or Oracle Streams?

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
