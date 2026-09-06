---
source_url: https://docs.aws.amazon.com/whitepapers/latest/designing-next-generation-vehicle-communication-aws-iot/mqttv5-support-on-aws-iot-core.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# MQTTv5 support on AWS IoT Core
<a name="mqttv5-support-on-aws-iot-core"></a>

 Recently, AWS IoT Core announced the General Availability of an upgraded message broker service that now includes support for the MQTT version 5 protocol (MQTTv5). With this release, customers can connect their devices to [AWS IoT Core](https://aws.amazon.com/iot-core/) over MQTTv5, or leverage a mix of MQTTv3 or MQTTv5 connected vehicles interacting with one another to support heterogeneous deployments.

 Working backward from automotive customers, our teams heard feedback on many features necessary to run and support vehicle workloads on AWS, and more specifically on AWS IoT Core. Many automotive customers adhere closely to standards and avoid having custom code from vendors in-vehicle. This provides the flexibility to be multi-cloud and switch brokers in case of ongoing issues. With IoT Core now adhering to the latest MQTTv5 standard, this allows automotive customers flexibility to align to an industry standard like MQTT with their in-vehicle architectures and code, but provides the flexibility to pivot to any number of different cloud message brokers depending on the implementation and customer requirements. Now that AWS IoT Core has adopted MQTTv5, OEMs see the long-term value in IoT Core as a managed broker.

 Automotive customers who already have MQTTv3.1.1 deployments can make use of the new MQTTv5 features as AWS IoT Core provides seamless integration between both versions and supports deployments during the migration process. In the next few sections, we will cover some MQTTv5 features with connected vehicle use cases to show how you can design more flexible and efficient IoT design patterns. We also show how MQTTv5 brings new possibilities for your existing vehicle fleet running AWS IoT Core.

## User properties
<a name="user-properties"></a>

 One of the new features of MQTTv5, user properties introduced basic key-value pairs that developers can append to most MQTT packets in the header, providing a mechanism to add meta-data that can be used in downstream processing of the packet. A customer can use a near unlimited number of user properties to add metadata to MQTT messages and pass information between publisher, broker, and subscriber.

 Utilizing an MQTT broker as a routing and transporting component in large scale data processing and streaming implementation is a well-documented use case. These types of deployments, especially in a connected vehicle vertical, frequently contain several different variations of either devices, firmware or both and so, it is not out of the ordinary for the requirement to be able to handle payloads from different devices or software versions different ways. For example, to ensure backwards compatibility, utilizing the software version to determine which processor to use or to identify a specific payload to be used with real-time streaming and other identification mechanism to route for more analytical storage of the same data. In this case, implementing MQTTv5 user properties can function as a routing mechanism for encoded or compressed payloads without the need for visibility into the message to ensure it is routed appropriately. The MQTT broker can then, with very little overhead, by just inspecting the header of the packet, route certain messages to a specific set of subscribers, based on the value of the fields in user properties. This allows for even more flexible application-level logic for providing message relevance to the proper processors and end state of the telemetry.

## Session expiry
<a name="session-expiry"></a>

 When connecting to the broker, in the CONNECT packet, a connecting client can now set a *session expiry interval* in seconds. This interval defines the period of time that the MQTT broker stores the client's session information and allows the customer to define fixed intervals. For example, if we wanted to set the session expiry to 10 seconds and the client is disconnected, the connected vehicle's session in the AWS IoT Core MQTT broker will be removed along with queued messages. Even if the message expiry intervals allow queuing messages, they won't be received by the connected car since the session is removed after 10 seconds. This allows for more granular control over client connection mechanisms when combined with cloud-side device management of these parameters, more holistic control over the entire fleet.

 In a similar context to the session expiry interval, the primary motivation to add the message expiry interval to the MQTT protocol standard was to implement the capability of automatic deletion of retained messages and additionally allowing more granular control over the payloads. Many connected vehicles are designed to be in a disconnected state for prolonged periods without an internet connection. For connected vehicles, retained messages are used to deliver critical payloads to the vehicle when it comes back online.

 In the disconnected state, messages are retained on the cloud broker and then delivered when the vehicle comes back online and subscribes to the topic. With larger implementations, providing the customer control over the types of messages and how long they are retained on the broker is key to ensuring the message is delivered (or not delivered). For example, a message about a local weather alert or a vehicle accident along the route is only relevant for a limited time. However, ensuring the vehicle receives a message about a pending OTA firmware updates must not expire until the next OTA software update is available to consume.

 Allowing customers to set an appropriate message expiry interval for payloads no longer need to be delivered within a certain amount of time and leaving critically-relevant messages without an expiry ensures that efficiencies, cost and the implementation is delivered appropriately.

## Topic aliases
<a name="topic-aliases"></a>

 The topic aliases feature allows MQTT clients to assign numeric aliases to topics and then refer to the alias when publishing further messages. This allows reduction in the transmitted MQTT packet size by referencing the topic with a single number instead of the topic itself.

 Most vehicles are running cellular devices in the telematics control unit (TCU) and use mobile networks to communicate with their back-end services. These TCUs are designed to operate on the lowest possible bandwidth because of their metered data services. Reducing the size of these transmission is key to sustaining limited power consumption, but more importantly saving on data egress costs on the MNO's network towards the cloud.

## Request/Response
<a name="requestresponse"></a>

 The request/response messaging pattern is a method to track responses to client requests in an asynchronous way. It's a mechanism implemented in MQTTv5 to allow the publisher to specify a topic for the response to be sent for a particular message. Therefore, when the subscriber receives the request, it also receives the topic to send the response. It also supports the correlation data field that allows tracking of packets, for example, request or device identification parameters. This will be reviewed in depth when remote commands are discussed later on in the document.
