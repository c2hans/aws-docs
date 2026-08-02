---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_DescribeLifecycleHookTypes_section.html
---

# Use `DescribeLifecycleHookTypes` with a CLI
<a name="example_auto-scaling_DescribeLifecycleHookTypes_section"></a>

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

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.
