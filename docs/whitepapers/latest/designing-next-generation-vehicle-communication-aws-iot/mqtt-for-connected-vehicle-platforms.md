---
source_url: https://docs.aws.amazon.com/whitepapers/latest/designing-next-generation-vehicle-communication-aws-iot/mqtt-for-connected-vehicle-platforms.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# MQTT for connected vehicle platforms
<a name="mqtt-for-connected-vehicle-platforms"></a>

 Over the years, MQTT has been adopted as the industry standard communication protocol for connected vehicle platforms. MQTT allows for a persistent, always-on connection between the vehicle and the cloud. With intermittent connectivity to the cloud, MQTT effortlessly handles buffering queuing and synchronizing when connectivity is re-established. Residing on top of the TCP/IP network stack, MQTT is a lightweight publish/subscribe messaging protocol designed for low-bandwidth, high latency and unreliable networks. These features make it the de facto standard in the industry to send high volumes of vehicle sensor data to the cloud.

 Unlike a traditional client-server model where the client communicates directly with a specified endpoint, MQTT clients fall into two separate categories: publishers and subscribers. The publishers in most connected vehicle use cases will be the vehicles, and the subscribers will be the processors of that telemetry data by downstream cloud services. The publisher and subscriber are isolated from each other and are completely decoupled and never communicate directly with each other, providing extensibility to writing applications at the edge or in the cloud. Between the publisher and subscriber, the MQTT message broker handles routing of the messages from the publisher to any endpoint subscribed to a specific topic.

 The message broker handles the management of topics (how publishers and subscribers communicate), the distribution of messages to subscribers and many other functions to ensure acceptance and delivery of the messages. AWS IoT Core offers this functionality as a managed broker, so no code, setup, or provisioning is necessary by the customers to begin working with MQTT on AWS IoT Core.

 Recently, the MQTT specification was updated to from version 3.1.1 to MQTT version 5. AWS IoT Core has adopted this specification with many new connected vehicle specific features that we will discuss over the next section. With the latest announcement of support for MQTT5, and the features that align to that version of the specification, AWS IoT Core is an industry leading managed message broker for connected vehicle workloads.

 The capability to provide separation of concerns between the publisher and subscribers, the bi-directional communication, the ability to define quality of service for the messages, the lightweight code footprint at the edge and the advanced message retention policies around unreliable networks makes. This makes MQTT an easy choice for delivering connected vehicle workloads to the cloud.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
