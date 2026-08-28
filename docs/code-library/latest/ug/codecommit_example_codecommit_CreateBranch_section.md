---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codecommit_example_codecommit_CreateBranch_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateBranch` with a CLI
<a name="codecommit_example_codecommit_CreateBranch_section"></a>

The following code examples show how to use `CreateBranch`.

------
#### [ CLI ]

**AWS CLI**
**To create a branch**
This example creates a branch in an AWS CodeCommit repository. This command produces output only if there are errors.
Command:

```
aws codecommit create-branch --repository-name {{MyDemoRepo}} --branch-name {{MyNewBranch}} --commit-id {{317f8570EXAMPLE}}
```
Output:

```
None.
```
+  For API details, see [CreateBranch](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/create-branch.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example creates a new branch with the specified name for the specified repository and the specified commit ID.**

```
New-CCBranch -RepositoryName MyDemoRepo -BranchName MyNewBranch -CommitId 7763222d...561fc9c9
```
+  For API details, see [CreateBranch](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example creates a new branch with the specified name for the specified repository and the specified commit ID.**

```
New-CCBranch -RepositoryName MyDemoRepo -BranchName MyNewBranch -CommitId 7763222d...561fc9c9
```
+  For API details, see [CreateBranch](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
