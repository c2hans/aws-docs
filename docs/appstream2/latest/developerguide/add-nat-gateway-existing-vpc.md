---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/add-nat-gateway-existing-vpc.html
---

# Add a NAT Gateway to an Existing VPC
<a name="add-nat-gateway-existing-vpc"></a>

If you have already configured a VPC, complete the following steps to add a NAT gateway to your VPC. If you need to create a new VPC, see [Create and Configure a New VPC](create-configure-new-vpc-with-private-public-subnets-nat.md).

**To add a NAT gateway to an existing VPC**

1. To create your NAT gateway, complete the steps in [Creating a NAT Gateway](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html#nat-gateway-creating) in the *Amazon VPC User Guide*.

1. Verify that your VPC has at least one private subnet. We recommend that you specify two private subnets from different Availability Zones for high availability and fault tolerance. For information about how to create a second private subnet, see [Step 3: Add a Second Private Subnet](create-configure-new-vpc-with-private-public-subnets-nat.md#vpc-with-private-and-public-subnets-add-private-subnet-nat).

1. Update the route table associated with one or more of your private subnets to point internet-bound traffic to the NAT gateway. This enables the streaming instances in your private subnets to communicate with the internet. To do so, complete the steps in [Configure route tables](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Route_Tables.html).

**Next Steps**

To enable your fleet instances, app block builders, and image builders to access the internet, complete the steps in [Enable Internet Access for Your Fleet, Image Builder, or App Block Builder in Amazon WorkSpaces Applications](managing-network-manual-enable-internet-access.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
