---
source_url: https://docs.aws.amazon.com/whitepapers/latest/designing-mqtt-topics-aws-iot-core/mqtt-communication-patterns.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# MQTT communication patterns
<a name="mqtt-communication-patterns"></a>

 IoT applications support multiple communication scenarios, such as device-to-device, device-to-cloud, cloud-to-device, and device-to-or-from-users. Although the range of patterns can significantly vary, a majority of MQTT communication models derive from three MQTT patterns: point-to-point, broadcast, and fan-in.

## Point-to-point
<a name="point-to-point"></a>

 A point-to-point communication pattern is one of the basic building blocks of how devices commonly send and receive messages in MQTT. Two devices use a single MQTT topic as the communication channel. The device that receives the event subscribes to an MQTT topic. The thing that sends the message publishes to the same known MQTT topic. This approach is common in smart home scenarios where an end user receives updates about the thing in the home. In the following example, the room occupancy publishes a message on a topic subscribed to by an application running on the digital display outside the screening room.

![One-to-one messaging in point-to-point communication](https://docs.aws.amazon.com/whitepapers/latest/designing-mqtt-topics-aws-iot-core/images/one-to-one-point-to-point.png)

* One-to-one messaging in point-to-point communication *

 Point-to-point communication is not limited to one-to-one communication between devices. Point-to-point is also used in one-to-many communication where a single publisher can publish to individual devices using a different MQTT topic per device.

This approach is common in notification scenarios where an administrator sends distinct updates to specific devices. In the following example, the repair service uses a set of point-to-point communications to programmatically loop through a list of appliances and publish a message.

![Repair service publishes messages to AWS IoT Core, which routes to subscribed devices.](https://docs.aws.amazon.com/whitepapers/latest/designing-mqtt-topics-aws-iot-core/images/one-to-many-point-to-point.png)

* One-to-many messaging in point-to-point communication *

## Broadcast
<a name="broadcast"></a>

 Broadcast patterns are used for one-to-many messaging. The broadcast pattern sends the same message to a large fleet of devices. In a broadcast, multiple devices subscribe to the same MQTT topic, and the sender publishes a message to that topic. A typical use of a broadcast pattern is to send a notification to devices based on the category or group of the device. For example, a weather station transmits a broadcast message based on a topic based on its geolocation.

 The following illustration depicts an example where a broadcast pattern sends a message on a weather topic that all delivery vehicles in the state subscribe to. The message includes weather conditions and detailed location coordinates. Based on the current location of the vehicle, it can ignore the message or take some action.

![Weather station publishes snow forecast to AWS IoT Core, which broadcasts to vehicles.](https://docs.aws.amazon.com/whitepapers/latest/designing-mqtt-topics-aws-iot-core/images/one-to-many-broadcast.png)

* One-to-many messaging in broadcast communication *

## Fan-In
<a name="fan-in"></a>

 The fan-in pattern is a many-to-one communication pattern and can be thought of as the reverse of the broadcast pattern.

Multiple devices publish on a shared or similar topic with a single subscriber to that topic. With the fan-in pattern, the subscriber may use wildcards as the publishers all use a similar but unique MQTT topics. The fan-in pattern is commonly used to aggregate telemetry data.

 In the following example, each device publishes to an MQTT topic containing a known group identifier. The AWS IoT Rules Engine uses a wildcard subscription to receive the messages and route them to an [Amazon Kinesis](https://aws.amazon.com/kinesis/) stream. Specifically, the air quality sensors publish on a fan-in topic associated with a specific building (LAX002). The administrative system receives all updates for the building using an MQTT wildcard (\+).

Rule: Select environment/building/lax002/airqual/\+

![IoT sensors publishing temperature and PPM data to IoT Core, filtered by IoT Rule to Kinesis.](https://docs.aws.amazon.com/whitepapers/latest/designing-mqtt-topics-aws-iot-core/images/many-to-one-fan-in.png)

* Many-to-one communication in a fan-in pattern *

 When devices communicate via the cloud using MQTT, avoid using the fan-in pattern to a single subscribing end device, because this routing may hit a non-adjustable limit on a single device MQTT connection. Instead, use the fan-in pattern to route a large fleet of messages to your IoT application via the AWS IoT Rules Engine.

For large scale fan-in scenarios, combine the Rules Engine with a wildcard subscription pattern and a Rules Engine action to route to Amazon Kinesis Data Streams, Amazon Data Firehose, or [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/).
