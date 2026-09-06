---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/perf_right_storage_solution_understand_char.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF03-BP01 Understand storage characteristics and requirements
<a name="perf_right_storage_solution_understand_char"></a>

 Identify and document the workload storage needs and define the storage characteristics of each location. Examples of storage characteristics include: shareable access, file size, growth rate, throughput, IOPS, latency, access patterns, and persistence of data. Use these characteristics to evaluate if block, file, object, or instance storage services are the most efficient solution for your storage needs.

 **Desired outcome:** Identify and document the storage requirements per storage requirement and evaluate the available storage solutions. Based on the key storage characteristics, your team will understand how the selected storage services will benefit your workload performance. Key criteria include data access patterns, growth rate, scaling needs, and latency requirements.

 **Common anti-patterns:**
+  You only use one storage type, such as Amazon Elastic Block Store (Amazon EBS), for all workloads.
+  You assume that all workloads have similar storage access performance requirements.

 **Benefits of establishing this best practice:** Selecting the storage solution based on the identified and required characteristics will help improve your workloads performance, decrease costs and lower your operational efforts in maintaining your workload. Your workload performance will benefit from the solution, configuration, and location of the storage service.

 **Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

 Identify your workload’s most important storage performance metrics and implement improvements as part of a data-driven approach, using benchmarking or load testing. Use this data to identify where your storage solution is constrained, and examine configuration options to improve the solution. Determine the expected growth rate for your workload and choose a storage solution that will meet those rates. Research the AWS storage offerings to determine the correct storage solution for your various workload needs. Provisioning storage solutions in AWS increases the opportunity for you to test storage offerings and determine if they are appropriate for your workload needs.

| AWS service | Key characteristics | Common use cases |
| --- | --- | --- |
| Amazon S3 | 99.999999999% durability, unlimited growth, accessible from anywhere, several cost models based on access and resiliency | Cloud-native application data, data archiving, and backups, analytics, data lakes, static website hosting, IoT data  |
| Amazon Glacier | Seconds to hours latency, unlimited growth, lowest cost, long-term storage | Data archiving, media archives, long-term backup retention. |
| Amazon EBS | Storage size requires management and monitoring, low latency, persistent storage, 99.8% to 99.9% durability, most volume types are accessible only from one EC2 instance. | COTS applications, I/O intensive applications, relational and NoSQL databases, backup and recovery |
| EC2 Instance Store | Pre-determined storage size, lowest latency, not persisted, accessible only from one EC2 instance | COTS applications, I/O intensive applications, in-memory data store |
| Amazon EFS | 99.999999999% durability, unlimited growth, accessible by multiple compute services | Modernized applications sharing files across multiple compute services, file storage for scaling content management systems |
| Amazon FSx | Supports four file systems (NetApp, OpenZFS, Windows File Server, and Amazon FSx for Lustre), storage available different per file system, accessible by multiple compute services | Cloud native workloads, private cloud bursting, migrated workloads that require a specific file system, VMC, ERP systems, on-premises file storage and backups  |
| Snow family | Portable devices, 256-bit encryption, NFS endpoint, on-board computing, TBs of storage | Migrating data to the cloud, storage, and computing in extreme on-premises conditions, disaster recovery, remote data collection |
| AWS Storage Gateway | Provides low-latency on-premises access to cloud-backed storage, fully managed on-premises cache  | On-premises data to cloud migrations, populate cloud data lakes from on-premises sources, modernized file sharing. |

 **Implementation steps:**

1. Use benchmarking or load tests to collect the key characteristics of your storage needs. Key characteristics include:

   1. Shareable (what components access this storage)

   1. Growth rate

   1. Throughput

   1. Latency

   1. I/O size

   1. Durability

   1. Access patterns (reads vs writes, frequency, spikey, or consistent)

