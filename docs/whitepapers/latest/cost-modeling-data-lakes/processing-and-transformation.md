---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cost-modeling-data-lakes/processing-and-transformation.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Processing and transformation
<a name="processing-and-transformation"></a>

 The cost of processing depends on number of factors, such as the size of the data being processed, the complexity of the transformations (which leads to the choice of tool), and how the data is stored (format and compression).

## Cost factors
<a name="processing-cost-factors"></a>

 The primary cost at this stage includes:
+  **Processing unit cost** - This is the cost of compute and memory required to process the data. If you use a service like Amazon EMR, the Amazon EC2 instance used to process the data will incur the cost.
+  **Managed service costs** - These are the costs you pay (usually per second or per hour) for the management of the service. For a serverless service like AWS Glue, this will be billed based on the utilization of the service.
+  **Storage cost** - This is the cost of storing the processed data.

## Cost optimization factors
<a name="processing-cost-optimization-factors"></a>

 AWS analytics services take care of many of the operational tasks of data processing and transformation. The managed analytics services from AWS offer advanced features without additional licensing fees and lower the customer’s cost of operations by eliminating the need for a dedicated team of experts to manage their clusters. As a result, customers using the managed analytics services will realize the benefit of Operational efficiency, Performance, Availability, and Scalability.

 We recommend that you consider the following actions to reduce the cost when using the following services:
+  [Amazon EMR](cost-optimization-in-analytics-services.md#amazon-emr)
+  [AWS Glue](cost-optimization-in-analytics-services.md#aws-glue)
+  [Lambda](cost-optimization-in-analytics-services.md#lambda)
+  [Amazon Athena](cost-optimization-in-analytics-services.md#amazon-athena)
+  [Amazon Redshift](cost-optimization-in-analytics-services.md#amazon-redshift)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
