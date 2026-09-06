---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-sap-cost-optimization/storage-optimization-services.html
---

# Storage optimization services
<a name="storage-optimization-services"></a>

With storage, you must balance performance against cost. This section contains several recommendations for potential storage configurations, based on HANA and the size of the instance selected.

This section contains the following services and tools:
+ [Logical Volume Manager](#logical-volume-manager)
+ [Amazon S3 lifecycle policy](#s3-lifecycle-policy)
+ [Amazon EBS volumes](#ebs-volumes)
+ [Amazon EFS lifecycle policy](#efs-lifecycle-policy)

## Logical Volume Manager
<a name="logical-volume-manager"></a>

In some cases, you might want to use Logical Volume Manager and combine (also known as *stripe*) several disks in order to provide the target input/output operations per second (IOPS) and throughput. This configuration is typically more cost advantageous than a single volume of a higher class. However, this approach can lead to some additional unused space that you should balance against size and cost considerations.

## Amazon S3 lifecycle policy
<a name="s3-lifecycle-policy"></a>

You can use [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) buckets for long-term and short-term storage of SAP database backups. This helps you balance costs against the need for access and resiliency. Configuring lifecycle policies automates the retention policy for your backup files. Within the lifecycle policy, you can set up transitions from one Amazon S3 storage class to a lower-cost storage class for backups that require long-term retention.

As part of your cost optimization strategy, this automation provides the necessary rules to keep your Amazon S3 costs aligned to your specific retention needs. Review these automations on a periodic schedule to confirm that the configuration is optimized and the contents of the S3 buckets adhere to the expected configuration rules.

## Amazon EBS volumes
<a name="ebs-volumes"></a>

[Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html) volumes are used to store your persistent data such as the operating system, SAP binary files and your SAP database files. The sizing of these volumes is critical when balanced with cost optimization. It is extremely easy to increase the size of a volume, therefore you should provision volumes with enough room to hold the actual volume of data plus a small percent to accommodate growth. Right sizing overprovisioned volumes can be labor intensive and require planned downtime. If this is where a large percentage of your spend is occurring though it will make sense to embark on such an activity.

As part of your cost optimization strategy the review of overprovisioned EBS volumes should be conducted every other review cycle. If there are continuous opportunities in this particular area automation can be developed to alleviate some of the manual effort involved.

## Amazon EFS lifecycle policy
<a name="efs-lifecycle-policy"></a>

[Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) automatically scales storage as files are added or removed. In SAP environments, this is typically used as your transport, interface, and cluster file systems. In addition, you might use it to temporarily store software for active projects. Although, in the long-term, it is recommended that you store software in an S3 bucket.

For SAP interface file systems, consider configuring an [EFS lifecycle policy](https://docs.aws.amazon.com/efs/latest/ug/lifecycle-management-efs.html). With lifecycle policies, you can reduce storage costs by transitioning files with specific retention requirements to a lower-cost storage class. If you use the industry-accepted estimate, 80% of your data is infrequently accessed. Moving this data to lower-cost storage classes is a prime opportunity to reduce your costs. For more information, see [Amazon EFS Infrequent Access](https://aws.amazon.com/efs/features/infrequent-access/).

As part of your cost optimization strategy, review EFS lifecycle policies every other review cycle. If there are continuous opportunities, enable EFS lifecycle policies to automate the process and implement a clean-up routine.
