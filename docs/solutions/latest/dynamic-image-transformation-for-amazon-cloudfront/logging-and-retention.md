---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/logging-and-retention.html
---

# Logging and retention
<a name="logging-and-retention"></a>

 **CloudWatch log retention**

The ECS architecture maintains separate log groups with different retention policies:
+  **Admin API logs**: 10 years retention for audit and compliance purposes
+  **Image processing logs**: 10 years retention for operational monitoring and troubleshooting

Log retention policies are automatically configured during deployment and help balance operational visibility with storage costs.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
