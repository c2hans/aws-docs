---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/attach-load-balancer-asg.html
---

# Attach an Elastic Load Balancing load balancer to your Auto Scaling group
<a name="attach-load-balancer-asg"></a>

This topic describes how to attach an Elastic Load Balancing load balancer to an Auto Scaling group. It also describes how to turn on Elastic Load Balancing health checks to let Amazon EC2 Auto Scaling replace instances that Elastic Load Balancing reports as unhealthy.

By default, Amazon EC2 Auto Scaling only replaces instances that are unhealthy or unreachable based on Amazon EC2 health checks. If you turn on Elastic Load Balancing health checks, Amazon EC2 Auto Scaling can replace a running instance if any of the Elastic Load Balancing load balancers you attach to the Auto Scaling group report it as unhealthy.

For a tutorial on attaching an Application Load Balancer to your Auto Scaling group, see [Tutorial: Set up a scaled and load-balanced application](tutorial-ec2-auto-scaling-load-balancer.md).

**Important**
Before you continue, complete all [prerequisites](getting-started-elastic-load-balancing.md) in the previous section.

**Contents**
+ [Attach a target group or Classic Load Balancer](#as-add-load-balancer-console)
+ [Detach a target group or Classic Load Balancer](#as-remove-load-balancer)

## Attach a target group or Classic Load Balancer
<a name="as-add-load-balancer-console"></a>

When you create or update an Auto Scaling group, you can attach one or more target groups or Classic Load Balancers. When you attach an Application Load Balancer, Network Load Balancer, or Gateway Load Balancer, you attach a target group rather than the load balancer itself.

Follow the steps in this section to use the console to:
+ Attach a target group or Classic Load Balancer to an Auto Scaling group
+ Turn on the health checks for Elastic Load Balancing

**To attach an existing load balancer as you are creating a new Auto Scaling group**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. On the navigation bar at the top of the screen, choose the AWS Region that you created your load balancer in.

1. Choose **Create Auto Scaling group**.

1.  In steps 1 and 2, choose the options as desired and proceed to **Step 3: Configure advanced options**.

1. For **Load balancing**, choose **Attach to an existing load balancer**.

1. Under **Attach to an existing load balancer**, do one of the following:

   1. For Application Load Balancers, Network Load Balancers, and Gateway Load Balancers:

      Choose **Choose from your load balancer target groups**, and then choose a target group in the **Existing load balancer target groups** field.

   1. For Classic Load Balancers:

      Choose **Choose from Classic Load Balancers**, and then choose your load balancer in the **Classic Load Balancers** field.

1. (Optional) For **Health checks**, **Additional health check types**, select **Turn on Elastic Load Balancing health checks**.

1. (Optional) For **Health check grace period**, enter the amount of time, in seconds. This is how long Amazon EC2 Auto Scaling needs to wait before checking the health status of an instance after it enters the `InService` state. For more information, see [Set the health check grace period for an Auto Scaling group](health-check-grace-period.md).

1. Proceed to create the Auto Scaling group. Your instances will be automatically registered to the load balancer after the Auto Scaling group has been created.

**To attach an existing load balancer to your Auto Scaling group after it's created**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to your Auto Scaling group.

   A split pane opens up in the bottom of the **Auto Scaling groups** page.

1. On the **Integrations** tab, choose **Load balancing**, **Edit**.

1. Under **Load balancing**, do one of the following:

   1. For **Application, Network or Gateway Load Balancer target groups**, select its check box and choose a target group.

   1. For **Classic Load Balancers**, select its check box and choose your load balancer.

1. Choose **Update**.

When you finish attaching the load balancer, you can optionally turn on the health checks that use it.

**To turn on the Elastic Load Balancing health checks**

1. On the **Details** tab, choose **Health checks**, **Edit**.

1. For **Health checks**, **Additional health check types**, select **Turn on Elastic Load Balancing health checks**.

1. For **Health check grace period**, enter the amount of time, in seconds. This is how long Amazon EC2 Auto Scaling needs to wait before checking the health status of an instance after it enters the `InService` state. For more information, see [Set the health check grace period for an Auto Scaling group](health-check-grace-period.md).

1. Choose **Update**.

**Note**
You can monitor the status of the load balancer while it is being attached by using the AWS CLI. When Amazon EC2 Auto Scaling has successfully registered the instances and at least one registered instance passes the health checks, you receive a status of `InService`. For more information, see [Verify the attachment status of your load balancer](load-balancer-status.md).

## Detach a target group or Classic Load Balancer
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
