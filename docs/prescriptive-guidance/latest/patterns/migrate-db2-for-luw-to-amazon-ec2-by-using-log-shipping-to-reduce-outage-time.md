---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/migrate-db2-for-luw-to-amazon-ec2-by-using-log-shipping-to-reduce-outage-time.html
---

# Migrate Db2 for LUW to Amazon EC2 by using log shipping to reduce outage time
<a name="migrate-db2-for-luw-to-amazon-ec2-by-using-log-shipping-to-reduce-outage-time"></a>

*Feng Cai, Ambarish Satarkar, and Saurabh Sharma, Amazon Web Services*

## Summary
<a name="migrate-db2-for-luw-to-amazon-ec2-by-using-log-shipping-to-reduce-outage-time-summary"></a>

When customers migrate their IBM Db2 for LUW (Linux, UNIX, and Windows) workloads to Amazon Web Services (AWS), using Amazon Elastic Compute Cloud (Amazon EC2) with the Bring Your Own License (BYOL) model is the fastest way. However, migrating large amounts of data from on-premises Db2 into AWS can be a challenge, especially when the outage window is short. Many customers try to set the outage window to less than 30 minutes, which leaves little time for the database itself.

This pattern covers how to accomplish a Db2 migration with a short outage window by using transaction log shipping. This approach applies to Db2 on a little-endian Linux platform.

