---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/sus_sus_data_a8.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SUS04-BP07 Minimize data movement across networks
<a name="sus_sus_data_a8"></a>

 Use shared storage and access data from regional data stores to minimize the total networking resources required to support data movement for your workload.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Store data as close to the consumer as possible.
+  Partition regionally consumed services so that their Region-specific data is stored within the Region where it is consumed.
+  Use block-level duplication instead of file or object-level duplication when copying changes across the network.
+  Compress data before moving it over the network.

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Optimizing your AWS Infrastructure for Sustainability, Part III: Networking](https://aws.amazon.com/blogs/architecture/optimizing-your-aws-infrastructure-for-sustainability-part-iii-networking/)
+  [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/)
+  [Amazon CloudFront Key Features including the CloudFront Global Edge Network](https://aws.amazon.com/cloudfront/features/)
+  [Compressing HTTP requests in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/gzip.html)
+  [Intermediate data compression with Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-output-compression.html#HadoopIntermediateDataCompression)
+  [Loading compressed data files from Amazon S3 into Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/t_loading-gzip-compressed-data-files-from-S3.html)
+  [Serving compressed files with Amazon CloudFront](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/ServingCompressedFiles.html)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
