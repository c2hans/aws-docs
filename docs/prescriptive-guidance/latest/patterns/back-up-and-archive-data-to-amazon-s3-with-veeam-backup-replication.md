---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/back-up-and-archive-data-to-amazon-s3-with-veeam-backup-replication.html
---

# Back up and archive data to Amazon S3 with Veeam Backup & Replication
<a name="back-up-and-archive-data-to-amazon-s3-with-veeam-backup-replication"></a>

*Jeanna James, Anthony Fiore (AWS), and William Quigley, Amazon Web Services*

## Summary
<a name="back-up-and-archive-data-to-amazon-s3-with-veeam-backup-replication-summary"></a>

This pattern details the process for sending backups created by Veeam Backup & Replication to supported Amazon Simple Storage Service (Amazon S3) object storage classes by using the Veeam scale-out backup repository capability.

Veeam supports multiple Amazon S3 storage classes to best fit your specific needs. You can choose the type of storage based on the data access, resiliency, and cost requirements of your backup or archive data. For example, you can store data that you don’t plan to use for 30 days or longer in Amazon S3 infrequent access (IA) for lower cost. If you’re planning to archive data for 90 days or longer, you can use S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive with Veeam’s archive tier. You can also use S3 Object Lock to make backups that are immutable within Amazon S3.

