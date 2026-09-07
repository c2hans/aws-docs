---
source_url: https://docs.aws.amazon.com/whitepapers/latest/security-best-practices-for-manufacturing-ot/secure-network-connection-to-the-cloud.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Secure network connection to the cloud
<a name="secure-network-connection-to-the-cloud"></a>

The best practice to manage a secure cloud connection is to keep the network traffic private and encrypted. If the network traffic can’t be routed through either a VPN or a private network and one needs to access a cloud service directly over the internet, the traffic must be encrypted and routed through a TLS proxy and an on-premises firewall for added protection. Figure 6 highlights some of these best practices.
+  **Establish secure connection with AWS via site-to-site VPN or Direct Connect** — AWS offers [multiple ways](https://docs.aws.amazon.com/whitepapers/latest/aws-vpc-connectivity-options/network-to-amazon-vpc-connectivity-options.html) and design patterns to establish a secure connection to the AWS environment from the manufacturing edge. Establish a secure VPN connection to AWS over the public internet, or set up a dedicated private connection via Direct Connect. Use [Site-to-Site VPN with Direct Connect](https://aws.amazon.com/premiumsupport/knowledge-center/create-vpn-direct-connect/) to encrypt traffic over Direct Connect.
+  **Prefer VPC endpoints or VPC Endpoint Services when possible** — Once a secure connection to AWS has been established via VPN over public internet or Direct Connect, use [VPC Endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpce-interface.html) whenever possible. VPC Endpoints enables customers to privately connect to supported regional services without requiring a public IP address. Endpoints also support endpoint policies, which further allow to control and limit access to only the required resources.

 [VPC Endpoint Services](https://docs.aws.amazon.com/vpc/latest/userguide/endpoint-service.html) (AWS PrivateLink) enables you to create your own application in your VPC in the cloud and configure it as a VPC Endpoint.
+  **Use TLS proxy and a firewall for services connecting to AWS over public internet** — If the VPC Endpoint for the required service is not available, you would have to establish a secure connection over the public internet. The best practice in such scenarios is to route these connections via a TLS proxy and a firewall.

The following figure shows an example of an [IoT AWS IoT Greengrass gateway connected to the cloud via a proxy](https://docs.aws.amazon.com/greengrass/latest/developerguide/gg-core.html#alpn-network-proxy). Using a proxy allows you to inspect and monitor cloud traffic, enabling threat and malware detection. It also allows the security policies to be applied at the network layer. Firewall rules need to be established for HTTPS and MQTT traffic. To sustain the intermittent loss of network connection, the gateway should utilize “store and forward” methods like [AWS IoT Greengrass Stream Manager](https://docs.aws.amazon.com/greengrass/v2/developerguide/stream-manager-component.html) to locally buffer data until the connection is restored.

![A diagram showing secure network connection to the cloud.](https://docs.aws.amazon.com/whitepapers/latest/security-best-practices-for-manufacturing-ot/images/secure-nw-connection.png)

* Secure network connection to the cloud *
