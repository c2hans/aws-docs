---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/cancel-instance-refresh.html
---

# Cancel an instance refresh using the AWS Management Console or AWS CLI
<a name="cancel-instance-refresh"></a>

You can cancel an instance refresh that is still in progress. You can't cancel it after it's finished.

Canceling an instance refresh does not roll back any instances that were already replaced. To roll back the changes to your instances, perform a rollback instead. For more information, see [Undo changes with a manual or auto rollback](instance-refresh-rollback.md).

**Topics**
+ [Cancel an instance refresh (console)](#cancel-instance-refresh-console)
+ [Cancel an instance refresh (AWS CLI)](#cancel-instance-refresh-cli)

## Cancel an instance refresh (console)
<a name="cancel-instance-refresh-console"></a>

**To cancel an instance refresh**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to the Auto Scaling group.

1. On the **Instance refresh** tab, in **Active instance refresh**, choose **Actions**, **Cancel**.

1. When prompted for confirmation, choose **Confirm**.

The status of the instance refresh is set to **Cancelling**. After the cancellation is complete, the status of the instance refresh is set to **Cancelled**.

## Cancel an instance refresh (AWS CLI)
<a name="cancel-instance-refresh-cli"></a>

**To cancel an instance refresh**
Use the [cancel-instance-refresh](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/cancel-instance-refresh.html) command from the AWS CLI and provide the Auto Scaling group name.

```
aws autoscaling cancel-instance-refresh --auto-scaling-group-name {{my-asg}}
```

Example output:

```
{
    "InstanceRefreshId": "08b91cf7-8fa6-48af-b6a6-d227f40f1b9b"
}
```

**To cancel an instance refresh without waiting for transitioning instances**
Use the `--no-wait-for-transitioning-instances` option with the [cancel-instance-refresh](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/cancel-instance-refresh.html) command from the AWS CLI to cancel an instance refresh without waiting for transitioning instances.

```
aws autoscaling cancel-instance-refresh —auto-scaling-group-name {{my-asg}} --no-wait-for-transitioning-instances
```

By default, when you cancel an instance refresh, Amazon EC2 Auto Scaling waits for any in-flight launches and terminations to complete before setting the status to **Cancelled**. If you have instances with long draining periods or need to start a new instance refresh immediately, you can use the command so that you don’t have to wait for these transitioning operations.

When you use this option, the instance refresh status changes to **Cancelled**, allowing you to start a new instance refresh. Any in-flight launches and terminations continue in the background.
