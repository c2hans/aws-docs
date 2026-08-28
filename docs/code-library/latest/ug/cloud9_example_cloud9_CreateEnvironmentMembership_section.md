---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloud9_example_cloud9_CreateEnvironmentMembership_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateEnvironmentMembership` with a CLI
<a name="cloud9_example_cloud9_CreateEnvironmentMembership_section"></a>

The following code examples show how to use `CreateEnvironmentMembership`.

------
#### [ CLI ]

**AWS CLI**
**To add an environment member to an AWS Cloud9 development environment**
This example adds the specified environment member to the specified AWS Cloud9 development environment.
Command:

```
aws cloud9 create-environment-membership --environment-id {{8a34f51ce1e04a08882f1e811bd706EX}} --user-arn {{arn:aws:iam::123456789012:user/AnotherDemoUser}} --permissions {{read-write}}
```
Output:

```
{
  "membership": {
    "environmentId": "8a34f51ce1e04a08882f1e811bd706EX",
    "userId": "AIDAJ3LOROMOUXTBSU6EX",
    "userArn": "arn:aws:iam::123456789012:user/AnotherDemoUser",
    "permissions": "read-write"
  }
}
```
+  For API details, see [CreateEnvironmentMembership](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/create-environment-membership.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example adds the specified environment member to the specified AWS Cloud9 development environment.**

```
New-C9EnvironmentMembership -UserArn arn:aws:iam::123456789012:user/AnotherDemoUser -EnvironmentId ffd88420d4824eeeaeaa8a04bfde8cEX -Permission read-write
```
**Output:**

```
EnvironmentId : ffd88420d4824eeeaeaa8a04bfde8cEX
LastAccess    : 1/1/0001 12:00:00 AM
Permissions   : read-write
UserArn       : arn:aws:iam::123456789012:user/AnotherDemoUser
UserId        : AIDAJ3BA6O2FMJWCWXHEX
```
+  For API details, see [CreateEnvironmentMembership](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example adds the specified environment member to the specified AWS Cloud9 development environment.**

```
New-C9EnvironmentMembership -UserArn arn:aws:iam::123456789012:user/AnotherDemoUser -EnvironmentId ffd88420d4824eeeaeaa8a04bfde8cEX -Permission read-write
```
**Output:**

```
EnvironmentId : ffd88420d4824eeeaeaa8a04bfde8cEX
LastAccess    : 1/1/0001 12:00:00 AM
Permissions   : read-write
UserArn       : arn:aws:iam::123456789012:user/AnotherDemoUser
UserId        : AIDAJ3BA6O2FMJWCWXHEX
```
+  For API details, see [CreateEnvironmentMembership](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
