---
source_url: https://docs.aws.amazon.com/whitepapers/latest/designing-next-generation-vehicle-communication-aws-iot/broker-modernization-on-aws-iot-core.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Broker modernization on AWS IoT Core
<a name="broker-modernization-on-aws-iot-core"></a>

 The broker modernization reference architecture provides some high-level guidance for table-stakes use cases, some of which might be already in use by the automaker, and some might be on the roadmap. Not all of these use cases have to be implemented, but we wanted to demonstrate the power of MQTTv5 on AWS IoT Core and repeatable design patterns with downstream AWS services. With the modernization approach, we make some basic assumptions in that the vehicle is (or can be) provisioned to AWS IoT Core using mTLS, the MQTT and cryptography libraries properly support the requirements to connect to AWS IoT Core. From there, all existing publish and subscribe mechanisms using MQTT will work with IoT Core, just the processing logic to handle the payloads will need to be setup to subscribe and publish to these topics from the rest of the cloud infrastructure.

 At AWS re:Invent 2022, Mercedes Benz [presented their broker modernization](https://youtu.be/Oaw_cpLBpoI?t=2384) approach and how they migrated millions of vehicles to AWS IoT Core, to reduce the overall complexity of the message broker, a top-down initiative to move towards managed services, serverless components and overall cost reduction. For Mercedes, the publish/subscribe architecture brings better observability on a per-vehicle basis for troubleshooting, debug and trace techniques. With a streaming architecture using a broker, they can separate telemetry vs commands, quickly iterate on prototyping on production workloads and integrate more seamlessly with other downstream AWS services such as [Amazon Kinesis](https://aws.amazon.com/pm/kinesis).

 With the broker modernization approach, vehicle manufacturers can begin their AWS IoT Core journey with a few simple steps, and have an immediate impact on their operationalization, observability, security, and scalability of their connected vehicle platforms. Eventually, the power of the AWS IoT Core ecosystem and the differentiation it brings will drive OEMs to extend their connected vehicle offering to implement other AWS managed services AWS IoT Core such as AWS IoT Device Management and AWS IoT Device Defender.

## Broker replacement
<a name="broker-replacement"></a>

 The first step to the broker modernization approach is to evaluate the current message broker implementation and determine if this approach will work for the existing vehicles in the field. The preference for this approach is to leave the edge implementation static and repointing the edge end from the old MQTT broker in the current production implementation to the AWS IoT Core endpoint. If MQTT 3.1.1 specification is followed in the existing vehicles, then this is the recommended approach to take, minimizing (or even eliminating) any code updates at the edge.

 To provision vehicles to IoT Core or to send telemetry with the service, an endpoint is necessary. Using IoT Core [custom domain configurations](https://docs.aws.amazon.com/iot/latest/developerguide/iot-custom-endpoints-configurable-custom.html), users can build configurable endpoints for AWS IoT Core. Enabling our customers to take their existing fully qualified domain names (FQDN) and create a traffic-based policy in Amazon Route 53 to resolve the location using geolocation or latency-based routing. If needed, a [just-in-time Provisioning](https://docs.aws.amazon.com/iot/latest/developerguide/provision-wo-cert.html) workflow (explained in detail later in the document) will allow auto-registration of your vehicles once they connect to AWS IoT Core or the devices could be provisioned in AWS IoT Core prior to the migration.

 Replacing the broker in your connected vehicle architecture reduces licensing costs, operationalization support and resources and allows AWS to handle the undifferentiated heavy lift of managing your MQTT broker at scale. Recently, we introduced several MQTTv5 features that can help with specific automotive use cases, those are discussed below.

## Shared subscriptions
<a name="shared-subscriptions"></a>

 Using shared subscriptions, incoming vehicle telemetry can be distributed to message processors in a more efficient manner. When higher than normal demand for telemetry processing exists, AWS IoT Core will randomly distribute the published payloads to a single subscriber spreading the message processing load across a larger set of subscribers enabling more of a load-balanced approach to ensure a single instance of a processor is not overwhelmed. If shared subscriptions is not enabled, each subscriber would get messages published to that topic, which creates redundant processing for the cloud.

 This allows for custom processing of telemetry ingest by having, perhaps, a micro-service container-based layer to handle the topic subscriptions and process the message as they are received. We could potentially ramp up the number of processors to handle peak-demand. Each micro-service can read from the shared topic on a shared subscription. This will help in distributing the processing load amongst the application servers within a group. Without the shared subscription feature, any messages that gets post on the MQTT topic will be published to all the clients subscribing to the topic. With the shared subscription feature only one of the groups clients will receive the message on this topic.

 Within the connected vehicle space, it is highly expedient for a peak-demand scenario where millions of vehicles publish messages to a common topic. Those millions of messages need to be processed and sent to backend systems for consumption which may be companion mobile applications that shows the driver trip data or perform pre-processing prior to storage in data lake, or a machine learning pipeline for predictive maintenance and many others.
