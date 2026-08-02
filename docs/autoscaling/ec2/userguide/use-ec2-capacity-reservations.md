---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/use-ec2-capacity-reservations.html
---

# Reserve capacity in specific Availability Zones with Capacity Reservations
<a name="use-ec2-capacity-reservations"></a>

Amazon EC2 On-Demand Capacity Reservations allow you to reserve compute capacity in specific Availability Zones. To start using Capacity Reservations with Auto Scaling, first you create a Capacity Reservation or a Capacity Reservation group in a specific Availability Zone. Then, you can add a Capacity Reservation preference to your Auto Scaling group when you create it or when you update an existing group.

To create a Capacity Reservation, see [Create a Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-create.html) in the *Amazon EC2 User Guide*. To create a Capacity Reservation group, see [Create a Capacity Reservation group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-cr-group.html) in the *Amazon EC2 User Guide*.

## Capacity Reservation preference
<a name="asg-capacity-reservation-preference"></a>

Capacity Reservation preference helps you use Capacity Reservations efficiently by prioritizing reserved capacity in a Capacity Reservation before using On-Demand capacity. You can select from the following Capacity Reservation preference options:
+ **Default** – Auto Scaling uses the Capacity Reservation preference from your launch template or an open Capacity Reservation.
+ **None** – Auto Scaling will not launch instances into a Capacity Reservation. Instances will run in On-Demand capacity.
+ **Capacity Reservations only** – Auto Scaling will only launch instances into a Capacity Reservation or Capacity Reservation group. If capacity isn't available, instances will fail to launch.
+ **Capacity Reservations first** – Auto Scaling will launch instances into a Capacity Reservation or Capacity Reservation group. If capacity isn't available instances will run in On-Demand capacity.

If you select Capacity Reservations only or Capacity Reservations first, you can specify a Capacity Reservation target.

**Note**
You must select a Capacity Reservation preference. Capacity Reservation target is optional.

**Considerations for Capacity Reservation preference and launch templates**
Consider the following if you select Capacity Reservations only or Capacity Reservations first:
+ If you select Capacity Reservations only or Capacity Reservations first, Auto Scaling will use the Capacity Reservation target specified in the Auto Scaling group instead of the Capacity Reservation target in the launch template.
+ If you select Capacity Reservations only or Capacity Reservations first and you don't specify a Capacity Reservation target, Auto Scaling will use the launch template Capacity Reservation target or an open Capacity Reservation.

**Capacity Reservation target specification**
If you select Capacity Reservations only or Capacity Reservations first, the following Capacity Reservation target options are available:
+ **Open** – Auto Scaling will launch instances into any open Capacity Reservation. If you selected Capacity Reservations only and capacity isn't available, instances will fail to launch. If you selected Capacity Reservations first and capacity isn't available, instances will launch in On-Demand capacity.
+ **Specify Capacity Reservation** – Auto Scaling will launch instances into the specified Capacity Reservation. If you selected Capacity Reservations only and capacity isn't available, instances will fail to launch. If you selected Capacity Reservations first and capacity isn't available, instances will launch in On-Demand capacity.
+ **Specify Capacity Reservation resource group** – Auto Scaling will launch instances into an open Capacity Reservation in the specified Capacity Reservation resource group. If you selected Capacity Reservations only and capacity isn't available, instances will fail to launch. If you selected Capacity Reservations first and capacity isn't available, instances will launch in On-Demand capacity.

## Availability Zone balance and Capacity Reservations
<a name="az-balance-capacity-reservations"></a>

Auto Scaling prioritizes Availability Zone balance even when you're using Capacity Reservations preferences. This means:
+ With `capacity-reservations-first` – The Auto Scaling group will distribute instances evenly across AZs first, then use Capacity Reservations where available. If Capacity Reservations aren't available in an AZ, instances will launch as On-Demand to maintain AZ balance.
+ With `capacity-reservations-only` – The Auto Scaling group will only use Capacity Reservations. This might result in uneven instance distribution across AZs based on where Capacity Reservations are available.

**Example**
If you have 10 Capacity Reservations in AZ-a, 3 in AZ-b, 1 in AZ-c, and a desired capacity of 9 instances:
+ Using `capacity-reservations-first` for 9 instances will result in 3 instances per AZ (maintaining AZ balance), with some instances potentially running as On-Demand.
+ Using `capacity-reservations-only` for 9 instances will result in uneven distribution based on available Capacity Reservations.
