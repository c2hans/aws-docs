---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/implement-cross-region-disaster-recovery-with-aws-dms-and-amazon-aurora.html
---

# Implement cross-Region disaster recovery with AWS DMS and Amazon Aurora
<a name="implement-cross-region-disaster-recovery-with-aws-dms-and-amazon-aurora"></a>

*Mark Hudson, Amazon Web Services*

## Summary
<a name="implement-cross-region-disaster-recovery-with-aws-dms-and-amazon-aurora-summary"></a>

Natural or human-induced disasters can occur at any time and can impact the availability of services and workloads running in a given AWS Region. To mitigate the risks, you must develop a disaster recovery (DR) plan that incorporates the built-in cross-Region capabilities of AWS services. For AWS services that do not inherently provide cross-Region functionality, the DR plan must also provide a solution to handle their failover across AWS Regions.

This pattern guides you through a disaster recovery setup involving two Amazon Aurora MySQL-Compatible Edition database clusters in a single Region. To meet DR requirements, the database clusters are configured to use the Amazon Aurora global database feature, with a single database spanning multiple AWS Regions. An AWS Database Migration Service (AWS DMS) task replicates data between the clusters in the local Region. AWS DMS, however, currently doesn’t support task failover between Regions. This pattern includes the steps required to work around that limitation and independently configure AWS DMS in both Regions.

## Prerequisites and limitations
<a name="implement-cross-region-disaster-recovery-with-aws-dms-and-amazon-aurora-prereqs"></a>

