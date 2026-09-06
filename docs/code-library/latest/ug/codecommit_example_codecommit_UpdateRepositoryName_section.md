---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codecommit_example_codecommit_UpdateRepositoryName_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `UpdateRepositoryName` with a CLI
<a name="codecommit_example_codecommit_UpdateRepositoryName_section"></a>

The following code examples show how to use `UpdateRepositoryName`.

------
#### [ CLI ]

**AWS CLI**
**To change the name of a repository**
This example changes the name of an AWS CodeCommit repository. This command produces output only if there are errors. Changing the name of the AWS CodeCommit repository will change the SSH and HTTPS URLs that users need to connect to the repository. Users will not be able to connect to this repository until they update their connection settings. Also, because the repository's ARN will change, changing the repository name will invalidate any IAM user policies that rely on this repository's ARN.
Command:

```
aws codecommit update-repository-name --old-name {{MyDemoRepo}} --new-name {{MyRenamedDemoRepo}}
```
Output:

```
None.
```
+  For API details, see [UpdateRepositoryName](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/update-repository-name.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example changes the name of the specified repository.**

```
Update-CCRepositoryName -NewName MyDemoRepo2 -OldName MyDemoRepo
```
+  For API details, see [UpdateRepositoryName](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example changes the name of the specified repository.**

```
Update-CCRepositoryName -NewName MyDemoRepo2 -OldName MyDemoRepo
```
+  For API details, see [UpdateRepositoryName](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
