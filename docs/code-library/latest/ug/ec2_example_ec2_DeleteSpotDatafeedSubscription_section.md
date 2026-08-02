---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ec2_example_ec2_DeleteSpotDatafeedSubscription_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteSpotDatafeedSubscription` with a CLI
<a name="ec2_example_ec2_DeleteSpotDatafeedSubscription_section"></a>

The following code examples show how to use `DeleteSpotDatafeedSubscription`.

------
#### [ CLI ]

**AWS CLI**
**To cancel a Spot Instance data feed subscription**
This example command deletes a Spot data feed subscription for the account. If the command succeeds, no output is returned.
Command:

```
aws ec2 delete-spot-datafeed-subscription
```
+  For API details, see [DeleteSpotDatafeedSubscription](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/delete-spot-datafeed-subscription.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example deletes your Spot instance data feed. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2SpotDatafeedSubscription
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2SpotDatafeedSubscription (DeleteSpotDatafeedSubscription)" on Target "".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteSpotDatafeedSubscription](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example deletes your Spot instance data feed. You are prompted for confirmation before the operation proceeds, unless you also specify the Force parameter.**

```
Remove-EC2SpotDatafeedSubscription
```
**Output:**

```
Confirm
Are you sure you want to perform this action?
Performing operation "Remove-EC2SpotDatafeedSubscription (DeleteSpotDatafeedSubscription)" on Target "".
[Y] Yes  [A] Yes to All  [N] No  [L] No to All  [S] Suspend  [?] Help (default is "Y"):
```
+  For API details, see [DeleteSpotDatafeedSubscription](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
