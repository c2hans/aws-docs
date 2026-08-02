---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/customer-managed-vpn-and-sd-wan.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Customer-managed VPN and SD-WAN
<a name="customer-managed-vpn-and-sd-wan"></a>

## Definition
<a name="definition-8"></a>

 Connectivity to the internet is a commodity and available bandwidth continues to increase every year. Some customers choose to build a virtual WAN on top of the internet instead of building and operating a private WAN. A software-defined wide area network (SD-WAN) allows companies to rapidly provision and manage centrally this virtual WAN through clever use of software. Other customers choose to adopt traditional self-managed site to site VPNs.

## Impact on design decisions
<a name="impact-on-design-decisions"></a>

 SD-WAN and customer-managed VPNs can run over internet or AWS Direct Connect. SD-WAN (or any software VPN overlay) is as reliable as the underlying network transport. Therefore, the reliability and SLA considerations discussed earlier in this whitepaper are applicable here. For instance, building a SD-WAN overlay over the internet will not offer the same reliability versus if it's built over an AWS Direct Connect.

## Requirement definition
<a name="requirement-definition"></a>
+  Do you use SD-WAN in your on-premises network?
+  Are there specific features you require which are only available on certain virtual appliances used for VPN termination?

## Technical solutions
<a name="technical-solutions-1"></a>

 AWS recommends integrating SD-WAN with AWS Transit Gateway, and publishes a list of [the vendors who support AWS Transit Gateway integration](https://aws.amazon.com/transit-gateway/network-manager/). AWS can act as a hub for SD-WAN sites or as a spoke site. The AWS backbone can be used to connect different SD-WAN hubs deployed in AWS with a highly reliable and performant network. SD-WAN solutions support automated failover through any available path, additional monitoring, and observability capabilities in a single management pane. Extensive use of auto configuration and automation allows rapid provisioning and visibility compare to traditional WANs. However, the use of tunneling and encryption overheads do not compare to dedicated, high-speed fiber links used in private connectivity.

 In some cases, you may choose to use a virtual appliance with VPN capability. Reasons for selecting a self-managed virtual appliance include technical features and compatibility with the rest of your network. When you select a self-managed VPN or an SD-WAN solution which uses a virtual appliance deployed in an EC2 instance, you are responsible for the management of such appliance. You are also responsible for high availability and failover between virtual appliances. Such design increases your operational responsibility; however, it could provide you more flexibility. The features and capabilities of the solution depend on the virtual appliance you select.

 AWS Marketplace contains many VPN virtual appliances which customers can deploy on Amazon EC2. AWS recommends starting with AWS managed S2S VPN and look at other options if it doesn’t meet your requirements. The management overhead of virtual appliances is the customer responsibility.
