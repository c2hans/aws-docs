---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codecommit_example_codecommit_GetBranch_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetBranch` with a CLI
<a name="codecommit_example_codecommit_GetBranch_section"></a>

The following code examples show how to use `GetBranch`.

------
#### [ CLI ]

**AWS CLI**
**To get information about a branch**
This example gets information about a branch in an AWS CodeCommit repository.
Command:

```
aws codecommit get-branch --repository-name {{MyDemoRepo}} --branch-name {{MyNewBranch}}
```
Output:

```
{
  "BranchInfo": {
        "commitID": "317f8570EXAMPLE",
                "branchName": "MyNewBranch"
  }
}
```
+  For API details, see [GetBranch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/get-branch.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example gets information about the specified branch for the specified repository.**

```
Get-CCBranch -RepositoryName MyDemoRepo -BranchName MyNewBranch
```
**Output:**

```
BranchName                              CommitId
----------                              --------
MyNewBranch                             7763222d...561fc9c9
```
+  For API details, see [GetBranch](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example gets information about the specified branch for the specified repository.**

```
Get-CCBranch -RepositoryName MyDemoRepo -BranchName MyNewBranch
```
**Output:**

```
BranchName                              CommitId
----------                              --------
MyNewBranch                             7763222d...561fc9c9
```
+  For API details, see [GetBranch](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
