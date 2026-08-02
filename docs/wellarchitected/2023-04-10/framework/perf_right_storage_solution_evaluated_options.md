---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/perf_right_storage_solution_evaluated_options.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# PERF03-BP02 Evaluate available configuration options
<a name="perf_right_storage_solution_evaluated_options"></a>

 Evaluate the various characteristics and configuration options and how they relate to storage. Understand where and how to use provisioned IOPS, SSDs, magnetic storage, object storage, archival storage, or ephemeral storage to optimize storage space and performance for your workload.

 [Amazon EBS](https://aws.amazon.com/ebs) provides a range of options that allow you to optimize storage performance and cost for your workload. These options are divided into two major categories: SSD-backed storage for transactional workloads, such as databases and boot volumes (performance depends primarily on IOPS), and HDD-backed storage for throughput-intensive workloads, such as MapReduce and log processing (performance depends primarily on MB/s).

 SSD-backed volumes include the highest performance provisioned IOPS SSD for latency-sensitive transactional workloads and general-purpose SSD that balance price and performance for a wide variety of transactional data.

 [Amazon S3 transfer acceleration](https://aws.amazon.com/s3/transfer-acceleration/) allows fast transfer of files over long distances between your client and your S3 bucket. Transfer acceleration leverages Amazon CloudFront globally distributed edge locations to route data over an optimized network path. For a workload in an S3 bucket that has intensive GET requests, use Amazon S3 with CloudFront. When uploading large files, use multi-part uploads with multiple parts uploading at the same time to help maximize network throughput.

 [Amazon Elastic File System (Amazon EFS)](https://aws.amazon.com/efs/) provides a simple, scalable, fully managed elastic NFS file system for use with AWS Cloud services and on-premises resources. To support a wide variety of cloud storage workloads, Amazon EFS offers two performance modes: general purpose performance mode, and max I/O performance mode. There are also two throughput modes to choose from for your file system: Bursting Throughput, and Provisioned Throughput. To determine which settings to use for your workload, see the [Amazon EFS User Guide](https://docs.aws.amazon.com/efs/latest/ug/performance.html).

 [Amazon FSx](https://aws.amazon.com/fsx/) provides four file systems to choose from: [Amazon FSx for Windows File Server](https://aws.amazon.com/fsx/windows/) for enterprise workloads, [Amazon FSx for Lustre](https://aws.amazon.com/fsx/lustre/) for high-performance workloads, [Amazon FSx for NetApp ONTAP](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/index.html) for NetApps popular ONTAP file system, and [Amazon FSx for OpenZFS](https://docs.aws.amazon.com/fsx/latest/OpenZFSGuide/what-is-fsx.html) for Linux-based file servers. FSx is SSD-backed and is designed to deliver fast, predictable, scalable, and consistent performance. Amazon FSx file systems deliver sustained high read and write speeds and consistent low latency data access. You can choose the throughput level you need to match your workload’s needs.

 **Common anti-patterns:**
+  You only use one storage type, such as Amazon EBS, for all workloads.
+  You use Provisioned IOPS for all workloads without real-world testing against all storage tiers.
+  You assume that all workloads have similar storage access performance requirements.

 **Benefits of establishing this best practice:** Evaluating all storage service options can reduce the cost of infrastructure and the effort required to maintain your workloads. It can potentially accelerate your time to market for deploying new services and features.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Determine storage characteristics: When you evaluate a storage solution, determine which storage characteristics you require, such as ability to share, file size, cache size, latency, throughput, and persistence of data. Then match your requirements to the AWS service that best fits your needs.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Cloud Storage with AWS](https://aws.amazon.com/products/storage/?ref=wellarchitected)
+  [Amazon EBS Volume Types](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumeTypes.html)
+  [Amazon EC2 Storage](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/Storage.html)
+  [Amazon EFS: Amazon EFS Performance](https://docs.aws.amazon.com/efs/latest/ug/performance.html)
+  [Amazon FSx for Lustre Performance](https://docs.aws.amazon.com/fsx/latest/LustreGuide/performance.html)
+  [Amazon FSx for Windows File Server Performance](https://docs.aws.amazon.com/fsx/latest/WindowsGuide/performance.html)
+  [Amazon Glacier: Amazon Glacier Documentation](https://docs.aws.amazon.com/amazonglacier/latest/dev/introduction.html)
+  [Amazon S3: Request Rate and Performance Considerations](https://docs.aws.amazon.com/AmazonS3/latest/dev/request-rate-perf-considerations.html)
+  [Cloud Storage with AWS](https://aws.amazon.com/products/storage/)
+  [Cloud Storage with AWS](https://aws.amazon.com/products/storage/?ref=wellarchitected)
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
