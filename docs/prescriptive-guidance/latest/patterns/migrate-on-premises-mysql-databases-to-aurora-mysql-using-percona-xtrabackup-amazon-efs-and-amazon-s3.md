---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-on-premises-mysql-databases-to-aurora-mysql-using-percona-xtrabackup-amazon-efs-and-amazon-s3.html
---

# Migrate on-premises MySQL databases to Aurora MySQL using Percona XtraBackup, Amazon EFS, and Amazon S3
<a name="migrate-on-premises-mysql-databases-to-aurora-mysql-using-percona-xtrabackup-amazon-efs-and-amazon-s3"></a>

*Rohan Jamadagni, Udayasimha Theepireddy, and sajith menon, Amazon Web Services*

## Summary
<a name="migrate-on-premises-mysql-databases-to-aurora-mysql-using-percona-xtrabackup-amazon-efs-and-amazon-s3-summary"></a>

This pattern describes how to migrate large, on-premises MySQL databases efficiently to Amazon Aurora MySQL by using Percona XtraBackup. Percona XtraBackup is an open-source, non-blocking backup utility for MySQL-based servers. The pattern shows how to use Amazon Elastic File System (Amazon EFS) to reduce the time to upload the backup to Amazon Simple Storage Service (Amazon S3) and to restore the backup to Amazon Aurora MySQL. The pattern also provides details on how to make incremental Percona backups to minimize the number of binary logs to be applied to the target Aurora MySQL database.

## Prerequisites and limitations
<a name="migrate-on-premises-mysql-databases-to-aurora-mysql-using-percona-xtrabackup-amazon-efs-and-amazon-s3-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ Permissions to create AWS Identity and Access Management (IAM) roles and policies
+ Network connectivity between the on-premises MySQL database and the virtual private cloud (VPC) on AWS

**Limitations **
+ The source servers must be Linux-based systems that can install a Network File System (NFS) client (nfs-utils/nfs-common).
+ The S3 bucket used for uploading backup files supports server-side encryption (SSE-S3/SSE-KMS) only.
+ Amazon S3 limits the size of the backup files to 5 TB. If your backup file exceeds 5 TB, you can split it into multiple, smaller files.
+ The number of source files uploaded to the S3 bucket cannot exceed one million files.
+ The pattern supports Percona XtraBackup full backup and incremental backup only. It doesn't support partial backups that use `--tables`, `--tables-exclude`, `--tables-file`,  `--databases`, `--databases-exclude`, or `--databases-file`.
+ Aurora doesn't restore users, functions, stored procedures, or time zone information from the source MySQL database.

**Product versions**
+ The source database must be MySQL version 5.5, 5.6, or 5.7.
+ For MySQL 5.7, you must use Percona XtraBackup 2.4.
+ For MySQL 5.6 and 5.6, you must use Percona XtraBackup 2.3 or 2.4.

## Architecture
<a name="migrate-on-premises-mysql-databases-to-aurora-mysql-using-percona-xtrabackup-amazon-efs-and-amazon-s3-architecture"></a>

**Source technology stack**
+ Linux-based operating system
+ MySQL server
+ Percona XtraBackup

**Target technology stack**
+ Amazon Aurora
+ Amazon S3
+ Amazon EFS

**Target architecture**

![Architecture to migrate large MySQL databases to Amazon Aurora MySQL by using Percona XtraBackup.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/bf327776-bafd-484d-9ae2-a6f5c8af6edd/images/7a410539-1511-4106-90e2-8c0c8e95f92b.png)

## Tools
<a name="migrate-on-premises-mysql-databases-to-aurora-mysql-using-percona-xtrabackup-amazon-efs-and-amazon-s3-tools"></a>