**Prerequisites **
+ Selected primary and secondary AWS Regions that support [Amazon Aurora global databases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Concepts.AuroraFeaturesRegionsDBEngines.grids.html#Concepts.Aurora_Fea_Regions_DB-eng.Feature.GlobalDatabase).
+ Two independent Amazon Aurora MySQL-Compatible Edition database clusters in a single account in the primary Region.
+ Database instance class db.r5 or higher (recommended).
+ An AWS DMS task in the primary Region performing ongoing replication between the existing database clusters.
+ DR Region resources in place to meet requirements for creating database instances. For more information, see [Working with a DB instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html).

**Limitations **
+ For the full list of Amazon Aurora global database limitations, see [Limitations of Amazon Aurora global databases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html#aurora-global-database.limitations).

**Product versions**
+ Amazon Aurora MySQL-Compatible Edition 5.7 or 8.0. For more information, see [Amazon Aurora versions](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.VersionPolicy.html).

## Architecture
<a name="implement-cross-region-disaster-recovery-with-aws-dms-and-amazon-aurora-architecture"></a>

**Target technology stack**
+ Amazon Aurora MySQL-Compatible Edition global database cluster
+ AWS DMS

**Target architecture**

The following diagram shows a global database for two AWS Regions, one with the primary main and reporter databases and AWS DMS replication, and one with the secondary main and reporter databases.

![Architecture diagram of the cross-Region global database.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/b01f5043-fcb5-4b1e-b79f-999792e89bed/images/3785384c-ed01-454f-b58c-fa09d223d57b.png)

**Automation and scale**

You can use AWS CloudFormation to create the prerequisite infrastructure in the secondary Region, such as the virtual private cloud (VPC), subnets, and parameter groups. You can also use AWS CloudFormation to create the secondary clusters in the DR Region and add them to the global database. If you used CloudFormation templates to create the database clusters in the primary Region, you can update or augment them with an additional template to create the global database resource. For more information, see [Creating an Amazon Aurora DB cluster with two DB instances](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-dbcluster.html#aws-resource-rds-dbcluster--examples) and [Creating a global database cluster for Aurora MySQL](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-rds-globalcluster.html#aws-resource-rds-globalcluster--examples).

Finally, you can create the AWS DMS tasks in the primary and secondary Regions using CloudFormation after failover and failback events occur. For more information, see [AWS::DMS::ReplicationTask](https://docs.amazonaws.cn/en_us/AWSCloudFormation/latest/UserGuide/aws-resource-dms-replicationtask.html).

## Tools
<a name="implement-cross-region-disaster-recovery-with-aws-dms-and-amazon-aurora-tools"></a>
+ [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) is a fully managed relational database engine that's compatible with MySQL and PostgreSQL. This pattern uses Amazon Aurora MySQL-Compatible Edition.
+ [Amazon Aurora global databases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html) are designed for globally distributed applications. A single Amazon Aurora global database can span multiple AWS Regions. It replicates your data with no impact on database performance. It also enables fast local reads with low latency in each Region, and it provides disaster recovery from Region-wide outages.
+ [AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/Welcome.html) provides one-time migration or on-going replication. An on-going replication task keeps your source and target databases in sync. After it is set up, the on-going replication task continuously applies source changes to the target with minimal latency. All AWS DMS features, such as data validation and transformations, are available for any replication task.

## Epics
<a name="implement-cross-region-disaster-recovery-with-aws-dms-and-amazon-aurora-epics"></a>

### Prepare the existing database clusters in the primary Region
<a name="prepare-the-existing-database-clusters-in-the-primary-region"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Modify the database cluster parameter group. | In the existing database cluster parameter group, activate row-level binary logging by setting the `binlog_format` parameter to a value of **row**.<br />AWS DMS requires row-level binary logging for MYSQL-compatible databases when performing ongoing replication or change data capture (CDC). For more information, see [Using an AWS managed MySQL-compatible database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html#CHAP_Source.MySQL.AmazonManaged). | AWS administrator |
| Update the database binary log retention period. | Using a MySQL client installed on your end-user device or an Amazon Elastic Compute Cloud (Amazon EC2) instance, run the following stored procedure provided by Amazon Relational Database Service (Amazon RDS) on the main database cluster's writer node, where `XX` is the number of hours to retain the logs.<pre>call mysql.rds_set_configuration('binlog retention hours', XX)</pre><br />Confirm the setting by running the following command.<pre>call mysql.rds_show_configuration;</pre><br />MySQL-compatible databases managed by AWS purge the binary logs as soon as possible. Therefore, the retention period must be long enough to ensure that the logs are not purged before the AWS DMS task runs. A value of 24 hours is usually sufficient, but the value should be based on the time required to set up the AWS DMS task in the DR Region. | DBA |

### Update the existing AWS DMS task in the primary Region
<a name="update-the-existing-aws-dms-task-in-the-primary-region"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Record the AWS DMS task ARN. | Use the Amazon Resource Name (ARN) to obtain the AWS DMS task name for later use. To retrieve the AWS DMS task ARN, view the task in the console or run the following command.<pre>aws dms describe-replication-tasks</pre><br />An ARN looks like the following.<pre>arn:aws:dms:us-east-1:<accountid>:task:AN6HFFMPM246XOZVEUHCNSOVF7MQCLTOZUIRAMY</pre><br />The characters after the last colon correspond to the task name used in a later step. | AWS administrator |
| Modify the existing AWS DMS task to record the checkpoint. | AWS DMS creates checkpoints that contain information so that the replication engine knows the recovery point for the change stream. To record checkpoint information, perform the following steps in the console:1. Stop the AWS DMS task.<br />2. Use the JSON editor in the task to set the TaskRecoveryTableEnabled parameter to **true**.<br />3. Start the AWS DMS task. | AWS administrator |
| Validate checkpoint information. | Using a MySQL client connected to the writer endpoint for the cluster, query the new metadata table in the reporter database cluster to verify that it exists and contains the replication state information. Run the following command.<pre>select * from awsdms_control.awsdms_txn_state;</pre><br />The task name from the ARN should be found in this table in the `Task_Name` column. | DBA |

### Expand both Amazon Aurora clusters to a DR Region
<a name="expand-both-amazon-aurora-clusters-to-a-dr-region"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create base infrastructure in the DR Region. | Create the base components required for the creation of and access to the Amazon Aurora clusters:+ Virtual private cloud (VPC)<br />+ Subnets<br />+ Security group<br />+ Network access control lists<br />+ Subnet group<br />+ DB parameter group<br />+ DB cluster parameter group<br />Ensure that the configuration of both parameter groups matches the configuration in the primary Region. | AWS administrator |
| Add the DR Region to both Amazon Aurora clusters. | Add a secondary Region (the DR Region) to the main and reporter Amazon Aurora clusters. For more information, see [Adding an AWS Region to an Amazon Aurora global database](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-getting-started.html#aurora-global-database-attaching). | AWS administrator |

### Perform failover
<a name="perform-failover"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Stop the AWS DMS task. | The AWS DMS task in the primary Region will not function properly after failover occurs and should be stopped to avoid errors. | AWS administrator |
| Perform a managed failover. | Perform a managed failover of the main database cluster to the DR Region. For instructions, see [Performing managed planned failovers for Amazon Aurora global databases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html#aurora-global-database-disaster-recovery.managed-failover). After failover on the main database cluster is complete, perform the same activity on the reporter database cluster. | AWS administrator, DBA |
| Load data into the main database. | Insert test data into writer node of the main database in the DR database cluster. This data will be used to validate that replication is functioning properly. | DBA |
| Create the AWS DMS replication instance. | To create the AWS DMS replication instance in the DR Region, see [Creating a replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.Creating.html). | AWS administrator, DBA |
| Create the AWS DMS source and target endpoints. | To create the AWS DMS source and target endpoints in the DR Region, see [Creating source and target endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.Creating.html). The source should point to the writer instance of the main database cluster. The target should point to the writer instance of the reporter database cluster. | AWS administrator, DBA |
| Obtain the replication checkpoint. | To obtain the replication checkpoint, use a MySQL client to query the metadata table by running the following against the writer node in the reporter database cluster in the DR Region.<pre>select * from awsdms_control.awsdms_txn_state;</pre><br />In the table, find the task\_name value that corresponds to the AWS DMS task’s ARN that exists in the primary Region that you obtained in the second epic. | DBA |
| Create an AWS DMS task. | Using the console, create an AWS DMS task in the DR Region. In the task, specify a migration method of **Replicate data changes only**. For more information, see [Creating a task](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.Creating.html). 1. In the task settings, use the wizard to specify the following:**CDC start mode for source transactions** – Enable custom CDC start mode**Custom CDC start point for source transactions** – Specify a recovery checkpoint<br />2. In the **Recovery checkpoint** box, enter the replication checkpoint value previously obtained through the database query on the `awsdms_txn_state` table. <br />3. In the task settings section, select the JSON editor, and set the **TaskRecoveryTableEnabled** parameter to **true**.  <br />Set the AWS DMS task **Start migration task** setting to **Automatically on create**. | AWS administrator, DBA |
| Record the AWS DMS task ARN. | Use the ARN to obtain the AWS DMS task name for later use. To retrieve the AWS DMS task ARN, run the following command.<pre>aws dms describe-replication-tasks</pre> | AWS administrator, DBA |
| Validate the replicated data. | Query the reporter database cluster in the DR Region to confirm that the test data that you loaded into the main database cluster has been replicated. | DBA |

### Perform failback
<a name="perform-failback"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Stop the AWS DMS task. | The AWS DMS task in the DR Region will not function properly after failback occurs and should be stopped to avoid errors. | AWS administrator |
| Perform a managed failback. | Fail back the main database cluster to the primary Region. For instructions, see [Performing managed planned failovers for Amazon Aurora global databases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database-disaster-recovery.html#aurora-global-database-disaster-recovery.managed-failover). After the failback on the main database cluster is complete, perform the same activity on the reporter database cluster. | AWS administrator, DBA |
| Obtain the replication checkpoint. | To obtain the replication checkpoint, use a MySQL client to query the metadata table by running the following against the writer node in the reporter database cluster in the DR Region.<pre>select * from awsdms_control.awsdms_txn_state;</pre><br />In the table, find the `task_name` value that corresponds to the AWS DMS task's ARN that exists in the DR Region that you obtained in the fourth epic. | DBA |
| Update the AWS DMS source and target endpoints. | After the database clusters have failed back, check the clusters in the primary Region to determine which nodes are the writer instances. Then verify the existing AWS DMS source and target endpoints in the primary Region are pointing to the writer instances. If not, update the endpoints with the writer instance Domain Name System (DNS) names. | AWS administrator |
| Create an AWS DMS task. | Using the console, create an AWS DMS task in the primary Region. In the task, specify a migration method of **Replicate data changes only**. For more information, see [Creating a task](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.Creating.html). 1. In the task settings, use the wizard and specify the following:**CDC start mode for source transactions** – Enable custom CDC start mode**Custom CDC start point for source transactions** – Specify a recovery checkpoint<br />2. In the **Recovery checkpoint** box, enter the replication checkpoint value previously obtained through the database query on the` awsdms_txn_state` table. <br />3. Also within the task settings section, select the JSON editor and set the **TaskRecoveryTableEnabled** parameter to **true**.<br />4. Finally, set the AWS DMS task **Start migration task** setting to **Automatically on create**. | AWS administrator, DBA |
| Record the AWS DMS task Amazon Resource Name (ARN). | Use the ARN to obtain the AWS DMS task name for later use. To retrieve the AWS DMS task ARN, run the following command:<pre>aws dms describe-replication-tasks</pre><br />The task name will be needed when performing another managed failover or during a DR scenario. | AWS administrator, DBA |
| Delete AWS DMS tasks. | Delete the original (currently stopped) AWS DMS task in the primary Region and the existing AWS DMS task (currently stopped) in the secondary Region. | AWS administrator |

## Related resources
<a name="implement-cross-region-disaster-recovery-with-aws-dms-and-amazon-aurora-resources"></a>
+ [Configuring your Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraSettingUp.html)
+ [Using Amazon Aurora global databases](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-global-database.html)
+ [Working with Amazon Aurora MySQL](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.html)
+ [Working with an AWS DMS replication instance](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_ReplicationInstance.html)
+ [Working with AWS DMS endpoints](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Endpoints.html)
+ [Working with AWS DMS tasks](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Tasks.html)
+ [What is AWS CloudFormation?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html)

## Additional information
<a name="implement-cross-region-disaster-recovery-with-aws-dms-and-amazon-aurora-additional"></a>

Amazon Aurora global databases are used in this example for DR because they provide an effective recovery time objective (RTO) of 1 second and a recovery point objective (RPO) of less than 1 minute, both lower than traditional replicated solutions and ideal for DR scenarios.

Amazon Aurora global databases offer many other advantages, including the following:
+ Global reads with local latency – Global consumers can access information in a local Region, with local latency.
+ Scalable secondary Amazon Aurora DB clusters – Secondary clusters can be scaled independently, adding up to 16 read-only replicas.
+ Fast replication from primary to secondary Amazon Aurora DB clusters – Replication has little performance impact on the primary cluster. It occurs at the storage layer, with typical cross-Region replication latencies of less than 1 second.

This pattern also uses AWS DMS for replication. Amazon Aurora databases provide the ability to create read replicas, which can simplify the replication process and the DR setup. However, AWS DMS is often used to replicate when data transformations are required or when the target database requires additional indexes that the source database does not have.
