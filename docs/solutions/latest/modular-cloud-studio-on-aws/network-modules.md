---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/network-modules.html
---

# Network modules
<a name="network-modules"></a>

Network modules create the necessary resources for other modules and components to communicate with each other.

The following Network modules are available in MCS after deployment:
+ Managed VPC module - Deploys a new VPC
+ Unmanaged VPC module - Receives existing VPC information from an input form

## Managed VPC module
<a name="managed-vpc-module"></a>

![managed vpc module](https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/images/managed-vpc-module.png)

1. The Solution deploys a VPC with two Availability Zones. Each zone contains:
   + One public subnet - routes traffic to an [internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)
   + One private subnet - routes traffic to a [NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)
**Note**
Pixel streaming traffic doesn’t travel through the NAT gateway.

1. The solution creates [VPC Endpoints](https://docs.aws.amazon.com/whitepapers/latest/aws-privatelink/what-are-vpc-endpoints.html) to ensure that internal traffic to these services connects privately and doesn’t traverse the public internet.

1. Default EventBridge buses in each enabled region send EC2 instance state change events to a state machine for applying tags to any EC2 instance launched within an MCS VPC.

## Unmanaged VPC module
<a name="unmanaged-vpc-module"></a>

![unmanaged vpc module](https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/images/unmanaged-vpc-module.png)

1. The solution can utilize an existing VPC for module deployment. However, any additional configuration required for module functionality must be managed by the MCS administrator.

1. You can optionally enable EventBridge infrastructure for automatic EC2 tagging through the Unmanaged VPC’s deployment parameters (default: Yes). When enabled, default EventBridge buses in each enabled region send EC2 instance state change events to a state machine for applying tags to any EC2 instance launched within an MCS VPC.

1. To toggle EC2 tagging post-deployment, locate the EventBridge rule created by your Unmanaged VPC deployment (rule name contains `EC2InstanceTagging`) and choose **Disable** or **Enable** as needed.

**Note**
If EventBridge EC2 Tagging Parameter is disabled at deployment, tagging infrastructure will not be deployed and the feature cannot be enabled later. If enabled, tagging can be toggled on or off post-deployment by enabling or disabling the EventBridge Rule.

## Spoke Managed VPC module
<a name="spoke-managed-vpc-module"></a>

![spoke managed vpc module](https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/images/spoke-managed-vpc-module.png)

1. The solution establishes a [VPC peering connection](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html) between the existing VPC in the hub Region and the VPC being created in this module, enabling inter-VPC communication.

1. The solution creates a VPC spanning two Availability Zones. Each zone contains:
   + One public subnet - routes traffic through an [Internet Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html)
   + One private subnet - routes outbound traffic through a [NAT gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html)

1. Default EventBridge buses in each enabled region send EC2 instance state change events to a state machine for applying tags to any EC2 instance launched within an MCS VPC.
