---
source_url: https://docs.aws.amazon.com/whitepapers/latest/designing-mqtt-topics-aws-iot-core/communication-workflows.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Communication workflows
<a name="communication-workflows"></a>

 The three common communication workflows are device-to-device, device-to-cloud, and cloud-to-device. Each workflow determines the topic structure of topic hierarchy. In the case of device-to-device, MQTT topics should contain identifiers for either the sender or receiver of a message. For device-to-cloud, MQTT messages should include information about the target application. The target application is responsible for augmenting any MQTT messages with internal metadata about the device. Last, for cloud-to-device communication, MQTT messages should contain session information for tracking acknowledgment of any critical messages.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
