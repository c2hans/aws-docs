---
source_url: https://docs.aws.amazon.com/ses/latest/dg/monitor-sending-using-event-publishing-setup.html
---

# Setting up Amazon SES event publishing
<a name="monitor-sending-using-event-publishing-setup"></a>

This section describes what you need to do to configure Amazon SES to publish your email sending events to the following AWS services:
+ Amazon CloudWatch
+ Amazon Data Firehose
+ Amazon Pinpoint
+ Amazon Simple Notification Service (Amazon SNS)

The following steps required for setting up event publishing are covered in the topics below:

1. You must create a *configuration set* using the Amazon SES console or API.

1. Add one or more *event destinations* (CloudWatch, Firehose, Pinpoint, or SNS) to the configuration set, and configure parameters unique to the event destination.

1. When you send an email, you specify which configuration set to use that contains your event destination.

**Topics**
+ [Step 1: Create a configuration set](event-publishing-create-configuration-set.md)
+ [Step 2: Add an event destination](event-publishing-add-event-destination.md)
+ [Step 3: Specify your configuration set when you send email](event-publishing-send-email.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Email Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ses` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
