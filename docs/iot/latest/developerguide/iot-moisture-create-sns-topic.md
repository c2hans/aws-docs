---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/iot-moisture-create-sns-topic.html
---

# Step 3: Create an Amazon SNS topic and subscription
<a name="iot-moisture-create-sns-topic"></a>

Create an Amazon SNS topic and subscription.

1. From the [AWS SNS console](https://console.aws.amazon.com/sns/home), in the navigation pane, choose **Topics**, and then choose **Create topic**.

1. Choose type as **Standard** and enter a name for the topic (for example, **MoistureSensorTopic**).

1. Enter a display name for the topic (for example, **Moisture Sensor Topic**). This is the name displayed for your topic in the Amazon SNS console.

1. Choose **Create topic**.

1. In the Amazon SNS topic detail page, choose **Create subscription**.

1. For **Protocol**, choose **Email**.

1. For **Endpoint**, enter your email address.

1. Choose **Create subscription**.

1. Open your email client and look for a message with the subject **MoistureSensorTopic**. Open the email and click the **Confirm subscription** link.
**Important**
You won't receive any email alerts from this Amazon SNS topic until you confirm the subscription.

You should receive an email message with the text you typed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
