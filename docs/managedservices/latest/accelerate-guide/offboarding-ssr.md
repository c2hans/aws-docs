---
source_url: https://docs.aws.amazon.com/managedservices/latest/accelerate-guide/offboarding-ssr.html
---

# Offboard from SSR
<a name="offboarding-ssr"></a>

To offboard from the SSR service, create a service request (SR) through the AMS console. After you submit the SR, an AMS operations engineers helps you offboard from SSR. In the SR, provide the reason for that you want to offboard.

To offboard an account and perform a resources cleanup, create an SR through the AMS console. After you submit the SR, an AMS operations engineers helps you delete the SSR Amazon S3 bucket.

If you offboard from AMS, you are automatically offboarded from the AMS SSR console. AMS automatically stops sending data to your account. AMS deletes your SSR S3 bucket as part of the offboarding process.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
