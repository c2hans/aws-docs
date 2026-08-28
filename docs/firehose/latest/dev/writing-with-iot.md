---
source_url: https://docs.aws.amazon.com/firehose/latest/dev/writing-with-iot.html
---

# Configure AWS IoT to send data to Firehose
<a name="writing-with-iot"></a>

You can configure AWS IoT to send information to a Firehose stream by adding an action.

**To create an action that sends events to an existing Firehose stream**

1. When creating a rule in the AWS IoT console, on the **Create a rule** page, under **Set one or more actions**, choose **Add action**.

1. Choose **Send messages to an Amazon Kinesis Firehose stream**.

1. Choose **Configure action**.

1. For **Stream name**, choose an existing Firehose stream.

1. For **Separator**, choose a separator character to be inserted between records.

1. For **IAM role name**, choose an existing IAM role or choose **Create a new role**.

1. Choose **Add action**.

For more information about creating AWS IoT rules, see [AWS IoT Rule Tutorials](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules-tutorial.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
