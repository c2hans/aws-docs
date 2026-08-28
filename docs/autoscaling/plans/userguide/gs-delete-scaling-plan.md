---
source_url: https://docs.aws.amazon.com/autoscaling/plans/userguide/gs-delete-scaling-plan.html
---

# Step 5: Clean up
<a name="gs-delete-scaling-plan"></a>

After you have completed the getting started tutorial, you can choose to keep your scaling plan. However, if you are not actively using your scaling plan, you should consider deleting it so that your account does not incur unnecessary charges.

Deleting a scaling plan deletes the target tracking scaling policies, their associated CloudWatch alarms, and the predictive scaling actions that AWS Auto Scaling created on your behalf.

Deleting a scaling plan does not delete your CloudFormation stack, Auto Scaling group, or other scalable resources.

**To delete a scaling plan**

1. Open the AWS Auto Scaling console at [https://console.aws.amazon.com/awsautoscaling/](https://console.aws.amazon.com/awsautoscaling/).

1. On the **Scaling plans** page, select the scaling plan that you created for this tutorial and choose **Delete**.

1. When prompted for confirmation, choose **Delete**.

After you delete your scaling plan, your resources do not revert to their original capacity. For example, if your Auto Scaling group is scaled to 10 instances when you delete the scaling plan, your group is still scaled to 10 instances after the scaling plan is deleted. You can update the capacity of specific resources by accessing the console for each individual service.

## Delete your Auto Scaling group
<a name="gs-delete-asg"></a>

To prevent your account from accruing Amazon EC2 charges, you should also delete the Auto Scaling group that you created for this tutorial.

For step-by-step instructions, see [Delete your Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-process-shutdown.html#as-shutdown-lbs-delete-asg-cli) in the *Amazon EC2 Auto Scaling User Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
