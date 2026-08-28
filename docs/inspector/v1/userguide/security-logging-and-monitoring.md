---
source_url: https://docs.aws.amazon.com/inspector/v1/userguide/security-logging-and-monitoring.html
---

 End of support notice: On May 20, 2026, AWS will end support for Amazon Inspector Classic. After May 20, 2026, you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. Amazon Inspector Classic no longer available to new accounts and accounts that have not completed an assessment in the last 6 months. For all other accounts, access will remain valid until May 20, 2026, after which you will no longer be able to access the Amazon Inspector Classic console or Amazon Inspector Classic resources. For more information, see [Amazon Inspector Classic end of support](https://docs.aws.amazon.com/inspector/v1/userguide/inspector-migration.html).

# Logging and monitoring in Amazon Inspector Classic
<a name="security-logging-and-monitoring"></a>

Amazon Inspector Classic is integrated with AWS CloudTrail, a service that provides a record of actions taken by a user, role, or an AWS service in Amazon Inspector Classic. CloudTrail captures all API calls for Amazon Inspector Classic as events, including calls from the Amazon Inspector Classic console and code calls to the Amazon Inspector Classic API operations.

For information on using CloudTrail logging in Amazon Inspector Classic, see [Logging Amazon Inspector Classic API calls with AWS CloudTrail](logging-using-cloudtrail.md).

You can monitor Amazon Inspector Classic using Amazon CloudWatch, which collects and processes raw data into readable, near-real time metrics. By default, Amazon Inspector Classic sends metric data to CloudWatch in 5-minute periods.

For information on using CloudWatch with Amazon Inspector Classic, see [Monitoring Amazon Inspector Classic using Amazon CloudWatch](using-cloudwatch.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
