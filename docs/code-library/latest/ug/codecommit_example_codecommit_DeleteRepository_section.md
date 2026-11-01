---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codecommit_example_codecommit_DeleteRepository_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteRepository` with a CLI
<a name="codecommit_example_codecommit_DeleteRepository_section"></a>

The following code examples show how to use `DeleteRepository`.

------
#### [ CLI ]

**AWS CLI**
**To delete a repository**
The following `delete-repository` example deletes an AWS CodeCommit repository.

```
aws codecommit delete-repository \
    --repository-name {{MyDemoRepo}}
```
Output:

```
{
    "repositoryId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111"
}
```
For more information, see [Delete an AWS CodeCommit repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-delete-repository.html#how-to-delete-repository-cli) in the *AWS CodeCommit User Guide*.
+  For API details, see [DeleteRepository](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/delete-repository.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example forcibly deletes the specified repository. The command will prompt for confirmation before proceeding. Add the -Force parameter to delete the repository without a prompt.**

```
Remove-CCRepository -RepositoryName MyDemoRepo
```
**Output:**

```
43ef2443-3372-4b12-9e78-65c27EXAMPLE
```
+  For API details, see [DeleteRepository](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

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

------
