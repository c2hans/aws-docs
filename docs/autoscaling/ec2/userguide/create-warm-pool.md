---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/create-warm-pool.html
---

# Create a warm pool for an Auto Scaling group
<a name="create-warm-pool"></a>

This topic describes how to create a warm pool for your Auto Scaling group.

**Important**
Before you continue, complete the [prerequisites](ec2-auto-scaling-warm-pools.md#warm-pool-prerequisites) for creating a warm pool and confirm that you have created a lifecycle hook for your Auto Scaling group.

## Create a warm pool
<a name="create-a-warm-pool"></a>

Use the following procedure to create a warm pool for your Auto Scaling group.

**To create a warm pool (console)**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to an existing group.

   A split pane opens up at the bottom of the page.

1. Choose the **Instance management** tab.

1. Under **Warm pool**, choose **Create warm pool**.

1. To configure a warm pool, do the following:

   1. For **Warm pool instance state**, choose which state you want to transition your instances to when they enter the warm pool. The default is `Stopped`.

   1. For **Minimum warm pool size**, enter the minimum number of instances to maintain in the warm pool.

   1. For **Instance reuse**, select the **Reuse on scale in** check box to allow instances in the Auto Scaling group to return to the warm pool on scale in.

   1. For **Warm pool size**, choose one of the available options:
      + **Default specification**: The size of the warm pool is determined by the difference between the maximum and desired capacity of the Auto Scaling group. This option streamlines warm pool management. After you create the warm pool, its size can be easily updated just by adjusting the maximum capacity of the group.
      + **Custom specification**: The size of the warm pool is determined by the difference between a custom value and the desired capacity of the Auto Scaling group. This option gives you flexibility to manage the size of your warm pool independently from the maximum capacity of the group.

1. View the **Estimated warm pool size based on current settings** section to confirm how the default or custom specification applies to the size of the warm pool. Remember, the warm pool size depends on the desired capacity of the Auto Scaling group, which will change if the group scales.

1. Choose **Create**.

## Instance type selection with mixed instance groups
<a name="warm-pool-mixed-instance-types"></a>

Auto Scaling prioritizes instance types that are already in the warm pool during scaling events when your group is configured with a mixed instances policy. Launch behavior:

1. Auto Scaling attempts to launch instances using instance types available in the warm pool.

1. If warm launch fails, Auto Scaling attempts cold launch using all remaining instance types in your mixed instances policy.

**Example**
**Example**
If you configure your Auto Scaling group with 10 instance types and your warm pool contains 6 of those instance types. During scale-out, Auto Scaling first tries the 6 instance types from the warm pool. If unsuccessful, Auto Scaling tries all configured instance types through cold launch.

This gives you warm pool performance benefits when possible while maintaining the flexibility of your full mixed instances configuration.

## Delete a warm pool
<a name="delete-warm-pool"></a>

When you no longer need the warm pool, use the following procedure to delete it.

**To delete your warm pool (console)**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to an existing group.

   A split pane opens up at the bottom of the page.

1. Choose the **Instance management** tab.

1. For **Warm pool**, choose **Actions**, **Delete**.

1. When prompted for confirmation, choose **Delete**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
