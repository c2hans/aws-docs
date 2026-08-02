---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/capacity-reservation-create-asg-procedure.html
---

# Use Capacity Reservation preference with your Auto Scaling group
<a name="capacity-reservation-create-asg-procedure"></a>

To use Capacity Reservations with your Auto Scaling group, you must first create a Capacity Reservation or a Capacity Reservation resource group. Then, you can add a Capacity Reservation preference to your Auto Scaling group when you create it or when you update an existing group.

To create a Capacity Reservation, see [Create a Capacity Reservation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-reservations-create.html) in the *Amazon EC2 User Guide*. To create a Capacity Reservation group, see [Create a Capacity Reservation group](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-group.html) in the *Amazon EC2 User Guide*.

Use one of the following methods to use Capacity Reservation preference when you are creating or editing a Auto Scaling group.

------
#### [ Console ]

**To use Capacity Reservation preference on a new group (console)**

1. Follow the instructions in [Create an Auto Scaling group using the Amazon EC2 launch wizard](create-asg-ec2-wizard.md) and complete each step in the procedure, up to step 3.

1. On the **Configure group size and scaling** page, under **Additional capacity settings**, **Capacity Reservation preference**, select a Capacity Reservation preference. For more information about Capacity Reservation preference, see [Capacity Reservation preference](use-ec2-capacity-reservations.md#asg-capacity-reservation-preference).

1. Continue with the steps in [Create an Auto Scaling group using the Amazon EC2 launch wizard](create-asg-ec2-wizard.md).

------
#### [ AWS CLI ]

**To use Capacity Reservation preference on a new group (AWS CLI)**
Add the `--capacity-reservation-specification` parameter to the [create-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/create-auto-scaling-group.html) command.

1. Specify a Capacity Reservation preference. For more information, see [Capacity Reservation preference](use-ec2-capacity-reservations.md#asg-capacity-reservation-preference).

1. Specify a Capacity Reservation target. If you select Capacity Reservations only or Capacity Reservations first and you don't specify a Capacity Reservation target, Auto Scaling will use the launch template Capacity Reservation target or an open Capacity Reservation.

------

------
#### [ Console ]

**To use Capacity Reservation preference on an existing group (console)**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. On the navigation bar at the top of the screen, choose the AWS Region that you created your Auto Scaling group in.

1. Select the check box next to the Auto Scaling group.

   A split pane opens up in the bottom of the page.

1. On the **Details** tab, under **Capacity Reservation preference**, choose **Edit**.

1. Under **Additional capacity settings**, **Capacity Reservation preference**, select a Capacity Reservation preference. For more information about Capacity Reservation preference, see [Capacity Reservation preference](use-ec2-capacity-reservations.md#asg-capacity-reservation-preference).

1. Choose **Update**.

------
#### [ AWS CLI ]

**To use Capacity Reservation preference on an existing group (AWS CLI)**
Add the `--capacity-reservation-specification` parameter to the [update-auto-scaling-group](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/update-auto-scaling-group.html) command.

1. Specify a Capacity Reservation preference. For more information, see [Capacity Reservation preference](use-ec2-capacity-reservations.md#asg-capacity-reservation-preference).

1. Specify a Capacity Reservation target. If you select Capacity Reservations only or Capacity Reservations first and you don't specify a Capacity Reservation target, Auto Scaling will use the launch template Capacity Reservation target or an open Capacity Reservation.

------
