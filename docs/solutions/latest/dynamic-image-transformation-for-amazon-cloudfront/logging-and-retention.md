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