## Prerequisites and limitations
<a name="migrate-db2-for-luw-to-amazon-ec2-by-using-log-shipping-to-reduce-outage-time-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ A Db2 instance running on EC2 instance that matches the on-premises file system layouts
+ An Amazon Simple Storage Service (Amazon S3) bucket accessible to the EC2 instance
+ An AWS Identity and Access Management (IAM) policy and role to make programmatic calls to Amazon S3
+ Synchronized time zone and system clocks on Amazon EC2 and the on-premises server
+ The on-premises network connected to AWS through [AWS Site-to-Site VPN](https://aws.amazon.com/vpn/) or [AWS Direct Connect](https://aws.amazon.com/directconnect/)

**Limitations**
+ The Db2 on-premises instance and Amazon EC2 must be on the same [platform family](https://www.ibm.com/docs/en/db2/11.1?topic=dbrs-backup-restore-operations-between-different-operating-systems-hardware-platforms).
+ The Db2 on-premises workload must be logged. To block any unlogged transaction, set `blocknonlogged=yes` in the database configuration.

**Product versions**
+ Db2 for LUW version 11.5.9 and later

## Architecture
<a name="migrate-db2-for-luw-to-amazon-ec2-by-using-log-shipping-to-reduce-outage-time-architecture"></a>

**Source technology stack**
+ Db2 on Linux** **x86\_64

** Target technology stack**
+ Amazon EBS
+ Amazon EC2
+ AWS Identity and Access Management (IAM)
+ Amazon S3
+ AWS Site-to-Site VPN or Direct Connect

**Target architecture**

The following diagram shows one Db2 instance running on-premises with a virtual private network (VPN) connection to Db2 on Amazon EC2. The dotted lines represent the VPN tunnel between your data center and the AWS Cloud.

![Workflow to accomplish a Db2 migration within short outage window using transaction log shipping.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7dec6e4a-a92e-4204-9e42-f89d7dcafbfa/images/a7e1c1d6-2ec1-4271-952d-a58260ad7c81.png)

## Tools
<a name="migrate-db2-for-luw-to-amazon-ec2-by-using-log-shipping-to-reduce-outage-time-tools"></a>

**AWS services**
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell.
+ [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html) links your internal network to a Direct Connect location over a standard Ethernet fiber-optic cable. With this connection, you can create virtual interfaces directly to public AWS services while bypassing internet service providers in your network path.
+ [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html) provides block-level storage volumes for use with Amazon Elastic Compute Cloud (Amazon EC2) instances.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS Site-to-Site VPN](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html) helps you pass traffic between instances that you launch on AWS and your own remote network.

**Other tools**
+ [db2cli](https://www.ibm.com/docs/en/db2/11.5?topic=commands-db2cli-db2-interactive-cli) is the Db2 interactive CLI command.

## Best practices
<a name="migrate-db2-for-luw-to-amazon-ec2-by-using-log-shipping-to-reduce-outage-time-best-practices"></a>
+ On the target database, use [gateway endpoints for Amazon S3](https://docs.aws.amazon.com/vpc/latest/privatelink/vpc-endpoints-s3.html) to access the database backup image and log files in Amazon S3.
+ On the source database, use [AWS PrivateLink for Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/privatelink-interface-endpoints.html) to send the database backup image and log files to Amazon S3.

## Epics
<a name="migrate-db2-for-luw-to-amazon-ec2-by-using-log-shipping-to-reduce-outage-time-epics"></a>

### Set environment variables
<a name="set-environment-variables"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set environment variables. | This pattern uses the following names:+ Instance name: `db2inst1`<br />+ Database name: `SAMPLE`<br />You can change them to fit your environment. | DBA |

### Configure the on-premises Db2 server
<a name="configure-the-on-premises-db2-server"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the AWS CLI. | To download and install the latest version of the AWS CLI, run the following commands:<pre>$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"<br />unzip awscliv2.zip<br />sudo ./aws/install</pre> | Linux administrator |
| Set up a local destination for Db2 archive logs. | To keep the target database on Amazon EC2 in sync with the on-premises source database, the latest transaction logs need be retrieved from the source.<br />In this setup, `/db2logs` is set by `LOGARCHMETH2` on the source as a staging area. The archived logs in this directory will be synced into Amazon S3 and accessed by Db2 on Amazon EC2. The pattern uses `LOGARCHMETH2` because `LOGARCHMETH1` might have been configured to use a third-party vendor tool that AWS CLI command cannot access. To retrieve the logs, run the following command: <pre>db2 connect to sample<br />db2 update db cfg for SAMPLE using LOGARCHMETH2 disk:/db2logs</pre> | DBA |
| Run an online database backup. | Run an online database backup, and save it to the local backup file system: <pre>db2 backup db sample online to /backup </pre> | DBA |

### Set up the S3 bucket and IAM policy
<a name="set-up-the-s3-bucket-and-iam-policy"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an S3 bucket. | Create an S3 bucket for the on-premises server to send the backup Db2 images and log files to on AWS. The bucket will also be accessed by Amazon EC2:<pre>aws s3api create-bucket --bucket logshipmig-db2 --region us-east-1 </pre> | AWS systems administrator |
|  Create an IAM policy. | The `db2bucket.json` file contains the IAM policy to access the Amazon S3 bucket:<pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Effect": "Allow",<br />            "Action": [<br />                "kms:GenerateDataKey",<br />                "kms:Decrypt",<br />                "s3:PutObject",<br />                "s3:GetObject",<br />                "s3:AbortMultipartUpload",<br />                "s3:ListBucket",<br />                "s3:DeleteObject",<br />                "s3:GetObjectVersion",<br />                "s3:ListMultipartUploadParts"<br />            ],<br />            "Resource": [<br />                "arn:aws:s3:::logshipmig-db2/*",<br />                "arn:aws:s3:::logshipmig-db2"<br />            ]<br />        }<br />    ]<br />}</pre><br />To create the policy, use the following AWS CLI command:<pre>aws iam create-policy \<br />      --policy-name db2s3policy \<br />      --policy-document file://db2bucket.json </pre><br /> The JSON output shows the Amazon Resource Name (ARN) for the policy, where `aws_account_id` represents your account ID:<pre>"Arn": "arn:aws:iam::aws_account_id:policy/db2s3policy"</pre> | AWS administrator, AWS systems administrator |
| Attach the IAM policy to the IAM role used by the EC2 instance. | In most AWS environments, a running EC2 instance has an IAM Role set by your systems administrator. If the IAM role is not set, create the role and choose **Modify IAM role** on the EC2 console to associate the role with the EC2 instance that hosts the Db2 database. Attach the IAM policy to the IAM role with the policy ARN:<pre>aws iam attach-role-policy \<br />    --policy-arn "arn:aws:iam::aws_account_id:policy/db2s3policy"  \<br />    --role-name db2s3role  </pre><br />After the policy is attached, any EC2 instance associated with the IAM role can access the S3 bucket. | AWS administrator, AWS systems administrator |

### Send the source database backup image and log files to Amazon S3
<a name="send-the-source-database-backup-image-and-log-files-to-amazon-s3"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure the AWS CLI on the on-premises Db2 server. | Configure the AWS CLI with the `Access Key ID` and `Secret Access Key` generated in the earlier step:<pre>$ aws configure <br />AWS Access Key ID [None]: *************<br />AWS Secret Access Key [None]: ***************************<br />Default region name [None]: us-east-1<br />Default output format [None]: json</pre><br />  | AWS administrator, AWS systems administrator |
| Send the backup image to Amazon S3. | Earlier, an online database backup was saved to the `/backup` local directory. To send that backup image to the S3 bucket, run the following command:<pre>aws s3 sync /backup s3://logshipmig-db2/SAMPLE_backup</pre> | AWS administrator, Migration engineer |
| Send the Db2 archive logs to Amazon S3. | Sync the on-premises Db2 archive logs with the S3 bucket that can be accessed by the target Db2 instance on Amazon EC2:<pre>aws s3 sync /db2logs s3://logshipmig-db2/SAMPLE_LOG</pre><br />Run this command periodically by using cron or other scheduling tools. The frequency depends on how often the source database archives transaction log files.  | AWS administrator, Migration engineer |

### Connect Db2 on Amazon EC2 to Amazon S3 and start the database sync
<a name="connect-db2-on-amazon-ec2-to-amazon-s3-and-start-the-database-sync"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a PKCS12 keystore. | Db2 uses a Public-Key Cryptography Standards (PKCS) encryption keystore to keep the AWS access key secure. Create a keystore and configure the source Db2 instance to use it:<pre>gsk8capicmd_64 -keydb -create -db "/home/db2inst1/.keystore/db2s3.p12" -pw "<password>" -type pkcs12 -stash <br /> <br />db2 "update dbm cfg using keystore_location /home/db2inst1/.keystore/db2s3.p12 keystore_type pkcs12"</pre> | DBA |
| Create the Db2 storage access alias. | To create the [storage access alias](https://www.ibm.com/docs/en/db2/11.5?topic=commands-catalog-storage-access), use the following script syntax:<br />`db2 "catalog storage access alias <alias_name> vendor S3 server <S3 endpoint> container '<bucket_name>'"`<br />For example, your script might look like the following: <br />`db2 "catalog storage access alias DB2AWSS3 vendor S3 server s3.us-east-1.amazonaws.com container 'logshipmig-db2'" ` | DBA |
| Set the staging area. | By default, Db2 uses `DB2_OBJECT_STORAGE_LOCAL_STAGING_PATH` as the staging area to upload and download files to and from Amazon S3. The default path is `sqllib/tmp/RemoteStorage.xxxx` under the instance home directory, with `xxxx` referring to the Db2 partition number. Note that the staging area must have enough capacity to hold the backup images and log files. You can use the registry to point the staging area into a different directory.<br />We also recommend using `DB2_ENABLE_COS_SDK=ON`, `DB2_OBJECT_STORAGE_SETTINGS=EnableStreamingRestore`, and the link to the `awssdk` library to bypass the Amazon S3 staging area for database backup and restore:<pre>#By root:<br />cp -rp /home/db2inst1/sqllib/lib64/awssdk/RHEL/7.6/* /home/db2inst1/sqllib/lib64/<br /><br />#By db2 instance owner:<br />db2set DB2_OBJECT_STORAGE_LOCAL_STAGING_PATH=/db2stage<br />db2set DB2_ENABLE_COS_SDK=ON<br />Db2set DB2_OBJECT_STORAGE_SETTINGS=EnableStreamingRestore<br />db2stop<br />db2start</pre> | DBA |
| Restore the database from the backup image. | Restore the target database on Amazon EC2 from the backup image in the S3 bucket:<pre>db2 restore db sample from DB2REMOTE://DB2AWSS3/logshipmig-db2/SAMPLE_backup replace existing</pre> | DBA |
| Roll forward the database. | After the restore is complete, the target database will be put into rollforward pending state. Configure `LOGARCHMETH1` and `LOGARCHMETH2` so that Db2 knows where to get the transaction log files:<pre>db2 update db cfg for SAMPLE using LOGARCHMETH1 'DB2REMOTE://DB2AWSS3//SAMPLE_LOGS/'<br />db2 update db cfg for SAMPLE using LOGARCHMETH2 OFF</pre><br />Start database rollforward:<pre>db2 ROLLFORWARD DATABASE sample to END OF LOGS</pre><br />This command processes all log files that have been transferred to the S3 bucket. Run it periodically based on the frequency of the `s3 sync` command on the on-premises Db2 servers. For example, if `s3 sync` runs at each hour, and it takes 10 minutes to sync all the log files, set the command to run at 10 minutes after each hour.  | DBA |

### Bring Db2 on Amazon EC2 online during the cutover window
<a name="bring-db2-on-amazon-ec2-online-during-the-cutover-window"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Bring the target database online. | During the cutover window, do one of the following:+ Put the on-premises database in `ADMIN MODE`, and run the `s3 sync` command to force the last transaction log to be archived.<br />+ Shut down the database.<br />After the last transaction log is synced into Amazon S3, run the `ROLLFORWARD` command for the final time:<pre>db2 rollforward DB sample to END OF LOGS<br />db2 rollforward DB sample complete<br /><br />                                 Rollforward Status<br />....<br /> Rollforward status                     = not pending<br />....<br />DB20000I  The ROLLFORWARD command completed successfully.<br /><br />db2 activate db sample<br />DB20000I  The ACTIVATE DATABASE command completed successfully.</pre><br />Bring the target database online, and point the application connections to Db2 on Amazon EC2. | DBA |

## Troubleshooting
<a name="migrate-db2-for-luw-to-amazon-ec2-by-using-log-shipping-to-reduce-outage-time-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| If multiple databases have the same instance name and database name on different hosts (DEV, QA, PROD), backups and logs might go to the same subdirectory. | Use different S3 buckets for DEV, QA, and PROD, and add the hostname as subdirectory prefix to avoid confusion. |
| If there are multiple backup images in the same location, you will get the following error when you restore:<br />`SQL2522N More than one backup file matches the time stamp value provided for the backed up database image.` | In the `restore` command, add the timestamp of the backup:<br />`db2 restore db sample from DB2REMOTE://DB2AWSS3/logshipmig-db2/SAMPLE_backup taken at 20230628164042 replace existing` |

## Related resources
<a name="migrate-db2-for-luw-to-amazon-ec2-by-using-log-shipping-to-reduce-outage-time-resources"></a>
+ [Db2 backup and restore operations between different operating systems and hardware platforms](https://www.ibm.com/docs/en/db2/11.5?topic=dbrs-backup-restore-operations-between-different-operating-systems-hardware-platforms)
+ [Set up Db2 STORAGE ACCESS ALIAS and DB2REMOTE](https://www.ibm.com/docs/en/db2/11.5?topic=commands-catalog-storage-access)
+ [Db2 ROLLFORWARD command](https://www.ibm.com/docs/en/db2/11.5?topic=commands-rollforward-database)
+ [Db2 secondary log archive method](https://www.ibm.com/docs/en/db2/11.5?topic=parameters-logarchmeth2-secondary-log-archive-method)
