---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/codedeploy_example_codedeploy_RegisterApplicationRevision_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `RegisterApplicationRevision` with a CLI
<a name="codedeploy_example_codedeploy_RegisterApplicationRevision_section"></a>

The following code examples show how to use `RegisterApplicationRevision`.

------
#### [ CLI ]

**AWS CLI**
**To register information about an already-uploaded application revision**
The following `register-application-revision` example registers information about an already-uploaded application revision stored in Amazon S3 with AWS CodeDeploy.

```
aws deploy register-application-revision \
    --application-name {{WordPress_App}} \
    --description {{"Revised WordPress application"}} \
    --s3-location {{bucket=amzn-s3-demo-bucket,key=RevisedWordPressApp.zip,bundleType=zip,eTag=cecc9b8a08eac650a6e71fdb88EXAMPLE}}
```
This command produces no output.
+  For API details, see [RegisterApplicationRevision](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/deploy/register-application-revision.html) in *AWS CLI Command Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example registers an application revision with the specified Amazon S3 location, for the specified application.**

```
Register-CDApplicationRevision -ApplicationName MyNewApplication -S3Location_Bucket amzn-s3-demo-bucket -S3Location_BundleType zip -S3Location_Key aws-codedeploy_linux-master.zip -Revision_RevisionType S3
```
+  For API details, see [RegisterApplicationRevision](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example registers an application revision with the specified Amazon S3 location, for the specified application.**

```
Register-CDApplicationRevision -ApplicationName MyNewApplication -S3Location_Bucket amzn-s3-demo-bucket -S3Location_BundleType zip -S3Location_Key aws-codedeploy_linux-master.zip -Revision_RevisionType S3
```
+  For API details, see [RegisterApplicationRevision](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
