---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/target-capacity-reservations.html
---

# Target Capacity Reservations from your Auto Scaling group
<a name="target-capacity-reservations"></a>

To target Amazon EC2 Capacity Reservations and Capacity Blocks for ML from your Auto Scaling group, you can configure a Capacity Reservation preference and target on the group itself, or set a market type on your launch template alongside a Capacity Reservation target on the group. To choose between these mechanisms, see [Use Capacity Reservations in your Auto Scaling group](use-ec2-capacity-reservations.md). For step-by-step procedures, see [Configure your Auto Scaling group to launch instances with Capacity Reservations](capacity-reservation-create-asg-procedure.md).

## Use a Capacity Reservation specification with your Auto Scaling group
<a name="capacity-reservation-specification"></a>

Use a Capacity Reservation specification (`CapacityReservationSpecification`) to indicate to your Auto Scaling group how and where to consume Capacity Reservations. A Capacity Reservation specification has two parts: a preference that tells Auto Scaling how strongly to prefer reserved capacity over On-Demand capacity, and an optional target that identifies which reservations to consume.

A Capacity Reservation specification alone handles consuming On-Demand Capacity Reservations from your Auto Scaling group.

To consume Capacity Blocks or interruptible Capacity Reservations, combine the specification with either:
+ A market type on your launch template. For more information, see [Target Capacity Blocks or interruptible Capacity Reservations from a launch template](capacity-reservation-create-asg-procedure.md#target-capacity-blocks-or-interruptible-capacity-reservations-from-a-launch-template).
+ A Capacity Reservation Resource Group as a target on your Auto Scaling group, together with distribution segments (`DistributionSegments`).

### Capacity Reservation preference
<a name="asg-capacity-reservation-preference"></a>

The Capacity Reservation preference (`CapacityReservationPreference`) tells Auto Scaling how to consume Capacity Reservations when launching instances. Choose one of the following values.
+ **Default** (`default`) – Auto Scaling uses the Capacity Reservation specification from your launch template. If your Auto Scaling group uses distribution segments, Auto Scaling instead consumes reservations according to the priority order defined in the distribution segments.
+ **Capacity Reservations only** (`capacity-reservations-only`) – Auto Scaling only launches instances into a Capacity Reservation or Capacity Reservation Resource Group. If no reserved capacity is available, instances fail to launch.
+ **Capacity Reservations first** (`capacity-reservations-first`) – Auto Scaling launches instances into a Capacity Reservation or Capacity Reservation Resource Group when available. If no reserved capacity is available, instances launch as On-Demand.
+ **None** (`none`) – Auto Scaling does not launch instances into a Capacity Reservation. Instances run as On-Demand capacity.

**Important**
**Distribution segments** – Only `default` is supported. You can configure `capacity-reservations-only` or `capacity-reservations-first` behavior by setting the capacity types priority in your distribution segments directly.

### Capacity Reservation target
<a name="capacity-reservation-target"></a>

The Capacity Reservation target (`CapacityReservationTarget`) tells Auto Scaling which Capacity Reservations it can launch instances into. Choose one of the following options.
+ **Specific Capacity Reservation** (`CapacityReservationIds`) – Provide a Capacity Reservation ID. Auto Scaling launches instances into this Capacity Reservation.
+ **Capacity Reservation Resource Group** (`CapacityReservationResourceGroupArns`) – Provide a Capacity Reservation Resource Group ARN. Auto Scaling launches instances into any Capacity Reservation in this group with matching attributes.
+ **Open** – Don't specify a target on your Auto Scaling group or launch template. Auto Scaling launches instances into any open Capacity Reservation in your account with compatible attributes.
+ **From launch template** – Don't specify a target on your Auto Scaling group. Auto Scaling uses the Capacity Reservation target from your launch template.

**Important**
Only a single Capacity Reservation ID or Capacity Reservation Resource Group ARN is allowed as a Capacity Reservation target.
**Precedence with distribution segments** – When distribution segments are configured, they take precedence over the Capacity Reservation and market type settings in your launch template.

### Availability Zone balance
<a name="az-balance-capacity-reservations"></a>

By default, Auto Scaling prioritizes Availability Zone balance when consuming Capacity Reservations. The exact behavior depends on whether On-Demand fallback is enabled:
+ **With On-Demand fallback** – Auto Scaling distributes instances evenly across Availability Zones. If reserved capacity isn't available in an Availability Zone, instances launch as On-Demand to maintain the balance.
+ **Without On-Demand fallback** – Auto Scaling only launches instances into Capacity Reservations. This can result in uneven distribution across Availability Zones, or the Auto Scaling group might not reach its desired capacity if reserved capacity is insufficient.

**Example**
If you have 10 Capacity Reservations in AZ-a, 3 in AZ-b, 1 in AZ-c, and a desired capacity of 9 instances:
+ With On-Demand fallback, Auto Scaling launches 3 instances per Availability Zone (maintaining balance), with some instances potentially launching as On-Demand.
+ Without On-Demand fallback, Auto Scaling launches into whichever Capacity Reservations are available, which can result in uneven distribution across Availability Zones. If matching reservations don't cover the full desired capacity, the Auto Scaling group might not launch all 9 instances.

**Note**
To prioritize Capacity Reservation utilization over Availability Zone balance, use the `reservations-then-balanced` Availability Zone distribution strategy. For more information, see [Auto Scaling group Availability Zone distribution](ec2-auto-scaling-availability-zone-balanced.md).
