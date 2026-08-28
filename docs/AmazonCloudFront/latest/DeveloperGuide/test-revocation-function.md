---
source_url: https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/test-revocation-function.html
---

# Step 3: Test your revocation function
<a name="test-revocation-function"></a>

Use the CloudFront console to test your Connection Function with sample certificates. Navigate to the Connection Function in the console and use the Test tab.

**Test with sample certificates**

1. Paste a sample certificate in PEM format into the test interface

1. Optionally specify a client IP address for testing IP-based logic

1. Choose **Test function** to see the execution results

1. Review the execution logs to verify your function logic

Test with both valid and revoked certificates to ensure your function handles both scenarios correctly. The execution logs show console.log output and any errors that occur during function execution.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudFront. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudFront` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
