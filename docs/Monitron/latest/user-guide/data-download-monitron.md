---
source_url: https://docs.aws.amazon.com/Monitron/latest/user-guide/data-download-monitron.html
---

Amazon Monitron is no longer open to new customers. Existing customers can continue to use the service as normal. For capabilities similar to Amazon Monitron, see our [blog post](https://aws.amazon.com/blogs/machine-learning/maintain-access-and-consider-alternatives-for-amazon-monitron).

# Exporting your Amazon Monitron data to Amazon S3
<a name="data-download-monitron"></a>

You may sometimes want to access the raw data that Amazon Monitron is storing for you, in order to stay informed about exactly what kind of data you’re securely storing with AWS.

You can get your raw data by filing a support ticket with AWS, and by giving Amazon Monitron permission to deliver your data to you.

To get real time operational data for Amazon Monitron resources that can be consumed programmatically, consider exporting your data using Kinesis streams. For more information, see [Amazon Monitron Kinesis data export v2](https://docs.aws.amazon.com/Monitron/latest/user-guide/monitron-kinesis-export-v2.html).

**Topics**
+ [Prerequisites](exporting-data-procedure.md)
+ [Exporting your data with CloudFormation (recommended option)](onetime-download-cflink.md)
+ [Exporting your data with the console](onetime-download-console.md)
+ [Exporting your data with CloudShell](export-shell.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Monitron. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Monitron` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
