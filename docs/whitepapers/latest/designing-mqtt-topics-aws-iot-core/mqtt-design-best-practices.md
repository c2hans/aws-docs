---
source_url: https://docs.aws.amazon.com/whitepapers/latest/designing-mqtt-topics-aws-iot-core/mqtt-design-best-practices.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# MQTT design best practices
<a name="mqtt-design-best-practices"></a>

## General best practices
<a name="general-best-practices"></a>

 Although there are numerous combinations of IoT communication patterns that share common approaches, there are several best practices that apply to any message pattern irrespective of how a device is publishing or receiving a message. This section articulates several overall best practices for you to review and implement as you design your MQTT topic structures.

 **Review the AWS IoT Core default service limits.** Design your communication pattern so that it aligns with any adjustable IoT [service limits](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_iot). AWS IoT has several adjustable and non-adjustable limits associated with using the AWS IoT Core service. As part of your topic review, review the AWS IoT limits, and ensure your MQTT topic and device communication do not conflict with any service limits.

 The maximum number of forward slashes (/) in the MQTT topic name for AWS IoT Core is seven. You should not prefix the topic with a forward slash as it counts towards the topic levels and may introduce confusion when building AWS IoT policies. This excludes the first three slashes in the mandatory segments for Basic Ingest topics `$AWS/rules/rule-name/`.

 The topic passed to AWS IoT Core when sending a publish request can be no larger than 256 bytes of UTF-8 encoded characters. This excludes the first three mandatory segments for Basic Ingest topics `$AWS/rules/rule-name/`.

 *Define a consistent naming standard for MQTT topic levels.* Since MQTT topics are case sensitive, it is important to use a standard set of naming conventions when designing MQTT topics. For this reason, customers should only use lowercase letters, numbers, and dashes when creating each topic level. Customers should avoid camel casing and using hard to debug characters such as spaces. Publish Topic names cannot contain wildcards (\# , \+). Topics that start with $ are reserved by AWS IoT Core. They are not supported for publishing and subscribing except for using the specific topic names defined by AWS IoT Core services (for example, the AWS IoT Device Shadow service).

 **Ensure MQTT topic levels structure follows a general to specific pattern.** As topic scheme flows left to right, the topic levels flow general to specific. For example, an HVAC system is associated with an IoT platform named **hv100**, is located in the **basement** of building **bld1518**, and has a Thing Name of **hvac719**. The topic structure begins with the general group, in this case, the name of the IoT platform, and ends with the most specific identity, the Thing Name. This example creates the following topic level structure:

![MQTT topic structure showing hierarchy from general hv100/bld1518/basement to specific hvac719.](https://docs.aws.amazon.com/whitepapers/latest/designing-mqtt-topics-aws-iot-core/images/topic-level-structure.png)

 **Include any relevant routing information in the MQTT topic.** Relevant routing information includes, but is not limited to, the IoT application identifier, any groups the device may be a part of, such as installed location, and the unique identity of your IoT device. To continue with the previous HVAC system example, the MQTT topic `hv100/bld1518/basement/hvac719` includes all relevant routing information. Based on this MQTT topic, you can design a system that captures any data related to the entire application using the identifier, `hv100`, but also can target different areas of interest for subscribing to messages, such as the building location.

 **Prefix your MQTT topics to distinguish data topics from command topics.** Make sure that your MQTT topics do not overlap between commands and data messages. By reserving the first topic level to denote data and command topics, you are more easily able to create fine-grained permissions using IoT policies, and monitor the status of commands and command responses separately from passive telemetry commands. For example, use the AWS IoT Device Shadow service for tracking reported and desired states, and use a separate data topic for passive, real-time telemetry data.

 **Document proposed MQTT topic structures as part of your operations practice.** The document should include all topics available for publishing, subscribing, or receiving data, along with the intended producers and consumers of the data. Review the document to ensure it adheres to any AWS IoT limits, internal security requirements, and any application use cases.

 **Include the Thing Name of the device in any MQTT topic the device uses for publishing or subscribing to its data.** To track messages destined for a particular device, include the Thing Name as part of any MQTT message that is published by the device or sent to a specific device. The Thing Name should appear near or at the end of the MQTT topic after any routing topic information.

 **Include additional contextual information about a specific message in the payload of the MQTT message.** This contextual information includes, but is not limited to, a session identifier, the requestor identifier, logging information, or the return topic on which a device is expecting to receive a response. Although the [MQTT 3.1.1 specification](http://docs.oasis-open.org/mqtt/mqtt/v3.1.1/csprd02/mqtt-v3.1.1-csprd02.html) does not require specific payload attributes, we recommend you include relevant tracking information inside of the MQTT payload. By creating a standard structure including fields such as session identifier and success or error codes, you can more easily analyze trends in device behavior. Standardizing the communication schema also strengthens a shared vernacular of device use cases across IoT teams.

 **Avoid MQTT communication patterns that result in a sizeable fan-in scenario to a single device.** Some AWS IoT limits cannot be raised as part of a limit increase and frequently correlate to per device actions, such as maximum publish-in on a single MQTT connection. Do not allow a single device to subscribe to a shared topic that is being published to by a large number of other devices. By avoiding this pattern, you are more likely to avoid hitting a single connection device limit, particularly a throughput per connection per second limit.

 **Never allow a device to subscribe to all topics using \#, and only use multi-level wildcard subscriptions in IoT rules.** By using multi-level wildcards, you can create unintended consequences when you inadvertently add new topics to the hierarchy that may not be intended for that particular device. Instead, reserve use of multi-level wildcards as part of the IoT rules engine, and use single level wildcards (\+) for device subscriptions.

## Best practices for telemetry
<a name="best-practices-for-telemetry"></a>

 Telemetry is read-only data that is transmitted by the device and processed in the cloud. It follows the device-to-cloud pattern along with the fan-in pattern for communication.

Telemetry does not require an acknowledge message back from the MQTT broker, beyond optionally setting a higher quality of service (QoS) level. Since telemetry is a passive activity, the MQTT topic for telemetry should not overlap with any MQTT topics for active workflows, such as command and control messages.

 A telemetry topic supports more complex devices that publish telemetry on behalf of other devices, such as an edge gateway or a mesh network with a single coordinator.

 In AWS IoT, you have the ability to use different AWS IoT services to support telemetry communication patterns. We recommend that you use a combination of AWS IoT Basic Ingest and standard MQTT topics to support your telemetry use cases.

### Using AWS IoT Basic Ingest for telemetry
<a name="basic-ingest"></a>

 Basic Ingest optimizes data flow for high volume data ingestion workloads by removing the pub/sub Message Broker from the ingestion path. As a result, you have a more cost-effective option to send device data to other AWS services while continuing to benefit from all the security and data processing features of AWS IoT Core.

In cases where devices do not require the publish and subscribe functionality of the Message Broker, Basic Ingest enables you to send data to cloud services through the Rules Engine.

 Basic Ingest is an ideal use case for telemetry when the only interested subscriber for an IoT message is your backend IoT application. Basic Ingest uses a reserved MQTT topic structure that is associated to a particular AWS IoT Rule.

A device can publish to the reserved topic associated to a specific AWS IoT Rule, and Basic Ingest will trigger the IoT Rule for the matching Rule Name. The MQTT topic structure for Basic Ingest follows a similar syntax as the following example:

```
$aws/rules/<rule-name>/<optional-customer-defined-segments>
```

 Where the field `rule-name` matches the name of the AWS IoT Rule that should be invoked, and `optional-customer-defined-segments` includes any additional topic levels a customer may use for routing or logging as part of the AWS IoT Rule Action.

#### Best practices for using AWS IoT Basic Ingest
<a name="best-practices-basic-ingest"></a>

**Include any additional routing information after the rule name in the Basic Ingest MQTT Topic.** As a best practice, AWS recommends you use the optional segments that can appear after the rule name in the MQTT topic to include relevant additional information that can be used by the AWS IoT Rule for features such as [Substitution Templates](https://docs.aws.amazon.com/iot/latest/developerguide/iot-substitution-templates.html), [IoT Rule SQL Functions](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-functions.html), and [Where Clauses](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-where.html). Similar to the overall best practice for MQTT topics, any fields that can be used for IoT Rule evaluation, such as application Identifier or device Identifier, should be appended to the end of the Basic Ingest topic. The following example would be publishing to an AWS IoT Rule named BuildingSecurity followed by customer defined segments:

 `$aws/rules/BuildingSecurity/buildings/warehouse4/section6/motion`

**Choose short, descriptive rule names for Basic Ingest.** When AWS IoT Rules are used directly by devices via Basic Ingest, AWS recommends that you ensure the rule name follows MQTT topic best practices for consistency. Since the rule will link directly to a reserved MQTT topic, ensure that the rule name is short, descriptive of the underlying use case of the rule, and adheres to the syntax rules described in the section [General best practices](#general-best-practices).

### Using the MQTT topics for telemetry
<a name="using-the-mqtt-topics-for-telemetry"></a>

In addition to using Basic Ingest, you can also leverage traditional MQTT topics. These types of MQTT messages are passive AWS IoT data that may be subscribed to by other devices now or in the future.

For example, a device that sends its current status may expect its data to be routed not only to your internal application but also to a user who needs the device’s current status. To achieve this level of flexibility, you can use standard MQTT topics for sending and receiving telemetry.

#### MQTT telemetry topic syntax
<a name="mqtt-telemetry-topic-syntax"></a>

 The following example and sections provide the MQTT topic structure for telemetry:

```
dt/<application>/<context>/<thing-name>/<dt-type>
```

 **dt:** Set prefix that refers to the type of message. For a telemetry topic, we use `dt`, short for data. All telemetry topics use this top-level prefix for an application. By reusing the same value for telemetry, you can identify the intent of a message by referring to the initial prefixed value. In this case, any `dt` topic is a telemetry topic.

 **application:** Identifies the overall IoT application associated with the device. Commonly used application attributes include device hardware version or an internal identifier for a cloud application that is the primary ingestion point for a message. The IoT application is associated with an internal name for your overarching IoT product or relates specifically to the type of hardware of your device. Because the application topic portion correlates to a group of device messages and is immutable, the application prefix portion of the telemetry MQTT topic is placed immediately after the `dt` message type.

 **context:** Single or multiple levels of additional contextual data about the message a device is publishing. Contextual information is related to information that is set during device provisioning. For example, contextual information in a factory setting could include the current physical location of a device in the facility. Another example of contextual information is a group-id in the MQTT topic. The group-id denotes when multiple devices have an inherent relationship based on specific attributes, such as buying a package of smart light bulbs to control lighting in a room. The group-id enables numerous devices to coordinate activities as a single unit.

 **thing-name:** Identifies which device is transmitting a telemetry message.

 **dt-type (optional):** Associates a message with a particular subcomponent of a device, or for edge gateways, any downstream devices. A complex device often has multiple subcomponents with specific tasks, such as sensors, actuators, or separate system on chips (SOCs). The `dt-type` allows you to associate each subcomponent of a particular device to an individual MQTT topic. One example of this is a subcomponent that measures geolocation and direction of a vehicle. That subcomponent would have a `dt-type` value of `geo` to distinguish its geolocation messages from other components of the car, such as the accelerometer.

## Best practices for commands
<a name="best-practices-for-commands"></a>

 In IoT applications, command topics are used to control a device remotely and to acknowledge successful command executions. Unlike telemetry, command topics are not read-only. Commands are a back and forth workflow that can occur between two devices or between the cloud and devices. Because commands are actionable messages, isolate the MQTT topic for command messages from telemetry topics.

 Several services are available for you to implement command and control operations on AWS IoT. With the capability to store the desired and reported states in the cloud, the AWS IoT Shadow is the preferred AWS IoT service for implementing individual device commands. AWS IoT Device Jobs should be used for fleet-wide operations as it provides extra benefits, such as Amazon CloudWatch metrics for Job tracking, and the ability to track multiple in-transit Jobs for a single device. You can use a combination of the AWS IoT Shadow, AWS IoT Jobs, and standard MQTT topics to support your command use cases.

### Using the AWS IoT Shadow for commands
<a name="using-the-aws-iot-shadow-for-commands"></a>

 [The AWS IoT Device Shadow](https://docs.aws.amazon.com/iot/latest/developerguide/iot-device-shadows.html) service acts as a state intermediary, allowing devices and applications to retrieve and update a device’s shadow state. You can use the shadow to get and set the state of a device over MQTT or HTTP. The shadow includes the following individual state properties that support command and control:

 **desired state.** Applications that have permissions to send commands to a device can write the requested state changes to the desired portion of the shadow document. By updating the desired state, the AWS IoT Shadow service stores the desired state change in the AWS cloud and then sends an MQTT message to the device using a reserved shadow topic. When a device receives a shadow request, it can execute the changes required from the desired state.

 **reported state.** The reported state of the AWS IoT Thing’s shadow stores the last published attributes published by a device. Devices write to this portion of the document to record their new state while applications read this portion of the Shadow to determine the state of a specific device. Because shadows are stored by AWS in the cloud, they can collect and report device state data from apps and other cloud services whether the device is connected or not. Use the AWS IoT Shadow in situations where a command persists for later use, even if the device is currently offline. For example, if a GPS system is sent a new destination through the Shadow desired state but is not immediately reachable, the new coordinates remain in the GPS IoT Shadow. Once the GPS system regains connectivity, it can actively request its last shadow state and retrieve the new coordinates. The shadow is also ideal for storing the last reported state for attributes of the device.

#### Best practices for using the AWS IoT Classic Shadow or Named Shadows
<a name="best-practices-for-using-the-aws-iot-shadow"></a>

 The AWS IoT is a mechanism for command and control along with storing the reported state of a specific device.

The following list of best practices offers advice on maximizing the efficiency of commands through the shadow:

 **IoT devices should not share shadows.** To separate commands for each device, make sure that each device has permissions to its own shadow and that devices do not share a single shadow. For complex scenarios, like edge gateways or large device assets with multiple subcomponents, the primary asset should use multiple IoT Things and shadows individually associated with the downstream devices.

*Consider using Named Shadows to create logical groups of properties.* You can create a unique access policy for each Named Shadow, therefore controlling what applications or services can view or update that group of properties. An example of this would be the device management team viewing the firmware, battery health, or WiFi signal strength but not having access to the data being published by the sensors on said devices.

 **Use the shadow for state or commands that have a medium to low transaction per second (TPS).** The shadow is an ideal fit for infrequent updates that occur in minutes, hours, or days as the shadow publishes on additional topics to acknowledge an action was successful. For a high frequency or throughput commands that do not require the updates to the shadow consider publishing to a MQTT command topic.

 **Use the shadow for storing status metrics of a device.** Store informational data about the current health of the device including, but not limited to, connectivity, the status of device sensors and control units, and any error information about those subcomponents. If you know the current status of the device, you can make actionable decisions during command requests.

 **Use the AWS IoT Device Shadow service to catalog the current firmware version.** The shadow is an ideal location for a device to report the firmware version installed on the hardware. The firmware should be a simple attribute, such as a field that highlights the `major.minor.patch` version of the service.

 **Use the optional `clientToken` field with AWS IoT Device Shadow service updates to track the sender of a shadow message.** The `clientToken` is a field in the Shadow that enables a subscriber to associate the responses with requests in your MQTT application. If a device sets the `clientToken` during a shadow update request, the AWS IoT Shadow service includes that same `clientToken` in the associated shadow output events.

### Using AWS IoT Jobs for Commands
<a name="using-the-aws-iot-jobs-for-commands"></a>

 AWS IoT Jobs is a service that allows you to define a set of remote operations that are sent to and executed on one or more things connected to AWS IoT. For command use cases, Jobs allows applications to run tasks that require executing multiple steps. An AWS IoT Job contains instructions that the thing must run to complete its transaction. AWS IoT Jobs are the recommended feature for fleet-wide operational tasks, such as software updates, that are only executed by trusted administrators of the entire IoT application.

#### Best practices for using AWS IoT Jobs
<a name="best-practices-for-using-the-aws-iot-jobs"></a>

 **Use thing groups to organize devices for AWS IoT Jobs**. Create multiple thing groups organized by common device attributes, such as the current firmware version, hardware version, or deployment environments (for example, staging or production). Thing groups should also have common hierarchical structures, such as business units or locations. During deployments, you can use thing groups as the deployment target for a specific IoT job.

 **Use staged rollouts to deploy commands using Device Jobs.** Device Jobs are the ideal solution for delivering fleet-wide operations to devices. Create multiple smaller deployments first, to subsets of the fleet, letting the devices apply your changes, and then rolling out the commands to a greater number of devices over time. By allowing changes to progress over weeks and months, you can have more confidence that there are fewer unforeseen issues and you can react more quickly if there is an issue during an earlier rollout.

### Using the MQTT topics for commands
<a name="using-the-mqtt-topics-for-commands"></a>

#### MQTT command topic syntax
<a name="mqtt-command-topic-syntax"></a>

 In some scenarios, you may want to design your command communication using the standard MQTT publish and subscribe model. These types of situations may occur when a device must execute a command that is temporal (that is, can only be processed at this current type and should fail if the device is unavailable) or run a single command across multiple devices simultaneously.

It is also possible in a brownfield environment where a device may be incapable of leveraging higher-level AWS IoT services. You may also require the flexibility to choose your own set of MQTT topics to define commands to and responses from devices.

 In cases where you are using a separate set of command topics, follow similar best practices for MQTT command topics as described for telemetry. A command topic should have flexibility for complex devices that publish or relay commands to other devices. Command topics should also provide visibility into essential attributes. MQTT command topics should be designed in a way that can answer operational questions based on the MQTT topic and payload:
+  Who is the originator of the command?
+  Who is the intended receiver of the command?
+  Was the command processed successfully?
+  What is the current status of the command?
+  If the command was not processed successfully, what is the error?

 In addition to these questions, you may also want to determine when a command was requested, when a device responded, and to monitor the state of any single request among the fleet in the cloud.

 When you design MQTT topics for command requests, follow this structure:

```
cmd/<application>/<context>/<destination-id>/<req-type>
```

 Since commands are two-way communication patterns, design a similar MQTT topic structure for responding to commands, such as the following:

```
 cmd/<application>/<context>/<destination-id>/<res-type>
```

 Because telemetry topic design is similar to command topic design, this section provides only the portions of the IoT topic for command requests and responses that differ.

 **cmd:** Prefix that refers to the type of message. Command topics use `cmd`, which is short for command. By prefixing all commands with `cmd` and all telemetry with `dt`, telemetry and commands are isolated on separate MQTT topics.

 **req-type:** Classifies the command. For simple request and response patterns, the req-type attribute should be a single command request static value such as `req`. In cases of limited command types, the MQTT message includes the additional data in the payload.

 In more complex systems, where a device is orchestrating multiple devices, actuators, or subcomponents, the `req-type` attribute relates to each subcomponent available to receive commands. For example, if a device is mobile, you may want to steer the device remotely or receive navigational information about the device's surroundings. This type of subcomponent would have a `req-type` of `nav` where commands are sent steering in single or multiple planes.

 **destination-id:** Identifies the destination device or application for this message. By including the `destination-id`, the target device can subscribe to its own set of command topics and receive any command requests.

 **res-type:** Denotes command responses and identifies responses that are related to a previously sent command. The `res-type` enables a single device to use one single-level wildcard subscription for all incoming command acknowledgments. If a device has limited commands, the response topic can use a static field, such as `res`.

#### MQTT command payload syntax
<a name="mqtt-command-payload-syntax"></a>

 In addition to creating a clear MQTT topic structure for commands, make sure that you generate a schema for message payloads. MQTT payload information is parsed by the receiving device or IoT application, to inform it of any additional logic it may need to complete its operation. For MQTT commands, include the following fields with the command message payload:

 **session-id:** Identifies a unique session. The requestor generates the `session-id` for the command and includes it in the request payload. The response topic uses the session-id upon command completion. By using a `session-id`, the AWS IoT Rules Engine can store and track the status of commands and determine if a request is still in transit, successful, or in error. Devices can also keep track of in-transit requests when communicating with multiple devices.

 **response-topic**: In a command, there is a request for an action to happen and then a response that indicates the status of the command (successful or error). To avoid hard-coding response topics, we recommend that for any MQTT command, the command request payload includes a field that has a response topic. The device publishes its response payload using the response topic. For example, consider the following command topic:

```
 cmd/security/device-1/cert-rotation
```

 In the payload of this request, the IoT application includes a field that denotes where the device (`device-1`) should send its response and a session identifier for tracking. See the following example for this command’s payload structure:

```
{
   "session-id":"session-820923084792",
   "res-topic":"cmd/security/app1/res"
}
```
