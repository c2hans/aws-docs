---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-remove-az-console.html
---

# Remove an Availability Zone
<a name="as-remove-az-console"></a>

To remove an Availability Zone from your Auto Scaling group and load balancer, use the following procedure.

**To remove an Availability Zone**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to an existing group.

   A split pane opens up in the bottom of the **Auto Scaling groups** page.

1. On the **Details** tab, choose **Network**, **Edit**.

1. In **Subnets**, choose the delete (X) icon for the subnet corresponding to the Availability Zone that you want to remove from the Auto Scaling group. If there is more than one subnet for that zone, choose the delete (X) icon for each one.

1. Choose **Update**.

1. To update the Availability Zones for your load balancer so that it shares the same Availability Zones as your Auto Scaling group, complete the following steps:

   1. On the navigation pane, under **Load Balancing**, choose **Load Balancers**.

   1. Choose your load balancer.

   1. Do one of the following:
      + For Application Load Balancers:

        1. On the **Description** tab, for **Availability Zones**, choose **Edit subnets**.

        1. On the **Edit subnets** page, for **Availability Zones**, clear the check box to remove the subnet for that Availability Zone.
      + For Classic Load Balancers in a VPC:

        1. On the **Instances** tab, choose **Edit Availability Zones**.

        1. On the **Add and Remove Subnets** page, for **Available subnets**, remove the subnet using its delete (-) icon. The subnet is moved under **Available subnets**.

   1. Choose **Save**.