1. Identify the type of storage solution that supports your storage characteristics.

   1. [Amazon S3](https://aws.amazon.com/s3/) is an object storage service with unlimited scalability, high availability, and multiple options for accessibility. Transferring and accessing objects in and out of Amazon S3 can use a service, such as [Transfer Acceleration](https://aws.amazon.com/s3/transfer-acceleration/) or [Access Points](https://aws.amazon.com/s3/features/access-points/) to support your location, security needs, and access patterns. Use the [Amazon S3 performance guidelines](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance-guidelines.html) to help you optimize your Amazon S3 configuration to meet your workload performance needs.

   1. [Amazon Glacier](https://aws.amazon.com/s3/storage-classes/glacier/) is a storage class of Amazon S3 built for data archiving. You can choose from three archiving solutions ranging from millisecond access to 5-12 hour access with different cost and security options. Amazon Glacier can help you meet performance requirements by implementing a data lifecycle that supports your business requirements and data characteristics.

   1. [Amazon Elastic Block Store (Amazon EBS)](https://aws.amazon.com/ebs/) is a high-performance block storage service designed for Amazon Elastic Compute Cloud (Amazon EC2). You can choose from [SSD- or HDD-based](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html) solutions with different characteristics that prioritize [IOPS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/provisioned-iops.html) or [throughput](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/hdd-vols.html). EBS volumes are well suited for high-performance workloads, primary storage for file systems, databases, or applications that can only access attached stage systems.

   1. [Amazon EC2 Instance Store](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/InstanceStorage.html) is similar to Amazon EBS as it attaches to an Amazon EC2 instance however, the Instance Store is only temporary storage that should ideally be used as a buffer, cache, or other temporary content. You cannot detach an Instance Store and all data is lost if the instance shuts down. Instance Stores can be used for high I/O performance and low latency use cases where data doesn’t need to persist.

   1. [Amazon Elastic File System (Amazon EFS)](https://aws.amazon.com/efs/) is a mountable file system that can be accessed by multiple types of compute solutions. Amazon EFS automatically grows and shrinks storage and is performance-optimized to deliver consistent low latencies. EFS has [two performance configuration modes](https://docs.aws.amazon.com/efs/latest/ug/performance.html): General Purpose and Max I/O. General Purpose has a sub-millisecond read latency and a single-digit millisecond write latency. The Max I/O feature can support thousands of compute instance requiring a shared file system. Amazon EFS supports [two throughput modes](https://docs.aws.amazon.com/efs/latest/ug/managing-throughput.html): Bursting and Provisioned. A workload that experiences a spikey access pattern will benefit from the bursting throughput mode while a workload that is consistently high would be performant with a provisioned throughput mode.

   1. [Amazon FSx](https://aws.amazon.com/fsx/) is built on the latest AWS compute solutions to support four commonly used file systems: NetApp ONTAP, OpenZFS, Windows File Server, and Lustre. Amazon FSx [latency, throughput, and IOPS](https://aws.amazon.com/fsx/when-to-choose-fsx/) vary per file system and should be considered when selecting the right file system for your workload needs.

   1. [AWS Snow Family](https://aws.amazon.com/snow/) are storage and compute devices that support online and offline data migration to the cloud and data storage and computing on premises. AWS Snow devices support collecting large amounts of on-premises data, processing of that data and moving that data to the cloud. There are several [documented performance best practices](https://docs.aws.amazon.com/snowball/latest/developer-guide/performance.html) when it comes to the number of files, file sizes, and compression.

   1. [AWS Storage Gateway](https://aws.amazon.com/storagegateway/) provides on-premises applications access to cloud-based storage. AWS Storage Gateway supports multiple cloud storage services including Amazon S3, Amazon Glacier, Amazon FSx, and Amazon EBS. It supports a number of protocols such as iSCSI, SMB, and NFS. It provides low-latency performance by caching frequently accessed data on premises and only sends changed data and compressed data to AWS.

1. After you have experimented with your new storage solution and identified the optimal configuration, plan your migration and validate your performance metrics. This is a continual process, and should be reevaluated when key characteristics change or available services or options change.

 **Level of effort for the implementation plan: **If a workload is moving from one storage solution to another, there could be a *moderate* level of effort involved in refactoring the application.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Amazon EBS Volume Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html)
+  [Amazon EC2 Storage](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Storage.html)
+  [Amazon EFS: Amazon EFS Performance](https://docs.aws.amazon.com/efs/latest/ug/performance.html)
+  [Amazon FSx for Lustre Performance](https://docs.aws.amazon.com/fsx/latest/LustreGuide/performance.html)
+  [Amazon FSx for Windows File Server Performance](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/performance.html)
+ [Amazon FSx for NetApp ONTAP performance](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/performance.html)
+ [Amazon FSx for OpenZFS performance](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/performance.html)
+  [Amazon Glacier: Amazon Glacier Documentation](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html)
+  [Amazon S3: Request Rate and Performance Considerations](https://docs.aws.amazon.com/AmazonS3/latest/dev/request-rate-perf-considerations.html)
+  [Cloud Storage with AWS](https://aws.amazon.com/products/storage/)
+ [AWS Snow Family](https://aws.amazon.com/snow/#Feature_comparison)
+  [EBS I/O Characteristics](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/ebs-io-characteristics.html)

 **Related videos:**
+  [Deep dive on Amazon EBS (STG303-R1)](https://www.youtube.com/watch?v=wsMWANWNoqQ)
+  [Optimize your storage performance with Amazon S3 (STG343)](https://www.youtube.com/watch?v=54AhwfME6wI)

 **Related examples:**
+  [Amazon EFS CSI Driver](https://github.com/kubernetes-sigs/aws-efs-csi-driver)
+  [Amazon EBS CSI Driver](https://github.com/kubernetes-sigs/aws-ebs-csi-driver)
+  [Amazon EFS Utilities](https://github.com/aws/efs-utils)
+  [Amazon EBS Autoscale](https://github.com/awslabs/amazon-ebs-autoscale)
+  [Amazon S3 Examples](https://docs.aws.amazon.com/sdk-for-javascript/v2/developer-guide/s3-examples.html)
+ [Amazon FSx for Lustre Container Storage Interface (CSI) Driver](https://github.com/kubernetes-sigs/aws-fsx-csi-driver)
