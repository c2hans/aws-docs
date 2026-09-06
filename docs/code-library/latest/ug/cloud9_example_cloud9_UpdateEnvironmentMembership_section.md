---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloud9_example_cloud9_UpdateEnvironmentMembership_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `UpdateEnvironmentMembership` with a CLI
<a name="cloud9_example_cloud9_UpdateEnvironmentMembership_section"></a>

The following code examples show how to use `UpdateEnvironmentMembership`.

------
#### [ CLI ]

**AWS CLI**
**To change the settings of an existing environment member for an AWS Cloud9 development environment**
This example changes the settings of the specified existing environment member for the specified AWS Cloud9 development environment.
Command:

```
aws cloud9 update-environment-membership --environment-id {{8a34f51ce1e04a08882f1e811bd706EX}} --user-arn {{arn:aws:iam::123456789012:user/AnotherDemoUser}} --permissions {{read-only}}
```
Output:

```
{
  "membership": {
    "environmentId": "8a34f51ce1e04a08882f1e811bd706EX",
    "userId": "AIDAJ3LOROMOUXTBSU6EX",
    "userArn": "arn:aws:iam::123456789012:user/AnotherDemoUser",
    "permissions": "read-only"
  }
}
```
+  For API details, see [UpdateEnvironmentMembership](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/update-environment-membership.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example changes the settings of the specified existing environment member for the specified AWS Cloud9 development environment.**

```
Update-C9EnvironmentMembership -UserArn arn:aws:iam::123456789012:user/AnotherDemoUser -EnvironmentId ffd88420d4824eeeaeaa8a04bfde8cEX -Permission read-only
```
**Output:**

```
EnvironmentId : ffd88420d4824eeeaeaa8a04bfde8cEX
LastAccess    : 1/1/0001 12:00:00 AM
Permissions   : read-only
UserArn       : arn:aws:iam::123456789012:user/AnotherDemoUser
UserId        : AIDAJ3BA6O2FMJWCWXHEX
```
+  For API details, see [UpdateEnvironmentMembership](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example changes the settings of the specified existing environment member for the specified AWS Cloud9 development environment.**

```
Update-C9EnvironmentMembership -UserArn arn:aws:iam::123456789012:user/AnotherDemoUser -EnvironmentId ffd88420d4824eeeaeaa8a04bfde8cEX -Permission read-only
```
**Output:**

```
EnvironmentId : ffd88420d4824eeeaeaa8a04bfde8cEX
LastAccess    : 1/1/0001 12:00:00 AM
Permissions   : read-only
UserArn       : arn:aws:iam::123456789012:user/AnotherDemoUser
UserId        : AIDAJ3BA6O2FMJWCWXHEX
```
+  For API details, see [UpdateEnvironmentMembership](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
