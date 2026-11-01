---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codecommit_example_codecommit_BatchGetRepositories_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `BatchGetRepositories` with a CLI
<a name="codecommit_example_codecommit_BatchGetRepositories_section"></a>

The following code examples show how to use `BatchGetRepositories`.

------
#### [ CLI ]

**AWS CLI**
**To view details about multiple repositories**
The following `batch-get-repositories` example shows details about multiple AWS CodeCommit repositories.

```
aws codecommit batch-get-repositories \
    --repository-names {{MyDemoRepo}} {{MyOtherDemoRepo}}
```
Output:

```
{
    "repositories": [
        {
            "creationDate": 1429203623.625,
            "defaultBranch": "main",
            "repositoryName": "MyDemoRepo",
            "cloneUrlSsh": "ssh://git-codecommit.us-west-2.amazonaws.com/v1/repos/MyDemoRepo",
            "lastModifiedDate": 1430783812.0869999,
            "repositoryDescription": "My demonstration repository",
            "cloneUrlHttp": "https://codecommit.us-west-2.amazonaws.com/v1/repos/MyDemoRepo",
            "repositoryId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "Arn": "arn:aws:codecommit:us-west-2:123456789012:MyDemoRepo",
            "accountId": "123456789012"
        },
        {
            "creationDate": 1429203623.627,
            "defaultBranch": "main",
            "repositoryName": "MyOtherDemoRepo",
            "cloneUrlSsh": "ssh://git-codecommit.us-west-2.amazonaws.com/v1/repos/MyOtherDemoRepo",
            "lastModifiedDate": 1430783812.0889999,
            "repositoryDescription": "My other demonstration repository",
            "cloneUrlHttp": "https://codecommit.us-west-2.amazonaws.com/v1/repos/MyOtherDemoRepo",
            "repositoryId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "Arn": "arn:aws:codecommit:us-west-2:123456789012:MyOtherDemoRepo",
            "accountId": "123456789012"
        }
    ],
    "repositoriesNotFound": []
}
```
For more information, see [View CodeCommit repository details](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-view-repository-details.html#how-to-view-repository-details-with-names-cli) in the *AWS CodeCommit User Guide*.
+  For API details, see [BatchGetRepositories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/codecommit/batch-get-repositories.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
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
+  For API details, see [BatchGetRepositories](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

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

------
