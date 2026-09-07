---
source_url: https://docs.aws.amazon.com/whitepapers/latest/designing-next-generation-vehicle-communication-aws-iot/remote-commands-for-companion-applications.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Remote commands for companion applications
<a name="remote-commands-for-companion-applications"></a>

 For connected vehicle platforms, sending telemetry is one of the more important use cases, but secondary to that, especially as a customer differentiator is the ability to manage the vehicle remotely. Enabling these remote functions will unlock several new features for customers and fleet operators. These use cases are being demanded by the end users, but OEMs have encountered several challenges in meeting those expectations from their customers.

 One of the challenges OEMs encounter is the end-to-end latency around downstream communication and commands with the vehicle. The ability to remote start, utilize a shared digital key, and a find-your-car feature are differentiated value adds to the customer experience in the next generation of vehicles. This is a difficult use case to accomplish for developers when there is limited, spotty or, a majority of the time, no connectivity (because the vehicle is not running) to the cloud platform from the vehicle to send a command.

 Currently, to implement remote commands when the vehicle is disconnected, to the vehicle most OEMs employ a shoulder tap architecture, where sending an SMS message to the device wakes it up and have it check the command queue for processing. The mobile terminated (MT-SMS) that initiates the internet protocol (IP) data session and is supported by current LTE modems that is a low-power or sleep mode which reduces the drain on the battery, but comes at a cost for reliability and speed.

 SMS is generally a reliable mechanism for exchanging messages, but can be troublesome if the cellular connectivity is reduced and without the ability to ACK the receipt of the SMS, produces a poor customer experience, especially in the unlock door use case. Customers have reported anywhere from 10-35 seconds for a remote command initiated by SMS to complete the end-to-end flow from companion application, to the cloud, to the vehicle, and to report success back to the customer.

 With the evolution of cellular technologies this problem becomes less ubiquitous and the OEM can modify the protocols used to receive the remote commands. With LTE Cat M1 or Cat 1 and extended discontinuous reception (eDRX) the device gains the ability in the vehicle to consume up to 10x less battery, a 50% reduction in module cost as compared to Cat 4 devices, and a lower MHz channel that allows for better penetration into parking garages. This requires widespread utilization of CAT M1 within the vehicle networks and has not been widely adopted by OEMs.

 The most common approach to solving the latency problem with remote commands is keep the MQTT connection to the broker open after the vehicle has been turned off, allowing for remote commands to be delivered to the vehicle immediately. In previous model years, keeping the broker connection open when the ignition is off, the battery drain would impact the ability to start the vehicle and so the customer experience suffered. with the evolution of the electric vehicle space and much higher capacity of vehicle batteries,

 OEMs are now enabled create a longer broker connection time upon ignition off. Many OEMs are switching to a longer Keep Alive, sometimes extending it up to seven days after ignition off. The Keep Alive is configured at the start of the MQTT session and requires a PINGREQ from the client and a PINGRESP from the broker ensuring the connection is still open. As these pings keep the connection open, remote commands are received from the native application in near real time and improves the overall customer experience drastically.

## MQTTv5 Request/Response
<a name="mqttv5-requestresponse"></a>

 Using some of the latest features of IoT Core and MQTTv5 can help enhance some of the more crucial customer experiences. Below, in Figure 4, we have a reference architecture that provides high-level guidance around developing a companion application for remote commands on AWS IoT. This implementation provides some basic patterns as described above to implement an architecture that could help provide a much better customer experience when attempting to execute a remote command. The guidance provides several scenarios for managing vehicles remotely, whether the vehicles are connected to the broker or disconnected. AWS IoT Lifecycle events help provide the connection status to the AWS AppSync middleware layer with various subscriptions and resolvers to the persistency state.

 After determining if the vehicle is connected, the backend can use the new request/response pattern (defined in MQTTv5 section) and send commands to the vehicle in the request topic which is paired with a response topic. When a command is executed (successfully or not) the vehicle will then post the result on the response topic which will then be sent back to the front-end application via AWS AppSync custom resolver. When the device is not connected, we provide a mechanism to send the SMS-shoulder tap via Amazon Simple Notification Service (SNS).

**Consumer identity**

 You can build and operate your own identity provider or use a cloud SaaS identity provider. [Amazon Cognito](https://aws.amazon.com/cognito/) is a fully managed identity provider that allows you to add user sign-up and sign-in features and control access to your web and mobile applications. [Amazon Cognito user pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) provides an identity store that scales to millions of users, supports social and enterprise identity federation, and offers advanced security features to protect your consumers and business. You can implement [Device Authorization grant using Cognito and AWS Lambda](https://aws.amazon.com/blogs/security/implement-oauth-2-0-device-grant-flow-by-using-amazon-cognito-and-aws-lambda/). AWS services such as [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/listener-authenticate-users.html) (ALB), [API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-integrate-with-cognito.html), [AWS AppSync](https://docs.aws.amazon.com/appsync/latest/devguide/security-authz.html), and [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/cognito-identities.html) can authenticate and authorize requests using tokens issued by Cognito User Pools.

![Reference architecture diagram for AWS connected vehicle companion application](https://docs.aws.amazon.com/whitepapers/latest/designing-next-generation-vehicle-communication-aws-iot/images/connected-vehicle-companion-app-refarch.png)

## AWS IoT Device Shadow service
<a name="aws-iot-device-shadow"></a>

 The [AWS IoT Device Shadow service](https://docs.aws.amazon.com/iot/latest/developerguide/iot-device-shadows.html) is a key feature set for AWS IoT remote command and control. The device shadow makes it possible for the developer to decouple the companion application and the vehicle architecture, passing messages between the two systems using JSON documents. A vehicle's shadow document is stored in AWS Cloud to persist the current state for the vehicle.

 With the device shadow, applications can interact with the vehicles even when they are not connected. This provides the following features:
+  Cloud representation of vehicle state
+  Last known state query for offline vehicles
+  Real-time vehicle state changes
+  Command and control via a change in state

 The state of the vehicle is persisted in the cloud and completely customizable to fit the OEM's trackable attributes. For example, if the window's state (up/down) can be remotely controlled via the companion application for a specific trim of a vehicle, but not for other trims, the windows attribute can be removed from the JSON shadow definition document for the trims that do not support that feature. This allows for complete flexibility as the OEM builds its state mechanism, but at the same time, Vehicle Shadow adds more cost to the overall solution and might not meet the flexibility required by the OEM.

## Remote command approach
<a name="remote-command-approach"></a>

 When building a connected vehicle platform, many decisions will need to be made on aligning to a specification or aligning to cloud services. For remote commands, AWS offers a solution to both approaches. With the request/response feature of MQTTv5, builders can implement remote command functionality, regardless of the underlying cloud provider. This approach will require more upfront work, and more operational overhead as connectivity state will need to be monitored and stored along with the existing state of the parameter being changed.

 With AWS IoT Device Shadow services, the implementation requires much less up-front work, but will have impacts on cost and aligns the platform closer to AWS IoT Core specific features which will not translate to other cloud providers. AWS works backwards from our customers to provide these flexible building blocks to ensure platform requirements are met, either reduction in operational overhead or being cloud agnostic.
