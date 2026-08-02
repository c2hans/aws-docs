---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/auto-scaling_example_auto-scaling_DescribeTerminationPolicyTypes_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeTerminationPolicyTypes` with a CLI
<a name="auto-scaling_example_auto-scaling_DescribeTerminationPolicyTypes_section"></a>

The following code examples show how to use `DescribeTerminationPolicyTypes`.

------
#### [ CLI ]

**AWS CLI**
**To describe available termination policy types**
This example describes the available termination policy types.

```
aws autoscaling describe-termination-policy-types
```
Output:

```
{
    "TerminationPolicyTypes": [
        "AllocationStrategy",
        "ClosestToNextInstanceHour",
        "Default",
        "NewestInstance",
        "OldestInstance",
        "OldestLaunchConfiguration",
        "OldestLaunchTemplate"
    ]
}
```
For more information, see [Controlling which Auto Scaling instances terminate during scale in](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-termination.html) in the *Amazon EC2 Auto Scaling User Guide*.
+  For API details, see [DescribeTerminationPolicyTypes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-termination-policy-types.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example lists the termination policies that are supported by Auto Scaling.**

```
Get-ASTerminationPolicyType
```
**Output:**

```
ClosestToNextInstanceHour
Default
NewestInstance
OldestInstance
OldestLaunchConfiguration
```
+  For API details, see [DescribeTerminationPolicyTypes](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example lists the termination policies that are supported by Auto Scaling.**

```
Get-ASTerminationPolicyType
```
**Output:**

```
ClosestToNextInstanceHour
Default
NewestInstance
OldestInstance
OldestLaunchConfiguration
```
+  For API details, see [DescribeTerminationPolicyTypes](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
