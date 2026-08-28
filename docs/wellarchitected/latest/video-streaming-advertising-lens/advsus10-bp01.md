---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/video-streaming-advertising-lens/advsus10-bp01.html
---

# ADVSUS10-BP01 Optimize content moderation systems for sustainable operation
<a name="advsus10-bp01"></a>

 As content grows for organizations, optimizing content moderation systems can benefit sustainability-related key performance indicators (KPIs). Implement or build architectures that include efficient machine learning models, automated scaling, and optimized storage patterns.

## Implementation guidance
<a name="implementation-guidance-advsus10-bp01"></a>
+  Use efficient machine learning models for content classification. Use AWS Inferentia chips when possible, for improved performance per watt.
+  Implement batch processing for non-real-time moderation tasks.
+  Configure regional content analysis to minimize data movement.
+  Use caching strategies for frequently accessed moderation rules.
+  Use energy-efficient computing resources, such as AWS Graviton, for moderation workloads.
+  Implement automated scaling based on moderation demand using auto scaling rules and Amazon CloudWatch metrics.
+  Optimize storage patterns for moderation results and audit trails. For workloads using Amazon S3, use Storage Lens for insights and recommendations to optimize storage use.

## Key AWS services
<a name="key-aws-services-59"></a>
+  Amazon Rekognition
+  AWS Inferentia
+  Amazon SageMaker AI
+  AWS Auto Scaling
+  AWS CloudWatch
+  Amazon ElastiCache
+  Amazon S3 Storage Lens

## **Resources**
<a name="resources-76"></a>
+  [Optimize AI/ML workloads for sustainability: Part 1, identify business goals, validate ML use, and process data](https://aws.amazon.com/blogs/architecture/optimize-ai-ml-workloads-for-sustainability-part-1-identify-business-goals-validate-ml-use-and-process-data/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
