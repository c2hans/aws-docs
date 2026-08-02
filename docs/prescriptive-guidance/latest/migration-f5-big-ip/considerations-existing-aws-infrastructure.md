---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-f5-big-ip/considerations-existing-aws-infrastructure.html
---

# Connecting to your AWS infrastructure
<a name="considerations-existing-aws-infrastructure"></a>

The following table shows key consideration for when you connect to your new AWS infrastructure during an F5 BIG-IP migration.

|
|
| Connectivity method | Routing protocol support | Bandwidth limits | Endpoint IP addressing (public, private, or both) | Support for alien address space | Multi-VPC support for one connection | Multi-Region support |
| --- |--- |--- |--- |--- |--- |--- |
| Internet | N/A | You link in to AWS, 5 GB-seconds per instance out | Public | No | Yes | Yes |
| VPN - VPC | Static, BGP | IPsec limits (about 1.2 GB-seconds per tunnel) | Private | Yes (you must set up an additional IPsec tunnel from the F5 BIG-IP in the VPC to the virtual gateway connected to the VPC). | No | No |
| VPN and AWS Transit Gateway | Static, BGP | IPsec limits (about 1.2 GB-seconds per tunnel) | Private | Yes | Yes | No (if the transit gateway is extended, it will be impacted) |
| AWS Direct Connect - VPC | Static, BGP | AWS Direct Connect limits (supports bonding), individual instances limited to 5 GB-seconds | Both | No | No | No |
| AWS Direct Connect - gateway | Static, BGP | AWS Direct Connect limits (supports bonding), individual instances limited to 5 GB-seconds | Both | No | Yes | Yes |
| AWS Direct Connect gateway - AWS Transit Gateway (limited to several AWS Regions) | Static, BGP | AWS Direct Connect limits (supports bonding), individual instances limited to 5 GB-seconds | Verbal confirmation from AWS architect team | Yes | Yes | Limited to several Regions |
