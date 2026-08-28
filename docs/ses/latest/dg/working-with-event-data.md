---
source_url: https://docs.aws.amazon.com/ses/latest/dg/working-with-event-data.html
---

# Working with Amazon SES event data
<a name="working-with-event-data"></a>

After you [set up event publishing](monitor-sending-using-event-publishing-setup.md) and specify a configuration set for sending emails, you can retrieve your email sending events from the event destination that you specified when you set up the configuration set associated with the email.

This section describes how to retrieve your email sending events from Amazon CloudWatch and Amazon Data Firehose, and how to interpret event data provided by Amazon SNS.
+ [Retrieving Amazon SES event data from CloudWatch](event-publishing-retrieving-cloudwatch.md)
+ [Retrieving Amazon SES event data from Firehose](event-publishing-retrieving-firehose.md)
+ [Interpreting Amazon SES event data from Amazon SNS](event-publishing-retrieving-sns.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Email Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
