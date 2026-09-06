---
source_url: https://docs.aws.amazon.com/whitepapers/latest/access-workspaces-with-access-cards/amazon-virtual-private-cloud.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Amazon Virtual Private Cloud
<a name="amazon-virtual-private-cloud"></a>

## Region selection
<a name="region-selection"></a>

Pre-session authentication is available only in the AWS GovCloud (US-West) Region at this time. In-session authentication is available in all Regions where WSP is supported.

## VPC configuration
<a name="vpc-configuration"></a>

Amazon WorkSpaces launches your WorkSpaces in a virtual private cloud (VPC). Your WorkSpaces must have access to the internet, so you can install updates to the operating system and deploy applications using [Amazon WorkSpaces Application Manager](https://aws.amazon.com/workspaces/applicationmanager/) (Amazon WAM).

You can create a VPC with two private subnets for your WorkSpaces and a [NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html) in a public subnet. Alternatively, you can create a VPC with two public subnets for your WorkSpaces and associate an Elastic IP address with each WorkSpace.

Your VPC's subnets must reside in different Availability Zones in the Region where you're launching WorkSpaces. Availability Zones are distinct locations that are engineered to be isolated from failures in other Availability Zones. By launching instances in separate Availability Zones, you can protect your applications from the failure of a single location. Each subnet must reside entirely within one Availability Zone, and cannot span zones.

For details on VPC configuration, see [Configure a VPC for Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-vpc.html).
