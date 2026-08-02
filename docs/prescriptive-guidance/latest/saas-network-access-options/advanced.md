---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/saas-network-access-options/advanced.html
---

# Advanced networking access scenarios for SaaS offerings in the AWS Cloud
<a name="advanced"></a>

The architectures discussed in the [Networking access scenarios for SaaS offerings in the AWS Cloud](options.md) section should help you find a solution for the majority of use cases. However, there are some scenarios that have specific technical requirements. Many are beyond the scope of this guide.

**This section discusses the following advanced technical requirements and considerations:**
+ [Bidirectional communication support](#advanced-bidirectional-communication)
+ [TCP, UDP, and proprietary protocols](#advanced-protocols)

## Bidirectional communication
<a name="advanced-bidirectional-communication"></a>

In some cases, applications require bidirectional traffic in order operate as expected. Common use cases are webhooks or notification services. Generally, you can achieve this by having a WebSocket connection between the server and the client. This connection keeps the TCP session open and allows both participants to send traffic over the connection. Most of the services discussed in this guide natively support WebSocket, including Network Load Balancers, Application Load Balancers, Amazon API Gateway, AWS PrivateLink, and AWS AppSync (through [private real-time endpoints](https://docs.aws.amazon.com/appsync/latest/devguide/real-time-websocket-client.html)).

In other cases, an application on the SaaS provider side might need access to resources on the consumer side, such as a database. When you connect through bidirectional channels, such as an AWS Site-to-Site VPN connection, that is not an issue.

On the other hand, AWS PrivateLink and Elastic Load Balancing support only unidirectional traffic. If you use these services, you must set up another network path for the traffic that initiates from your SaaS offering. For example, this might be an additional AWS PrivateLink connection that goes in the reverse direction.

## TCP, UDP, and proprietary protocols
<a name="advanced-protocols"></a>

Many applications are served through HTTP or HTTPS, but not all. Some may use other Layer 7 protocols on top of TCP, such as Message Queuing Telemetry Support (MQTT). Others might even use UDP to serve consumers. In rare cases, services use proprietary protocols that must be transmitted inside packets (Layer 3). For these scenarios, it is important to understand which services support your SaaS offering.

For Layer 3 services, you can use AWS PrivateLink and Network Load Balancers, both of which support all TCP and UDP traffic.

For Layer 7 services, Application Load Balancers and Amazon CloudFront support HTTP, HTTPS, WebSocket, and Google Remote Procedure Calls (gRPC). Similarly, Amazon API Gateway and AWS AppSync each support HTTP, HTTPS, and WebSocket. Amazon CloudFront is the only service that currently supports HTTP/3.

You can use Amazon VPC Lattice to connect Layer 7 applications and Layer 3 resources. It supports HTTP, HTTPS, gRPC, TCP, and TLS passthrough.

If the application can serve traffic only over Layer 3, it is crucial that you use core AWS networking services, such as AWS Transit Gateway, AWS Direct Connect, AWS Site-to-Site VPN, and VPC peering. The traffic should then be routed directly from the SaaS consumer to the compute layer of the SaaS offering.
