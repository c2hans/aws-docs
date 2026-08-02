---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/replatform-oracle-database-options/phase-1-prepare-assess.html
---

# Phase 1: Assess
<a name="phase-1-prepare-assess"></a>

The assess phase focuses on collecting and analyzing information about the source Oracle database. It's the fundamental part of migration because all subsequent phases are based on the data points that are collected in this phase. The analysis result of this phase is the input of the remaining phases. It determines the most appropriate choice for the replatforming option, migration tool, and approach.

You can use the following tools to assess the source Oracle database when preparing for migration to AWS.

## Oracle diagnostic support scripts
<a name="diagnostic-scripts"></a>

[Oracle diagnostic support scripts](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_SupportScripts.Oracle.html) analyze an on-premises Oracle database. These scripts have the following characteristics:
+ Oracle diagnostic scripts are all written to run using the SQL\*Plus command-line utility. A user account with permissions to query Oracle dictionary views is necessary to prepare the report.
+ The scripts collect information related to the Oracle database configuration and database objects.
+ The scripts produce an HTML report of multiple sections that include database size, schema size, Large Object (LOB) information, redo log, and archive log statistics.
+ The report can assist with deciding the migration strategy.

## Oracle Automatic Workload Repository
<a name="oracle-awr"></a>

[Oracle Automatic Workload Repository (AWR)](https://docs.oracle.com/en/database/oracle/oracle-database/21/tgdba/gathering-database-statistics.html) is a native Oracle tool with the following characteristics:
+ Oracle AWR collects, processes, and maintains database performance statistics.
+ This information is gathered at regular intervals or on-demand. It can be displayed in both reports and views.
+ AWR produces reports of CPU, memory, I/O, and other critical information. The reports help you to understand the nature of the workload running in the database and the resources required in the AWS Cloud.

## Collecting statistics
<a name="collect"></a>

By using these tools, you can collect statistics about Oracle Database configuration, usage, and performance. To achieve a successful migration, you also need to understand the complexity, compatibility, and dependency of the database. This includes information about the operating system, network, application, and business requirements.

The following list contains the most common preparation tasks:
+ Identify the recovery time objective (RTO), recovery point objective (RPO), and service-level agreement (SLA) requirements for the Oracle database.
+ Check the network connectivity between the on-premises environment and AWS. Make sure that it provides enough bandwidth for fast transfers of data between on premises and AWS.
+ Determine the amount of downtime available for migration. This helps you to choose an online or an offline migration approach.
+ Check the chipset endian platform of the database workload. AWS supports x86-x64 little-endian platforms. Other platforms, such as Sun SPARC, HP Tru64, or IBM Z series-based big-endian platforms, require cross-platform migration.
+ AWS supports Linux (32-bit and 64-bit) and Windows operating systems. It doesn't support Solaris, HP-UX, or IBM AIX operating systems, which are commonly used for Oracle databases. Migrating Oracle databases from these operating systems requires platform conversion.
+ Review current architecture and auditing or compliance needs to make sure that all requirements can be met after migrating to AWS.
+ Understand the limitations of different replatforming options:
  + Check the [edition and version](editions-versions.md) of the Oracle database software to make sure it's supported.
  + Determine the input/output operations per second (IOPS) and throughput of the database.
  + Check the current database size and storage growth pattern.
+ If you are migrating Oracle Database Enterprise Edition, identify which Enterprise Edition features are actually used by the application. This is important when evaluating the option of downgrading Enterprise Edition to Standard Edition 2 (SE2).
+ Collect details of the current license agreement for Oracle databases.
+ Check for application dependencies. If the Oracle database supports legacy, custom, or packaged applications, the application will need access to the database administrator privilege and underlying operating system.
