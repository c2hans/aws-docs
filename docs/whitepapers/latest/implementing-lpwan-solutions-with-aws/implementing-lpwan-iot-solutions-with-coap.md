---
source_url: https://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/implementing-lpwan-iot-solutions-with-coap.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Implementing LPWAN IoT solutions with CoAP
<a name="implementing-lpwan-iot-solutions-with-coap"></a>

 This section first provides an overview of the architectural considerations for an implementation of a CoAP-based IoT solution. It then describes typical implementation patterns that AWS customers can use to implement CoAP-based IoT solutions.

## Introduction to CoAP
<a name="introduction-to-coap"></a>

 CoAP is an application layer protocol that was purpose built for constrained devices. It has low overhead and allows simple implementation on IoT devices. For example, the smallest size of the CoAP message is four bytes, if omitting tokens, options, and payload. Using CoAP, you can implement HTTP-like request/response patterns. Because CoAP is based on UDP, implementation using CoAP is more energy-efficient than when using MQTT or HTTP. You will find a specification of CoAP in [RFC 7252](https://datatracker.ietf.org/doc/html/rfc7252).

## CoAP client and server
<a name="coap-client-and-server"></a>

 Depending on use case requirements, an IoT device can act as a CoAP client, a CoAP server, or both. Battery-operated LPWAN devices will act as a CoAP client for the purpose of reduction of energy consumption. A mainline-operated LPWAN device can also act as a CoAP server.

## CoAP resource model
<a name="coap-resource-model"></a>

 CoAP is based on a resource model. A *resource*, in the context of CoAP, is a logical container on the CoAP server. Each CoAP resource is mapped to a Unique Resource Identifier (URI). A CoAP resource URI consists of host, port, path, and query. An example CoAP URI is coaps://host:port/path/to/resource?key=value. To interact with resources, CoAP supports methods such as GET, PUT, POST, and DELETE with semantics and return codes similar (but not identical) to HTTP.

## Confirmable and non-confirmable requests
<a name="confirmable-and-non-confirmable-requests"></a>

 CoAP supports both confirmable and non-confirmable requests. When using confirmable requests, the CoAP server must acknowledge the request with an acknowledgement in response. The response acknowledgement can optionally contain the payload sent by the server. Clients can use the confirmable messages to deal with the packet loss. If CoAP client does not receive an acknowledgement from the server, the CoAP client can perform a retry.

 The following figure shows examples for common patterns of using both confirmable and non-confirmable requests. For the requests from the CoAP client to the CoAP server, the figure specifies a CoAP method (for example, POST), URI-path (for example, /temperature), type of message (CONfirmable or NON-confirmable), and—where applicable—payload (for example, “36.6”). For the responses from the CoAP server to the CoAP client, the figure specifies the response code (for example, 2.05 which means “Content”) and—where applicable—payload.

![Diagram showing the types of CoAP requests](http://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/images/coap-requests.png)

 As mentioned previously, an IoT device can act as a CoAP client, CoAP server, or both. For the use case of telemetry ingestion from battery-operated LPWAN devices, the IoT device will act as a CoAP client.

## Block-wise transfer mode
<a name="block-wise-transfer-mode"></a>

 Normal CoAP messages are restricted in size and typically used for small payloads, such as measurements from the sensors or commands to the actuators. The size restriction results from factors such as maximum UDP datagram size or maximum MTU size enforced by cellular network operators. To enable applications to transfer larger amounts of data (for example, for the purpose of firmware updates), CoAP supports block-wise transfer mode as specified in [RFC 7959](https://datatracker.ietf.org/doc/html/rfc7959). Block-wise transfer mode is applicable to both CoAP requests and CoAP responses.

 In the following example, a payload with the size of 384 bytes needs to be sent from the server to the client, over a connection limiting the maximum payload size per UDP datagram to 128 bytes. CoAP client performs a GET request, and CoAP server sends three blocks of 128 bytes each.

![Example of CoAP block-wise transfer](http://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/images/coap-block-wise-transfer.png)

## Encryption in transit and device authentication
<a name="encryption-in-transit-and-device-authentication"></a>

 CoAP provides neither capability for encryption in transit, no dedicated features for device authentication. For the purpose of encryption in transit and device authentication, DTLS can be used. You will find more details on DTLS in [RFC6347](https://datatracker.ietf.org/doc/html/rfc6347).

## Architectural considerations
<a name="architectural-considerations"></a>

 When architecting an IoT solution based on CoAP, AWS recommends several fundamental considerations. First, consider whether your IoT device should take on the role of CoAP client, CoAP server, or both. Battery-powered IoT devices that use LPWAN connectivity should act as CoAP clients for energy efficiency. However, depending on the use case, your IoT device might also need to operate as a CoAP server. In this case, it is important to note that not all implementation patterns described in the following section support IoT devices acting as CoAP servers.

 The second consideration is a definition of the CoAP features required for an implementation of your use case. AWS recommends that you consider both CoAP features which are required in the short term and CoAP features which may be required at a later point of time as your IoT solution evolves. This step is important because individual implementation approaches may differ depending on the subset of CoAP features they support. Examples of such CoAP features can be support for [GET/PUT/POST/DELETE methods](https://datatracker.ietf.org/doc/html/rfc7252#section-5.8), [block-wise transfer](https://datatracker.ietf.org/doc/html/rfc7959), [confirmable messages](https://datatracker.ietf.org/doc/html/rfc7252#section-2), [piggybacked response](https://datatracker.ietf.org/doc/html/rfc7252#section-5.2.1), and [separate response](https://datatracker.ietf.org/doc/html/rfc7252#section-5.2.2). Also, support for individual [CoAP options](https://datatracker.ietf.org/doc/html/rfc7252#section-5.4) such as [ETag](https://en.wikipedia.org/wiki/HTTP_ETag) may vary depending on the chosen solution.

 If you plan to use DTLS as a security layer for CoAP, an analysis of required DTLS features is also recommended. Examples for such features are support for authentication methods (for example, [No-Sec, Pre-shared keys (PSK), Raw Public Key Certificates, X.509 certificates](https://datatracker.ietf.org/doc/html/rfc7252#section-9.1.1)) and [Session resumption](https://datatracker.ietf.org/doc/html/rfc7925#section-7) with session ID and connection ID.

## Implementation patterns
<a name="implementation-patterns"></a>

 When implementing data ingestion and device commands with CoAP, there are three implementation patterns to consider. These patterns differ depending which entity operates the CoAP software components, such as CoAP server or CoAP client. These patterns are: CoAP software components are operated by telco, CoAP software components are operated by an AWS Partner, and CoAP software components are operated by the customers. In the latter case, two different varations shall be distinguished, depending on how the data in transit are secured. The data in transit can be secured by a VPN connection between telco and customer’s account, or by using a communication protocol such as DTLS.

 The following diagram illustrates three patterns, including two variations of the latter one:

![Diagram of patterns for implementing IoT solutions with AWS using CoAP](http://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/images/dtls-patterns-1.png)![Diagram of patterns for implementing IoT solutions with AWS using CoAP](http://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/images/dtls-patterns-2.png)

 The following sections contain a detailed description of each of these patterns.

### Pattern 1: CoAP components are operated by telco
<a name="pattern-1-coap-components-are-operated-by-telco"></a>

![Architecture for CoAP server operated by telco](http://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/images/telco-coap-server.png)

 In this pattern, the telecom provider operates a CoAP endpoint, which acts as a CoAP server. Customers can configure the CoAP endpoint to integrate with the customer’s AWS account. Each time the CoAP client on the IoT device sends a message to the CoAP server, the CoAP server will perform the steps of encapsulation, enrichment, and ingestion into the customer’s account.

 In the encapsulation and enrichment step, the CoAP server first encapsulates the binary payload into a JSON message, and then enriches this JSON message with additional useful information. An example of additional information is the International Mobile Subscriber Identity (IMSI) of the IoT device.

**Note**
The binary payload remains unchanged in this step. If necessary, binary decoding should be performed in the customer’s AWS account.

 In the ingestion step, the CoAP server forwards the JSON message to the AWS IoT Core service in the customer’s AWS account. After the data arrive in AWS IoT Core message broker or AWS IoT Core rule engine, it can be further processed by a broad range of AWS services.

 If you want to give telco provider access to AWS resources in your account, AWS recommends using IAM roles with external IDs to delegate access of your AWS resources to the telco AWS account.

 Refer to the following resource for examples of AWS Partners supporting this pattern:
+  [Automated Device Provisioning to AWS IoT Core Using 1NCE Global SIM](https://aws.amazon.com/blogs/apn/automated-device-provisioning-to-aws-iot-core-using-1nce-global-sim/)
+  [Ericsson Cloud Connect: Making it easy for enterprises to securely connect cellular devices to Amazon Web Services](https://www.ericsson.com/en/portfolio/iot-and-new-business/iot-solutions/iot-accelerator/cloud-connect)

### Pattern 2: CoAP components are operated by an AWS Partner
<a name="pattern-2-coap-components-are-operated-by-an-aws-partner"></a>

![Architecture for CoAP server operated by an AWS Partner](http://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/images/partner-coap-server.png)

 In this pattern, an AWS Partner operates a CoAP endpoint, which acts as a CoAP server. Customers can configure the CoAP endpoint to integrate with a customer’s AWS account. Each time the CoAP client on the IoT device sends a message to the CoAP server, it will perform the steps of encapsulation and ingestion into the customer’s account.

1.  **Encapsulation step** – The CoAP server encapsulates the binary payload into a JSON message. Note that the binary payload remains unchanged in this step. If necessary, binary decoding should be performed in the customer’s AWS account.

1.  **Ingestion step** – The CoAP server forwards the JSON message to the AWS IoT Core service in the customer’s AWS account. After the data arrive in the AWS IoT Core message broker or AWS IoT Core rule engine, the data can be further processed by a broad range of AWS services.

 If you want to give an AWS Partner access to AWS resources in your account, AWS recommends using IAM roles with external IDs to delegate access from your AWS resources to the AWS Partner account.

 Refer to the following resources for examples of AWS Partners supporting this pattern:
+  [IoTerop Nebraska in AWS Marketplace](https://aws.amazon.com/marketplace/pp/prodview-7qavahv2clh42)
+  [Ericsson Cloud Connect: Making it easy for enterprises to securely connect cellular devices to Amazon Web Services](https://www.ericsson.com/en/portfolio/iot-and-new-business/iot-solutions/iot-accelerator/cloud-connect)

### Pattern 3: CoAP components are operated by the customer
<a name="pattern-3-coap-components-are-operated-by-the-customer"></a>

![Architecture for CoAP server and client operated by customer](http://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/images/customer-coap-server.png)

 In this pattern, the AWS customer operates a CoAP endpoint in their AWS account. Depending on the use case requirements, the CoAP endpoint can operate as CoAP server, CoAP client, or both. The CoAP endpoint can handle forwarding the incoming CoAP messages to AWS IoT Core, and sending CoAP messages to the IoT devices. To ingest messages to AWS IoT Core, AWS recommends using [AWS IoT data plane APIs](https://docs.aws.amazon.com/iot/latest/apireference/API_Operations_AWS_IoT_Data_Plane.html) authorized by IAM mechanisms.

 When using this pattern, a mechanism used for securing data in transit needs to be defined. This mechanism will protect the complete path of communication from the IoT device to the customer’s AWS account. The first consideration is to protect the data in transit between the IoT device and the telco provider’s infrastructure. The second consideration is to protect the data in transit between the telco provider’s infrastructure and the customer’s AWS account. There are two possible variants for securing data in transit:

### Securing data in transit with a VPN connection between telco and customer’s AWS account
<a name="securing-data-in-transit-with-a-vpn-connection-between-telco-and-customers-aws-account"></a>

![Using VPN to secure data in transit](http://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/images/telco-customer-vpn-secured.png)

 In this variant, customers rely on the telco provider’s infrastructure for protection data in transit between the IoT device and the telco provider’s infrastructure. No protocol-level security is used, and CoAP is used in NoSec mode. To protect data in transit between telco provider’s infrastructure and the customer’s AWS account, a VPN connection is established between the telco provider and the customer’s AWS account.

 For further information on using VPN, review the [Site-to-Site VPN](https://aws.amazon.com/vpn/) documentation. For examples of AWS Partners supporting this pattern, refer to [Using a Telefonica Data Bridge to Connect Narrow Band IoT Devices to AWS IoT Core](https://aws.amazon.com/blogs/apn/using-a-telefonica-data-bridge-to-connect-narrow-band-iot-devices-to-aws-iot-core/).

### Securing data in transit with protocols as DTLS
<a name="securing-data-in-transit-with-protocols-as-dtls"></a>

![Using DTLS to secure data in transit](http://docs.aws.amazon.com/whitepapers/latest/implementing-lpwan-solutions-with-aws/images/dtls-secure-data-in-transit.png)

 In this variant, customers use DTLS protocol as a mechanism for infrastructure for protection data in transit between the IoT device and telco provider’s infrastructure, and between telco provider’s infrastructure and the customer’s AWS account.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
