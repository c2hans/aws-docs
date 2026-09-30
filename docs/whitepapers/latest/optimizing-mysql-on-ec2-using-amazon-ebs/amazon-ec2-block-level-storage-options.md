---
source_url: https://docs.aws.amazon.com/whitepapers/latest/optimizing-mysql-on-ec2-using-amazon-ebs/amazon-ec2-block-level-storage-options.html
---

# Amazon EC2 block-level storage options
<a name="amazon-ec2-block-level-storage-options"></a>

 There are two block-level storage options for Amazon EC2 instances. The first option is an instance store, which consists of one or more instance store volumes exposed as block I/O devices. An instance store volume is a disk that is physically attached to the host computer that runs the Amazon EC2 virtual machine (VM). You must specify instance store volumes when you launch the Amazon EC2 instance. Data on instance store volumes will not persist if the instance stops, ends, or if the underlying disk drive fails.

 The second option is an Amazon EBS volume, which provides off-instance storage that will persist independently from the life of the instance. The data on the Amazon EBS volume persists even if the Amazon EC2 instance that the volume is attached to shuts down or there is a hardware failure on the underlying host. The data persists on the volume until the volume is explicitly deleted. Refer to [Solid state drives (SSD)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html#solid-state-drives) in the AWS documentation for the details about SSD-backed Amazon EBS volumes.

 Due to the immediate proximity of the instance to the instance store volume, the I/O latency to an instance store volume tends to be lower than to an Amazon EBS volume. Use cases for instance store volumes include acting as a layer of cache or buffer, storing temporary database tables or logs, or providing storage for read replicas. For a list of the instance types that support instance store volumes, refer to [Amazon EC2 instance store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) within the Amazon EC2 User Guide for Linux instances. The remainder of this paper focuses on Amazon EBS volume-backed Amazon EC2 instances.
