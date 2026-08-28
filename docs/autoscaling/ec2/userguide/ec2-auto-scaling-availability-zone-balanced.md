---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-availability-zone-balanced.html
---

# Auto Scaling group Availability Zone distribution
<a name="ec2-auto-scaling-availability-zone-balanced"></a>

The following information describes Auto Scaling group Availability Zone strategies.

**Balanced best effort**
Auto Scaling maintains an equal number of instances across enabled Availability Zones. If launch attempts fail in an Availability Zone, Auto Scaling attempts to launch instances in another healthy Availability Zone. This strategy is important for applications that need Availability Zone redundancy and are not impacted by imbalanced groups.

**Balanced only**
Auto Scaling maintains an equal number of instances across enabled Availability Zones. If launch attempts fail in an Availability Zone, Auto Scaling will continue to attempt to launch instances in the Availability Zone. This strategy is important to meet certain requirements such as quorum-based workloads or if your Auto Scaling group can tolerate the loss of an Availability Zone because you have sufficient capacity in the remaining Availability Zones.

**Reservations then balanced**
Auto Scaling first launches instances into the Capacity Reservations associated with the group, prioritizing reservation use over even distribution across the group's enabled Availability Zones. After all available reservations are filled, Auto Scaling distributes any remaining capacity evenly across the enabled Availability Zones. Use this strategy for cost-sensitive workloads that use Capacity Reservations, such as GPU, high performance computing (HPC), or machine learning workloads. With this strategy, maximizing reservation utilization takes priority over even Availability Zone distribution.
You specify the reservations to prioritize by providing a Capacity Reservation group or an individual Capacity Reservation ID. You can specify the target in your launch template or on the Auto Scaling group using [CapacityReservationTarget](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_CapacityReservationTarget.html). To prioritize more than one reservation, you can create a Capacity Reservation resource group. This strategy supports On-Demand Capacity Reservations, Capacity Blocks, and interruptible Capacity Reservations.
During scale in, Auto Scaling removes instances that are not in a reservation first, to preserve reservation utilization. If further scale in is required, Auto Scaling then removes reserved instances, starting with the Availability Zone that has the most reserved instances.

The Availability Zone distribution strategy selection is in the **Network** section of the AWS Management Console or you can use the [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) or [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) commands.

When you choose the **Reservations then balanced** strategy, you must also specify the Capacity Reservations to prioritize, either by Capacity Reservation Resource Group or by individual Capacity Reservation ID.

For more information, see [Create Auto Scaling groups using launch templates](create-auto-scaling-groups-launch-template.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
