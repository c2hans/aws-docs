---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cost-modeling-data-lakes/analytics-and-storage.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Analytics and storage
<a name="analytics-and-storage"></a>

 The business value of data lakes is derived using tools in analytics stage. Cost in this stage correlates directly to the amount of data collected and analytics done on the data to derive the required value.

## Cost factors
<a name="analytics-cost-factors"></a>

 The primary cost of this stage includes:
+  **Processing Unit cost** - This is the cost of instances used by the analytics tool being used. Data Warehouse solution like Amazon Redshift or analytics solutions on Amazon EMR or operational analytics on Amazon OpenSearch Service are all billed based on the instance type and number of nodes used.
+  **Storage cost** - The data stored for analysis either on Amazon S3 or on the nodes of the analytics tool itself contribute to this cost.
+  **Scanned data cost** - This is applicable only for serverless service like Athena and Amazon Redshift Spectrum, where the cost is based on the data scanned by the analytics queries.

## Cost optimization factors
<a name="analytics-cost-optimization-factors"></a>

 AWS provides reliable, scalable, and inexpensive storage and compute building blocks combined with fully managed value-added analytics services to help customers quickly gain insights into their data. In addition, the AWS-managed storage and analytics services help customers simplify the storage and analytics of their data by taking care of the infrastructure administration and management.

 We recommend that you consider the following actions to reduce the cost when using the following services:
+  [Amazon EMR](cost-optimization-in-analytics-services.md#amazon-emr)
+  [AWS Glue](cost-optimization-in-analytics-services.md#aws-glue)
+  [Lambda](cost-optimization-in-analytics-services.md#lambda)
+  [Amazon Athena](cost-optimization-in-analytics-services.md#amazon-athena)
+  [Amazon Redshift](cost-optimization-in-analytics-services.md#amazon-redshift)
+  [S3](cost-optimization-in-analytics-services.md#s3)
