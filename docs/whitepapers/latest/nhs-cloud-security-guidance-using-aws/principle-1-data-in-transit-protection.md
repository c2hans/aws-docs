---
source_url: https://docs.aws.amazon.com/whitepapers/latest/nhs-cloud-security-guidance-using-aws/principle-1-data-in-transit-protection.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Principle 1: Data in transit protection
<a name="principle-1-data-in-transit-protection"></a>

 *User data transiting networks should be adequately protected against tampering and eavesdropping.*

****
 The Service User should utilise strong cryptography as defined by NIST SP800-57 to encrypt communications between the Cloud and the End-user.

 **Applicable risk classes:** III-V

 There may be multiple channels of data communication between end users and the system deployed to AWS. These may be divided into two categories: those accessing the system itself as deployed into an [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/) (Amazon VPC), and those accessing AWS APIs outside of that VPC.

 For the first category, two different controls are applicable: an IPsec VPN and a Direct Connect link to the VPC.
+  **IPsec VPN** — An IPsec VPN connection connects a customer’s VPC to another network designated by the customer. IPsec is a protocol suite for securing IP communications by authenticating and encrypting each IP packet of a data stream. Amazon VPC customers can create an IPsec VPN connection to their VPC by first establishing an internet key exchange (IKE) security association between their Amazon VPC, VPN gateway, and another network gateway using a pre-shared key as the authenticator.

   Upon establishment, IKE negotiates an ephemeral key to secure future IKE messages. An IKE security association cannot be established unless there is complete agreement among the parameters, including authentication (such as SHA-1) and encryption (such as AES 128-bit).

   Next, using the IKE ephemeral key, keys are exchanged between the VPN gateway and customer gateway to form an IPsec association. Traffic between gateways is encrypted and decrypted using this security association. IKE automatically rotates the ephemeral keys used to encrypt traffic within the IPsec security association on a regular basis to ensure confidentiality of communications.

   For steps describing how to establish a VPN connection between a customer environment and an Amazon VPC, see the [AWS Site-to-Site VPN User Guide](https://docs.aws.amazon.com/vpn/latest/s2svpn/SetUpVPNConnections.html).
+  **Direct Connect link** — AWS Direct Connect (DX) is a direct logical connection between the customer’s environment from which end users are accessing the system and the VPC which it is deployed. Because this is an entirely private link, the risk of data in transit being intercepted is greatly reduced. However, to minimise it, and implement the guidance, it is possible to establish a VPN within that link. For steps, see this [AWS Direct Connect Support](https://aws.amazon.com/premiumsupport/knowledge-center/create-vpn-direct-connect/) article.

   For the second category, accessing AWS public APIs outside of a VPC, the primary applicable controls for data in transit protection are the TLS-secured API endpoints, accessible via the AWS Management Console, the [AWS Command Line Interface](https://aws.amazon.com/cli/) (AWS CLI) or [software development kits](https://aws.amazon.com/tools/) (SDKs) for a variety of programming languages. These may only be accessed with appropriate authentication (see [Section 9.1: Authentication of [admin] users to management interfaces and support channels](principle-9-secure-user-management.md#section-9.1-authentication-of-admin-users-to-management-interfaces-and-support-channels) of this document for more detail).

   While these public APIs are very secure, thanks to their encryption with TLS, customers also have the option of configuring their AWS environments to access these solely from within their VPCs using VPC endpoints. For a detailed explanation and associated directions on how to use these, see [VPC endpoints](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-endpoints.html).
