---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-remove-load-balancer.html
---

# Detach a target group or Classic Load Balancer from your Auto Scaling group
<a name="as-remove-load-balancer"></a>

When you no longer need the load balancer, use the following procedure to detach it from your Auto Scaling group.

**To detach a load balancer from a group**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to an existing group.

   A split pane opens up in the bottom of the **Auto Scaling groups** page.

1. On the **Details** tab, choose **Load balancing**, **Edit**.

1. Under **Load balancing**, do one of the following:

   1. For **Application, Network or Gateway Load Balancer target groups**, choose the delete (X) icon next to the target group.

   1. For **Classic Load Balancers**, choose the delete (X) icon next to the load balancer.

1. Choose **Update**.

When you finish detaching the target group, you can turn off the Elastic Load Balancing health checks.

**To turn off the Elastic Load Balancing health checks**

1. On the **Details** tab, choose **Health checks**, **Edit**.

1. For **Health checks**, **Additional health check types**, deselect **Turn on Elastic Load Balancing health checks**.

1. Choose **Update**.
