---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DescribeTerminationPolicyTypes_section.html
---

# Use `DescribeTerminationPolicyTypes` with a CLI
<a name="example_auto-scaling_DescribeTerminationPolicyTypes_section"></a>

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

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
