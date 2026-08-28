---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-add-az-console.html
---

# Add an Availability Zone
<a name="as-add-az-console"></a>

To take advantage of the safety and reliability of geographic redundancy, span your Auto Scaling group across multiple Availability Zones of the Region you are working in and attach a load balancer to distribute incoming traffic across those Availability Zones.

When one Availability Zone becomes unhealthy or unavailable, Amazon EC2 Auto Scaling launches new instances in an unaffected Availability Zone. When the unhealthy Availability Zone returns to a healthy state, Amazon EC2 Auto Scaling automatically redistributes the application instances evenly across all the Availability Zones for your Auto Scaling group. Amazon EC2 Auto Scaling does this by attempting to launch new instances in the Availability Zone with the fewest instances. If the attempt fails, however, Amazon EC2 Auto Scaling attempts to launch in other Availability Zones until it succeeds.

Elastic Load Balancing creates a load balancer node for each Availability Zone you enable for the load balancer. If you enable cross-zone load balancing for your load balancer, each load balancer node distributes traffic evenly across the registered instances in all enabled Availability Zones. If cross-zone load balancing is disabled, each load balancer node distributes requests evenly across the registered instances in its Availability Zone only.

You must specify at least one Availability Zone when you are creating your Auto Scaling group. Later, you can expand the availability of your application by adding an Availability Zone to your Auto Scaling group and enabling that Availability Zone for your load balancer (if the load balancer supports it).

**Limitations**
To update which Availability Zones are enabled for your load balancer, you need to be aware of the following limitations:
+ When you enable an Availability Zone for your load balancer, you specify one subnet from that Availability Zone. Note that you can enable at most one subnet per Availability Zone for your load balancer.
+ For internet-facing load balancers, the subnets that you specify for the load balancer must have at least eight available IP addresses.
+ For Application Load Balancers, you must enable at least two Availability Zones.
+ For Network Load Balancers, you cannot disable the enabled Availability Zones, but you can enable additional ones.
+ For Gateway Load Balancers, you cannot disable the enabled Availability Zones, but you can enable additional ones.

Use the following procedure to expand your Auto Scaling group and load balancer to a subnet in an additional Availability Zone.

**To add an Availability Zone**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to an existing group.

   A split pane opens up in the bottom of the **Auto Scaling groups** page.

1. On the **Details** tab, choose **Network**, **Edit**.

1. In **Subnets**, choose the subnet corresponding to the Availability Zone that you want to add to the Auto Scaling group.

1. Choose **Update**.

1. To update the Availability Zones for your load balancer so that it shares the same Availability Zones as your Auto Scaling group, complete the following steps:

   1. On the navigation pane, under **Load Balancing**, choose **Load Balancers**.

   1. Choose your load balancer.

   1. Do one of the following:
      + For Application Load Balancers and Network Load Balancers:

        1. On the **Description** tab, for **Availability Zones**, choose **Edit subnets**.

        1. On the **Edit subnets** page, for **Availability Zones**, select the check box for the Availability Zone to add. If there is only one subnet for that zone, it is selected. If there is more than one subnet for that zone, select one of the subnets.
      + For Classic Load Balancers in a VPC:

        1. On the **Instances** tab, choose **Edit Availability Zones**.

        1. On the **Add and Remove Subnets** page, for **Available subnets**, select the subnet using its add (\+) icon. The subnet is moved under **Selected subnets**.

   1. Choose **Save**.

## Related resources
<a name="availability-zone-related-resources"></a>

Amazon EC2 Auto Scaling rebalances your group when you change Availability Zones. This means replacing and redistributing some instances. For more information, see [Example: Distribute instances across Availability Zones](auto-scaling-benefits.md#arch-AutoScalingMultiAZ).

If you have registered targets in Availability Zones that are not enabled for the load balancer, the load balancer does not route traffic to them. For more information, see [How Elastic Load Balancing works](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html) in the *Elastic Load Balancing User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
