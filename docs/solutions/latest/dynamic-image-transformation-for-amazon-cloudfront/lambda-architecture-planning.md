---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/lambda-architecture-planning.html
---

# Lambda Architecture
<a name="lambda-architecture-planning"></a>

This cost-optimized serverless architecture is ideal for most image transformation workloads with moderate performance requirements.

 **Key characteristics:**
+  **Image size limit**: Up to 6 MB per image
+  **Pricing model**: Pay-per-request with no idle costs
+  **Scaling**: Automatic scaling with built-in high availability
+  **Maintenance**: Fully managed serverless infrastructure
+  **Feature set**: Core image transformation capabilities

 **Best suited for:**
+ Small to medium-sized images (under 6 MB)
+ Cost-sensitive deployments
+ Variable or unpredictable traffic patterns
+ Simple transformation requirements
+ S3 only origins

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
