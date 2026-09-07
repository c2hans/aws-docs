---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-db2-for-luw-to-amazon-ec2-with-high-availability-disaster-recovery.html
---

# Migrate Db2 for LUW to Amazon EC2 with high availability disaster recovery
<a name="migrate-db2-for-luw-to-amazon-ec2-with-high-availability-disaster-recovery"></a>

*Feng Cai, Aruna Gangireddy, and Venkatesan Govindan, Amazon Web Services*

## Summary
<a name="migrate-db2-for-luw-to-amazon-ec2-with-high-availability-disaster-recovery-summary"></a>

When customers migrate their IBM Db2 LUW (Linux, UNIX, and Windows) workload to Amazon Web Services (AWS), using Amazon Elastic Compute Cloud (Amazon EC2) with the Bring Your Own License (BYOL) model is the fastest way. However, migrating large amounts of data from on-premises Db2 into AWS can be a challenge, especially when the outage window is short. Many customers try to set the outage window to less than 30 minutes, which leaves little time for the database itself.

This pattern covers how to accomplish a Db2 migration with a short outage window by using Db2 high availability disaster recovery (HADR). This approach applies to Db2 databases that are on the little-endian Linux platform and are not using Data Partitioning Feature (DPF).

## Prerequisites and limitations
<a name="migrate-db2-for-luw-to-amazon-ec2-with-high-availability-disaster-recovery-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ A Db2 instance running on an Amazon EC2 instance that matches the on-premises file system layouts
+ An Amazon Simple Storage Service (Amazon S3) bucket accessible to the EC2 instance
+ An AWS Identity and Access Management (IAM) policy and role to make programmatic calls to Amazon S3
+ Synchronized time zone and system clocks on Amazon EC2 and the on-premises server
+ The on-premises network connected to AWS through [AWS Site-to-Site VPN](https://aws.amazon.com/vpn/) or [AWS Direct Connect](https://aws.amazon.com/directconnect/)
+ Communication between the on-premises server and Amazon EC2 on HADR ports

**Limitations **
+ The Db2 on-premises instance and Amazon EC2 must be on the same [platform family](https://www.ibm.com/docs/en/db2/11.1?topic=dbrs-backup-restore-operations-between-different-operating-systems-hardware-platforms).
+ HADR is not supported in a partitioned database environment.
+ HADR doesn’t support the use of raw I/O (direct disk access) for database log files.
+ HADR doesn’t support infinite logging.
+ `LOGINDEXBUILD` must be set to `YES`, which will increase the log usage for rebuilding the index.
+ The Db2 on-premises workload must be logged. Set `blocknonlogged=yes` in the database configuration to block any unlogged transactions.

**Product versions**
+ Db2 for LUW version 11.5.9 and later

## Architecture
<a name="migrate-db2-for-luw-to-amazon-ec2-with-high-availability-disaster-recovery-architecture"></a>

**Source technology stack**
+ Db2 on Linux** **x86\_64

**Target technology stack**
+ Amazon EC2
+ AWS Identity and Access Management (IAM)
+ Amazon S3
+ AWS Site-to-Site VPN

**Target architecture**

In the following diagram, Db2 on premises is running on `db2-server1` as the primary. It has two HADR standby targets. One standby target is on premises and is optional. The other standby target, `db2-ec2`, is on Amazon EC2. After the database is cut over to AWS, `db2-ec2` becomes the primary.

![Workflow to migrate with a short outage window an on-premises Db2 by using Db2 HADR.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/2db43e4b-f0ea-4a92-96da-4cafb7d3368b/images/5295420e-3cd8-4127-9a18-ade971c36339.png)

1. Logs are streamed from the primary on-premises database to the standby on-premises database.

1. Using Db2 HADR, logs are streamed from the primary on-premises database through Site-to-Site VPN to Db2 on Amazon EC2.

1. Db2 backup and archive logs are sent from the primary on-premises database to the S3 bucket on AWS.

## Tools
<a name="migrate-db2-for-luw-to-amazon-ec2-with-high-availability-disaster-recovery-tools"></a>

**AWS services**
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell.
+ [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) links your internal network to a Direct Connect location over a standard Ethernet fiber-optic cable. With this connection, you can create virtual interfaces directly to public AWS services while bypassing internet service providers in your network path.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) helps you pass traffic between instances that you launch on AWS and your own remote network.

**Other tools**
+ [db2cli](https://www.ibm.com/docs/en/db2/11.5?topic=commands-db2cli-db2-interactive-cli) is the Db2 interactive CLI command.

## Best practices
<a name="migrate-db2-for-luw-to-amazon-ec2-with-high-availability-disaster-recovery-best-practices"></a>
+ On the target database, use [gateway endpoints for Amazon S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html) to access the database backup image and log files in Amazon S3.
+ On the source database, use [AWS PrivateLink for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html) to send the database backup image and log files to Amazon S3.

## Epics
<a name="migrate-db2-for-luw-to-amazon-ec2-with-high-availability-disaster-recovery-epics"></a>

### Set environment variables
<a name="set-environment-variables"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set environment variables. | This pattern uses the following names and ports:1. Db2 on-premises hostname: `db2-server1`<br />2. HADR standby hostname: `db2-server2` (if HADR is currently running on premises)<br />3. Amazon EC2 hostname: `db2-ec2`<br />4. Instance name: `db2inst1`<br />5. Database name: `SAMPLE`<br />6. HADR ports:`db2-server1: 50010``db2-server2: 50011``db2-ec2: 50012`<br />You can change them to fit your environment. | DBA |

### Configure the on-premises Db2 server
<a name="configure-the-on-premises-db2-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up AWS CLI. | To download and install the latest version of AWS CLI, run the following commands:<pre>$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"<br />unzip awscliv2.zip<br />sudo ./aws/install</pre> | Linux administrator |
| Set up a local destination for Db2 archive logs. | Conditions such as heavy update batch jobs and network slowdowns can cause the HADR standby server to have a lag. To catch up, the standby server needs the transaction logs from the primary server. The sequence of places to request logs is the following:+ The active log directory on the primary server<br />+ The `LOGARCHMETH1` or `LOGARCHMETH2` location on the standby server<br />+ The `LOGARCHMETH1` or `LOGARCHMETH2` location on the primary server<br />In this setup, `/db2logs` is set by `LOGARCHMETH2` on the source as a staging area. The archived logs in this directory will be synced into Amazon S3 and accessed by Db2 on Amazon EC2. The pattern uses `LOGARCHMETH2` because `LOGARCHMETH1` might have been configured to use a third-party vendor tool that the AWS CLI command cannot access:<pre>db2 connect to sample<br />db2 update db cfg for SAMPLE using LOGARCHMETH2 disk:/db2logs</pre> | DBA |
| Run an online database backup. | Run an online database backup, and save it to the local backup file system:<pre>db2 backup db sample online to /backup </pre> | DBA |

### Set up the S3 bucket and IAM policy
<a name="set-up-the-s3-bucket-and-iam-policy"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an S3 bucket. | Create an S3 bucket for the on-premises server to send the backup Db2 images and log files to on AWS. The bucket will be accessed by Amazon EC2:<pre>aws s3api create-bucket --bucket hadrmig-db2 --region us-east-1 </pre> | AWS administrator |
| Create an IAM policy. | The `db2bucket.json` file contains the IAM policy for accessing the S3 bucket:<pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Effect": "Allow",<br />            "Action": [<br />                "kms:GenerateDataKey",<br />                "kms:Decrypt",<br />                "s3:PutObject",<br />                "s3:GetObject",<br />                "s3:AbortMultipartUpload",<br />                "s3:ListBucket",<br />                "s3:DeleteObject",<br />                "s3:GetObjectVersion",<br />                "s3:ListMultipartUploadParts"<br />            ],<br />            "Resource": [<br />                "arn:aws:s3:::hadrmig-db2/*",<br />                "arn:aws:s3:::hadrmig-db2"<br />            ]<br />        }<br />    ]<br />}</pre><br />To create the policy, use the following AWS CLI command:<pre>aws iam create-policy \<br />      --policy-name db2s3hapolicy \<br />      --policy-document file://db2bucket.json </pre><br />The JSON output shows the Amazon Resource Name (ARN) for the policy, where `aws_account_id` represents your account ID:<pre>"Arn": "arn:aws:iam::aws_account_id:policy/db2s3hapolicy"</pre> | AWS administrator, AWS systems administrator |
| Attach the IAM policy to the IAM role. | Usually, the EC2 instance with Db2 running would have an IAM role assigned by the systems administrator. If no IAM role is assigned, you can choose **Modify IAM role** on the Amazon EC2 console.<br />Attach the IAM policy to the IAM role associated with the EC2 instance. After the policy is attached, the EC2 instance can access the S3 bucket:<pre>aws iam attach-role-policy --policy-arn "arn:aws:iam::aws_account_id:policy/db2s3hapolicy" --role-name db2s3harole   </pre> |  |

### Send the source database backup image and log files to Amazon S3
<a name="send-the-source-database-backup-image-and-log-files-to-amazon-s3"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure AWS CLI on the on-premises Db2 server. | Configure AWS CLI with the `Access Key ID` and `Secret Access Key` that you generated earlier:<pre>$ aws configure <br />AWS Access Key ID [None]: *************<br />AWS Secret Access Key [None]: ***************************<br />Default region name [None]: us-east-1<br />Default output format [None]: json</pre> | AWS administrator, AWS systems administrator |
| Send the backup image to Amazon S3. | Earlier, an online database backup was saved to the `/backup` local directory. To send that backup image to the S3 bucket, run the following command:<pre>aws s3 sync /backup s3://hadrmig-db2/SAMPLE_backup</pre> | AWS administrator, AWS systems administrator |
| Send the Db2 archive logs to Amazon S3. | Sync the on-premises Db2 archive logs with the Amazon S3 bucket that can be accessed by the target Db2 instance on Amazon EC2:<pre>aws s3 sync /db2logs s3://hadrmig-db2/SAMPLE_LOGS</pre><br />Run this command periodically by using cron or other scheduling tools. The frequency depends on how often the source database archives transaction log files. |  |

### Connect Db2 on Amazon EC2 to Amazon S3 and start the initial database sync
<a name="connect-db2-on-amazon-ec2-to-amazon-s3-and-start-the-initial-database-sync"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a PKCS12 keystore. | Db2 uses a Public-Key Cryptography Standards (PKCS) encryption keystore to keep the AWS access key secure. Create a keystore, and configure the source Db2 to use it:<pre>gsk8capicmd_64 -keydb -create -db "/home/db2inst1/.keystore/db2s3.p12" -pw "<password>" -type pkcs12 -stash <br /> <br />db2 "update dbm cfg using keystore_location /home/db2inst1/.keystore/db2s3.p12 keystore_type pkcs12"</pre> | DBA |
| Create the Db2 storage access alias. | Db2 uses a storage access alias to access Amazon S3 directly with the `INGEST`, `LOAD`, `BACKUP DATABASE`, or `RESTORE DATABASE` commands. <br />Because you assigned an IAM role to the EC2 instance, `USER` and `PASSWORD` are not required:<br />`db2 "catalog storage access alias <alias_name> vendor S3 server <S3 endpoint> container '<bucket_name>'"`<br />For example, your script might look like the following: <br />`db2 "catalog storage access alias DB2AWSS3 vendor S3 server s3.us-east-1.amazonaws.com container 'hadrmig-db2'" ` | DBA |
| Set the staging area. | We recommend using `DB2_ENABLE_COS_SDK=ON`, `DB2_OBJECT_STORAGE_SETTINGS=EnableStreamingRestore`, and the link to the `awssdk` library to bypass the Amazon S3 staging area for database backup and restore:<pre>#By root:<br />cp -rp /home/db2inst1/sqllib/lib64/awssdk/RHEL/7.6/* /home/db2inst1/sqllib/lib64/<br /><br />#By db2 instance owner:<br />db2set DB2_OBJECT_STORAGE_LOCAL_STAGING_PATH=/db2stage<br />db2set DB2_ENABLE_COS_SDK=ON<br />db2set DB2_OBJECT_STORAGE_LOCAL_STAGING_PATH=/db2stage<br />db2stop<br />db2start</pre> | DBA |
| Restore the database from the backup image. | Restore the target database on Amazon EC2 from the backup image in the S3 bucket:<pre>db2 create db sample on /data1<br />db2 restore db sample from DB2REMOTE://DB2AWSS3/hadrmig-db2/SAMPLE_backup replace existing</pre> | DBA |

### Set up HADR with no HADR on premises
<a name="set-up-hadr-with-no-hadr-on-premises"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure the on-premises Db2 server as the primary. | Update the database configuration settings for HADR on `db2-server1` (the on-premises source) as the primary. Set `HADR_SYNCMODE` to `SUPERASYNC` mode, which has the shortest transaction response time:<br />`db2 update db cfg for sample using HADR_LOCAL_HOST db2-server1 HADR_LOCAL_SVC 50010 HADR_REMOTE_HOST db2-ec2 HADR_REMOTE_SVC 50012 HADR_REMOTE_INST db2inst1 HADR_SYNCMODE SUPERASYNC DB20000I The UPDATE DATABASE CONFIGURATION command completed successfully`<br />Some network delays between the on-premises data center and AWS are expected. (You can set a different `HADR_SYNCMODE` value based on network reliability. For more information, see the [Related resources](#migrate-db2-for-luw-to-amazon-ec2-with-high-availability-disaster-recovery-resources) section). | DBA |
| Change the target database log archive destination. | Change the target database log archive destination to match the Amazon EC2 environment:<pre>db2 update db cfg for SAMPLE using LOGARCHMETH1 'DB2REMOTE://DB2AWSS3//SAMPLE_LOGS/' LOGARCHMETH2 OFF<br />DB20000I  The UPDATE DATABASE CONFIGURATION command completed successfully</pre> | DBA |
| Configure HADR for Db2 on the Amazon EC2 server. | Update database configuration for HADR on `db2-ec2` as standby:<br />`db2 update db cfg for sample using HADR_LOCAL_HOST db2-ec2 HADR_LOCAL_SVC 50012 HADR_REMOTE_HOST db2-server1 HADR_REMOTE_SVC 50010 HADR_REMOTE_INST db2inst1 HADR_SYNCMODE SUPERASYNC DB20000I The UPDATE DATABASE CONFIGURATION command completed successfully` | DBA |
| Verify HADR setup. | Verify the HADR parameters on the source and target Db2 servers.<br />To verify the setup on `db2-server1`, run the following command:<pre>db2 get db cfg for sample|grep HADR<br /> HADR database role                                      = PRIMARY<br /> HADR local host name                  (HADR_LOCAL_HOST) = db2-server1<br /> HADR local service name                (HADR_LOCAL_SVC) = 50010<br /> HADR remote host name                (HADR_REMOTE_HOST) = db2-ec2<br /> HADR remote service name              (HADR_REMOTE_SVC) = 50012<br /> HADR instance name of remote server  (HADR_REMOTE_INST) = db2inst1<br /> HADR timeout value                       (HADR_TIMEOUT) = 120<br /> HADR target list                     (HADR_TARGET_LIST) = <br /> HADR log write synchronization mode     (HADR_SYNCMODE) = NEARSYNC<br /> HADR spool log data limit (4KB)      (HADR_SPOOL_LIMIT) = AUTOMATIC(52000)<br /> HADR log replay delay (seconds)     (HADR_REPLAY_DELAY) = 0<br /> HADR peer window duration (seconds)  (HADR_PEER_WINDOW) = 0<br /> HADR SSL certificate label             (HADR_SSL_LABEL) =<br /> HADR SSL Hostname Validation        (HADR_SSL_HOST_VAL) = OFF</pre><br /> To verify the setup on `db2-ec2`, run the following command:<pre>db2 get db cfg for sample|grep HADR<br /> HADR database role                                      = STANDBY<br /> HADR local host name                  (HADR_LOCAL_HOST) = db2-ec2<br /> HADR local service name                (HADR_LOCAL_SVC) = 50012<br /> HADR remote host name                (HADR_REMOTE_HOST) = db2-server1<br /> HADR remote service name              (HADR_REMOTE_SVC) = 50010<br /> HADR instance name of remote server  (HADR_REMOTE_INST) = db2inst1<br /> HADR timeout value                       (HADR_TIMEOUT) = 120<br /> HADR target list                     (HADR_TARGET_LIST) = <br /> HADR log write synchronization mode     (HADR_SYNCMODE) = SUPERASYNC<br /> HADR spool log data limit (4KB)      (HADR_SPOOL_LIMIT) = AUTOMATIC(52000)<br /> HADR log replay delay (seconds)     (HADR_REPLAY_DELAY) = 0<br /> HADR peer window duration (seconds)  (HADR_PEER_WINDOW) = 0<br /> HADR SSL certificate label             (HADR_SSL_LABEL) =<br /> HADR SSL Hostname Validation        (HADR_SSL_HOST_VAL) = OFF</pre><br />The `HADR_LOCAL_HOST`, `HADR_LOCAL_SVC`, `HADR_REMOTE_HOST`, and `HADR_REMOTE_SVC` parameters indicate the one primary and one standby HADR setup. | DBA |
| Start up the Db2 HADR instance. | Start the Db2 HADR instance on the standby server `db2-ec2` first:<pre>db2 start hadr on db sample as standby<br />DB20000I  The START HADR ON DATABASE command completed successfully.</pre><br />Start Db2 HADR on the primary (source) server `db2-server1`:<pre>db2 start hadr on db sample as primary<br />DB20000I  The START HADR ON DATABASE command completed successfully.</pre><br />The HADR connection between Db2 on premises and on Amazon EC2 has now been successfully established. The Db2 primary server `db2-server1` starts streaming transaction log records to `db2-ec2` in real time. | DBA |

### Set up HADR when HADR exists on premises
<a name="set-up-hadr-when-hadr-exists-on-premises"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Add Db2 on Amazon EC2 as an auxiliary standby. | If HADR is running on the on-premises Db2 instance, you can add Db2 on Amazon EC2 as an auxiliary standby using `HADR_TARGET_LIST` by running the following commands on `db2-ec2`:<br />`db2 update db cfg for sample using HADR_LOCAL_HOST db2-ec2 HADR_LOCAL_SVC 50012 HADR_REMOTE_HOST db2-server1 HADR_REMOTE_SVC 50010 HADR_REMOTE_INST db2inst1 HADR_SYNCMODE SUPERASYNC DB20000I The UPDATE DATABASE CONFIGURATION command completed successfully. db2 update db cfg for sample using HADR_TARGET_LIST "db2-server1:50010\|db2-server2:50011" DB20000I The UPDATE DATABASE CONFIGURATION command completed successfully.` | DBA |
| Add the auxiliary standby information to the on-premises servers. | Update `HADR_TARGET_LIST` on the two on-premises servers (primary and standby).<br />On `db2-server1`, run the following code:<br />`db2 update db cfg for sample using HADR_TARGET_LIST "db2-server2:50011\|db2-ec2:50012" DB20000I The UPDATE DATABASE CONFIGURATION command completed successfully. SQL1363W One or more of the parameters submitted for immediate modification were not changed dynamically. For these configuration parameters, the database must be shutdown and reactivated before the configuration parameter changes become effective.`<br />On `db2-server2`, run the following code:<br />`db2 update db cfg for sample using HADR_TARGET_LIST "db2-server1:50010\|db2-ec2:50012" DB20000I The UPDATE DATABASE CONFIGURATION command completed successfully. SQL1363W One or more of the parameters submitted for immediate modification were not changed dynamically. For these configuration parameters, the database must be shutdown and reactivated before the configuration parameter changes become effective.` | DBA |
| Verify HADR setup. | Verify the HADR parameters on the source and target Db2 servers.<br />On `db2-server1`, run the following code:<pre>db2 get db cfg for sample|grep HADR<br /> HADR database role                                      = PRIMARY<br /> HADR local host name                  (HADR_LOCAL_HOST) = db2-server1<br /> HADR local service name                (HADR_LOCAL_SVC) = 50010<br /> HADR remote host name                (HADR_REMOTE_HOST) = db2-server2<br /> HADR remote service name              (HADR_REMOTE_SVC) = 50011<br /> HADR instance name of remote server  (HADR_REMOTE_INST) = db2inst1<br /> HADR timeout value                       (HADR_TIMEOUT) = 120<br /> HADR target list                     (HADR_TARGET_LIST) = db2-server2:50011|db2-ec2:50012<br /> HADR log write synchronization mode     (HADR_SYNCMODE) = NEARSYNC<br /> HADR spool log data limit (4KB)      (HADR_SPOOL_LIMIT) = AUTOMATIC(52000)<br /> HADR log replay delay (seconds)     (HADR_REPLAY_DELAY) = 0<br /> HADR peer window duration (seconds)  (HADR_PEER_WINDOW) = 0<br /> HADR SSL certificate label             (HADR_SSL_LABEL) =<br /> HADR SSL Hostname Validation        (HADR_SSL_HOST_VAL) = OFF</pre><br />On `db2-server2`, run the following code:<pre>db2 get db cfg for sample|grep HADR<br /> HADR database role                                      = STANDBY<br /> HADR local host name                  (HADR_LOCAL_HOST) = db2-server2<br /> HADR local service name                (HADR_LOCAL_SVC) = 50011<br /> HADR remote host name                (HADR_REMOTE_HOST) = db2-server1<br /> HADR remote service name              (HADR_REMOTE_SVC) = 50010<br /> HADR instance name of remote server  (HADR_REMOTE_INST) = db2inst1<br /> HADR timeout value                       (HADR_TIMEOUT) = 120<br /> HADR target list                     (HADR_TARGET_LIST) = db2-server1:50010|db2-ec2:50012<br /> HADR log write synchronization mode     (HADR_SYNCMODE) = NEARSYNC<br /> HADR spool log data limit (4KB)      (HADR_SPOOL_LIMIT) = AUTOMATIC(52000)<br /> HADR log replay delay (seconds)     (HADR_REPLAY_DELAY) = 0<br /> HADR peer window duration (seconds)  (HADR_PEER_WINDOW) = 0<br /> HADR SSL certificate label             (HADR_SSL_LABEL) =<br /> HADR SSL Hostname Validation        (HADR_SSL_HOST_VAL) = OFF</pre><br />On `db2-ec2`, run the following code:<pre>db2 get db cfg for sample|grep HADR<br /> HADR database role                                      = STANDBY<br /> HADR local host name                  (HADR_LOCAL_HOST) = db2-ec2<br /> HADR local service name                (HADR_LOCAL_SVC) = 50012<br /> HADR remote host name                (HADR_REMOTE_HOST) = db2-server1<br /> HADR remote service name              (HADR_REMOTE_SVC) = 50010<br /> HADR instance name of remote server  (HADR_REMOTE_INST) = db2inst1<br /> HADR timeout value                       (HADR_TIMEOUT) = 120<br /> HADR target list                     (HADR_TARGET_LIST) = db2-server1:50010|db2-server2:50011<br /> HADR log write synchronization mode     (HADR_SYNCMODE) = SUPERASYNC<br /> HADR spool log data limit (4KB)      (HADR_SPOOL_LIMIT) = AUTOMATIC(52000)<br /> HADR log replay delay (seconds)     (HADR_REPLAY_DELAY) = 0<br /> HADR peer window duration (seconds)  (HADR_PEER_WINDOW) = 0<br /> HADR SSL certificate label             (HADR_SSL_LABEL) =<br /> HADR SSL Hostname Validation        (HADR_SSL_HOST_VAL) = OFF</pre><br />The `HADR_LOCAL_HOST`, `HADR_LOCAL_SVC`, `HADR_REMOTE_HOST`, `HADR_REMOTE_SVC`, and `HADR_TARGET_LIST` parameters indicate the one primary and two standby HADR setup. |  |
| Stop and start Db2 HADR. | `HADR_TARGET_LIST` is now set up on all three servers. Each Db2 server is aware of the other two. Stop and restart HADR (brief outage) to take advantage of the new configuration.<br />On `db2-server1`, run the following commands:<pre>db2 stop hadr on db sample<br />db2 deactivate db sample<br />db2 activate db sample</pre><br />On `db2-server2`, run the following commands:<pre>db2 deactivate db sample<br />db2 start hadr on db sample as standby<br />SQL1766W  The command completed successfully</pre><br />On `db2-ec2`, run the following commands:<pre>db2 start hadr on db sample as standby<br />SQL1766W  The command completed successfully</pre><br />On `db2-server1`, run the following commands:<pre>db2 start hadr on db sample as primary<br />SQL1766W  The command completed successfully</pre><br />The HADR connection between Db2 on premises and on Amazon EC2 is now successfully established. The Db2 primary server `db2-server1` starts streaming transaction log records to both `db2-server2` and `db2-ec2` in real time.  | DBA |

### Make Db2 on Amazon EC2 as primary during the cutover window
<a name="make-db2-on-amazon-ec2-as-primary-during-the-cutover-window"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Make sure that there is no HADR lag on the standby server. | Check HADR status from the primary server `db2-server1`. Don’t be alarmed when `HADR_STATE` is in `REMOTE_CATCHUP` status, which is normal when `HADR_SYNCMODE` is set to `SUPERASYNC`. The `PRIMARY_LOG_TIME` and `STANDBY_REPLAY_LOG_TIME` show that they are in sync:<pre>db2pd -hadr -db sample<br />                            HADR_ROLE = PRIMARY<br />                          REPLAY_TYPE = PHYSICAL<br />                        HADR_SYNCMODE = SUPERASYNC<br />                           STANDBY_ID = 2<br />                        LOG_STREAM_ID = 0<br />                           HADR_STATE = REMOTE_CATCHUP<br />.....<br />                     PRIMARY_LOG_TIME = 10/26/2022 02:11:32.000000 (1666750292)<br />                     STANDBY_LOG_TIME = 10/26/2022 02:11:32.000000 (1666750292)<br />              STANDBY_REPLAY_LOG_TIME = 10/26/2022 02:11:32.000000 (1666750292)</pre> | DBA |
| Run HADR takeover. | To complete the migration, make `db2-ec2` the primary database by running the HADR takeover command. Use the command `db2pd` to verify the `HADR_ROLE` value:<pre>db2 TAKEOVER HADR ON DATABASE sample<br />DB20000I  The TAKEOVER HADR ON DATABASE command completed successfully.<br /><br />db2pd -hadr -db sample<br />Database Member 0 -- Database SAMPLE -- Active -- Up 0 days 00:03:25 -- Date 2022-10-26-02.46.45.048988<br /><br />                            HADR_ROLE = PRIMARY<br />                          REPLAY_TYPE = PHYSICAL</pre><br />To complete the migration to AWS, point the application connections to Db2 on Amazon EC2. |  |

## Troubleshooting
<a name="migrate-db2-for-luw-to-amazon-ec2-with-high-availability-disaster-recovery-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| If you use NAT for firewall and security reasons, the host can have two IP addresses (one internal and one external), which can cause an HADR IP address check failure. The `START HADR ON DATABASE` command will return the following message:<br />`HADR_LOCAL_HOST:HADR_LOCAL_SVC (-xx-xx-xx-xx.:50011 (xx.xx.xx.xx:50011)) on remote database is different from HADR_REMOTE_HOST:HADR_REMOTE_SVC (xx-xx-xx-xx.:50011 (x.x.x.x:50011)) on local database.` | To [support HADR in a NAT environment,](https://www.ibm.com/docs/en/db2/11.5?topic=support-hadr-nat) you can configure the `HADR_LOCAL_HOST` with both the internal and external address. For example, if the Db2 server has the internal name `host1` and the external name `host1E`, `HADR_LOCAL_HOST` can be `HADR_LOCAL_HOST: "host1 \| host1E"`. |

## Related resources
<a name="migrate-db2-for-luw-to-amazon-ec2-with-high-availability-disaster-recovery-resources"></a>
+ [Db2 backup and restore operations between different operating systems and hardware platforms](https://www.ibm.com/docs/en/db2/11.5?topic=dbrs-backup-restore-operations-between-different-operating-systems-hardware-platforms)
+ [Set up Db2 STORAGE ACCESS ALIAS and DB2REMOTE](https://www.ibm.com/docs/en/db2/11.5?topic=commands-catalog-storage-access)
+ [Db2 high availability disaster recovery](https://www.ibm.com/docs/en/db2/11.5?topic=server-high-availability-disaster-recovery-hadr)
+ [hadr\_syncmode - HADR synchronization mode for log writes in peer state configuration parameter](https://www.ibm.com/docs/en/db2/11.5?topic=dcp-hadr-syncmode-hadr-synchronization-mode-log-writes-in-peer-state)
