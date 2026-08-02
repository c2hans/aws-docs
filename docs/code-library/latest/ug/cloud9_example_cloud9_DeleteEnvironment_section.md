---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloud9_example_cloud9_DeleteEnvironment_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteEnvironment` with a CLI
<a name="cloud9_example_cloud9_DeleteEnvironment_section"></a>

The following code examples show how to use `DeleteEnvironment`.

------
#### [ CLI ]

**AWS CLI**
**To delete an AWS Cloud9 development environment**
This example deletes the specified AWS Cloud9 development environment. If an Amazon EC2 instance is connected to the environment, also terminates the instance.
Command:

```
aws cloud9 delete-environment --environment-id {{8a34f51ce1e04a08882f1e811bd706EX}}
```
Output:

```
None.
```
+  For API details, see [DeleteEnvironment](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/delete-environment.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example deletes the specified AWS Cloud9 development environment. If an Amazon EC2 instance is connected to the environment, also terminates the instance.**

```
Remove-C9Environment -EnvironmentId ffd88420d4824eeeaeaa8a04bfde8cEX
```
+  For API details, see [DeleteEnvironment](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example deletes the specified AWS Cloud9 development environment. If an Amazon EC2 instance is connected to the environment, also terminates the instance.**

```
Remove-C9Environment -EnvironmentId ffd88420d4824eeeaeaa8a04bfde8cEX
```
+  For API details, see [DeleteEnvironment](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
