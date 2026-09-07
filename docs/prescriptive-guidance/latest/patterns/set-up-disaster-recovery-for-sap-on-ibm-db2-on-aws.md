---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/set-up-disaster-recovery-for-sap-on-ibm-db2-on-aws.html
---

# Set up disaster recovery for SAP on IBM Db2 on AWS
<a name="set-up-disaster-recovery-for-sap-on-ibm-db2-on-aws"></a>

*Ambarish Satarkar and Debasis Sahoo, Amazon Web Services*

## Summary
<a name="set-up-disaster-recovery-for-sap-on-ibm-db2-on-aws-summary"></a>

This pattern outlines the steps to set up a disaster recovery (DR) system for SAP workloads with IBM Db2 as the database platform, running on the Amazon Web Services (AWS) Cloud. The objective is to provide a low-cost solution for providing business continuity in the event of an outage.

The pattern uses the [pilot light approach](https://aws.amazon.com/blogs/architecture/disaster-recovery-dr-architecture-on-aws-part-iii-pilot-light-and-warm-standby/). By implementing pilot light DR on AWS, you can reduce downtime and maintain business continuity. The pilot light approach focuses on setting up a minimal DR environment in AWS, including an SAP system and a standby Db2 database, that is synchronized with the production environment.

This solution is scalable. You can extend it to a full-scale disaster recovery environment as needed.

## Prerequisites and limitations
<a name="set-up-disaster-recovery-for-sap-on-ibm-db2-on-aws-prereqs"></a>

**Prerequisites**
+ An SAP instance running on an Amazon Elastic Compute Cloud (Amazon EC2) instance
+ An IBM Db2 database
+ An operating system that is supported by the SAP Product Availability Matrix (PAM)
+ Different physical database hostnames for production and standby database hosts
+ An Amazon Simple Storage Service (Amazon S3) bucket in each AWS Region with [Cross-Region Replication (CRR)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html) enabled

**Product versions**
+ IBM Db2 Database version 11.5.7 or later

## Architecture
<a name="set-up-disaster-recovery-for-sap-on-ibm-db2-on-aws-architecture"></a>

**Target technology stack**
+ Amazon EC2
+ Amazon Simple Storage Service (Amazon S3)
+ Amazon Virtual Private Cloud (VPC peering)
+ Amazon Route 53
+ IBM Db2 High Availability Disaster Recovery (HADR)

**Target architecture**

This architecture implements a DR solution for SAP workloads with Db2 as the database platform. The production database is deployed in AWS Region 1 and a standby database is deployed in a second Region. The standby database is referred to as the DR system. Db2 Database supports multiple standby databases (up to three). It uses Db2 HADR for setting up the DR database and automating log shipping between the production and standby databases.

In the event of a disaster that makes Region 1 unavailable, the standby database in the DR Region takes over the production database role. SAP application servers can be built in advance or by using [AWS Elastic Disaster Recovery](https://aws.amazon.com/disaster-recovery/) or an Amazon Machine Image (AMI) to meet the recovery time objective (RTO) requirements. This pattern uses an AMI.

Db2 HADR implements a production-standby setup, where production acts as the primary server, and all users are connected to it. All transactions are written to log files, which are transferred to the standby server by using TCP/IP. The standby server updates its local database by rolling forward the transferred log records, which helps to ensure that it is kept in sync with the production server.

VPC peering is used so that instances in the production Region and DR Region can communicate with each other. Amazon Route 53 routes end users to internet applications.

![Db2 on AWS with cross-Region replication](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/06edfa4c-0827-4d05-95cf-2d2651e74323/images/e77c1e4e-36f3-4af4-89d0-8eec72348f0a.png)

1. [Create an AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html#creating-an-ami) of the application server in Region 1 and [copy the AMI](https://repost.aws/knowledge-center/copy-ami-region) to Region 2. Use the AMI to launch servers in Region 2 in the event of a disaster.

1. Set up Db2 HADR replication between the production database (in Region 1) and the standby database (in Region 2).

1. Change the EC2 instance type to match the production instance in the event of a disaster.

1. In Region 1, `LOGARCHMETH1` is set to `db2remote: S3 path`.

1. In Region 2, `LOGARCHMETH1` is set to `db2remote: S3 path`.

1. Cross-Region Replication is performed between the S3 buckets.

## Tools
<a name="set-up-disaster-recovery-for-sap-on-ibm-db2-on-aws-tools"></a>

**AWS services**
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html) is a highly available and scalable DNS web service.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html) helps you launch AWS resources into a virtual network that you’ve defined. This virtual network resembles a traditional network that you’d operate in your own data center, with the benefits of using the scalable infrastructure of AWS. This pattern uses [VPC peering](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-peering.html).

## Best practices
<a name="set-up-disaster-recovery-for-sap-on-ibm-db2-on-aws-best-practices"></a>
+ The network plays a key role in deciding the HADR replication mode. For DR across AWS Regions, we recommend that you use Db2 HADR ASYNC or SUPERASYNC mode.
+ For more information about replication modes for Db2 HADR, see the [IBM documentation](https://ibm.github.io/db2-hadr-wiki/hadrSyncMode.html#Description_of_the_Modes).
+ You can use the AWS Management Console or the AWS Command Line Interface (AWS CLI) to [create a new AMI](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html#creating-an-ami) of your existing SAP system. You can then use the AMI to recover your existing SAP system or to create a clone.
+ [AWS Systems Manager Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html) can help with the common maintenance and deployment tasks of EC2 instances and other AWS resources.
+ AWS provides multiple native services to monitor and manage your infrastructure and applications on AWS. Services such as Amazon CloudWatch and AWS CloudTrail can be used to monitor your underlying infrastructure and API operations, respectively. For more details, see [SAP on AWS – IBM Db2 HADR with Pacemaker](https://docs.aws.amazon.com/sap/latest/sap-AnyDB/sap-ibm-pacemaker.html).

## Epics
<a name="set-up-disaster-recovery-for-sap-on-ibm-db2-on-aws-epics"></a>

### Prepare the environment
<a name="prepare-the-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Check the system and logs. | 1. Confirm that the production SAP on Db2 system is set up.<br />2. Confirm that log backup is turned on and configured to save the logs in the S3 bucket. This can be checked by the Db2 parameter `LOGARCHMETH1`.<br />3. Create an AMI of the additional application server. | AWS administrator, SAP Basis administrator |

### Set up the servers and replication
<a name="set-up-the-servers-and-replication"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the SAP and database servers. | 1. To deploy the infrastructure for the DR Region, use an AWS CloudFormation script or use an AMI of the production instance. As a part of the pilot light approach, you can use a smaller EC2 instance in the same family as the production instance. For example, if your production instance type is `r6i.12xlarge`, you can use the `r6i.xlarge` instance type for the DR build. However, make sure that you allocate the same storage capacity on the DR instance to restore the production database backup.<br />2. Create Amazon Elastic File System (Amazon EFS) mount points for `/sapmnt/<SID>/`, and make sure that it is [set to be replicated](https://docs.aws.amazon.com/efs/latest/ug/efs-replication.html) from the primary system.<br />3. Take a FULL database backup (online or offline) from the production system. You will use this backup to build the DR database.<br />4. In the DR system, use the SAP Software Provisioning Manager (SWPM) system copy method with **Using system copy with backup/restore for HA/DR purposes** to build the DR SAP system.<br />5. When asked by SWPM, restore the database in DR with the backup that you took from the production. The DR database will be in the rollforward pending state.The rollforward pending state is set by default after the full backup is restored. The rollforward pending state indicates that the database is in the process of being restored and that some changes might need to be applied. For more information, see the [IBM documentation](https://www.ibm.com/docs/en/db2/11.5?topic=commands-rollforward-database). | SAP Basis administrator |
| Check the configuration. | 1. To set up log archiving for HADR, both the production and DR databases must be able to retrieve logs automatically from all log archive locations. Verify that the `LOGARCHMETH1` parameter in the DR database is set to the same location as in the production database. If the same location is not accessible because of Regional limitations, ensure that the DR system can automatically fetch logs from the primary system.<br />2. To enable TCP/IP ports for database replication enablement, modify `/etc/services` in the production and DR hosts by adding the following two entries. In the code, `<SID>` refers to the System ID (SID) of the Db2 database (for example, `PR1`).<pre><SID>_HADR_1      55001/tcp       # DB2 HADR  Port1<br /><SID>_HADR_2      55002/tcp       # DB2 HADR  Port2</pre><br />Confirm that both ports allow inbound and outbound traffic between both the primary and the standby.<br />3. Check `/etc/hosts` in the production and DR hosts to confirm that hostnames for both production and standby hosts are pointing to the correct IP addresses. | AWS administrator, SAP Basis administrator |
| Set up replication from the production DB to the DR DB (using ASYNC mode). | 1. In the production database, run the following commands to update the parameters.<pre>db2 UPDATE DB CFG FOR <SID> USING HADR_LOCAL_HOST HOST1<br />db2 UPDATE DB CFG FOR <SID> USING HADR_LOCAL_SVC <SID>_HADR_1<br />db2 UPDATE DB CFG FOR <SID> USING HADR_REMOTE_HOST HOST2<br />db2 UPDATE DB CFG FOR <SID> USING HADR_REMOTE_SVC <SID>_HADR_2<br />db2 UPDATE DB CFG FOR <SID> USING HADR_REMOTE_INST db2<sid><br />db2 UPDATE DB CFG FOR <SID> USING HADR_TIMEOUT 120<br />db2 UPDATE DB CFG FOR <SID> USING HADR_SYNCMODE ASYNC<br />db2 UPDATE DB CFG FOR <SID> USING HADR_SPOOL_LIMIT 1000<br />db2 UPDATE DB CFG FOR <SID> USING HADR_PEER_WINDOW 240<br />db2 UPDATE DB CFG FOR <SID> USING indexrec RESTART logindexbuild ON</pre><br />2. In the DR database, run the following commands to update the parameters.<pre>db2 UPDATE DB CFG FOR <SID> USING HADR_LOCAL_HOST HOST2<br />db2 UPDATE DB CFG FOR <SID> USING HADR_LOCAL_SVC <SID>_HADR_2<br />db2 UPDATE DB CFG FOR <SID> USING HADR_REMOTE_HOST HOST1<br />db2 UPDATE DB CFG FOR <SID> USING HADR_REMOTE_SVC <SID>_HADR_1<br />db2 UPDATE DB CFG FOR <SID> USING HADR_REMOTE_INST db2<sid><br />db2 UPDATE DB CFG FOR <SID> USING HADR_TIMEOUT 120<br />db2 UPDATE DB CFG FOR <SID> USING HADR_SYNCMODE ASYNC<br />db2 UPDATE DB CFG FOR <SID> USING HADR_SPOOL_LIMIT 1000<br />db2 UPDATE DB CFG FOR <SID> USING HADR_PEER_WINDOW 240<br />db2 UPDATE DB CFG FOR <SID> USING indexrec RESTART logindexbuild ON</pre><br />These parameters are required to provide HADR-related information to both databases. In the Db2 database, HADR gets activated based on the values for each of the previously set parameters. For more information about these parameters, see the [IBM documentation](https://ibm.github.io/db2-hadr-wiki/hadrConfig.html#HADR_Database_Configuration_Parameters).<br />3. Start HADR first on the newly created standby database by using the following command.<pre>db2 deactivate db <SID><br />db2 start hadr on db <SID> as standby</pre><br />4. Start HADR on the production database by using the following command.<pre>db2 deactivate db <SID><br />db2 start hadr on db <SID> as primary</pre><br />5. Check whether the production and standby Db2 databases are in sync and log shipping is ongoing.<br />To monitor HADR replication status, use the following `db2pd` command.<pre>db2pd -d <SID> -hadr</pre><br />For more information about monitoring HADR, see the [IBM documentation](https://ibm.github.io/db2-hadr-wiki/hadrMonitoring.html#db2pd__hadr). | SAP Basis administrator |

### Test DR failover tasks
<a name="test-dr-failover-tasks"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Plan the production business downtime for the DR test. | Make sure that you plan the required business downtime on production environment for testing the DR failover scenario. | SAP Basis administrator |
| Create a test user. | Create a test user (or any test changes) that can be validated in the DR host to confirm log replication after DR failover. | SAP Basis administrator |
| On the console, stop the production EC2 instances. | Ungraceful shutdown is initiated in this step to mimic a disaster scenario. | AWS systems administrator |
| Scale up the DR EC2 instance to match the requirements. | On the EC2 console, change the instance type in the DR Region.1. Stop the instance: If the instance is running, you must stop it before you can change its instance type. On the EC2 console, select the instance, and choose **Stop**.<br />2. Modify the instance type: On the EC2 console, select the instance, and choose **Actions**, **Instance Settings**, **Change Instance Type**. Select the instance type that matches the primary instance, and choose **Apply**.<br />3. Start the instance: After the instance type change is complete, start the instance from the EC2 console by selecting the instance and choosing **Start**.<br />4. To start the Db2 database, use the following command.<pre>db2start<br />    db2 start HADR on db <SID> as standby</pre> | SAP Basis Admin |
| Initiate takeover. | From the DR system (`host2`), initiate the take-over process and bring up the DR database as the primary.<pre>db2 takeover hadr on database <SID> by force</pre><br />Optionally, you can set the following parameters to adjust database memory allocation automatically based on the instance type. The `INSTANCE_MEMORY` value can be decided based on the dedicated portion of memory to be allocated to the Db2 database.<pre>db2 update db cfg for <SID> using INSTANCE_MEMORY <FIXED VALUE> IMMEDIATE;<br />db2 get db cfg for <SID> | grep -i DATABASE_MEMORY AUTOMATIC IMMEDIATE; <br />db2 update db cfg for <SID> using self_tuning_mem ON IMMEDIATE;</pre><br />Verify the change by using the following commands.<pre>db2 get db cfg for <SID> | grep -i MEMORY<br />db2 get db cfg for <SID> | grep -i self_tuning_mem</pre> | SAP Basis administrator |
| Launch the application server for SAP in the DR Region. | Using the AMI that you made of the production system, [launch a new additional application server](https://aws.amazon.com/premiumsupport/knowledge-center/launch-instance-custom-ami/) in the DR Region. | SAP Basis administrator |
| Perform validation before starting the SAP application. | 1. Validate the `/etc/hosts` and `/etc/fstab` entries.<br />2. Mount `/sapmnt/<SID>/` on the DR system.<br />3. Validate that the DR file system `/sapmnt/<SID>/` is synced with the production `/sapmnt/<SID>/`.<br />4. Log in to `<sid>adm` user, run `R3trans -d`, and verify the output in the `trans.log` file. The `trans.log` file is generated in the same location where you ran the `R3trans -d` command. | AWS administrator, SAP Basis administrator |
| Start the SAP application on the DR system. | Start the SAP application on the DR system by using `<sid>adm` user. Use the following code, in which `XX` represents the instance number of your SAP ABAP SAP Central Services (ASCS) server, and `YY` represents the instance number of your SAP application server.<pre>sapconrol -nr XX -function StartService <SID><br />sapconrol -nr XX -function StartSystem<br />sapconrol -nr YY -function StartService <SID><br />sapconrol -nr YY -function StartSystem</pre> | SAP Basis administrator |
| Perform SAP validation. | This is performed as a DR test to provide evidence or to check the data replication success to the DR Region. | Test engineer |

### Perform DR failback tasks
<a name="perform-dr-failback-tasks"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Start the production SAP and database servers. | On the console, start the EC2 instances that host SAP and the database in the production system. | SAP Basis administrator |
| Start the production database and set up HADR. | Log in to production system (`host1`) and verify that the DB is in recovery mode by using the following command.<pre>db2start<br />db2 start HADR on db P3V as standby<br />db2 connect to <SID></pre><br />Verify that the HADR status is `connected`. Replication status should be `peer`.<pre>db2pd -d <SID> -hadr</pre><br />If the database is not inconsistent and is not at `connected` and `peer` status, a backup and restore might be required to bring the database (on `host1`) in sync with the currently active database (`host2` in the DR Region). In that case, restore the DB backup from the database in the `host2` DR Region to the database in the `host1` production Region. | SAP Basis administrator |
| Fail back the database to the production Region. | In a normal business-as-usual scenario, this step is performed in a scheduled downtime. Applications running on the DR system are stopped, and the database is failed back to the production Region (Region 1) to resume operations from the production Region.1. Log in to the SAP application server in the DR Region, and stop the SAP application.<br />2. Unmount `/sapmnt/<SID>` from the DR system, making sure that the changes are reverse-replicated to `/sapmnt/<SID>` of the production system.<br />3. Log in to the database server (`host1`) in the production Region, and perform the takeover.<pre>db2 takeover hadr on database <SID></pre><br />4. Check the HADR status: `HADR_ROLE` should be `PRIMARY` on `host1` and `StandBy` on `host2`.<pre>db2pd -d <SID> -hadr</pre> | SAP Basis administrator |
| Perform validation before starting the SAP application. | 1. Validate the `/etc/hosts` and `/etc/fstab` entries.<br />2. Mount `/sapmnt/<SID>/` on the production system.<br />3. Make sure it is in sync with the DR system `/sapmnt/<SID>/`.<br />4. Log in to `<sid>adm` user, run `R3trans -d`, and verify the output in the `trans.log` file. The `trans.log` file is generated in the same location where you ran the `R3trans -d` command. | AWS administrator, SAP Basis administrator |
| Start the SAP application. | 1. Start the SAP application on the production system using `<sid>adm` user. Use the following code, in which `XX` represents the instance number of your SAP ASCS server, and `YY` represents the instance number of your SAP application server.<pre>sapconrol -nr XX -function StartService <SID><br />sapconrol -nr XX -function StartSystem<br />sapconrol -nr YY -function StartService <SID><br />sapconrol -nr YY -function StartSystem</pre><br />2.  To confirm that application servers are available, log in to SAP and perform checks by using the SICK and SM51 transactions. | SAP Basis administrator |

## Troubleshooting
<a name="set-up-disaster-recovery-for-sap-on-ibm-db2-on-aws-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Key log files and commands to troubleshoot HADR-related issues | + `db2 get db cfg \| grep -i hadr`<br />+ `db2pd -d sid -hadr`<br />+ `Db2diag.log` (This file is generally located inside the `db2dump` directory, and the `db2dump` path is defined by the parameter `DIAGPATH`.) |
| SAP note for troubleshooting HADR issues on Db2 UDB | Refer to SAP [Note 1154013 - DB6: DB problems in HADR environment](https://service.sap.com/sap/support/notes/1154013). (You need SAP portal credentials to access this note.) |

## Related resources
<a name="set-up-disaster-recovery-for-sap-on-ibm-db2-on-aws-resources"></a>
+ [Disaster recovery approaches for Db2 databases on AWS](https://aws.amazon.com/blogs/architecture/disaster-recovery-approaches-for-db2-databases-on-aws/) (blog post)
+ [SAP on AWS – IBM Db2 HADR with Pacemaker](https://docs.aws.amazon.com/sap/latest/sap-AnyDB/sap-ibm-pacemaker.html)
+ [Step by Step Procedure to set up HADR replication between DB2 databases](https://www.ibm.com/support/pages/step-step-procedure-set-hadr-replication-between-db2-databases)
+ [Db2 HADR Wiki](https://ibm.github.io/db2-hadr-wiki/index.html)

## Additional information
<a name="set-up-disaster-recovery-for-sap-on-ibm-db2-on-aws-additional"></a>

Using this pattern, you can set up a disaster recovery system for an SAP system running on the Db2 database. In a disaster situation, business should be able to continue within your defined recovery time objective (RTO) and recovery point objective (RPO) requirements:
+ **RTO** is the maximum acceptable delay between the interruption of service and restoration of service. This determines what is considered an acceptable time window when service is unavailable.
+ **RPO** is the maximum acceptable amount of time since the last data recovery point. This determines what is considered an acceptable loss of data between the last recovery point and the interruption of service.

For FAQs related to HADR, see [SAP note \#1612105 - DB6: FAQ on Db2 High Availability Disaster Recovery (HADR)](https://launchpad.support.sap.com/#/notes/1612105). (You need SAP portal credentials to access this note.)
