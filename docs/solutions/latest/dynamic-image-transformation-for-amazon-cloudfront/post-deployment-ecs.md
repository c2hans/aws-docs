---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/post-deployment-ecs.html
---

# Post-deployment configuration (ECS architecture)
<a name="post-deployment-ecs"></a>

After deploying the ECS template, additional configuration steps are required to fully utilize the advanced features:

 **Admin UI Access:** The Admin UI link is available in the CloudFormation stack outputs section. Access the Admin UI from there and sign in using the provided Cognito credentials.

 **Initial Configuration:**
+  **Configure Origins**: Use the Admin UI to add your S3 buckets and external origins
+  **Create Mappings**: Set up path-based or host-header mappings to route requests to origins
+  **Define Policies**: Create transformation policies for consistent image processing

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
