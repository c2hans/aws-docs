---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/enable-debug-logs.html
---

# Enable debug logs
<a name="enable-debug-logs"></a>

 **Problem:** Need detailed logging information for troubleshooting image processing issues.

 **Solution:** Debug logs are not enabled by default. To enable debug logging:

1. Navigate to the AWS Lambda console

1. Find the image processing Lambda function created by the solution

1. Go to the **Configuration** tab

1. Select **Environment variables**

1. Add or modify the debug logging environment variables (exact variable names can be found in the CDK construct)

1. Save the changes

Debug logs will provide detailed information about image processing operations, transformation steps, and error details to help with troubleshooting.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
