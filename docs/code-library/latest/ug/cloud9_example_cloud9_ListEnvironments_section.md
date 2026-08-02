---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloud9_example_cloud9_ListEnvironments_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListEnvironments` with a CLI
<a name="cloud9_example_cloud9_ListEnvironments_section"></a>

The following code examples show how to use `ListEnvironments`.

------
#### [ CLI ]

**AWS CLI**
**To get a list of available AWS Cloud9 development environment identifiers**
This example gets a list of available AWS Cloud9 development environment identifiers.
Command:

```
aws cloud9 list-environments
```
Output:

```
{
  "environmentIds": [
    "685f892f431b45c2b28cb69eadcdb0EX",
    "1980b80e5f584920801c09086667f0EX"
  ]
}
```
+  For API details, see [ListEnvironments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloud9/list-environments.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example gets a list of available AWS Cloud9 development environment identifiers.**

```
Get-C9EnvironmentList
```
**Output:**

```
685f892f431b45c2b28cb69eadcdb0EX
1980b80e5f584920801c09086667f0EX
```
+  For API details, see [ListEnvironments](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example gets a list of available AWS Cloud9 development environment identifiers.**

```
Get-C9EnvironmentList
```
**Output:**

```
685f892f431b45c2b28cb69eadcdb0EX
1980b80e5f584920801c09086667f0EX
```
+  For API details, see [ListEnvironments](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
