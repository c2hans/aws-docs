---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/check-status-instance-refresh.html
---

# Monitor an instance refresh using the AWS Management Console or AWS CLI
<a name="check-status-instance-refresh"></a>

You can monitor an in progress instance refresh or look up the status of past instance refreshes from the last six weeks using the AWS Management Console or AWS CLI.

## Monitor and check the status of an instance refresh
<a name="monitor-and-check-status"></a>

To monitor and check the status of an instance refresh, use one of the following methods:

------
#### [ Console ]

**Tip**
In this procedure, the named columns should already be displayed. To display hidden columns or change the number of rows shown, choose the gear icon on the top right corner of the section to open the preferences modal. Update the settings as needed and choose **Confirm**.

**To monitor and check the status of an instance refresh (console)**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/), and choose **Auto Scaling Groups** from the navigation pane.

1. Select the check box next to the Auto Scaling group.

   A split pane opens up at the bottom of the page.

1. On the **Instance refresh** tab, under **Instance refresh history**, you can determine the status of your request by looking at the **Status** column. The operation goes into `Pending` status while it's initializing. The status should then quickly change to `InProgress`. When all instances are updated, the status changes to `Successful`.

1. You can further monitor the success or failure of in progress activities by viewing the group's scaling activities. On the **Activity** tab, under **Activity history**, when the instance refresh starts, you see entries when instances are terminated and another set of entries when instances are launched. If you have numerous scaling activities, you can see more of them by choosing the **>** icon at the top of the activity history. For information about troubleshooting issues that might cause activities to fail, see [Troubleshoot issues in Amazon EC2 Auto Scaling](CHAP_Troubleshooting.md).

1. (Optional) On the **Instance management** tab, under **Instances**, you can review the progress of specific instances as needed.

------
#### [ AWS CLI ]

**To monitor and check the status of an instance refresh (AWS CLI)**
Use the following [describe-instance-refreshes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-instance-refreshes.html) command.

```
aws autoscaling describe-instance-refreshes --auto-scaling-group-name {{my-asg}}
```

The following is example output.

Instance refreshes are ordered by start time. Instance refreshes still in progress are described first.

```
{
  "InstanceRefreshes":[
    {
      "InstanceRefreshId":"08b91cf7-8fa6-48af-b6a6-d227f40f1b9b",
      "AutoScalingGroupName":"my-asg",
      "Status":"InProgress",
      "StatusReason":"Waiting for instances to warm up before continuing. For example: i-0645704820a8e83ff is warming up.",
      "StartTime":"2023-11-24T16:46:52+00:00",
      "PercentageComplete":50,
      "InstancesToUpdate":0,
      "Preferences":{
        "MaxHealthyPercentage":120,
        "MinHealthyPercentage":90,
        "InstanceWarmup":60,
        "SkipMatching":false,
        "AutoRollback":true,
        "ScaleInProtectedInstances":"Ignore",
        "StandbyInstances":"Ignore"
      }
    },
    {
      "InstanceRefreshId":"0e151305-1e57-4a32-a256-1fd14157c5ec",
      "AutoScalingGroupName":"my-asg",
      "Status":"Successful",
      "StartTime":"2023-11-22T13:53:37+00:00",
      "EndTime":"2023-11-22T13:59:45+00:00",
      "PercentageComplete":100,
      "InstancesToUpdate":0,
      "Preferences":{
        "MaxHealthyPercentage":120,
        "MinHealthyPercentage":90,
        "InstanceWarmup":60,
        "SkipMatching":false,
        "AutoRollback":true,
        "ScaleInProtectedInstances":"Ignore",
        "StandbyInstances":"Ignore"
      }
    }
  ]
}
```

You can further monitor the success or failure of in progress activities by viewing the group's scaling activities. The scaling activities also help you drill in for more details to help you troubleshoot issues with an instance refresh. For more information, see [Troubleshoot issues in Amazon EC2 Auto Scaling](CHAP_Troubleshooting.md).

------

## Instance refresh statuses
<a name="instance-refresh-statuses"></a>

When you start an instance refresh, it enters the **Pending** status. It passes from **Pending** to **InProgress** until it reaches **Successful**, **Failed**, **Cancelled**, **RollbackSuccessful**, or **RollbackFailed**.

An instance refresh can have the following statuses:

| Status | Description |
| --- | --- |
| Pending | The request was created, but the instance refresh has not started. |
| InProgress | An instance refresh is in progress. |
| Successful | An instance refresh completed successfully. |
| Failed | An instance refresh failed to complete. You can troubleshoot using the status reason and the scaling activities. |
| Cancelling | An ongoing instance refresh is being cancelled. |
| Cancelled | The instance refresh is cancelled. |
| RollbackInProgress | An instance refresh is being rolled back. |
| RollbackFailed | The rollback failed to complete. You can troubleshoot using the status reason and the scaling activities. |
| RollbackSuccessful | The rollback completed successfully. |
| Baking | Waiting the specified bake time after an instance refresh has finished updating instances. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
