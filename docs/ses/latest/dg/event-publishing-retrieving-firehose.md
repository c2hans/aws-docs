---
source_url: https://docs.aws.amazon.com/ses/latest/dg/event-publishing-retrieving-firehose.html
---

# Retrieving Amazon SES event data from Firehose
<a name="event-publishing-retrieving-firehose"></a>

Amazon SES publishes email sending events to Firehose as JSON records. Firehose then publishes the records to the AWS service destination that you chose when you set up the delivery stream in Firehose. For information about setting up Firehose delivery streams, see [Creating an Firehose Delivery Stream](https://docs.aws.amazon.com/firehose/latest/dev/basic-create.html) in the *Amazon Data Firehose Developer Guide*.

**Topics**
+ [Contents of event data that Amazon SES publishes to Firehose](event-publishing-retrieving-firehose-contents.md)
+ [Examples of event data that Amazon SES publishes to Firehose](event-publishing-retrieving-firehose-examples.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Email Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
