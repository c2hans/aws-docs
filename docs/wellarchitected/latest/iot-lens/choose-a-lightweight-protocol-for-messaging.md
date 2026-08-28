---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/iot-lens/choose-a-lightweight-protocol-for-messaging.html
---

# Choose a lightweight protocol for messaging
<a name="choose-a-lightweight-protocol-for-messaging"></a>

 IoT devices can use a number of application layer protocols to communicate with each other as well as the cloud.  The most common protocol for IoT devices is [MQTT](https://mqtt.org/mqtt-specification/).

 MQTT is designed to be a lightweight and power efficient protocol for IoT applications that require low power consumption and low bandwidth usage. It uses a publish-subscribe model, which allows devices to exchange small messages with each other using a minimal amount of network bandwidth.

 HTTP, on the other hand, is a more heavyweight protocol that is used for web-based applications. While HTTP is not specifically designed for IoT applications, it is widely used for sending and receiving data over the internet. HTTP uses a request-response model, which requires devices to send larger amounts of data back and forth over the network. This can result in higher power consumption and shorter battery life for IoT devices.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
