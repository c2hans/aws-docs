---
source_url: https://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/implementing-lpwan-iot-solutions-with-udp.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Implementing LPWAN IoT solutions with UDP
<a name="implementing-lpwan-iot-solutions-with-udp"></a>

 User Datagram Protocol (UDP) is a lightweight protocol based on a principle of a connectionless communication. UDP is based on the Internet Protocol (IP). UDP/IP is a protocol stack allowing an optimization of power consumption (for example, for use cases requiring longer device battery duration).

 UDP, by itself, does not ensure confidentiality, integrity, or authenticity of information exchange. To secure communication with UDP, additional measures need to be taken. An example of such a measure is to use transport layer security protocols such as DTLS.

 When implementing IoT solutions using UDP, further characteristics need to be considered. A transmission using UDP is not reliable, because UDP does not include acknowledgement or retransmission mechanisms. In rare cases, UDP messages can be duplicated (for example, by network hardware components such as routers).

 Transmission using UDP is not ordered. If several messages are sent to a recipient, no specific order of arrival can be guaranteed. If your IoT solutions requires guaranteed transmission of messages, deduplication, or message ordering when using UDP, appropriate mechanisms need to be developed on the application layer.

 This whitepaper describes an approach on how to ingest UDP communication from a microcontroller unit (MCU) device to an AWS IoT Core MQTT topic. An important consideration when using UDP or CoAP/UDP is securing a communication in terms of implementing reliable authentication of the device in the cloud, confidentiality of communication between the device and the cloud, and integrity of exchanged data. Another consideration is to decide which capabilities to build and operate (such as, make approach) and which capabilities to source (such as, buy approach”).

 There are three implementation patterns which provide different approaches regarding these considerations:
+  Telecommunications (telco)-provided fully integrated solution
+  Customer-operated solution secured by Telco-provided VPN
+  Customer-operated solution secured by DTLS

 The following figure provides an overview of these patterns:

