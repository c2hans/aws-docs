---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-spot-instances-cancel.html
---

# Cancel a Spot Instance request
<a name="using-spot-instances-cancel"></a>

If you no longer want your Spot Instance request, you can cancel it. You can only cancel Spot Instance requests that are `open`, `active`, or `disabled`.
+ Your Spot Instance request is `open` when your request has not yet been fulfilled and no instances have been launched.
+ Your Spot Instance request is `active` when your request has been fulfilled and Spot Instances have launched as a result.
+ Your Spot Instance request is `disabled` when you stop your Spot Instance.

If your Spot Instance request is `active` and has an associated running Spot Instance, canceling the request does not terminate the instance. For more information about terminating a Spot Instance, see [Terminate a Spot Instance](using-spot-instances-request.md#terminating-a-spot-instance).

------
#### [ Console ]

**To cancel a Spot Instance request**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, choose **Spot Requests**.

1. Select the Spot Instance request.

1. Choose **Actions**, **Cancel request**.

1. (Optional) If you are finished with the associated Spot Instances, you can terminate them. In the **Cancel Spot request** dialog box, select **Terminate instances**, and then choose **Confirm**.

------
#### [ AWS CLI ]

**To cancel a Spot Instance request**
Use the following [cancel-spot-instance-requests](https://docs.aws.amazon.com/cli/latest/reference/ec2/cancel-spot-instance-requests.html) command.

```
aws ec2 cancel-spot-instance-requests --spot-instance-request-ids {{sir-0e54a519c9EXAMPLE}}
```

------
#### [ PowerShell ]

**To cancel a Spot Instance request**
Use the [Stop-EC2SpotInstanceRequest](https://docs.aws.amazon.com/powershell/latest/reference/items/Stop-EC2SpotInstanceRequest.html) cmdlet.

```
Stop-EC2SpotInstanceRequest -SpotInstanceRequestId {{sir-0e54a519c9EXAMPLE}}
```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
