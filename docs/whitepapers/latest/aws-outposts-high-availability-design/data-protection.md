---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/data-protection.html
---

# Data protection
<a name="data-protection"></a>

 **For EBS Volumes:** AWS Outposts rack supports EBS volume snapshots to provide a simple and secure data protection mechanism to protect your block storage data. Snapshots are point-in-time incremental backups of your EBS volumes. By default, [snapshots of Amazon EBS volumes](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSSnapshots.html) on your Outpost are stored on Amazon S3 in the Region. If your Outposts have been configured with S3 on Outposts capacity, you can use [EBS Local Snapshots on Outposts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/snapshots-outposts.html) to store snapshots locally on your Outpost using S3 on Outposts storage.

 **For S3 on Outposts buckets (data residency use cases):**
+ You can use [S3 Versioning on Outposts](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsManagingVersioning.html), to save all changes, and history of objects. When enabled, S3 Versioning saves multiple distinct copies of an object in the same bucket. You can use S3 Versioning to preserve, retrieve, and restore every version of every object stored in your Outposts buckets. S3 Versioning helps you recover from unintended user actions and application failures.
+ You can use [S3 Replication on Outposts](https://docs.aws.amazon.com/AmazonS3/latest/userguide/S3OutpostsReplication.html), to create and configure replication rules to automatically replicate your S3 objects to another Outpost, or to another bucket on the same Outpost. During replication, S3 on Outposts objects are sent over the customer's local gateway (LGW), and objects do not travel back to the AWS Region. S3 Replication on Outposts provides an easy and flexible way to automatically replicate data within a specific [data perimeter](https://aws.amazon.com/identity/data-perimeters-on-aws/) to address data redundancy and compliance requirements.

  S3 Replication on Outposts also provides detailed metrics and notifications to monitor the status of your object replication. You can monitor replication progress by tracking bytes pending, operations pending, and replication latency between your source and destination Outposts buckets using Amazon CloudWatch. You can also set up Amazon EventBridge rules to receive replication failure events to quickly diagnose and correct configuration issues. See the [Amazon S3 Replication on Outposts](https://www.youtube.com/watch?v=Rt7VoQie7R4) YouTube video for additional details on how to configure.
![Reference architecture diagram showing using Amazon EventBridge and Amazon CloudWatch](http://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/s3-on-outposts-ha.png)

**For S3 on Outposts buckets (non-data residency use cases) to AWS Regions:** You can use [AWS DataSync to automate Amazon S3 on Outposts](https://aws.amazon.com/blogs/storage/automate-data-synchronization-between-aws-outposts-racks-and-amazon-s3-with-aws-datasync/) data transfers between your Outpost and the Region. DataSync allows you to choose what to transfer, when to transfer, and how much bandwidth to use. Backing up your on-premises S3 on Outposts buckets to S3 buckets in the AWS Region allows you to leverage the 99.999999999% (11 9's) of data durability and additional storage tiers (Standard, Infrequent Access, and Glacier) for cost optimization available with the regional S3 service.

 **Instance replication:** You can use [use AWS Elastic Disaster Recovery (AWS DRS)](https://docs.aws.amazon.com/drs/latest/userguide/outposts.html) to replicate individual instances and attached block storage from on-premises systems to an Outpost, from an Outpost to the Region, from the Region to an Outpost, or from one Outpost to another Outpost. The [Architecting for Disaster Recovery on AWS Outposts Racks with AWS Elastic Disaster Recovery](https://aws.amazon.com/blogs/compute/architecting-for-disaster-recovery-on-aws-outposts-racks-with-aws-elastic-disaster-recovery/) blog post describes each of these scenarios and how to design a solution with AWS DRS.

![Diagram showing disaster recovery (DR) from an Outpost to the Region](http://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/images/page-43-dr-outpost-to-region.png)

 Using AWS Outposts rack as an AWS DRS destination (replication target) requires S3 on Outposts storage, which is used for the purpose of storing replicated Amazon EBS snapshots. S3 on Outposts storage is also required on the source Outposts for failback. The Outposts rack must be using Direct VPC Routing (DVR) to use AWS DRS. AWS DRS cannot be used to protect managed service instances on Outposts, it is only supported for disaster recovery of EC2 instances and their attached EBS volumes.

## Recommended practices for data protection:
<a name="recommended-practices-for-data-protection"></a>
+  Use EBS snapshots to create point-in-time backups of block storage volumes to Amazon S3 in the Region or S3 on Outposts.
+  Use S3 on Outposts object versioning to maintain multiple versions and history of your objects.
+  Use S3 Replication on Outposts to automatically replicate your object data to another Outpost.
+ For non-data residency use cases, use AWS DataSync to back up objects stored in S3 on Outpost to Amazon S3 in the Region.
+  Use AWS DRS to replicate instances between on-premises systems, logical Outposts, and the Region.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