This pattern doesn’t cover how to set up Veeam Backup & Replication with a tape gateway in AWS Storage Gateway. For information about that topic, see [Veeam Backup & Replication using AWS VTL Gateway - Deployment Guide](https://www.veeam.com/resources/wp-using-aws-vtl-gateway-deployment-guide.html) on the Veeam website.

|
|
| Warning: This scenario requires AWS Identity and Access Management (IAM) users with programmatic access and long-term credentials, which present a security risk. To help mitigate this risk, we recommend that you provide these users with only the permissions they require to perform the task and that you remove these users when they are no longer needed. Access keys can be updated if necessary. For more information, see [Updating access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html#Using_RotateAccessKey) in the *IAM User Guide*. |
| --- |

## Prerequisites and limitations
<a name="back-up-and-archive-data-to-amazon-s3-with-veeam-backup-replication-prereqs"></a>

**Prerequisites**
+ Veeam Backup & Replication, including Veeam Availability Suite or Veeam Backup Essentials, installed (you can register for a [free trial](https://www.veeam.com/backup-replication-virtual-physical-cloud.html))
+ Veeam Backup & Replication license with Enterprise or Enterprise Plus functionality, which includes Veeam Universal License (VUL)
+ An active IAM user with access to an Amazon S3 bucket
+ An active IAM user with access to Amazon Elastic Compute Cloud (Amazon EC2) and Amazon Virtual Private Cloud (Amazon VPC), if using archive tier
+ Network connectivity from on premises to AWS services with available bandwidth for backup and restore traffic through a public internet connection or an AWS Direct Connect public virtual interface (VIF)
+ The following network ports and endpoints opened to ensure proper communication with object storage repositories:
  + Amazon S3 storage – TCP – port 443: Used to communicate with Amazon S3 storage.
  + Amazon S3 storage – cloud endpoints – `*.amazonaws.com` for AWS Regions and the AWS GovCloud (US) Regions, or `*.amazonaws.com.cn` for China Regions: Used to communicate with Amazon S3 storage. For a complete list of connection endpoints, see [Amazon S3 endpoints](https://docs.aws.amazon.com/general/latest/gr/s3.html#s3_region) in the AWS documentation.
  + Amazon S3 storage – TCP HTTP – port 80: Used to verify certificate status. Consider that certificate verification endpoints—certificate revocation list (CRL) URLs and Online Certificate Status Protocol (OCSP) servers—are subject to change. The actual list of addresses can be found in the certificate itself.
  + Amazon S3 storage – certificate verification endpoints – `*.amazontrust.com`: Used to verify certificate status. Consider that certificate verification endpoints (CRL URLs and OCSP servers) are subject to change. The actual list of addresses can be found in the certificate itself.

**Limitations**
+ Veeam doesn’t support S3 Lifecycle policies on any S3 buckets that are used as Veeam object storage repositories. These include polices with Amazon S3 storage class transitions and S3 Lifecycle expiration rules. Veeam **must** be the sole entity that manages these objects. Enabling S3 Lifecycle policies might have unexpected results, including data loss.

**Product versions**
+ Veeam Backup & Replication v9.5 Update 4 or later (backup only or capacity tier)
+ Veeam Backup & Replication v10 or later (backup or capacity tier and S3 Object Lock)
+ Veeam Backup & Replication v11 or later (backup or capacity tier, archive or archive tier, and S3 Object Lock)
+ Veeam Backup & Replication v12 or later (performance tier, backup or capacity tier, archive or archive tier, and S3 Object Lock)
+ S3 Standard
+ S3 Standard-IA
+ S3 One Zone-IA
+ S3 Glacier Flexible Retrieval (v11 and later only)
+ S3 Glacier Deep Archive (v11 and later only)
+ S3 Glacier Instant Retrieval (v12 and later only)

## Architecture
<a name="back-up-and-archive-data-to-amazon-s3-with-veeam-backup-replication-architecture"></a>

**Source technology stack**
+ On-premises Veeam Backup & Replication installation with connectivity from a Veeam backup server or a Veeam gateway server to Amazon S3

**Target technology stack  **
+ Amazon S3
+ Amazon VPC and Amazon EC2 (if using archive tier)

**Target architecture: SOBR **

The following diagram shows the scale-out backup repository (SOBR) architecture.

![SOBR architecture for backing up data from Veeam to Amazon S3](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7f3a36f7-31dc-45c8-87b2-c5dd37f7a01e/images/b48fd0cd-b66c-4ef7-b6fa-0ed53354e1a2.png)

Veeam Backup and Replication software protects data from logical errors such as system failures, application errors, or accidental deletion. In this diagram, backups are run on premises first, and a secondary copy is sent directly to Amazon S3. A backup represents a point-in-time copy of the data.

The workflow consists of three primary components that are required for tiering or copying backups to Amazon S3, and one optional component:
+ Veeam Backup & Replication (1) – The backup server that is responsible for coordinating, controlling, and managing backup infrastructure, settings, jobs, recovery tasks, and other processes.
+ Veeam gateway server (not shown in the diagram) – An optional on-premises gateway server that is required if the Veeam backup server doesn’t have outbound connectivity to Amazon S3.
+ Scale-out backup repository (2) – Repository system with horizontal scaling support for multi-tier storage of data. The scale-out backup repository consists of one or more backup repositories that provide fast access to data and can be expanded with Amazon S3 object storage repositories for long-term storage (capacity tier) and archiving (archive tier). Veeam uses the scale-out backup repository to tier data automatically between local (performance tier) and Amazon S3 object storage (capacity and archive tiers).
**Note**
Starting with Veeam Backup & Replication v12.2, the Direct to S3 Glacier feature makes the S3 capacity tier optional. A SOBR can be configured with a performance tier and an S3 Glacier archive tier. This configuration is useful for users who have significant investments in local (on-premises) storage for the capacity tier and who require only long-term archive retention in the cloud. For more information, see the [Veeam Backup & Replication documentation](https://helpcenter.veeam.com/docs/backup/vsphere/archive_tier.html?ver=120).
+ Amazon S3 (3) – AWS object storage service that offers scalability, data availability, security, and performance.

**Target architecture: DTO**

The following diagram shows the direct-to-object (DTO) architecture.

![DTO architecture for backing up data from Veeam to Amazon S3](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7f3a36f7-31dc-45c8-87b2-c5dd37f7a01e/images/9debe53a-d70a-43fa-844c-f93fa22124eb.png)

In this diagram, backup data goes directly to Amazon S3 without being stored on premises first. Secondary copies can be stored in S3 Glacier.

**Automation and scale**

You can automate the creation of IAM resources and S3 buckets by using the CloudFormation templates provided in the [VeeamHub GitHub repository](https://github.com/VeeamHub/veeam-aws-cloudformation/tree/master/veeam-backup-and-replication). The templates include both standard and immutable options.

## Tools
<a name="back-up-and-archive-data-to-amazon-s3-with-veeam-backup-replication-tools"></a>

**Tools and AWS services**
+ [Veeam Backup & Replication](https://www.veeam.com/vm-backup-recovery-replication-software.html) is a solution from Veeam for protecting, backing up, replicating, and restoring your virtual and physical workloads.
+ [CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you model and set up your AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle. You can use a template to describe your resources and their dependencies, and launch and configure them together as a stack, instead of managing resources individually. You can manage and provision stacks across multiple AWS accounts and AWS Regions.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/ec2/) provides scalable computing capacity in the AWS Cloud. You can use Amazon EC2 to launch as many or as few virtual servers as you need, and you can scale out or scale in.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) is a web service for securely controlling access to AWS services. With IAM, you can centrally manage users, security credentials such as access keys, and permissions that control which AWS resources users and applications can access.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is an object storage service. You can use Amazon S3 to store and retrieve any amount of data at any time, from anywhere on the web.
+ [Amazon S3 Glacier (S3 Glacier)](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html) is a secure and durable service for low-cost data archiving and long-term backup.
+ [Amazon Virtual Private Cloud (Amazon VPC)](https://docs.aws.amazon.com/vpc/) provisions a logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you've defined. This virtual network closely resembles a traditional network that you'd operate in your own data center, with the benefits of using the scalable infrastructure of AWS.

**Code **

Use the CloudFormation templates provided in the [VeeamHub GitHub repository](https://github.com/VeeamHub/veeam-aws-cloudformation/tree/master/veeam-backup-and-replication) to automatically create the IAM resources and S3 buckets for this pattern. If you prefer to create these resources manually, follow the steps in the *Epics* section.

## Best practices
<a name="back-up-and-archive-data-to-amazon-s3-with-veeam-backup-replication-best-practices"></a>

In accordance with IAM best practices, we strongly recommend that you regularly rotate long-term IAM user credentials, such as the IAM user that you use for writing Veeam Backup & Replication backups to Amazon S3. For more information, see [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#rotate-credentials) in the IAM documentation.

## Epics
<a name="back-up-and-archive-data-to-amazon-s3-with-veeam-backup-replication-epics"></a>

### Configure Amazon S3 storage in your account
<a name="configure-s3-storage-in-your-account"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an IAM user. | Follow the [instructions in the IAM documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) to create an IAM user. This user should not have AWS console access, and you will need to create an access key for this user. Veeam uses this entity to authenticate with AWS to read and write to your S3 buckets. You must grant least privilege (that is, grant only the permissions required to perform a task) so the user doesn’t have more authority than it needs. For example IAM policies to attach to your Veeam IAM user, see the [Additional information](#back-up-and-archive-data-to-amazon-s3-with-veeam-backup-replication-additional) section.Alternatively, you can use the CloudFormation templates provided in the [VeeamHub GitHub repository](https://github.com/VeeamHub/veeam-aws-cloudformation/tree/master/veeam-backup-and-replication) to create an IAM user and S3 bucket for this pattern. | AWS administrator |
| Create an S3 bucket. | 1. Sign in to the AWS Management Console and open the [Amazon S3 console](https://console.aws.amazon.com/s3/). <br />2. If you don't already have an existing S3 bucket to use as the target storage, choose **Create bucket**, and specify a bucket name, AWS Region, and bucket settings.We recommend that you enable the [Block Public Access option](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html) for the S3 bucket and set up the access and user permission policies to meet your organization's requirements. For an example, see the [Amazon S3documentation](https://docs.aws.amazon.com/AmazonS3/latest/userguide/example-walkthroughs-managing-access-example1.html).We recommend that you enable [S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html), even if you don’t intend to use it right away. This setting can be enabled only at the time of S3 bucket creation.For more information, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) in the Amazon S3 documentation. | AWS administrator |

### Add Amazon S3 and S3 Glacier Flexible Retrieval (or S3 Glacier Deep Archive) to Veeam Backup & Replication
<a name="add-s3-and-s3-storage-class-glacier-or-s3-storage-class-deep-archive-to-veeam-backup-amp-replication"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Launch the New Object Repository wizard. | Before you set up the object storage and scale-out backup repositories in Veeam, you must add the Amazon S3 and S3 Glacier storage repositories that you want to use for the capacity and archive tiers. In the next epic, you’ll connect these storage repositories to your scale-out backup repository.1. On the Veeam console, open the **Backup Infrastructure** view. <br />2. In the inventory pane, choose the **Backup Repositories** node, and then choose **Add Repository**. <br />3. In the **Add Backup Repository** dialog box, choose **Object Storage**, **Amazon S3**. | AWS administrator, App owner |
| Add Amazon S3 storage for the capacity tier. | 1. In the **Amazon Cloud Storage Services** dialog box, choose **Amazon S3**.<br />2. At the **Name** step of the wizard, specify the object storage name and a brief description, such as the creator and creation date. <br />3. At the **Account **step of the wizard, specify the object storage account. For **Credentials**, choose the IAM user that you created in the first epic to access your Amazon S3 object storage. For **AWS region**, choose the AWS Region where the S3 bucket is located.<br />4. At the **Bucket **step of the wizard, specify object storage settings.For **Data center region**, choose the AWS Region where the S3 bucket is located.For **Bucket**, choose the S3 bucket that you created in the first epic.For **Folder**, create or select a cloud folder to map your object storage repository to. If you want to enable immutability, choose **Make recent backups immutable for X days **and set the period of time during which your backups should be locked. Note that enabling immutability results in increased costs because of the increased number of API calls to Amazon S3 from Veeam.<br />5. At the **Summary** step of the wizard, review the configuration information, and then choose **Finish**. | AWS administrator, App owner |
| Add S3 Glacier storage for the archive tier. | If you want to create an archive tier, use the IAM permissions detailed in the [Additional information](#back-up-and-archive-data-to-amazon-s3-with-veeam-backup-replication-additional) section. 1. Launch the New Object Repository wizard as described previously.<br />2. In the **Amazon Cloud Storage Services** dialog box, choose **Amazon S3 Glacier**.<br />3. At the **Name** step of the wizard, specify the object storage name and a brief description, such as the creator and creation date.<br />4. At the **Account **step of the wizard, specify the object storage account.For **Credentials**, choose the IAM user that you created in the first epic to access your S3 Glacier object storage. For **AWS region**, choose the AWS Region where the S3 bucket is located.<br />5. At the **Bucket **step of the wizard, specify object storage settings.For **Data center region**, choose the AWS Region.For **Bucket**, choose an S3 bucket to store your backup data. This can be the same bucket you used for the capacity tier.For **Folder**, create or select a cloud folder to map your object storage repository to. If you want to enable immutability, choose **Make recent backups immutable for the entire duration of their retention policy**. Note that enabling immutability results in increased costs because of the increased number of API calls to Amazon S3 from Veeam.If you want to use S3 Glacier Deep Archive as your archival storage class, choose **Use the Deep Archive Storage Class**.<br />6. At the **Proxy Appliance **step of the wizard,  configure the auxiliary instance that is used to transfer the data from Amazon S3 to S3 Glacier. You can use the default settings or configure each setting manually. To configure the settings manually:Choose** Customize**.For ** EC2 instance type**, choose the instance type for the proxy appliance, based on your speed and cost requirements for transferring the backup files to the archive tier of your scale-out backup repository.For **Amazon VPC**, choose the VPC for the target instance.For **Subnet**, choose the subnet for the proxy appliance.For **Security group**, choose the security group to associate with the proxy appliance.For **Redirector port**, specify the TCP port for routing requests between the proxy appliance and backup infrastructure components.Choose **OK** to confirm your settings.<br />7. At the **Summary** step of the wizard, review the configuration information, and then choose **Finish**. | AWS administrator, App owner |

### Add scale-out backup repositories
<a name="add-scale-out-backup-repositories"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Launch the New Scale-Out Backup Repository wizard. | 1. On the Veeam console, open the **Backup Infrastructure** view. <br />2. In the inventory pane, choose **Scale-out Repositories,** and then choose **Add Scale-out Repository**. | App owner, AWS systems administrator |
| Add a scale-out backup repository and configure capacity and archive tiers. | 1. At the **Name** step of the wizard, specify the name and a brief description of the scale-out backup repository. <br />2. If needed, add performance extents. You can also use your existing Veeam local backup repository as your performance tier. Starting with Veeam version 12, you can add an S3 bucket as a performance extent for direct-to-object (DTO) backups, bypassing a local performance tier.<br />3. Choose **Advanced**, and specify additional options for the scale-out backup repository.Choose **Use per-machine backup files** to create a separate backup file for each machine and write these files to the backup repository in multiple streams simultaneously. This option is recommended for better storage and compute resource utilization.Choose **Perform full backup when required extent is offline** to create a full backup file in case an extent that contains restore points for an  incremental backup goes offline. This option requires free space in the scale-out backup repository to host a full backup file.<br />4. At the **Policy **step of the wizard, specify the backup placement policy for the repository. Choose **Data locality** to store full and incremental backup files that belong to the same chain together, to the same performance extent. You can store files that belong to a new backup chain to the same performance extent or to another one (unless you use a deduplicating storage appliance as a performance extent).Choose **Performance** to store full and incremental backup files to different performance extents. This option requires a fast and reliable network connection. If you choose **Performance**, you can restrict the types of backup files to store on each performance extent. For example, you can store full backup files on one extent and incremental backup files on other extents. To choose file types:Choose **Customize**.In the **Backup Placement Settings** dialog box, choose a performance extent, and then choose **Edit**.Choose the type of backup files you want to store on the extent.<br />5. At the **Capacity Tier **step of the wizard, configure the long-term storage tier that you want to attach to the scale-out backup repository.  Choose **Extend scale-out backup repository capacity with object storage**. For the object storage repository, choose the Amazon S3 storage for the capacity tier that you added in the previous epic.Choose **Window** to select a time window for moving or copying data.Choose **Copy backups to object storage as soon as they are created** to copy all or only recently created backup files to the capacity extent. Choose **Move backups to object storage as they age out of the operational restores window** to transfer inactive backup chains to the capacity extent. In the **Move backup files older than X days** field, specify a duration after which backup files should be offloaded. (To offload inactive backup chains on the day they were created, specify 0 days.) You can also choose **Override** to move backup files sooner if the scale-out backup repository has reached a threshold that you specify.Choose **Encrypt data uploaded to object storage** and specify a password to encrypt all data and their metadata for offloading. Choose **Add** or **Manage passwords** to specify a new password.<br />6. At the **Archive Tier **step of the wizard, configure the archive storage tier that you want to attach to the scale-out backup repository. (This step doesn’t appear if you skipped adding Amazon S3 Glacier storage.) Choose **Archive GFS full backups to object storage**. For the object storage repository, choose the Amazon Glacier storage you added in the previous epic.For **Archive GFS backups older than N days**, choose a time window for moving files to the archive extent. (To archive inactive backup chains on the day they were created, specify 0 days.)<br />7. At the **Summary** step of the wizard, review the configuration of the scale-out backup repository, and then choose **Finish**. | App owner, AWS systems administrator |

## Related resources
<a name="back-up-and-archive-data-to-amazon-s3-with-veeam-backup-replication-resources"></a>
+ [Creating an IAM user in your AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html) (IAM documentation)
+ [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) (Amazon S3 documentation)
+ [Blocking public access to your Amazon S3 storage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html) (Amazon S3 documentation)
+ [Using S3 Object Lock](https://docs.aws.amazon.com/AmazonS3/latest/userguide/object-lock.html) (Amazon S3 documentation)
+ [Veeam technical documentation](https://www.veeam.com/documentation-guides-datasheets.html)
+ [How to Create Secure IAM Policy for Connection to S3 Object Storage](https://www.veeam.com/kb3151) (Veeam documentation)

## Additional information
<a name="back-up-and-archive-data-to-amazon-s3-with-veeam-backup-replication-additional"></a>

The following sections provide sample IAM policies you can use when you create an IAM user in the [Epics](#back-up-and-archive-data-to-amazon-s3-with-veeam-backup-replication-epics) section of this pattern.

**IAM policy for capacity tier**

**Note**
Change the name of the S3 buckets in the example policy from `<yourbucketname>` to the name of the S3 bucket that you want to use for Veeam capacity tier backups. Also note that the policy should be restricted to the specific resources used for Veeam (indicated by the `Resource` specification in the following policy), and that the first part of the policy disables client-side encryption, as discussed in the AWS blog post [Preventing unintended encryption of Amazon S3 objects](https://aws.amazon.com/blogs/security/preventing-unintended-encryption-of-amazon-s3-objects/).

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "RestrictSSECObjectUploads",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:PutObject",
            "Resource": "arn:aws:s3:::<your-bucket-name>/*",
            "Condition": {
                "Null": {
                    "s3:x-amz-server-side-encryption-customer-algorithm": "false"
                }
            }
        },
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "s3:GetObjectVersion",
                "s3:ListBucketVersions",
                "s3:ListBucket",
                "s3:PutObjectLegalHold",
                "s3:GetBucketVersioning",
                "s3:GetObjectLegalHold",
                "s3:GetBucketObjectLockConfiguration",
                "s3:PutObject*",
                "s3:GetObject*",
                "s3:GetEncryptionConfiguration",
                "s3:PutObjectRetention",
                "s3:PutBucketObjectLockConfiguration",
                "s3:DeleteObject*",
                "s3:DeleteObjectVersion",
                "s3:GetBucketLocation"

            ],
            "Resource": [
                "arn:aws:s3:::<yourbucketname>",
                "arn:aws:s3:::<yourbucketname>/*"
            ]
        },
        {
            "Sid": "VisualEditor1",
            "Effect": "Allow",
            "Action": [
                "s3:ListAllMyBuckets",
                "s3:ListBucket"
            ],
            "Resource": "arn:aws:s3:::*"
        }
    ]
}
```

**IAM policy for archive tier**

**Note**
 Change the name of the S3 buckets in the example policy from `<yourbucketname>` to the name of the S3 bucket that you want to use for Veeam archive tier backups.

**To use your existing VPC, subnet, and security groups:**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "S3Permissions",
            "Effect": "Allow",
            "Action": [
                "s3:DeleteObject",
                "s3:PutObject",
                "s3:GetObject",
                "s3:RestoreObject",
                "s3:ListBucket",
                "s3:AbortMultipartUpload",
                "s3:GetBucketVersioning",
                "s3:ListAllMyBuckets",
                "s3:GetBucketLocation",
                "s3:GetBucketObjectLockConfiguration",
                "s3:PutObjectRetention",
                "s3:GetObjectVersion",
                "s3:PutObjectLegalHold",
                "s3:GetObjectRetention",
                "s3:DeleteObjectVersion",
                "s3:ListBucketVersions"
            ],
            "Resource": [
                "arn:aws:s3:::<bucket-name>",
                "arn:aws:s3:::<bucket-name>/*"
            ]
        }
    ]
}

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EC2Permissions",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstances",
                "ec2:CreateKeyPair",
                "ec2:DescribeKeyPairs",
                "ec2:RunInstances",
                "ec2:DeleteKeyPair",
                "ec2:DescribeVpcAttribute",
                "ec2:CreateTags",
                "ec2:DescribeSubnets",
                "ec2:TerminateInstances",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeImages",
                "ec2:DescribeVpcs"
            ],
            "Resource": "arn:aws:ec2:<region>:<account-id>:*"
        }
    ]
}
```

**To create new VPC, subnet, and security groups:**

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "S3Permissions",
            "Effect": "Allow",
            "Action": [
                "s3:DeleteObject",
                "s3:PutObject",
                "s3:GetObject",
                "s3:RestoreObject",
                "s3:ListBucket",
                "s3:AbortMultipartUpload",
                "s3:GetBucketVersioning",
                "s3:ListAllMyBuckets",
                "s3:GetBucketLocation",
                "s3:GetBucketObjectLockConfiguration",
                "s3:PutObjectRetention",
                "s3:GetObjectVersion",
                "s3:PutObjectLegalHold",
                "s3:GetObjectRetention",
                "s3:DeleteObjectVersion",
                "s3:ListBucketVersions"
            ],
            "Resource": [
                "arn:aws:s3:::<bucket-name>",
                "arn:aws:s3:::<bucket-name>/*"
            ]
        }
    ]
}

{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "EC2Permissions",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstances",
                "ec2:CreateKeyPair",
                "ec2:DescribeKeyPairs",
                "ec2:RunInstances",
                "ec2:DeleteKeyPair",
                "ec2:DescribeVpcAttribute",
                "ec2:CreateTags",
                "ec2:DescribeSubnets",
                "ec2:TerminateInstances",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeImages",
                "ec2:DescribeVpcs",
                "ec2:CreateVpc",
                "ec2:CreateSubnet",
                "ec2:DescribeAvailabilityZones",
                "ec2:CreateRoute",
                "ec2:CreateInternetGateway",
                "ec2:AttachInternetGateway",
                "ec2:ModifyVpcAttribute",
                "ec2:CreateSecurityGroup",
                "ec2:DeleteSecurityGroup",
                "ec2:AuthorizeSecurityGroupIngress",
                "ec2:AuthorizeSecurityGroupEgress",
                "ec2:DescribeRouteTables",
                "ec2:DescribeInstanceTypes"
            ],
            "Resource": "*"
        }
    ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
