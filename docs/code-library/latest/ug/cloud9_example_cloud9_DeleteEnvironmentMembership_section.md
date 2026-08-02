---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloud9_example_cloud9_DeleteEnvironmentMembership_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteEnvironmentMembership` with a CLI
<a name="cloud9_example_cloud9_DeleteEnvironmentMembership_section"></a>

The following code examples show how to use `DeleteEnvironmentMembership`.

------
#### [ CLI ]

**AWS CLI**
**To delete an environment member from an AWS Cloud9 development environment**
This example deletes the specified environment member from the specified AWS Cloud9 development environment.
Command:

```
aws cloud9 delete-environment-membership --environment-id {{8a34f51ce1e04a08882f1e811bd706EX}} --user-arn {{arn:aws:iam::123456789012:user/AnotherDemoUser}}
```
Output:

```
None.
```
+  For API details, see [DeleteEnvironmentMembership](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/delete-environment-membership.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example deletes the specified environment member from the specified AWS Cloud9 development environment.**

```
Remove-C9EnvironmentMembership -UserArn arn:aws:iam::123456789012:user/AnotherDemoUser -EnvironmentId ffd88420d4824eeeaeaa8a04bfde8cEX
```
+  For API details, see [DeleteEnvironmentMembership](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example deletes the specified environment member from the specified AWS Cloud9 development environment.**

```
Remove-C9EnvironmentMembership -UserArn arn:aws:iam::123456789012:user/AnotherDemoUser -EnvironmentId ffd88420d4824eeeaeaa8a04bfde8cEX
```
+  For API details, see [DeleteEnvironmentMembership](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
