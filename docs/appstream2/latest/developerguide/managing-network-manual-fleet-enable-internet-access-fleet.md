---
source_url: https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-network-manual-fleet-enable-internet-access-fleet.html
---

# Enable Internet Access for Your Fleet in Amazon WorkSpaces Applications
<a name="managing-network-manual-fleet-enable-internet-access-fleet"></a>

You can enable internet access either when you create the fleet or later.

**To enable internet access at fleet creation**

1. Complete the steps in [Create a Fleet in Amazon WorkSpaces Applications](set-up-stacks-fleets-create.md) up to **Step 4: Configure Network**.

1. Choose a VPC with a NAT gateway.

1. If the subnet fields are empty, select a private subnet for **Subnet 1** and, optionally, another private subnet for **Subnet 2**. If you don't already have a private subnet in your VPC, you may need to create a second private subnet.

1. Continue with the steps in [Create a Fleet in Amazon WorkSpaces Applications](set-up-stacks-fleets-create.md).

**To enable internet access after fleet creation by using a NAT gateway**

1. In the navigation pane, choose **Fleets**.

1. Select a fleet and verify that the state is **Stopped**.

1. Choose **Fleet Details**, **Edit**, and choose a VPC with a NAT gateway.

1. Choose a private subnet for **Subnet 1** and, optionally, another private subnet for **Subnet 2**. If you don't already have a private subnet in your VPC, you may need to [create a second private subnet](create-configure-new-vpc-with-private-public-subnets-nat.md#vpc-with-private-and-public-subnets-add-private-subnet-nat).

1. Choose **Update**.

You can test your internet connectivity by starting your fleet, and then connecting to your streaming instance and browsing to the internet.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
