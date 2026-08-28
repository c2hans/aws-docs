---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/ssm_example_ssm_DescribeInstancePatchStates_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeInstancePatchStates` with a CLI
<a name="ssm_example_ssm_DescribeInstancePatchStates_section"></a>

The following code examples show how to use `DescribeInstancePatchStates`.

------
#### [ CLI ]

**AWS CLI**
**To get the patch summary states for instances**
This `describe-instance-patch-states` example gets the patch summary states for an instance.

```
aws ssm describe-instance-patch-states \
    --instance-ids {{"i-1234567890abcdef0"}}
```
Output:

```
{
    "InstancePatchStates": [
        {
            "InstanceId": "i-1234567890abcdef0",
            "PatchGroup": "my-patch-group",
            "BaselineId": "pb-0713accee01234567",
            "SnapshotId": "521c3536-930c-4aa9-950e-01234567abcd",
            "CriticalNonCompliantCount": 2,
            "SecurityNonCompliantCount": 2,
            "OtherNonCompliantCount": 1,
            "InstalledCount": 123,
            "InstalledOtherCount": 334,
            "InstalledPendingRebootCount": 0,
            "InstalledRejectedCount": 0,
            "MissingCount": 1,
            "FailedCount": 2,
            "UnreportedNotApplicableCount": 11,
            "NotApplicableCount": 2063,
            "OperationStartTime": "2021-05-03T11:00:56-07:00",
            "OperationEndTime": "2021-05-03T11:01:09-07:00",
            "Operation": "Scan",
            "LastNoRebootInstallOperationTime": "2020-06-14T12:17:41-07:00",
            "RebootOption": "RebootIfNeeded"
        }
    ]
}
```
For more information, see [About Patch Compliance](https://docs.aws.amazon.com/systems-manager/latest/userguide/about-patch-compliance.html) in the *AWS Systems Manager User Guide*.
+  For API details, see [DescribeInstancePatchStates](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ssm/describe-instance-patch-states.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example gets the patch summary states for an instance.**

```
Get-SSMInstancePatchState -InstanceId "i-08ee91c0b17045407"
```
**Example 2: This example gets the patch summary states for two instances.**

```
Get-SSMInstancePatchState -InstanceId "i-08ee91c0b17045407","i-09a618aec652973a9"
```
+  For API details, see [DescribeInstancePatchStates](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example gets the patch summary states for an instance.**

```
Get-SSMInstancePatchState -InstanceId "i-08ee91c0b17045407"
```
**Example 2: This example gets the patch summary states for two instances.**

```
Get-SSMInstancePatchState -InstanceId "i-08ee91c0b17045407","i-09a618aec652973a9"
```
+  For API details, see [DescribeInstancePatchStates](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
