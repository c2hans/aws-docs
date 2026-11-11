---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/optimize-costs-microsoft-workloads/ebs-migrate-ebs-snapshots.html
---

# Modify Amazon EBS snapshots
<a name="ebs-migrate-ebs-snapshots"></a>

## Overview
<a name="ebs-migrate-ebs-snapshots-overview"></a>

Deleting volumes in [Amazon Elastic Block Store](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) (Amazon EBS) and managing the retention and archiving of snapshots are important aspects of controlling costs from the start. You can back up the data on your EBS volumes to Amazon Simple Storage Service (Amazon S3) by taking point-in-time snapshots. Snapshots are incremental backups, so they save only the blocks on the devices that changed after your most recent snapshot. This minimizes the time required to create the snapshot and saves on storage costs by not duplicating data. Each snapshot contains all the information that's required to restore your data (from when the snapshot was created) to a new EBS volume.

Charges for EBS snapshots are calculated by the gigabyte-month. You're billed for how large the snapshot is and how long you keep the snapshot. Pricing varies depending on the storage tier. For the [Standard tier](https://aws.amazon.com/ebs/pricing/), you're billed only for changed blocks that are stored. For the Archive tier, you're billed for all snapshot blocks that are stored. You're also billed for retrieving snapshots from the [Archive tier](https://aws.amazon.com/ebs/pricing/). The following are example scenarios for each storage tier:
+ **Standard tier** – You have a volume that's storing 100 GB of data. You're billed for the full 100 GB of data for the first snapshot (snap A). At the time of the next snapshot (snap B), you have 105 GB of data. You're then billed for only the additional 5 GB of storage for incremental snap B.
+ **Archive tier** – You archive snap B. The snapshot is then moved to the Archive tier, and you're billed for the full 105 GB snapshot block.

You can use [Amazon Data Lifecycle Manager](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-lifecycle.html) to set up a lifecycle policy that retains and manages your snapshots on a schedule.

## Cost impact
<a name="ebs-migrate-ebs-snapshots-cost"></a>

Charges for volumes and snapshots in [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) are managed separately. Amazon EBS snapshots are billed at a lower rate than active Amazon EBS volumes. When an instance terminates, the value of the [DeleteOnTermination attribute](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/terminating-instances.html#preserving-volumes-on-termination) for each attached Amazon EBS volume determines whether to preserve or delete the volume. By default, the `DeleteOnTermination` attribute is set to `True` for the root volume. It's set to `False` for all other volume types. As a result, when you delete an EC2 instance, you might leave behind volumes that you added to the instance in addition to the root volume. For instructions about checking volumes (and their associated snapshots) that you no longer require, see [View information about an Amazon EBS volume](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-describing-volumes.html) in the Amazon EBS documentation.

By default, when you create a snapshot, it's stored in the Amazon EBS Snapshot Standard tier (standard tier). Snapshots stored in the standard tier are incremental. This means that only the blocks on the volume that have changed after your most recent snapshot are saved. The [Amazon EBS Snapshots Archive](https://docs.aws.amazon.com/ebs/latest/userguide/snapshot-archive.html) is a storage tier that you can use for low-cost, long-term storage of snapshots that you rarely access and that don't require frequent or fast retrieval. Consider the pricing difference between the standard and archive tiers when you plan your snapshot strategy. Amazon EBS Snapshots Archive offers up to 75 percent lower snapshot storage costs for snapshots that you plan to store for 90 days or longer and that you rarely need to access.

|
|
| Amazon EBS Snapshot Storage | Cost |
| --- |--- |
| Standard | $0.05/GB-month |
| Archive | $0.0125/GB-month |

In smaller environments, the cost savings might not be significant. The savings are greater at a large scale, where multiple accounts and thousands of EC2 instances have terabytes of Amazon EBS snapshots that remain after you delete the Amazon EBS volumes.

The following table compares the standard and archive tiers per month at 50 TB of usage. Even at this scale, the annual savings are approximately $2,800.

|
|
| Amazon EBS Snapshot Storage | Cost per month | Cost per year |
| --- |--- |--- |
| Standard 50 TB | $312.50 | $3,750 |
| Archive 50 TB | $78.13 | $937.60 |
|  | **Annual savings** | $2,812.40 |

## Cost optimization recommendations
<a name="ebs-migrate-ebs-snapshots-rec"></a>

Deleting a snapshot might not reduce your organization's data storage costs. Other snapshots might reference that snapshot's data, and AWS preserves referenced data. For example, when you take the first snapshot of a volume with 10 GiB of data, the size of the snapshot is also 10 GiB. Because snapshots are incremental, the second snapshot that you take of the same volume contains only blocks of data that changed since you took the first snapshot. The second snapshot also references the data in the first snapshot. If you change 4 GiB of data and take a second snapshot, the size of the second snapshot is 4 GiB. In addition, the second snapshot references the unchanged 6 GiB in the first snapshot. For more information, see [Why did my storage costs not reduce after I deleted a snapshot of my EBS volume and then deleted the volume itself?](https://repost.aws/knowledge-center/ebs-volume-snapshot-cost) in the AWS Knowledge Center.

Consider the following:
+ You aren't billed for snapshots that another AWS account owns and shares with your account. You're billed only when you copy the shared snapshot to your account. You're also billed for Amazon EBS volumes that you create from the shared snapshot.
+ If another snapshot (snap B) references a snapshot (snap A), then deleting snap B might not reduce the storage costs. When you delete a snapshot, AWS removes only the data that's unique to that snapshot. Data that other snapshots reference remains, and you're billed for this referenced data. To delete an incremental snapshot, see [Incremental snapshot deletion](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-deleting-snapshot.html#ebs-deleting-snapshot-incremental) in the Amazon EBS documentation.

Regularly deleting snapshots that you no longer need is a standard practice when you run your workloads on AWS. Over time, unneeded snapshots can increase your storage costs.

## Additional resources
<a name="ebs-migrate-ebs-snapshots-resources"></a>
+ [Controlling your AWS costs by deleting unused Amazon EBS volumes](https://aws.amazon.com/blogs/mt/controlling-your-aws-costs-by-deleting-unused-amazon-ebs-volumes/) (AWS Cloud Operations & Migrations Blog)
+ [Delete an Amazon EBS snapshot](https://docs.aws.amazon.com/ebs/latest/userguide/ebs-deleting-snapshot.html) (Amazon EBS documentation)
+ [Cost Optimization Workshop](https://wellarchitectedlabs.com/cost-optimization/) (AWS Well-Architected Labs)
+ [Automatically archive Amazon EBS Snapshots with Amazon Data Lifecycle Manager](https://aws.amazon.com/blogs/storage/automatically-archive-amazon-ebs-snapshots-with-amazon-data-lifecycle-manager/) (AWS Storage Blog)
