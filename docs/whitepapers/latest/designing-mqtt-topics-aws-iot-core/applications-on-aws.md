---
source_url: https://docs.aws.amazon.com/whitepapers/latest/designing-mqtt-topics-aws-iot-core/applications-on-aws.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Applications on AWS
<a name="applications-on-aws"></a>

 The following sections provide use cases for implementing MQTT topic best practices using AWS IoT.

## MQTT command topics example
<a name="mqtt-command-topics-example"></a>

 For a smart door lock application, a user must be able to submit a command to the lock that initiates a temporary key to be issued for an approved visitor. The temporary key consists of a TTL, code, and information about the authorized user.

 The ability to create a temporary key allows another individual to open the lock for a specified period. This use case would apply in scenarios such as visiting family member arriving at the home while the primary owner is at work.

This scenario assumes the following details:
+  The homeowner has a mobile device ID of `mobile-1`
+  The approved visitor has a mobile device ID of `mobile-2`
+  The smart lock is installed as part of a group of other locks in the home. The set of locks has a context for `groupId` where `groupId` equals `group-3`
+  The smart lock for the front door has a `lockId` of `lock-1`
+ The smart lock hardware has a series number of `series100`. The series is a unique identifier for this product version.

### Command request to generate a smart lock code
<a name="command-request-to-generate-a-smart-lock-code"></a>

 The primary owner first publishes a command to the lock requesting a temporary access code created for an approved visitor. The command payload includes the identification of the homeowner’s mobile device, a randomly generated session identifier for tracking the current request, an action field that contains the type of command, and a topic field. The smart lock uses the topic in the topic field for publishing its response back to the homeowner.

![Mobile user requests temporary credentials for the front door](http://docs.aws.amazon.com/whitepapers/latest/designing-mqtt-topics-aws-iot-core/images/image8.png)

*Mobile user requests temporary credentials for the front door *

Augment MQTT messages using any internal standards for requests, responses, and telemetry. For example, by adding in the requestor of the command in the payload, applications can specify different response topics based on the use case. If the homeowner requests a temporary lock but needs the response to reach all door locks in the home, the topic field could be changed to send to a group of devices.

### Command processing on the smart lock
<a name="command-processing-on-the-smart-lock"></a>

 The smart lock receives the command message from the MQTT topic. By leveraging a consistent naming schema for commands in this application, the smart lock can ensure that it only receives commands on its specific command topic. This topic design also makes it possible for the lock to subscribe using a single level MQTT wildcard after its identifier.

 The single level wildcard command is backward compatible as the IoT application adds new command types. The following example is a simplified example to show the topic structure. Consider using device attributes and policy variables restricting the topic(s) that a device can subscribe or publish to.

![AWS IoT Core sending command to Smart Lock 1 with JSON payload for passcode generation.](http://docs.aws.amazon.com/whitepapers/latest/designing-mqtt-topics-aws-iot-core/images/image9.png)

After receiving the MQTT payload, the smart lock parses the command request to determine what type of action to run. In this case, the command is related to credentials. The device also extracts the client ID, the session ID, and the response topic from the command payload.

Because a home can have multiple authorized homeowners, the client ID determines which homeowner has requested this change. In this example, the action field includes the type of credentials request, generate-password, and the associated user for the temporary key. Last, the device obtains the response topic field in the MQTT message and uses this information to publish its response.

![Smart Lock publishing response with client ID, session ID, passcode, and success code to AWS IoT Core.](http://docs.aws.amazon.com/whitepapers/latest/designing-mqtt-topics-aws-iot-core/images/image9b.png)

* Smart lock response published to AWS IoT Core*

### Command response delivered to the mobile client
<a name="command-response-delivered-to-the-mobile-client"></a>

The homeowner's mobile client subscribes to command responses for any smart locks in the group. Whenever the mobile client receives a successful command response, the temporary code along with any additional authorization permissions can be processed on the device and simultaneously stored in the AWS Cloud. Later, the authorized visitor can use the temporary code along with additional security credentials, such as exchanging for OAuth credentials, proving local presence to the door, and so on, to apply the temporary code to the smart lock.

In this workflow, the application used a command topic for a single device. However, a similar workflow may be used to request commands for multiple devices in a group, such as locking all of the doors in the home.

![Mobile client sending request to AWS IoT Core with JSON payload containing client ID, session ID, passcode, TTL, and response code.](http://docs.aws.amazon.com/whitepapers/latest/designing-mqtt-topics-aws-iot-core/images/image10.png)

* Command response sent from AWS IoT Core to mobile client *

## MQTT telemetry topics example
<a name="mqtt-telemetry-topics-example"></a>

 This section is an example of aggregating telemetry from a set of occupancy sensors that are placed throughout a building to monitor room usage. The occupancy sensors communicate to a local gateway that is running [AWS IoT Greengrass](https://aws.amazon.com/greengrass/). AWS IoT Greengrass. AWS IoT Greengrass then delivers all sensor metrics on an MQTT topic to AWS IoT Core. Because this use case is focused on telemetry, a response topic is not needed between AWS IoT Greengrass and AWS IoT Core, either locally or upstream.

 This scenario assumes the following details:
+  The occupancy sensors have IDs of `occupancy-1` and `occupancy-2`
+  The building is called `building-fresco`
+  Each sensor is placed on a specific floor and within a specific room name in `building-fresco`.
+  The AWS IoT Greengrass local gateway has a unique identifier of `gateway-1`
+  The current building automation system correlates to an internal project called `acme`

### Local telemetry from occupancy sensor to AWS IoT Greengrass
<a name="local-telemetry-from-occupancy-sensor-to-greengrass"></a>

 Each occupancy sensor publishes an occupancy reading once per minute and whenever a person enters or leaves the room. Because the occupancy sensors do not correlate precisely to the state of the device and instead refer to the state of the room, the sensor publishes the room status on a telemetry topic. The payload includes a timestamp, occupancy count, and any efficiency countdown for turning off lights if a room is vacant. The occupancy sensor uses an MQTT topic that includes the contextual information about the position of the sensor within the building and its associated project. A AWS IoT Greengrass core receives all occupancy sensor data locally.

![Occupancy sensor publishing to dt/acme/building-fresco/room4/occupancy-1 topic to AWS IoT Greengrass.](http://docs.aws.amazon.com/whitepapers/latest/designing-mqtt-topics-aws-iot-core/images/image15.png)

* Local occupancy sensor publishes sensor reading to AWS IoT Greengrass *

### AWS IoT Greengrass telemetry from Edge to cloud
<a name="greengrass-telemetry-from-edge-to-cloud"></a>

 In this example, the primary role of AWS IoT Greengrass is to aggregate the data from multiple occupancy sensors then send the data to AWS IoT Core. Because AWS IoT Greengrass is the local bridge to the cloud, AWS IoT Greengrass adds metadata to each sensor reading.

AWS IoT Greengrass adds building information to each message to show the overall usage of the building in 5-minute increments. AWS IoT Greengrass also augments the MQTT topic by including the appropriate application identifier, `acme`.

![AWS IoT Greengrass publishing JSON payload with occupancy data to AWS IoT Core topic.](http://docs.aws.amazon.com/whitepapers/latest/designing-mqtt-topics-aws-iot-core/images/image16.png)

*AWS IoT Greengrass aggregates and augments telemetry, then forwards messages to AWS IoT Core*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
