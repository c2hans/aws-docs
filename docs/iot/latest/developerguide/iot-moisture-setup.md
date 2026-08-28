---
source_url: https://docs.aws.amazon.com/iot/latest/developerguide/iot-moisture-setup.html
---

# Setting up AWS IoT
<a name="iot-moisture-setup"></a>

To complete this tutorial, you need to create the following resources. To connect a device to AWS IoT, you create an IoT thing, a device certificate, and an AWS IoT policy.
+ An AWS IoT thing.

  A thing represents a physical device (in this case, your Rasberry Pi) and contains static metadata about the device.
+ A device certificate.

  All devices must have a device certificate to connect to and authenticate with AWS IoT.
+ An AWS IoT policy.

  Each device certificate has one or more AWS IoT policies associated with it. These policies determine which AWS IoT resources the device can access.
+ An AWS IoT root CA certificate.

  Devices and other clients use an AWS IoT root CA certificate to authenticate the AWS IoT server with which they are communicating. For more information, see [Server authentication](server-authentication.md).
+ An AWS IoT rule.

  A rule contains a query and one or more rule actions. The query extracts data from device messages to determine if the message data should be processed. The rule action specifies what to do if the data matches the query.
+ An Amazon SNS topic and topic subscription.

  The rule listens for moisture data from your Raspberry Pi. If the value is below a threshold, it sends a message to the Amazon SNS topic. Amazon SNS sends that message to all email addresses subscribed to the topic.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT Core. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
