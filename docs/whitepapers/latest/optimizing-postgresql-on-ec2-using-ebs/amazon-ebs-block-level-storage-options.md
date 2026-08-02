---
source_url: https://docs.aws.amazon.com/whitepapers/latest/optimizing-postgresql-on-ec2-using-ebs/amazon-ebs-block-level-storage-options.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Amazon EBS block-level storage options
<a name="amazon-ebs-block-level-storage-options"></a>

 Amazon EBS provides flexible, cost effective, and easy-to-use data storage options for Amazon EC2 instances. Each option has a unique combination of performance and durability. These storage options can be used independently or in combination to suit workloads' requirements.

 There are two primary block-level storage options for Amazon EC2 instances.
+  [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html)
+  [Amazon Elastic Block Store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEBS.html)

## Amazon EC2 instance store
<a name="amazon-ec2-instance-store"></a>

 The instance store volume consists of one or more storage volumes exposed as block I/O devices. It provides temporary block-level storage for instances. An instance store volume is a disk that is physically attached to the Amazon EC2 instance. You must specify instance store volumes when you launch the Amazon EC2 instance. Data on instance store volumes does not persist if the instance stops, hibernates, or terminates; or if the underlying disk drive fails.

## Amazon Elastic Block Store
<a name="amazon-ebs"></a>

 Amazon EBS provides durable, block-level storage volumes that can be attached to a running instance. An Amazon EBS volume behaves like a raw, unformatted, external block device that you can attach to an instance. The volume persists independently from the running life of an instance. The data on the Amazon EBS volume persists even if the associated Amazon EC2 instance shuts down or goes through a hardware failure. The data persists on the volume until the volume is explicitly deleted. Refer to [Solid state drives (SSD)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html#solid-state-drives) in the AWS documentation for the details about SSD-backed Amazon EBS volumes.

 Due to the immediate proximity of the instance to the instance store volume, the I/O latency to an instance store volume tends to be lower than to an Amazon EBS volume. Use cases for instance store volumes include acting as a layer of cache or buffer, storing temporary database tables or logs, or providing storage for read replicas. For a list of the instance types that support instance store volumes, refer to [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) within the Amazon EC2 User Guide for Linux instances. Unlike Amazon EBS volumes, you can't detach an instance store volume from one instance and attach it to a different instance. An instance store volume exists only during the lifetime of the instance to which it is attached. You can't configure an instance store volume to persist beyond the lifetime of its associated instance.

 The remainder of this paper focuses on Amazon EBS SSD volumes:
+ General Purpose (`gp2`, `gp3`)
+ Provisioned IOPS (`io1`, `io2`, `io2bx`)
