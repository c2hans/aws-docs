---
source_url: https://docs.aws.amazon.com/powershell/v5/userguide/powershell_codecommit_code_examples.html
---

Version 5 (V5) of the AWS Tools for PowerShell has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html).

 [![Orange button with text "Click here for details".](http://docs.aws.amazon.com/powershell/v5/userguide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/powershell/v5/userguide/migrating-v5.html)

# CodeCommit examples using Tools for PowerShell V5
<a name="powershell_codecommit_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Tools for PowerShell V5 with CodeCommit.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `Get-CCBranch`
<a name="codecommit_GetBranch_powershell_topic"></a>

The following code example shows how to use `Get-CCBranch`.

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

### `Get-CCBranchList`
<a name="codecommit_ListBranches_powershell_topic"></a>

The following code example shows how to use `Get-CCBranchList`.

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

### `Get-CCRepository`
<a name="codecommit_GetRepository_powershell_topic"></a>

The following code example shows how to use `Get-CCRepository`.

**Tools for PowerShell V5**
**Example 1: This example gets information for the specified repository.**

```
Get-CCRepository -RepositoryName MyDemoRepo
```
**Output:**

```
AccountId             : 80398EXAMPLE
Arn                   : arn:aws:codecommit:us-east-1:80398EXAMPLE:MyDemoRepo
CloneUrlHttp          : https://git-codecommit.us-east-1.amazonaws.com/v1/repos/MyDemoRepo
CloneUrlSsh           : ssh://git-codecommit.us-east-1.amazonaws.com/v1/repos/MyDemoRepo
CreationDate          : 9/8/2015 3:21:33 PM
DefaultBranch         :
LastModifiedDate      : 9/8/2015 3:21:33 PM
RepositoryDescription : This is a repository for demonstration purposes.
RepositoryId          : c7d0d2b0-ce40-4303-b4c3-38529EXAMPLE
RepositoryName        : MyDemoRepo
```
+  For API details, see [GetRepository](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CCRepositoryBatch`
<a name="codecommit_BatchGetRepositories_powershell_topic"></a>

The following code example shows how to use `Get-CCRepositoryBatch`.

**Tools for PowerShell V5**
**Example 1: This example confirms which of the specified repositories are found and not found.**

```
Get-CCRepositoryBatch -RepositoryName MyDemoRepo, MyNewRepo, AMissingRepo
```
**Output:**

```
Repositories                            RepositoriesNotFound
------------                            --------------------
{MyDemoRepo, MyNewRepo}                {AMissingRepo}
```
+  For API details, see [BatchGetRepositories](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Get-CCRepositoryList`
<a name="codecommit_ListRepositories_powershell_topic"></a>

The following code example shows how to use `Get-CCRepositoryList`.

**Tools for PowerShell V5**
**Example 1: This example lists all repositories in ascending order by repository name.**

```
Get-CCRepositoryList -Order Ascending -SortBy RepositoryName
```
**Output:**

```
RepositoryId                            RepositoryName
------------                            --------------
c7d0d2b0-ce40-4303-b4c3-38529EXAMPLE    MyDemoRepo
05f30c66-e3e3-4f91-a0cd-1c84aEXAMPLE    MyNewRepo
```
+  For API details, see [ListRepositories](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-CCBranch`
<a name="codecommit_CreateBranch_powershell_topic"></a>

The following code example shows how to use `New-CCBranch`.

**Tools for PowerShell V5**
**Example 1: This example creates a new branch with the specified name for the specified repository and the specified commit ID.**

```
New-CCBranch -RepositoryName MyDemoRepo -BranchName MyNewBranch -CommitId 7763222d...561fc9c9
```
+  For API details, see [CreateBranch](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `New-CCRepository`
<a name="codecommit_CreateRepository_powershell_topic"></a>

The following code example shows how to use `New-CCRepository`.

**Tools for PowerShell V5**
**Example 1: This example creates a new repository with the specified name and the specified description.**

```
New-CCRepository -RepositoryName MyDemoRepo -RepositoryDescription "This is a repository for demonstration purposes."
```
**Output:**

```
AccountId             : 80398EXAMPLE
Arn                   : arn:aws:codecommit:us-east-1:80398EXAMPLE:MyDemoRepo
CloneUrlHttp          : https://git-codecommit.us-east-1.amazonaws.com/v1/repos/MyDemoRepo
CloneUrlSsh           : ssh://git-codecommit.us-east-1.amazonaws.com/v1/repos/MyDemoRepo
CreationDate          : 9/18/2015 4:13:25 PM
DefaultBranch         :
LastModifiedDate      : 9/18/2015 4:13:25 PM
RepositoryDescription : This is a repository for demonstration purposes.
RepositoryId          : 43ef2443-3372-4b12-9e78-65c27EXAMPLE
RepositoryName        : MyDemoRepo
```
+  For API details, see [CreateRepository](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Remove-CCRepository`
<a name="codecommit_DeleteRepository_powershell_topic"></a>

The following code example shows how to use `Remove-CCRepository`.

**Tools for PowerShell V5**
**Example 1: This example forcibly deletes the specified repository. The command will prompt for confirmation before proceeding. Add the -Force parameter to delete the repository without a prompt.**

```
Remove-CCRepository -RepositoryName MyDemoRepo
```
**Output:**

```
43ef2443-3372-4b12-9e78-65c27EXAMPLE
```
+  For API details, see [DeleteRepository](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Update-CCDefaultBranch`
<a name="codecommit_UpdateDefaultBranch_powershell_topic"></a>

The following code example shows how to use `Update-CCDefaultBranch`.

**Tools for PowerShell V5**
**Example 1: This example changes the default branch for the specified repository to the specified branch.**

```
Update-CCDefaultBranch -RepositoryName MyDemoRepo -DefaultBranchName MyNewBranch
```
+  For API details, see [UpdateDefaultBranch](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Update-CCRepositoryDescription`
<a name="codecommit_UpdateRepositoryDescription_powershell_topic"></a>

The following code example shows how to use `Update-CCRepositoryDescription`.

**Tools for PowerShell V5**
**Example 1: This example changes the description for the specified repository.**

```
Update-CCRepositoryDescription -RepositoryName MyDemoRepo -RepositoryDescription "This is an updated description."
```
+  For API details, see [UpdateRepositoryDescription](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

### `Update-CCRepositoryName`
<a name="codecommit_UpdateRepositoryName_powershell_topic"></a>

The following code example shows how to use `Update-CCRepositoryName`.

**Tools for PowerShell V5**
**Example 1: This example changes the name of the specified repository.**

```
Update-CCRepositoryName -NewName MyDemoRepo2 -OldName MyDemoRepo
```
+  For API details, see [UpdateRepositoryName](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Tools for PowerShell. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query powershell` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
