---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/security.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Security
<a name="security"></a>

## Definition
<a name="definition-sec"></a>

 Security requirements will influence your hybrid connectivity type. These considerations include:
+  Transport type – internet or private network connection
+  Encryption requirements

## Key questions
<a name="key-questions-sec"></a>
+  Do your security requirements and policies allow the use of encrypted connections over the internet to connect to AWS, or do they mandate the use of private network connections?
+  When leveraging private network connections, does the network layer have to provide encryption in transit?

## Technical solutions
<a name="technical-solutions"></a>

 Your security requirements and policies might permit use of internet or require use of a private network connection between AWS and your company network. They also affect the decision if the network must provide encryption in transit, or if performing encryption at application layer is acceptable.

 If you can leverage the internet, then AWS Site-to-Site VPN can be used to create encrypted tunnels between your network and your Amazon VPCs or AWS Transit Gateways over the internet. Extending your [SD-WAN](https://en.wikipedia.org/wiki/SD-WAN) solution into AWS over the internet is also an option if you are leveraging an internet-based connection. The section Customer-managed VPN and SD-WAN later in this whitepaper covers the specific considerations for SD-WAN.

 If you require a private network connection between AWS and your company network, then AWS recommends using AWS Direct Connect Dedicated Connections or Hosted Connections. If encryption in transit is required over a private network connection, then you should establish a VPN over Direct Connect (either over public VIF or transit VIF), or consider using MACsec on a 10Gbps or 100Gbps Dedicated connection.

*Table 2 – Example Automotive Corp connectivity type requirements*

|   |  Site-to-Site VPN  |  Direct Connect  |
| --- | --- | --- |
|  Transport  |  Internet  |  Private network connection  |
|  Encryption in transit  |  Yes  |  Requires S2S VPN over DX, S2S VPN over a transit VIF, or MACsec on a 10Gbps or 100Gbps Dedicated Connection  |
