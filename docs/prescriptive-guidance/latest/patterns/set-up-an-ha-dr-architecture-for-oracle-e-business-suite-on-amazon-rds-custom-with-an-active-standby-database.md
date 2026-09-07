---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-an-ha-dr-architecture-for-oracle-e-business-suite-on-amazon-rds-custom-with-an-active-standby-database.html
---

# Set up an HA/DR architecture for Oracle E-Business Suite on Amazon RDS Custom with an active standby database
<a name="set-up-an-ha-dr-architecture-for-oracle-e-business-suite-on-amazon-rds-custom-with-an-active-standby-database"></a>

*Simon Cunningham, Jaydeep Nandy, and Nitin Saxena, Amazon Web Services*

## Summary
<a name="set-up-an-ha-dr-architecture-for-oracle-e-business-suite-on-amazon-rds-custom-with-an-active-standby-database-summary"></a>

This pattern describes how you can architect your Oracle E-Business solution on Amazon Relational Database Service (Amazon RDS) Custom for high availability (HA) and disaster recovery (DR) by setting up an Amazon RDS Custom read replica database in another Amazon Web Services (AWS) Availability Zone and converting it to an active standby database. The creation of the Amazon RDS Custom read replica is fully automated through the AWS Management Console.

This pattern doesn’t discuss the steps for adding additional application tiers and shared file systems, which can also be part of an HA/DR architecture. For more information about those topics, see the following Oracle Support Notes: 1375769.1, 1375670.1, and 1383621.1 (section 5, *Advanced Cloning Options*). (Access requires an [Oracle Support](https://support.oracle.com/portal/) account.)

To migrate E-Business Suite system to a single-tier, Single-AZ architecture on Amazon Web Services (AWS), see the pattern [Migrate Oracle E-Business Suite to Amazon RDS Custom](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-oracle-e-business-suite-to-amazon-rds-custom.html).

Oracle E-Business Suite is an Enterprise Resource Planning (ERP) solution for automating enterprise-wide processes such as financials, human resources, supply chains, and manufacturing. It has a three-tier architecture: client, application, and database. Previously, you had to run your E-Business Suite database on a self-managed [Amazon Elastic Compute Cloud (Amazon EC2) instance,](https://aws.amazon.com/ec2/) but you can now benefit from [Amazon RDS Custom](https://aws.amazon.com/rds/custom/).

## Prerequisites and limitations
<a name="set-up-an-ha-dr-architecture-for-oracle-e-business-suite-on-amazon-rds-custom-with-an-active-standby-database-prereqs"></a>

**Prerequisites**
+ An existing E-Business Suite installation on Amazon RDS Custom; see the pattern [Migrate Oracle E-Business Suite to Amazon RDS Custom](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-oracle-e-business-suite-to-amazon-rds-custom.html)
+ If you want to change the read replica to read-only and use it to offload reporting to the standby, an [Oracle Active Data Guard database license](https://www.oracle.com/corporate/pricing/) (see the *Oracle Technology Commercial Price List*)

**Limitations**
+ Limitations and unsupported configurations for [Oracle databases on Amazon RDS Custom](https://docs.amazonaws.cn/en_us/AmazonRDS/latest/UserGuide/custom-reqs-limits.html#custom-reqs-limits.limits)
+ Limitations associated with [Amazon RDS Custom for Oracle read replicas](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-rr.html#custom-rr.limitations)

**Product versions**

For Oracle Database versions and instance classes supported by Amazon RDS Custom, see [Requirements and limitations for Amazon RDS Custom for Oracle](https://docs.amazonaws.cn/en_us/AmazonRDS/latest/UserGuide/custom-reqs-limits.html).

## Architecture
<a name="set-up-an-ha-dr-architecture-for-oracle-e-business-suite-on-amazon-rds-custom-with-an-active-standby-database-architecture"></a>

The following diagram illustrates a representative architecture for E-Business Suite on AWS that includes multiple Availability Zones and application tiers in an active/passive setup. The database uses an Amazon RDS Custom DB instance and Amazon RDS Custom read replica. The read replica uses Active Data Guard to replicate to another Availability Zone. You can also use the read replica to offload read traffic on the primary database and for reporting purposes.

![Multi-AZ architecture for Oracle E-Business Suite on AWS](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/a17947e8-56b1-4d92-91df-096c02ff4c19/images/ffdaa2d4-123b-44a0-8d52-b1352a4eee44.png)

For more information, see [Working with read replicas for Amazon RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-rr.html) in the Amazon RDS documentation.

The Amazon RDS Custom read replica is created by default as mounted. However, if you want to offload some of your read-only workloads to the standby database to reduce the load on your primary database, you can manually change the mode of mounted replicas to read-only by following the steps in the [Epics](#set-up-an-ha-dr-architecture-for-oracle-e-business-suite-on-amazon-rds-custom-with-an-active-standby-database-epics) section. A typical use case for this would be to run your reports from the standby database. Changing to read-only requires an active standby database license.

When you create a read replica on AWS, the system uses Oracle Data Guard broker under the covers.  This configuration is automatically generated and set up in Maximum Performance mode as follows:

```
DGMGRL> show configuration
Configuration - rds_dg
  Protection Mode: MaxPerformance
  Members:
  vis_a - Primary database
    vis_b - Physical standby database
Fast-Start Failover: DISABLED
Configuration Status:
SUCCESS   (status updated 58 seconds ago)
```

## Tools
<a name="set-up-an-ha-dr-architecture-for-oracle-e-business-suite-on-amazon-rds-custom-with-an-active-standby-database-tools"></a>

**AWS services**
+ [Amazon RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/working-with-custom-oracle.html) is a managed database service for legacy, custom, and packaged applications that require access to the underlying operating system and database environment. It automates database administration tasks and operations while making it possible for you, as a database administrator, to access and customize your database environment and operating system.

**Other tools**
+ Oracle Data Guard is a tool that helps you create and manage Oracle standby databases. This pattern uses Oracle Data Guard to set up an active standby database on Amazon RDS Custom.

## Epics
<a name="set-up-an-ha-dr-architecture-for-oracle-e-business-suite-on-amazon-rds-custom-with-an-active-standby-database-epics"></a>

### Create a read replica
<a name="create-a-read-replica"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a read replica of the Amazon RDS Custom DB instance. | To create a read replica, follow the instructions in the [Amazon RDS documentation](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ReadRepl.html#USER_ReadRepl.Create) and use the Amazon RDS Custom DB instance you created (see the [Prerequisites](#set-up-an-ha-dr-architecture-for-oracle-e-business-suite-on-amazon-rds-custom-with-an-active-standby-database-prereqs) section) as the source database.<br />By default, the Amazon RDS Custom read replica is created as a physical standby and is in the mounted state. This is intentional to ensure compliance with the Oracle Active Data Guard license. Follow the next steps to convert the read replica to read-only mode. | DBA |

### Change the read replica to a read-only active standby
<a name="change-the-read-replica-to-a-read-only-active-standby"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Connect to the Amazon RDS Custom read replica. | Use the following commands to convert your physical standby database to an active standby database.  These commands require an Oracle active standby license. To get a license, contact your Oracle representative.<pre>$ sudo su - rdsdb<br />-bash-4.2$ sql<br />SQL> select process,status,sequence# from v$managed_standby;<br /><br />PROCESS    STATUS        SEQUENCE#<br />--------- ------------ ----------<br />ARCH       CLOSING            3956<br />ARCH       CONNECTED             0<br />ARCH       CLOSING            3955<br />ARCH       CLOSING            3957<br />RFS        IDLE                  0<br />RFS        IDLE               3958<br />MRP0       APPLYING_LOG       3958<br />SQL> select name, database_role, open_mode from v$database;<br /><br />NAME       DATABASE_ROLE    OPEN_MODE<br />--------- ---------------- --------------------<br />VIS        PHYSICAL STANDBY MOUNTED<br />SQL> alter database recover managed standby database cancel;<br />Database altered.<br />Open the standby database<br />SQL> alter database open;<br />Database altered.<br />SQL> select name, database_role, open_mode from v$database;<br /><br />NAME       DATABASE_ROLE    OPEN_MODE<br />--------- ---------------- --------------------<br />VIS        PHYSICAL STANDBY READ ONLY</pre> | DBA |
| Start media recovery with real-time log apply. | To enable the real-time log apply feature, use the following commands. These convert and validate the standby (read replica) as an active standby database, so you can connect and run read-only queries.<pre>SQL>   alter database recover managed standby database using current logfile disconnect from session;<br />Database altered</pre> | DBA |
| Check the database status. | To check the status of the database, use the following command.<pre>SQL> select name, database_role, open_mode from v$database;<br />NAME      DATABASE_ROLE    OPEN_MODE<br />--------- ---------------- --------------------<br />VIS       PHYSICAL STANDBY READ ONLY WITH APPLY</pre> | DBA |
| Check redo apply mode. | To check redo apply mode, use the following command.<pre>SQL> select process,status,sequence# from v$managed_standby;<br />PROCESS    STATUS        SEQUENCE#<br />--------- ------------ ----------<br />ARCH       CLOSING            3956<br />ARCH       CONNECTED             0<br />ARCH       CLOSING            3955<br />ARCH       CLOSING            3957<br />RFS        IDLE                  0<br />RFS        IDLE               3958<br />MRP0       APPLYING_LOG       3958<br /> <br />SQL> select open_mode from v$database;<br />OPEN_MODE<br />--------------------<br />READ ONLY WITH APPLY</pre> | DBA |

## Related resources
<a name="set-up-an-ha-dr-architecture-for-oracle-e-business-suite-on-amazon-rds-custom-with-an-active-standby-database-resources"></a>
+ [Migrate Oracle E-Business Suite to Amazon RDS Custom](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-oracle-e-business-suite-to-amazon-rds-custom.html) (AWS Prescriptive Guidance)
+ [Working with Amazon RDS Custom](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/rds-custom.html) (Amazon RDS documentation)
+ [Working with read replicas for Amazon RDS Custom for Oracle](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/custom-rr.html) (Amazon RDS documentation)
+ [Amazon RDS Custom for Oracle – New Control Capabilities in Database Environment](https://aws.amazon.com/blogs/aws/amazon-rds-custom-for-oracle-new-control-capabilities-in-database-environment/) (AWS News blog)
+ [Migrating Oracle E-Business Suite on AWS](https://d1.awsstatic.com/whitepapers/migrate-oracle-e-business-suite.pdf) (AWS whitepaper)
+ [Oracle E-Business Suite architecture on AWS](https://docs.aws.amazon.com/whitepapers/latest/overview-oracle-e-business-suite/oracle-e-business-suite-architecture-on-aws.html) (AWS whitepaper)
