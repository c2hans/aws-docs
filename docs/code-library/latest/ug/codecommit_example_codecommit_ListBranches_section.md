---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codecommit_example_codecommit_ListBranches_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListBranches` with a CLI
<a name="codecommit_example_codecommit_ListBranches_section"></a>

The following code examples show how to use `ListBranches`.

------
#### [ CLI ]

**AWS CLI**
**To view a list of branch names**
This example lists all branch names in an AWS CodeCommit repository.

```
aws codecommit list-branches \
    --repository-name {{MyDemoRepo}}
```
Output:

```
{
    "branches": [
        "MyNewBranch",
        "main"
    ]
}
```
+  For API details, see [ListBranches](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-branches.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example gets a list of branch names for the specified repository.**

```
Get-CCBranchList -RepositoryName MyDemoRepo
```
**Output:**

```
master
MyNewBranch
```
+  For API details, see [ListBranches](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example gets a list of branch names for the specified repository.**

```
Get-CCBranchList -RepositoryName MyDemoRepo
```
**Output:**

```
master
MyNewBranch
```
+  For API details, see [ListBranches](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
