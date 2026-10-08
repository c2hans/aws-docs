---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codedeploy_example_codedeploy_ListApplicationRevisions_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListApplicationRevisions` with a CLI
<a name="codedeploy_example_codedeploy_ListApplicationRevisions_section"></a>

The following code examples show how to use `ListApplicationRevisions`.

------
#### [ CLI ]

**AWS CLI**
**To get information about application revisions**
The following `list-application-revisions` example displays information about all application revisions that are associated with the specified application.

```
aws deploy list-application-revisions \
    --application-name {{WordPress_App}} \
    --s-3-bucket {{CodeDeployDemoBucket}} \
    --deployed {{exclude}} \
    --s-3-key-prefix {{WordPress_}} \
    --sort-by {{lastUsedTime}} \
    --sort-order {{descending}}
```
Output:

```
{
    "revisions": [
        {
            "revisionType": "S3",
            "s3Location": {
                "version": "uTecLusvCB_JqHFXtfUcyfV8bEXAMPLE",
                "bucket": "CodeDeployDemoBucket",
                "key": "WordPress_App.zip",
                "bundleType": "zip"
            }
        },
        {
            "revisionType": "S3",
            "s3Location": {
                "version": "tMk.UxgDpMEVb7V187ZM6wVAWEXAMPLE",
                "bucket": "CodeDeployDemoBucket",
                "key": "WordPress_App_2-0.zip",
                "bundleType": "zip"
            }
        }
    ]
}
```
+  For API details, see [ListApplicationRevisions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/list-application-revisions.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example gets information about available revisions for the specified application.**

```
ForEach ($revision in (Get-CDApplicationRevisionList -ApplicationName CodeDeployDemoApplication -Deployed Ignore)) {
>>   If ($revision.RevisionType -Eq "S3") {
>>     Write-Output ("Type = S3, Bucket = " + $revision.S3Location.Bucket + ", BundleType = " + $revision.S3Location.BundleType + ", ETag = " + $revision.S3Location.ETag + ", Key = " + $revision.S3Location.Key)
>>   }
>>   If ($revision.RevisionType -Eq "GitHub") {
>>     Write-Output ("Type = GitHub, CommitId = " + $revision.GitHubLocation.CommitId + ", Repository = " + $revision.GitHubLocation.Repository)
>>   }
>> }
>>
```
**Output:**

```
Type = S3, Bucket = amzn-s3-demo-bucket, BundleType = zip, ETag = 4565c1ac97187f190c1a90265EXAMPLE, Key = 5xd27EX.zip
Type = GitHub, CommitId = f48933c3...76405362, Repository = MyGitHubUser/CodeDeployDemoRepo
```
+  For API details, see [ListApplicationRevisions](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example gets information about available revisions for the specified application.**

```
ForEach ($revision in (Get-CDApplicationRevisionList -ApplicationName CodeDeployDemoApplication -Deployed Ignore)) {
>>   If ($revision.RevisionType -Eq "S3") {
>>     Write-Output ("Type = S3, Bucket = " + $revision.S3Location.Bucket + ", BundleType = " + $revision.S3Location.BundleType + ", ETag = " + $revision.S3Location.ETag + ", Key = " + $revision.S3Location.Key)
>>   }
>>   If ($revision.RevisionType -Eq "GitHub") {
>>     Write-Output ("Type = GitHub, CommitId = " + $revision.GitHubLocation.CommitId + ", Repository = " + $revision.GitHubLocation.Repository)
>>   }
>> }
>>
```
**Output:**

```
Type = S3, Bucket = amzn-s3-demo-bucket, BundleType = zip, ETag = 4565c1ac97187f190c1a90265EXAMPLE, Key = 5xd27EX.zip
Type = GitHub, CommitId = f48933c3...76405362, Repository = MyGitHubUser/CodeDeployDemoRepo
```
+  For API details, see [ListApplicationRevisions](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
