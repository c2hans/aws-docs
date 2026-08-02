---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codecommit_example_codecommit_ListRepositories_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListRepositories` with a CLI
<a name="codecommit_example_codecommit_ListRepositories_section"></a>

The following code examples show how to use `ListRepositories`.

------
#### [ CLI ]

**AWS CLI**
**To view a list of repositories**
This example lists all AWS CodeCommit repositories associated with the user's AWS account.
Command:

```
aws codecommit list-repositories
```
Output:

```
{
  "repositories": [
      {
         "repositoryName": "MyDemoRepo"
         "repositoryId": "f7579e13-b83e-4027-aaef-650c0EXAMPLE",
      },
      {
         "repositoryName": "MyOtherDemoRepo"
         "repositoryId": "cfc29ac4-b0cb-44dc-9990-f6f51EXAMPLE"
      }
  ]
}
```
+  For API details, see [ListRepositories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/list-repositories.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
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
+  For API details, see [ListRepositories](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

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

------
