---
source_url: https://docs.aws.amazon.com/apigateway/latest/developerguide/infrastructure-security.html
---

# Infrastructure security in Amazon API Gateway

As a managed service, Amazon API Gateway is protected by AWS global network security. For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/). To design your AWS environment using the best practices for infrastructure security, see [Infrastructure Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) in *Security Pillar AWS Well‐Architected Framework*.

You use AWS published API calls to access API Gateway through the network. Clients must support the following:
+ Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
+ Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.

You can call these API operations from any network location, but API Gateway does support resource-based access policies, which can include restrictions based on the source IP address. You can also use resource-based policies to control access from specific Amazon Virtual Private Cloud (Amazon VPC) endpoints or specific VPCs. Effectively, this isolates network access to a given API Gateway resource from only the specific VPC within the AWS network.

API Portal control plane requests use the `apiportal` Regional endpoints over TLS. You can access the API Portal control plane from your VPC through an interface Amazon VPC endpoint (); for more information, see [Access an AWS service using an interface VPC endpoint](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) in the * Guide*. The endpoint service name is `com.amazonaws.{{region}}.apiportal`. Documentation portals are websites served through CloudFront; a portal with authorization set to **None** is reachable from the internet. To restrict who can view a portal, require Amazon Cognito authorization, and turn on fine-grained access control to limit which products each signed-in user sees. Portal authorization doesn't change the access controls on the APIs that the portal documents. For more information, see [Documentation portals in API Portal](apiportal-documentation-portals.md).
