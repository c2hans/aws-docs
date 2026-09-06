---
source_url: https://docs.aws.amazon.com/whitepapers/latest/genomics-data-transfer-analytics-and-machine-learning/appendix-j-scaling-secondary-analysis.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Appendix J: Scaling secondary analysis
<a name="appendix-j-scaling-secondary-analysis"></a>

 To scale secondary analysis in your account using AWS Step Functions and AWS Batch, there are a few optimizations that can be made and service limits that may need to be increased.

 You should provide the Amazon EC2 instances in your AWS Batch compute environments with access to reference genome files either through a shared file system like Amazon Elastic File System (EFS) or Amazon FSx for Lustre, or mount an Elastic Block Store (EBS) volume on each instance that contains the reference genome files. This avoids downloading the reference files for each job which will decrease job runtime, limit data transfer volume, and limit put or get requests to Amazon S3.

 Configure your VPC and AWS Batch compute environments to use multiple Availability Zones (AZs) so you have access to a bigger pool of instances. Configure your compute environment to use instance types or instance families that are optimal for your workload, for example, the Sentieon aligner and variant caller both run optimally with 40 cores and 50 GB of RAM and are compute bound so the c5.12xlarge and c5.24xlarge would provide optimal performance and maximum utilization of the compute instances. Try to include as many instance types as possible to increase the pool of instances that can be used in your compute environments.

 You may need to increase your Amazon EC2 instance limits, Elastic Block Store (EBS) volumes limit, and move to a shared file system like Amazon Elastic File System (EFS) or Amazon FSx for Lustre to avoid request rate limits in Amazon S3.
