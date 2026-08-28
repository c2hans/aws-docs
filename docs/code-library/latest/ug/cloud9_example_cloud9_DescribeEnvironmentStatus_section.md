---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloud9_example_cloud9_DescribeEnvironmentStatus_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeEnvironmentStatus` with a CLI
<a name="cloud9_example_cloud9_DescribeEnvironmentStatus_section"></a>

The following code examples show how to use `DescribeEnvironmentStatus`.

------
#### [ CLI ]

**AWS CLI**
**To get status information for an AWS Cloud9 development environment**
This example gets status information for the specified AWS Cloud9 development environment.
Command:

```
aws cloud9 describe-environment-status --environment-id {{685f892f431b45c2b28cb69eadcdb0EX}}
```
Output:

```
{
  "status": "ready",
  "message": "Environment is ready to use"
}
```
+  For API details, see [DescribeEnvironmentStatus](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/describe-environment-status.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example gets status information for the specified AWS Cloud9 development environment.**

```
Get-C9EnvironmentStatus -EnvironmentId 349c86d4579e4e7298d500ff57a6b2EX
```
**Output:**

```
Message                     Status
-------                     ------
Environment is ready to use ready
```
+  For API details, see [DescribeEnvironmentStatus](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example gets status information for the specified AWS Cloud9 development environment.**

```
Get-C9EnvironmentStatus -EnvironmentId 349c86d4579e4e7298d500ff57a6b2EX
```
**Output:**

```
Message                     Status
-------                     ------
Environment is ready to use ready
```
+  For API details, see [DescribeEnvironmentStatus](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
