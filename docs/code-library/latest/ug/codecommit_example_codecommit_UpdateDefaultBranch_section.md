---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codecommit_example_codecommit_UpdateDefaultBranch_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `UpdateDefaultBranch` with a CLI
<a name="codecommit_example_codecommit_UpdateDefaultBranch_section"></a>

The following code examples show how to use `UpdateDefaultBranch`.

------
#### [ CLI ]

**AWS CLI**
**To change the default branch for a repository**
The following `update-default-branch` example changes the default branch for an AWS CodeCommit repository.

```
aws codecommit update-default-branch \
    --repository-name {{MyDemoRepo}} \
    --default-branch-name {{MyNewBranch}}
```
This command produces no output.
For more information, see [Change branch settings in AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-change-branch.html) in the *AWS CodeCommit User Guide*.
+  For API details, see [UpdateDefaultBranch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-default-branch.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example changes the default branch for the specified repository to the specified branch.**

```
Update-CCDefaultBranch -RepositoryName MyDemoRepo -DefaultBranchName MyNewBranch
```
+  For API details, see [UpdateDefaultBranch](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example changes the default branch for the specified repository to the specified branch.**

```
Update-CCDefaultBranch -RepositoryName MyDemoRepo -DefaultBranchName MyNewBranch
```
+  For API details, see [UpdateDefaultBranch](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