![Diagram showing patterns for implementing IoT solutions with AWS using UDP protocol](http://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/images/udp-iot-solutions.png)

## Pattern 1: Telco-provided fully integrated solution
<a name="pattern-1-telco-provided-fully-integrated-solution"></a>

![Architecture of a fully integrated solution provided by the telco](http://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/images/telco-full-solution.png)

 In this pattern, the telco provider is operating a UDP endpoint. The customer’s devices target this endpoint for ingesting the payloads using UDP. Telco’s software component then encapsulates the binary payload from the UDP message into a JSON format. Finally, the telco will ingest the payload into the customer’s AWS account. A deployment of an [AWS CloudFormation](https://aws.amazon.com/cloudformation/) template into the customer’s account is typically necessary for the integration between telco’s infrastructure and customer’s AWS account.

### Device-side considerations
<a name="device-side-considerations"></a>

 For the purpose of device authentication, international mobile equipment identity (IMEI) or international mobile subscriber identity (IMSI) numbers are typically used. The telecommunication provider will offer an option to enrich this authentication data when ingesting messages into the customer’s account.

 For the purpose of telemetry ingestion using UDP, customers can use a UDP library available on their MCU. When using FreeRTOS, customers can refer to [Sending UDP Data examples](https://www.freertos.org/FreeRTOS-Plus/FreeRTOS_Plus_TCP/Networking_Tutorial_Sending_UDP_Data.html). Before ingesting UDP data, customers need to configure a UDP endpoint and port supplied by their telecommunication provider.

 To send data to the device for the purpose of command processing, the implementation varies depending on the telecommunication provider. When using FreeRTOS, customers can refer to [Receiving UDP Data examples](https://www.freertos.org/FreeRTOS-Plus/FreeRTOS_Plus_TCP/Networking_tutorial_Receiving_UDP_Data.html).

### Cloud-side considerations
<a name="cloud-side-considerations"></a>

 Key considerations for an implementation on the cloud side are integration between telco and customer’s account, payload binary decoding, and integration of decoded payload with other AWS services.

 For an integration between telco and customer’s account, telco will ingest the incoming payload from the device into customer’s account AWS IoT Core. A possible implementation pattern for the ingestion is an invocation of an AWS IoT Core service API (for example, [Publish action of AWS IoT data API](https://docs.aws.amazon.com/iot/latest/apireference/API_iotdata_Publish.html)) in the customer’s account by the telco provider. To give telco provider access to AWS resources in your account, AWS recommends using IAM roles with external IDs to delegate access to your AWS resources to the telco’s AWS account.

 The payload binary decoding is necessary, because the telecommunication provider will encapsulate the device’s binary UDP payload into a JSON message, without performing binary decoding. After the telco ingests the JSON message into the customer’s account, binary decoding is performed. To implement binary decoding, customers can use the [AWS IoT SQL aws\_lambda](https://docs.aws.amazon.com/iot/latest/developerguide/iot-sql-functions.html) function in [AWS IoT rules](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html).

 For integration of decoded payload with other AWS services, the recommended approach is to use [AWS IoT rules](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html) and [AWS IoT rule actions](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rule-actions.html).

### Useful resources
<a name="useful-resources"></a>

 Refer to the following resource for further details:
+  [Automated Device Provisioning to AWS IoT Core Using 1NCE Global SIM](https://aws.amazon.com/blogs/apn/automated-device-provisioning-to-aws-iot-core-using-1nce-global-sim/)

## Pattern 2: Customer-operated solution secured by Telco-provided VPN
<a name="pattern-2-customer-operated-solution-secured-by-telco-provided-vpn"></a>

![Architecture of a customer-operated solution secured by VPN](http://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/images/vpn-secured-solution.png)

 In this pattern, the customer is operating a solution for ingesting UDP payloads for the customer’s IoT devices. The solution can be built by the customer, the AWS Partner, or—if available—sourced from the telecommunication provider.

 To secure confidentiality and integrity of the communication between the telecommunication provider and the customer’s account, some telecommunication provider, a Site-to-Site VPN between the telecommunication provider and the customer’s AWS account is established.

### Cloud-side considerations
<a name="cloud-side-considerations-1"></a>

 In this pattern, the customer is operating a solution for ingesting UDP payloads for the customer’s IoT devices. The solution can be built by the customer, the AWS Partner or—if available—sourced from the telecommunication provider.

 Key features of this solution are payload binary decoding, ingestion to AWS IoT Core, and integration with other AWS services. The payload binary decoding is necessary, because the devices will place a binary payload into UDP for energy efficiency reasons. During payload binary decoding, a transformation from a binary representation of payload into, for example, JSON takes place. For further processing, an ingestion to IoT Core [MQTT topic](https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html) or [AWS IoT rule](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html) can be performed. After the payload arrives on IoT Core MQTT topic or AWS IoT rule, it can be simply integrated with more than [20 AWS services supported by AWS IoT rules](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rule-actions.html).

 To ingest messages to AWS IoT Core, the recommended approach is to use [AWS IoT Data plane APIs](https://docs.aws.amazon.com/iot/latest/apireference/API_Operations_AWS_IoT_Data_Plane.html) authorized by [IAM](https://docs.aws.amazon.com/iot/latest/developerguide/security_iam_service-with-iam.html) mechanisms.

 The same software component can also support downlink communication to the devices. For example, this software component can be designed to attach downlink payload data to the UDP response to uplink message (piggybacking mechanism). The source of the downlink data can be [AWS IoT Device Shadow](https://docs.aws.amazon.com/iot/latest/developerguide/iot-device-shadows.html) or a database such as [Amazon DynamoDB](https://aws.amazon.com/dynamodb). The following figure illustrates this approach:

![Example architecture for processing UDP datagrams with AWS](http://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/images/udp-architecture.png)

### Device-side considerations
<a name="device-side-considerations-1"></a>

 For device authentication, the customer can use DTLS protocol (outlined in [*Pattern 3*](#pattern-3-customer-operated-solution-secured-by-dtls)).

 For the purpose of telemetry ingestion using UDP, customers can use a UDP library available on their MCU. When using FreeRTOS, customers can refer to [Sending UDP Data examples](https://www.freertos.org/FreeRTOS-Plus/FreeRTOS_Plus_TCP/Networking_Tutorial_Sending_UDP_Data.html). Before ingesting UDP data, customers need to configure a UDP endpoint and port pointing to the DNS record or [Elastic IP address](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/elastic-ip-addresses-eip.html) of the UDP server in their AWS account.

 To send data to the device for the purpose of command processing, customers have multiple options. One possible option is to use the piggybacking mechanism as described in the *Cloud-side considerations* section of this document. That mechanism improves energy efficiency, but might introduce longer reachability times. Another option is to send data to device by addressing the devices by their internal IP addresses in the telecommunication provider’s network. When using this option, devices should operate a UDP server to be capable to process incoming UDP. This approach reduces reachability times, but using this approach can increase power consumption on the device.

### Useful resources
<a name="useful-resources-1"></a>

 Refer to the following resource for further details:
+  [Using a Telefonica Data Bridge to Connect Narrow Band IoT Devices to AWS IoT Core](https://aws.amazon.com/blogs/apn/using-a-telefonica-data-bridge-to-connect-narrow-band-iot-devices-to-aws-iot-core/)

## Pattern 3: Customer-operated solution secured by DTLS
<a name="pattern-3-customer-operated-solution-secured-by-dtls"></a>

![Architecture of a customer-operated solution secured by DTLS](http://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/images/dtls-secured-solution.png)

 DTLS is a protocol which can be used to secure UDP-based communication in terms of device authentication, confidentiality, and integrity. The current version of DTLS 1.2 for use with UDP is defined in [RFC6347](https://datatracker.ietf.org/doc/html/rfc6347). When using DTLS, the payload of underlying UDP messages remains unchanged. Consequently, DTLS-based communication shows the same characteristics as UDP: best effort delivery without built-in acknowledgement and retry mechanisms, no guarantee for ordering of messages, and the possibility for duplicated messages. DTLS supports pre-shared secret, certificates and raw public keys as credentials. When using DTLS, a secure storage of pre-shared secret and certificates is an important precondition to avoid impersonation attacks.

 Use of DTLS might have several benefits. First, the communication from the IoT devices to the customer’s AWS account can be secured in terms of confidentiality and integrity without needing to rely on the telecommunication provider’s VPC peering or VPN solutions described in [*Pattern 2*](#pattern-2-customer-operated-solution-secured-by-telco-provided-vpn). This might simplify switching telecommunication providers or using multiple telecommunication providers. Second, DTLS provides an effective way of securing the device authentication. By associating the pre-shared secret or certificate of an IoT devices with the device identifier, the cloud application is able to verify the identity of the device.

 However, when using DTLS, the aspects of increased energy consumption and credential management need to be considered. When using DTLS, additional operations need to be performed on the IoT device to encrypt the outgoing messages and decrypt the incoming messages. These operations will result in an increase of energy consumption compared to sending unencrypted UDP payloads as described in the other discussed patterns. Increased energy consumption can reduce the battery lifetime of the IoT devices. Another aspect to consider is credential management (for example, an approach for provisioning, storing, and rotating the DTLS credentials on the IoT devices).

### Device-side considerations
<a name="device-side-considerations-2"></a>

 For device authentication, you can use DTLS.

### Cloud-side considerations
<a name="cloud-side-considerations-2"></a>

 In this pattern, the customer is operating a solution for ingesting DTLS-encrypted UDP payloads for the customer’s IoT devices. The solution can be built by the customer or AWS Partner. A key component of this solution is software which receives incoming UDP messages, authenticates the device payload, performs decryption and decoding of message payload, and forwards the payload for further processing to AWS IoT Core [MQTT topic](https://docs.aws.amazon.com/iot/latest/developerguide/mqtt.html) or [AWS IoT rule](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rules.html). To ingest messages to AWS IoT Core we recommend to use [AWS IoT Data plane APIs](https://docs.aws.amazon.com/iot/latest/apireference/API_Operations_AWS_IoT_Data_Plane.html) authorized by [IAM](https://docs.aws.amazon.com/iot/latest/developerguide/security_iam_service-with-iam.html) mechanisms. After the payload arrives on IoT Core MQTT topic or AWS IoT rule, it can be simply integrated with more than [20 AWS services supported by AWS IoT rules](https://docs.aws.amazon.com/iot/latest/developerguide/iot-rule-actions.html).
