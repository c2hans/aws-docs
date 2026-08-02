---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/auto-scaling_example_auto-scaling_DescribeLifecycleHookTypes_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeLifecycleHookTypes` with a CLI
<a name="auto-scaling_example_auto-scaling_DescribeLifecycleHookTypes_section"></a>

The following code examples show how to use `DescribeLifecycleHookTypes`.

------
#### [ CLI ]

**AWS CLI**
**To describe the available lifecycle hook types**
This example describes the available lifecycle hook types.

```
aws autoscaling describe-lifecycle-hook-types
```
Output:

```
{
    "LifecycleHookTypes": [
        "autoscaling:EC2_INSTANCE_LAUNCHING",
        "autoscaling:EC2_INSTANCE_TERMINATING"
    ]
}
```
+  For API details, see [DescribeLifecycleHookTypes](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/describe-lifecycle-hook-types.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example lists the lifecycle hook types supported by Auto Scaling.**

```
Get-ASLifecycleHookType
```
**Output:**

```
autoscaling:EC2_INSTANCE_LAUNCHING
auto-scaling:EC2_INSTANCE_TERMINATING
```
+  For API details, see [DescribeLifecycleHookTypes](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example lists the lifecycle hook types supported by Auto Scaling.**

```
Get-ASLifecycleHookType
```
**Output:**

```
autoscaling:EC2_INSTANCE_LAUNCHING
auto-scaling:EC2_INSTANCE_TERMINATING
```
+  For API details, see [DescribeLifecycleHookTypes](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
