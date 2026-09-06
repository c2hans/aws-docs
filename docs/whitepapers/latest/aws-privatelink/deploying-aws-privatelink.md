---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/deploying-aws-privatelink.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Deploying AWS PrivateLink
<a name="deploying-aws-privatelink"></a>

## AWS PrivateLink considerations
<a name="aws-privatelink-considerations"></a>

 When deploying an endpoint, customers should consider the following:
+  Traffic will be sourced from the Network Load Balancer inside the service provider Amazon VPC. When service consumers send traffic to a service through an interface endpoint, the source IP addresses provided to the application are the private IP addresses of the Network Load Balancer nodes, and not the IP addresses of the service consumers.
+  Proxy Protocol v2 can be [*enabled to gain insight into the network traffic*](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-service.html#endpoint-service-proxy-protocol). Network Load Balancers use Proxy Protocol v2 to send additional connection information such as the source and destination. This may require changes to the application.
+  Proxy Protocol v2 can be enabled on the load balancer and the client IP addresses can be obtained from the Proxy Protocol header when IP addressesof the service consumers and their corresponding interface endpoint IDs are needed.
+  Customers can create an Amazon Simple Notification Service (SNS) to receive alerts for specific events that occur on the endpoints that are attached or when they attempt to attach to their endpoint service. For example, one can receive an email when an endpoint request is accepted or rejected for the endpoint service.
+  The Amazon SNS topic that a customer can use for notifications must have a topic policy that allows the VPC endpoint service to publish notifications on your behalf. Include the following statement in the topic policy:

 For more information see the documentation on [*Authentication and Access Control for Amazon SNS*](https://docs.aws.amazon.com/sns/latest/dg/AccessPolicyLanguage.html)
+  Endpoint services cannot be tagged.
+  The private DNS of the endpoint does not resolve outside of the Amazon VPC. For more information, read [*accessing a service through an interface endpoint*](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/vpce-interface.html#access-service-though-endpoint). Note that private DNS hostnames can be configured to point to endpoint network interface IP addresses directly. Endpoint services are available in the AWS Region in which they are created and can be accessed in remote AWS Regions using inter-Region VPC peering.
+  If an endpoint service is associated with multiple Network Load Balancers, then for a specific Availability Zone, an interface endpoint will establish a connection with one Network Load Balancer instance only.
+  Availability Zone names in a customer account might not map to the same locations as Availability Zone names in another account. For example, the Availability Zone US-EAST-1A might not be the same Availability Zone as US- EAST-1A for another account. An endpoint service gets configured in Availability Zones according to their mapping in a customer’s account.
+  For low latency and fault tolerance, we recommend creating a Network Load Balancer with targets in each available Availability Zone of the AWS Region.

## AWS PrivateLink configuration
<a name="aws-privatelink-configuration"></a>

 Full details on how to configure AWS PrivateLink can be found in the [*documentation on interface VPC endpoints*](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-service.html).
