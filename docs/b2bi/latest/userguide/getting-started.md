---
source_url: https://docs.aws.amazon.com/b2bi/latest/userguide/getting-started.html
---

# Getting started with AWS B2B Data Interchange
<a name="getting-started"></a>

To use AWS B2B Data Interchange, you create profiles, transformers, capabilities, and partnerships. This topic describes how to create and configure these basic building blocks for this service. After you have met the prerequisites, follow the instructions in [Transforming and generating EDI](transform-variations.md) or use the [Quick setup using the console](getting-started-quick.md)

After you create the necessary resources (profile, transformer, trading capability and partnership), your trading partners can use AWS Transfer Family or any connectivity software send you X12 documents.

When the X12 documents land in the configured input folder in your Amazon S3 bucket, the documents are automatically picked up and transformed by B2B Data Interchange. Each inbound X12 EDI document transformed also generates acknowledgments (such as 999 or 997) that you can return to your partner.

 Similarly, when JSON or XML files are dropped into in specified input directories in Amazon S3, B2B Data Interchange automatically transforms the files to generate X12. You can then use AWS Transfer Family servers (that use either the AS2 or SFTP protocol) to send this X12 to your trading partner.

All transformation activity and status updates, including the generation of acknowledgements, are logged to CloudWatch and emit events to Amazon EventBridge. For details, see [Details fields for transformation events](events-detail-reference.md#detail-fields-transform). You can also monitor the transformation activity using processed input-output pairs view.

**Topics**
+ [Prerequisites for using AWS B2B Data Interchange](b2bi-prereq.md)
+ [Quick setup using the console](getting-started-quick.md)
+ [Configure AWS B2B Data Interchange using an CloudFormation template](quickstart-template.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS B2B Data Interchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query b2bi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
