---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-image-transformation-for-amazon-cloudfront/tracing-api-errors.html
---

# Tracing API errors using request ID
<a name="tracing-api-errors"></a>

 **Problem:** Need to identify the root cause of API errors or failed image processing requests.

 **Solution:** Each API response includes an `x-amz-request-id` header that can be used to trace the request in CloudWatch logs:

1. Capture the `x-amz-request-id` from the API response headers

1. Navigate to the CloudWatch console

1. Go to **Log groups**

1. Find the log group for the image processing service:
   + Lambda architecture: Look for the Lambda function log group
   + ECS architecture: Look for the ECS task log group

1. Search for the request ID in the logs:
   + Use the CloudWatch Logs Insights query: `fields @timestamp, @message | filter @message like /REQUEST_ID/`
   + Replace `REQUEST_ID` with the actual request ID value

1. Review the log entries to identify error messages, stack traces, or processing details

The request ID allows you to trace the complete request lifecycle and identify exactly where errors occurred during image processing.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Image Transformation for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
