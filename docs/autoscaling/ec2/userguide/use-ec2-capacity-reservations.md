---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/use-ec2-capacity-reservations.html
---

# Use Capacity Reservations in your Auto Scaling group
<a name="use-ec2-capacity-reservations"></a>

With Amazon EC2 Auto Scaling and Amazon EC2 Capacity Reservations, you can launch instances from your Auto Scaling group into reserved compute capacity. This page describes the Capacity Reservation types that Auto Scaling supports and helps you choose the approach that fits your workload.

## What are Capacity Reservations?
<a name="what-are-capacity-reservations"></a>

A Capacity Reservation reserves Amazon EC2 compute capacity in a specific Availability Zone, so that capacity is available when your Auto Scaling group needs to launch instances. Amazon EC2 offers several types of Capacity Reservations that fit different workload patterns. For more information, see [Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html) in the *Amazon EC2 User Guide*.

## Capacity Reservation types supported
<a name="capacity-reservation-types-supported"></a>

Auto Scaling supports the following Amazon EC2 Capacity Reservation types.
+ **On-Demand Capacity Reservations** – Reserve compute capacity in a specific Availability Zone with no term commitment. For more information, see [Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-reservations.html) in the *Amazon EC2 User Guide*.
+ **Capacity Blocks** – Reserve GPU-based compute capacity for a fixed window, commonly used for machine learning training, fine-tuning, and inference. When the Capacity Block expires, Amazon EC2 terminates the instances running in it. For more information, see [Capacity Blocks for ML](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-capacity-blocks.html) in the *Amazon EC2 User Guide*.
+ **Interruptible Capacity Reservations** – Unused reserved capacity from your On-Demand Capacity Reservations, or interruptible reservations shared with you through AWS Resource Access Manager, in exchange for accepting a 2-minute reclamation notice. For more information, see [Interruptible Capacity Reservations](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/interruptible-capacity-reservations.html) in the *Amazon EC2 User Guide*.

## How to use Capacity Reservations with your Auto Scaling group
<a name="how-to-use-capacity-reservations"></a>

Auto Scaling supports the following ways to consume Capacity Reservations. Choose based on your workload and the types of reservations you use.

| If you want to... | Use | Learn more |
| --- | --- | --- |
| Consume On-Demand Capacity Reservations from your Auto Scaling group | A Capacity Reservation preference and target on your Auto Scaling group | [Target Capacity Reservations from your Auto Scaling group](target-capacity-reservations.md) |
| Mix On-Demand Capacity Reservations, Capacity Blocks for ML, interruptible Capacity Reservations, and On-Demand capacity in one group with priority ordering | A Capacity Reservation Resource Group with multiple Capacity Reservations or Capacity Blocks for ML targeted from your Auto Scaling group | [Use Distribution Segments to target multiple Capacity Reservation types](use-distribution-segments.md) |
| Consume any mix of Capacity Blocks for ML or interruptible Capacity Reservations through a launch template | A market type on your launch template, and a Capacity Reservation target on your Auto Scaling group | [Target Capacity Blocks or interruptible Capacity Reservations from a launch template](capacity-reservation-create-asg-procedure.md#target-capacity-blocks-or-interruptible-capacity-reservations-from-a-launch-template) |

If you want to launch instances into different types of Capacity Reservations across multiple instances, we recommend creating a Capacity Reservation Resource Group that contains different types of Capacity Reservations. You can then target the Capacity Reservation Resource Group from your Auto Scaling group using Distribution Segments, which lets you configure priority-based ordering with optional fallback to On-Demand capacity, all without modifying your launch template.

If your Auto Scaling group uses only a single instance type and you don't want to migrate to a mixed instances policy, launch-template-based targeting continues to be supported for Capacity Blocks and interruptible Capacity Reservations.

## Prerequisites
<a name="capacity-reservations-prerequisites"></a>

Before you can use Capacity Reservations in your Auto Scaling group, you must create the reservations that you want to use. Depending on the reservation type, see one of the following in the *Amazon EC2 User Guide*:
+ [Create a Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-create.html) – for On-Demand Capacity Reservations
+ [Find and purchase Capacity Blocks](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-blocks-purchase.html) – for Capacity Blocks for ML
+ [Interruptible Capacity Reservations for capacity owners](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/interruptible-capacity-reservations.html#capacity-owner-considerations) – for interruptible Capacity Reservations

If you intend to use multiple Capacity Reservations with one Auto Scaling group, you can also create a Capacity Reservation Resource Group. For more information, see [Capacity Reservation Resource Groups](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-cr-group.html) in the *Amazon EC2 User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
