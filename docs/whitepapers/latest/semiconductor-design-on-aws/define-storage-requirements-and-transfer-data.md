---
source_url: https://docs.aws.amazon.com/whitepapers/latest/semiconductor-design-on-aws/define-storage-requirements-and-transfer-data.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Define storage requirements and transfer data
<a name="define-storage-requirements-and-transfer-data"></a>

After workloads are selected for migration, analyze what data is required by the workload, and the capacity and performance requirements of the storage subsystem. This evaluation process can significantly delay the process of migrating to AWS, so it is recommended that you begin the process of identifying workload data dependencies early.

You also need to analyze whether data can be migrated to the cloud once, or if it needs to be synchronized with the on-premises storage. In addition to increasing workflow turnaround time, copying large volumes of data between on-premises sites and AWS has cost implications. Moving data into AWS is free, but moving data out is not. For these reasons it is desirable to minimize data transfer back and forth between on-premises sites and AWS.

AWS provides several ways to migrate on-premises data to the cloud that will initially store the data in [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3). Amazon S3 is a secure, high-performance object storage service that provides 99.999999999% of durability, fine grained access control, up to 25 Gbps transfer to EC2 instances (per instance), cross-region replication, data tiering, and more. See [Amazon S3 Features](https://aws.amazon.com/s3/features/) and [Amazon S3 FAQs](https://aws.amazon.com/s3/faqs/) for more information.

Although tools and semiconductor flows require POSIX-compliant file systems and do not currently support object storage, S3 can be used as the back-end for creating an AWS-managed, POSIX-compliant file system using [Amazon FSx for Lustre](https://aws.amazon.com/fsx/lustre/). Having the data in S3 enables agility and fast failure. An S3 bucket can be the golden repository of data, and be used to quickly create new file systems or transfer data to EC2 instances so that different storage solutions can easily and quickly be created and evaluated. The data in S3 can also be used for disaster recovery to quickly restore data from job or system failures.

The method of transfer largely depends on how much data you need to move. If you have a relatively small amount of static data and you have a fast, reliable internet connection, you may be able to use your internet connection. Leveraging AWS Direct Connect allows for high-bandwidth ingress and egress to AWS. [AWS DataSync](https://aws.amazon.com/datasync/) makes it simple and fast to move large amounts of data between on-premises storage and Amazon S3, [Amazon Elastic File System](https://aws.amazon.com/efs/) (Amazon EFS), and Amazon FSx for Lustre over the internet or Direct Connect.

If you have large amounts of library, design, or simulation data that requires an initial one-time transfer, consider using [AWS Snowball Edge](https://aws.amazon.com/snowball/). [AWS Snowball Edge Edge](https://docs.aws.amazon.com/snowball/latest/developer-guide/whatisedge.html) supports 80TB of usable storage, and has a rich feature set that provides edge services and clustering abilities. For additional information, see the “When to use Snowball Edge” section of the [AWS Snowball Edge FAQs](https://aws.amazon.com/snowball/faqs/).
