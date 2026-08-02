---
source_url: https://docs.aws.amazon.com/whitepapers/latest/designing-mqtt-topics-aws-iot-core/communication-workflows.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Communication workflows
<a name="communication-workflows"></a>

 The three common communication workflows are device-to-device, device-to-cloud, and cloud-to-device. Each workflow determines the topic structure of topic hierarchy. In the case of device-to-device, MQTT topics should contain identifiers for either the sender or receiver of a message. For device-to-cloud, MQTT messages should include information about the target application. The target application is responsible for augmenting any MQTT messages with internal metadata about the device. Last, for cloud-to-device communication, MQTT messages should contain session information for tracking acknowledgment of any critical messages.
