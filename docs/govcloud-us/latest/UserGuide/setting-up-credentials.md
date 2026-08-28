---
source_url: https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/setting-up-credentials.html
---

# Credentials
<a name="setting-up-credentials"></a>

If you use CloudFront with AWS GovCloud (US), be sure that you use the correct credentials:
+ To use CloudFront with your AWS GovCloud (US) resources, you must have an AWS GovCloud (US) account. If you don’t have an account, see [AWS GovCloud (US) Sign Up](getting-started-sign-up.md) for more information.
+ To set up CloudFront, sign in to the [CloudFront console](https://console.aws.amazon.com/cloudfront/) by using your standard AWS credentials. You cannot use your AWS GovCloud (US) account credentials to sign in to the standard AWS Management Console.
+ It is important to note that CloudFront is located outside of the AWS GovCloud (US) boundary and customers should not enter or store ITAR-controlled data in the service.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS GovCloud (US). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query govcloud-us` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
