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
