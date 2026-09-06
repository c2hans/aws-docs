---
source_url: https://docs.aws.amazon.com/whitepapers/latest/web-application-hosting-best-practices/storage-and-backup-of-data-and-assets.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Storage and backup of data and assets
<a name="storage-and-backup-of-data-and-assets"></a>

 There are numerous options within the AWS Cloud for storing, accessing, and backing up your web application data and assets. Amazon S3 provides a highly available and redundant object store. Amazon S3 is a great storage solution for somewhat static or slow-changing objects, such as images, videos, and other static media. Amazon S3 also supports edge caching and streaming of these assets by interacting with CloudFront.

 For attached file system-like storage, EC2 instances can have EBS volumes attached. These act like mountable disks for running EC2 instances. Amazon EBS is great for data that needs to be accessed as block storage and that requires persistence beyond the life of the running instance, such as database partitions and application logs.

 In addition to having a lifetime that is independent of the EC2 instance, you can take snapshots of EBS volumes and store them in Amazon S3. Because EBS snapshots only back up changes since the previous snapshot, more frequent snapshots can reduce snapshot times. You can also use an EBS snapshot as a baseline for replicating data across multiple EBS volumes and attaching those volumes to other running instances.

EBS volumes can be as large as 16TB, and multiple EBS volumes can be striped for even larger volumes or for increased input/output (I/O) performance. To maximize the performance of your I/O-intensive applications, you can use Provisioned IOPS volumes. Provisioned IOPS volumes are designed to meet the needs of I/O-intensive workloads, particularly database workloads that are sensitive to storage performance and consistency in random access I/O throughput.

You specify an IOPS rate when you create the volume and Amazon EBS provisions that rate for the lifetime of the volume. Amazon EBS currently supports IOPS per volume ranging from maximum of 16000 (for all instance types) up to 64,000 ([for instances built on Nitro System](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html#ec2-nitro-instances)). You can stripe multiple volumes together to deliver thousands of IOPS per instance to your application. Apart from this, for higher throughput and mission critical workloads requiring sub-millisecond latency, you can use io2 block express volume type which can support up-to 256,000 IOPS with a maximum storage capacity of 64TB.
