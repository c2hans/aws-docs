---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codedeploy_example_codedeploy_GetApplicationRevision_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetApplicationRevision` with a CLI
<a name="codedeploy_example_codedeploy_GetApplicationRevision_section"></a>

The following code examples show how to use `GetApplicationRevision`.

------
#### [ CLI ]

**AWS CLI**
**To get information about an application revision**
The following `get-application-revision` example displays information about an application revision that is associated with the specified application.

```
aws deploy get-application-revision \
    --application-name {{WordPress_App}} \
    --s3-location {{bucket=amzn-s3-demo-bucket,bundleType=zip,eTag=dd56cfdEXAMPLE8e768f9d77fEXAMPLE,key=WordPressApp.zip}}
```
Output:

```
{
    "applicationName": "WordPress_App",
    "revisionInfo": {
        "description": "Application revision registered by Deployment ID: d-A1B2C3111",
        "registerTime": 1411076520.009,
        "deploymentGroups": "WordPress_DG",
        "lastUsedTime": 1411076520.009,
        "firstUsedTime": 1411076520.009
    },
    "revision": {
        "revisionType": "S3",
        "s3Location": {
            "bundleType": "zip",
            "eTag": "dd56cfdEXAMPLE8e768f9d77fEXAMPLE",
            "bucket": "amzn-s3-demo-bucket",
            "key": "WordPressApp.zip"
        }
    }
}
```
+  For API details, see [GetApplicationRevision](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/get-application-revision.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example gets information about the specified application revision.**

```
$revision = Get-CDApplicationRevision -ApplicationName CodeDeployDemoApplication -S3Location_Bucket amzn-s3-demo-bucket -Revision_RevisionType S3 -S3Location_Key 5xd27EX.zip -S3Location_BundleType zip -S3Location_ETag 4565c1ac97187f190c1a90265EXAMPLE
Write-Output ("Description = " + $revision.RevisionInfo.Description + ", RegisterTime = " + $revision.RevisionInfo.RegisterTime)
```
**Output:**

```
Description = Application revision registered by Deployment ID: d-CX9CHN3EX, RegisterTime = 07/20/2015 23:46:42
```
+  For API details, see [GetApplicationRevision](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example gets information about the specified application revision.**

```
$revision = Get-CDApplicationRevision -ApplicationName CodeDeployDemoApplication -S3Location_Bucket amzn-s3-demo-bucket -Revision_RevisionType S3 -S3Location_Key 5xd27EX.zip -S3Location_BundleType zip -S3Location_ETag 4565c1ac97187f190c1a90265EXAMPLE
Write-Output ("Description = " + $revision.RevisionInfo.Description + ", RegisterTime = " + $revision.RevisionInfo.RegisterTime)
```
**Output:**

```
Description = Application revision registered by Deployment ID: d-CX9CHN3EX, RegisterTime = 07/20/2015 23:46:42
```
+  For API details, see [GetApplicationRevision](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
