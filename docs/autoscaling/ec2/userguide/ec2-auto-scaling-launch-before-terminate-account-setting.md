---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/ec2-auto-scaling-launch-before-terminate-account-setting.html
---

# Launch replacement instances before terminating old ones
<a name="ec2-auto-scaling-launch-before-terminate-account-setting"></a>

*Launch before terminate* is an Amazon EC2 Auto Scaling feature that changes how your Auto Scaling groups replace instances. With launch before terminate, Amazon EC2 Auto Scaling launches replacement instances and waits for them to pass health checks before terminating the instances they replace, which prioritizes availability during replacement.

You can enable launch before terminate for an individual Auto Scaling group by setting an instance maintenance policy on the group, or for an individual instance refresh by setting minimum and maximum healthy percentage preferences. One way to make launch before terminate the default for all of your Auto Scaling groups is to enable the `launchBeforeTerminate` account setting. For more information about instance maintenance policies, see [Set an instance maintenance policy](set-instance-maintenance-policy.md).

Enable launch before terminate when you want your Auto Scaling groups to keep full capacity during instance replacements, so that a group doesn't drop below its desired capacity while a replacement is in progress. This helps during an instance refresh, and during other lifecycle events such as health check replacements, maximum instance lifetime replacements, and Availability Zone rebalancing.

When the account setting is enabled, Amazon EC2 Auto Scaling uses a minimum healthy percentage of **100** and a maximum healthy percentage of **110** by default. This default applies to groups that don't have an instance maintenance policy or set instance refresh preferences. If you configure an instance maintenance policy on a group, that policy takes precedence.

Similarly, if you start an [instance refresh](asg-instance-refresh.md) with minimum and maximum healthy percentage preferences, those preferences take precedence. An instance refresh started without those preferences uses the **100** and **110** defaults if there is no instance maintenance policy.

**Considerations**
Before you enable launch before terminate, review the following considerations:
+ **Capacity headroom** – This setting runs one additional instance for a short time during each replacement.
+ **Cost** – Because the setting runs one extra instance for the duration of each replacement, you pay for that extra instance for a short time.

**Instance replacement failure**
Launch before terminate must launch a replacement before it terminates the instance that it replaces. If Amazon EC2 Auto Scaling can't get capacity for the replacement, it keeps the original instance in service and retries, so your group doesn't lose capacity. A replacement can fail to launch when there isn't enough On-Demand capacity for the group's instance types and Availability Zones, or when a Capacity Reservation is full. To reduce the chance that a replacement can't launch, do one or more of the following:
+ Reserve more capacity than your group's desired capacity, so there's room for the extra instance during a replacement.
+ Make sure your group can use On-Demand capacity, so replacements can launch even when a Capacity Reservation is full.
+ Give your group more instance types and more Availability Zones to choose from, so Amazon EC2 Auto Scaling has more options for finding capacity.

**Recommendations for Capacity Reservations**
When you enable launch before terminate, a targeted On-Demand Capacity Reservation that you reference by a specific Capacity Reservation ID can leave one replacement instance running as regular On-Demand capacity. To keep replacements covered by your reservation, reference Capacity Reservations through a Capacity Reservation resource group by using the `CapacityReservationResourceGroupArns` parameter, or use open On-Demand Capacity Reservations. For more information, see [Use Capacity Reservations in your Auto Scaling group](use-ec2-capacity-reservations.md).

**Example: launch before terminate with a Capacity Reservation**  <a name="launch-before-terminate-cr-example"></a>
Suppose your Auto Scaling group runs 10 instances, you have an On-Demand Capacity Reservation for 10 instances, and the group uses all 10 reserved slots (the reservation is fully used). The group is configured to use its Capacity Reservations first.
When Amazon EC2 Auto Scaling replaces an instance, launch before terminate launches the replacement before it terminates the old instance. For a moment, the group needs capacity for 11 instances, but the reservation holds only 10 and the old instance still occupies its reserved slot. The replacement therefore launches as regular On-Demand capacity. After the old instance terminates, its reserved slot becomes free.
What happens to that running On-Demand instance depends on how your reservation is configured:
+ If you use an open Capacity Reservation, or you reference your reservation through a Capacity Reservation resource group, the freed slot reclaims the On-Demand instance automatically. Full reservation coverage is restored.
+ If you use a targeted Capacity Reservation that you reference by a specific Capacity Reservation ID, the freed slot does not reclaim the instance. One instance keeps running as On-Demand capacity while one reserved slot stays unused.
To keep replacements covered by your reservation, use an open Capacity Reservation, or reference a targeted Capacity Reservation through a Capacity Reservation resource group.
If your reservation has more capacity than your group uses (for example, a reservation for 11 instances for a group of 10), the replacement launches directly into a free reserved slot. In that case there is no On-Demand instance and no uncovered slot.

**To enable launch before terminate**
Use the [put-account-setting](https://docs.aws.amazon.com/cli/latest/reference/autoscaling/put-account-setting.html) command to set `launchBeforeTerminate` to `enabled`.

```
aws autoscaling put-account-setting \
    --name launchBeforeTerminate \
    --value enabled
```

**To view the current launch before terminate status**
Use the [describe-account-settings](https://docs.aws.amazon.com/cli/latest/reference/autoscaling/describe-account-settings.html) command.

```
aws autoscaling describe-account-settings \
    --name launchBeforeTerminate
```

For more information, see [Amazon EC2 Auto Scaling account settings](ec2-auto-scaling-account-settings.md).