*AWS services*
+ [Amazon Aurora](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.AuroraMySQL.html) is a fully managed relational database engine that makes it simple and cost-effective to set up, operate, and scale MySQL deployments. Aurora MySQL is a drop-in replacement for MySQL.
+ [Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) helps you create and configure shared file systems in the AWS Cloud.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Other tools**
+ [Percona XtraBackup](https://www.percona.com/doc/percona-xtrabackup/2.4/index.html) is an open-source utility that performs streaming, compressed, and incremental backups of MySQL databases without disrupting or blocking your databases.

## Epics
<a name="migrate-on-premises-mysql-databases-to-aurora-mysql-using-percona-xtrabackup-amazon-efs-and-amazon-s3-epics"></a>

### Create an Amazon EFS file system
<a name="create-an-amazon-efs-file-system"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a security group to associate with Amazon EFS mount targets. | Create a security group in the VPC that is configured with a VPN attachment to the on-premises database over AWS Transit Gateway. For more information about the commands and steps described in this and other stories, see the links in the "Related resources" section at the end of this pattern. | AWS DevOps/database administrator |
| Edit the security group rules. | Add an inbound rule, using type NFS, port 2049, and the IP range of the on-premises database server as the source. By default, the outbound rule allows all the traffic to leave. If this is not the case , add an outbound rule to open a connection for the NFS port. Add two more inbound rules: port 2049 (source: security group ID of this same security group) and port 22 (source: IP range from where you will connect to an EC2 instance). | AWS DevOps/database administrator |
| Create a file system. | In the mount targets, use the VPC and security group you created in the previous story. Choose the throughput mode and performance based on the I/O requirements of the on-premises database. Optionally, enable encryption at rest. | AWS DevOps/database administrator |

### Mount the file system
<a name="mount-the-file-system"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an IAM instance profile role to be associated with an EC2 instance. | Create an IAM role that has permissions to upload and access objects in Amazon S3. Choose the S3 bucket where the backup will be stored as a policy resource. | AWS DevOps |
| Create an EC2 instance. | Launch an Linux-based EC2 instance and attach the IAM instance profile role that you created in the previous step, and the security group you created earlier. | AWS DevOps |
| Install the NFS client. | Install the NFS client on the on-premises database server and on the EC2 instance. For installation instructions, see the "Additional information" section. | DevOps |
| Mount the Amazon EFS file system. | Mount the Amazon EFS file system on premises and on the EC2 instance. On each server, create a directory for storing the backup, and mount the file system by using the mount target endpoint. For an example, see the "Additional information" section. | DevOps |

### Make a backup of the MySQL source database
<a name="make-a-backup-of-the-mysql-source-database"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install Percona XtraBackup. | Install Percona XtraBackup 2.3 or 2.4 (depending on the version of your MySQL database) on the on-premises database server. For installation links, see the "Related resources" section. | Database administrator |
| Count the schemas and tables in the source database. | Gather and note the number of schemas and objects in the source MySQL database. You will use these counts to validate the Aurora MySQL database after migration. | Database administrator |
| (Optional) Note the latest binary log sequence from the source database. | Perform this step if you want to establish binary log replication between the source database and Aurora MySQL to minimize downtime. log-bin must be enabled, and server\_id must be unique. Note the current binary log sequence from the source database, just before initiating a backup. Perform this step just before full backup if you're planning to use only full backup. If you're planning to make incremental backups after a full backup, perform this step just before the final incremental backup that you will restore on the Aurora MySQL DB instance. | Database administrator |
| Start a full backup of the source MySQL database. | Make a full backup of the MySQL source database using Percona XtraBackup. For example commands for full and incremental backups, see the "Additional information" section. | Database administrator |
| (Optional) Make incremental backups using Percona XtraBackup. | Incremental backups can be used to reduce the amount of binary logs you need to apply to sync the source database with Aurora MySQL. Large-size and transaction-heavy databases might generate a large number of binary logs during backups. By taking incremental backups and storing them on a shared Amazon EFS file system, you can significantly reduce the time for backing up and uploading your database. For details, see the "Additional information" section. Continue to make incremental backups until you're ready to begin the migration process to Aurora. | Database administrator |
| Prepare backups. | In this step, transactional logs are applied to the backup for transactions that were in flight during the backup. Continue to apply transactional logs (--apply-log-only) to each incremental backup to merge the backups, except for the last backup. For examples, see the "Additional information" section. After this step, the complete, merged backup will be in \~/<efs\_mount\_name>/fullbackup. | Database administrator |
| Zip and split the final merged backup. | After you prepare the final, merged backup, use tar, zip, and split commands to create smaller zipped files of the backup. For examples, see the "Additional information" section. | Database administrator |

### Restore the backup to an Aurora MySQL DB cluster
<a name="restore-the-backup-to-an-aurora-mysql-db-cluster"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Upload the backup to Amazon S3. | The Amazon EFS file system where the backup files are stored is mounted on both the on-premises database and an EC2 instance, so the backup files are readily available to the EC2 instance. Connect to the EC2 instance by using Secure Shell (SSH) and upload the zipped backup files to a new or existing S3 bucket; for example: aws s3 sync \~/<efs\_mount\_name>/fullbackup s3://<bucket\_name>/fullbackup. For additional details, see the links in the "Related resources" section. | AWS DevOps |
| Create a service role for Aurora to access Amazon S3. | Create an IAM role with trust "rds.amazonaws.com" and a policy that will enable Aurora to access the S3 bucket where the backup files are stored. The required permissions are ListBucket, GetObject, and GetObjectVersion. | AWS DevOps |
| Create the networking configuration for Aurora. | Create a cluster DB subnet group with at least two Availability Zones and a subnet route table configuration that allows outbound connectivity to the source database. Create a security group that allows outbound connections to the on-premises database, and allows administrators to connect to the Aurora DB cluster. For more information, see the links in the "Related resources" section. | AWS DevOps/database administrator |
| Restore the backup to an Aurora MySQL DB cluster. | Restore your data from the backup that you uploaded to Amazon S3. Specify the MySQL version of your source database, provide the S3 bucket name and folder path prefix where you uploaded the backup file (for example, "fullbackup" for the examples in the "Additional information" section), and provide the IAM role you created to authorize Aurora to access Amazon S3. | AWS DevOps/database administrator |
| Validate the Aurora MySQL database. | Validate the count of schema and objects in the restored Aurora DB cluster against the count you obtained from the source database. | Database administrator |
| Set up binlog replication.  | Use the binary log sequence that you noted earlier, before making the last backup that was restored to the Aurora DB cluster. Create a replication user on the source database, and follow the instructions in the "Additional information" section to provide the appropriate privileges, to enable replication on Aurora, and to confirm that the replication is in sync. | AWS DevOps/database administrator |

## Related resources
<a name="migrate-on-premises-mysql-databases-to-aurora-mysql-using-percona-xtrabackup-amazon-efs-and-amazon-s3-resources"></a>

**Creating an Amazon EFS file system**
+ [Creating a security group](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html#CreatingSecurityGroups) (Amazon VPC documentation)
+ [Transit gateway VPN attachments](https://docs.aws.amazon.com/vpc/latest/tgw/tgw-vpn-attachments.html) (Amazon VPC documentation)
+ [Scaling VPN throughput using AWS Transit Gateway](https://aws.amazon.com/blogs/networking-and-content-delivery/scaling-vpn-throughput-using-aws-transit-gateway/) (Networking & Content Delivery blog)
+ [Creating an Amazon EFS file system](https://docs.aws.amazon.com/efs/latest/ug/efs-onpremises.html#wt5-step1-efs) (Amazon EFS documentation)
+ [Creating mount targets](https://docs.aws.amazon.com/efs/latest/ug/accessing-fs.html) (Amazon EFS documentation)
+ [Encrypting data at rest](https://docs.aws.amazon.com/efs/latest/ug/encryption-at-rest.html) (Amazon EFS documentation)

**Mounting the file system**
+ [IAM roles for Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html) (Amazon EC2 documentation)
+ [Launching an Amazon EC2 Linux instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EC2_GetStarted.html#ec2-launch-instance) (Amazon EC2 documentation)
+ [Installing the NFS client](https://docs.aws.amazon.com/efs/latest/ug/efs-onpremises.html#wt5-step4-install-nfs) (Amazon EFS documentation)
+ [Mounting the Amazon EFS file system on your on-premises client](https://docs.aws.amazon.com/efs/latest/ug/efs-onpremises.html#wt5-step3-connect) (Amazon EFS documentation)
+ [Mounting EFS File Systems](https://docs.aws.amazon.com/efs/latest/ug/mounting-fs.html) (Amazon EFS documentation)

**Making a backup of the MySQL source database**
+ [Installing Percona XtraBackup 2.3](https://www.percona.com/doc/percona-xtrabackup/2.3/installation.html) (Percona XtraBackup documentation)
+ [Installing Percona XtraBackup 2.4](https://www.percona.com/doc/percona-xtrabackup/2.4/installation.html) (Percona XtraBackup documentation)
+ [Setting the replication master configuration](https://dev.mysql.com/doc/refman/5.7/en/replication-howto-masterbaseconfig.html) (MySQL documentation)
+ [Migrating data from an external MySQL database to an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrating.ExtMySQL.html) (Aurora documentation)
+ [Incremental backup](https://www.percona.com/doc/percona-xtrabackup/2.4/backup_scenarios/incremental_backup.html) (Percona XtraBackup documentation)

**Restoring the backup to Amazon Aurora MySQL**
+ [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingBucket.html#create-bucket-intro) (Amazon S3 documentation)
+ [Connecting to your Linux instance using SSH](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstancesLinux.html) (Amazon Ec2 documentation)
+ [Configuring the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) (AWS CLI documentation)
+ [sync command](https://docs.aws.amazon.com/cli/latest/reference/s3/sync.html) (AWS CLI command reference)
+ [Creating an IAM policy to access Amazon S3 resources](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Integrating.Authorizing.IAM.S3CreatePolicy.html) (Aurora documentation)
+ [DB cluster prerequisites](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.CreateInstance.html#Aurora.CreateInstance.Prerequisites) (Aurora documentation)
+ [Working with DB subnet groups](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html#USER_VPC.Subnets) (Aurora documentation)
+ [Creating a VPC security group for a private DB instance](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_Tutorials.WebServerDB.CreateVPC.html#CHAP_Tutorials.WebServerDB.CreateVPC.SecurityGroupDB) (Aurora documentation)
+ [Restoring an Aurora MySQL DB cluster from an S3 bucket](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrating.ExtMySQL.html#AuroraMySQL.Migrating.ExtMySQL.S3.Restore) (Aurora documentation)
+ [Setting up replication with MySQL or another Aurora DB cluster ](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Replication.MySQL.html#AuroraMySQL.Replication.MySQL.SettingUp) (Aurora documentation)
+ [mysql.rds\_set\_external\_master procedure](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql_rds_set_external_master.html) (MySQL on Amazon RDS SQL reference)
+ [mysql.rds\_start\_replication procedure](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/mysql_rds_start_replication.html) (MySQL on Amazon RDS SQL reference)

**Additional references**
+ [Migrating data from an external MySQL database to an Aurora MySQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrating.ExtMySQL.html) (Aurora documentation)
+ [MySQL server downloads](https://downloads.mysql.com/archives/community/) (Oracle website)

**Tutorials and videos **
+  [Migrating MySQL data to an Aurora MySQL DB cluster using Amazon S3](https://aws.amazon.com/premiumsupport/knowledge-center/migrate-mysql-aurora-innobackup/) (AWS Knowledge Center)
+  [Amazon EFS setup and mount](https://www.youtube.com/watch?v=NR8rVsSn_dY) (video)

## Additional information
<a name="migrate-on-premises-mysql-databases-to-aurora-mysql-using-percona-xtrabackup-amazon-efs-and-amazon-s3-additional"></a>

**Installing an NFS client**
+ If you are using Red Hat or a similar Linux operating system, use the command:

```
$ sudo yum -y install nfs-utils
```
+ If you are using Ubuntu or a similar Linux operating system, use the command:

```
$ sudo apt-get -y install nfs-common
```

For more information, see the [walkthrough](https://docs.aws.amazon.com/efs/latest/ug/efs-onpremises.html#wt5-step4-install-nfs) in the Amazon EFS documentation.

**Mounting the Amazon EFS file system**

Use the commands:

```
mkdir ~/<efs_mount_name>
$ sudo mount -t nfs -o nfsvers=4.1,rsize=1048576,wsize=1048576,hard,timeo=600,retrans=2,noresvport mount-target-IP:/ ~/<efs_mount_name>
```

For more information, see the [walkthrough](https://docs.aws.amazon.com/efs/latest/ug/efs-onpremises.html#wt5-step3-connect) and [Mounting EFS File Systems](https://docs.aws.amazon.com/efs/latest/ug/mounting-fs.html) in the Amazon EFS documentation.

**Making backups of the MySQL source database**

*Full backups*

Use a command like the following, which takes the backup, zips it, and splits it into smaller chunks of 1 GB each:

```
xtrabackup --backup --user=dbuser --password=<password> --binlog-info=AUTO --stream=tar --target-dir=~/<efs_mount_name>/fullbackup | gzip - | split -d --bytes=1024MB - ~/<efs_mount_name>/fullbackup/backup.tar.gz &
```

If you're planning to make subsequent incremental backups after the full backup, do not zip and split the backup. Instead, use a command similar to the following:

```
xtrabackup --backup --user=dbuser --password=<password> --target-dir=~/<efs_mount_name>/fullbackup/
```

*Incremental backups*

Use the full backup path for the `--incremental-basedir` parameter; for example:

```
xtrabackup --backup --user=dbuser --password=<password> --target-dir=~/<efs_mount_name>/incremental/backupdate --incremental-basedir=~/<efs_mount_name>/fullbackup
```

where *basedir *is the path to the full backup and the xtrabackup\_checkpoints file.

For more information about making backups, see [Migrating Data from an External MySQL Database to an Amazon Aurora MySQL DB Cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/AuroraMySQL.Migrating.ExtMySQL.html) in the Aurora documentation.

**Preparing backups**

To prepare a full backup:

```
xtrabackup --prepare --apply-log-only --target-dir=~/<efs_mount_name>/fullbackup
```

To prepare an incremental backup:

```
xtrabackup --prepare --apply-log-only --target-dir=~/<efs_mount_name>/fullbackup --incremental-dir=~/<efs_mount_name>/incremental/06062020
```

To prepare the final backup:

```
xtrabackup --prepare --target-dir=~/<efs_mount_name>/fullbackup --incremental-dir=~/<efs_mount_name>/incremental/06072020
```

For more information, see [Incremental backups](https://www.percona.com/doc/percona-xtrabackup/2.4/backup_scenarios/incremental_backup.html) in the Percona XtraBackup documentation.

**Zipping and splitting the merged backup**

To zip the merged backup at \~/<efs\_mount\_name>/fullbackup:

```
tar -zcvf <backupfilename.tar.gz> ~/<efs_mount_name>/fullbackup
```

To split the backup:

```
split -d -b1024M --verbose  <backupfilename.tar.gz> <backupfilename.tar.gz>
```

**Setting up binlog replication**

To create a replication user on the source database and provide the appropriate privileges:

```
CREATE USER 'repl_user'@'' IDENTIFIED BY ''; GRANT REPLICATION CLIENT, REPLICATION SLAVE ON *.* TO 'repl_user'@'';
```

To enable replication on Aurora by connecting to the Aurora DB cluster, enable binary logs in the DB cluster parameter group. Set `binlog_format = mixed` (mixed mode is preferred). This change requires that you restart the instance to apply the update.

```
CALL mysql.rds_set_external_master ('sourcedbinstanceIP', sourcedbport, 'repl_user', '', 'binlog_file_name', binlog_file_position, 0); CALL mysql.rds_start_replication;
```

To confirm that the replication is in sync:

```
SHOW Slave Status \G;
```

The **Seconds behind master** field shows how far behind Aurora is from the on-premises database.
