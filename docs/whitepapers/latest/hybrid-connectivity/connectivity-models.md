---
source_url: https://docs.aws.amazon.com/whitepapers/latest/hybrid-connectivity/connectivity-models.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Connectivity models
<a name="connectivity-models"></a>

## Definition
<a name="definition-con"></a>

 The connectivity model refers to the communication pattern between on-premises network(s) and the cloud resources in AWS. You can deploy cloud resources within an Amazon VPC within a single AWS Region or multiple VPCs across multiple Regions, as well as AWS services which have a public endpoint in a single or multiple AWS Regions, such as Amazon S3 and DynamoDB.

## Key questions
<a name="key-questions-con"></a>
+  Is there a requirement for inter-VPC communication within a Region and across Regions?
+  Is there any requirement to access AWS public endpoints directly from on-premises?
+  Is there a requirement to access AWS services using VPC endpoints from on-premises?

## Capabilities to consider
<a name="capabilities-to-consider-con"></a>

 The following are some of the most common connectivity model scenarios. Each connectivity model covers requirements, attributes, and considerations.

 Note: as highlighted earlier, this whitepaper is focused on the hybrid connectivity between on-premises networks and AWS. For further details on the design to interconnect VPCs, refer to the [Building a Scalable and Secure Multi-VPC AWS Network Infrastructure](https://docs.aws.amazon.com/whitepapers/latest/building-scalable-secure-multi-vpc-network-infrastructure/welcome.html) whitepaper.

**Topics**
+ [Definition](#definition-con)
+ [Key questions](#key-questions-con)
+ [Capabilities to consider](#capabilities-to-consider-con)
+ [AWS Accelerated Site-to-Site VPN – AWS Transit Gateway, Single AWS Region](aws-accelerated-site-to-site-vpn-aws-transit-gateway-single-aws-region.md)
+ [AWS DX – DXGW with VGW, Single Region](aws-dx-dxgw-with-vgw-single-region.md)
+ [AWS DX – DXGW with VGW, Multi-Regions, and AWS Public Peering](aws-dx-dxgw-with-vgw-multi-regions-and-aws-public-peering.md)
+ [AWS DX – DXGW with AWS Transit Gateway, Multi-Regions, and AWS Public Peering](aws-dx-dxgw-with-aws-transit-gateway-multi-regions-and-aws-public-peering.md)
+ [AWS DX – DXGW with AWS Transit Gateway, Multi-Regions (more than 3)](aws-dx-dxgw-with-aws-transit-gateway-multi-regions-more-than-3.md)
