---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_RevisionLocation.html
---

# RevisionLocation
<a name="API_RevisionLocation"></a>

Information about the location of an application revision.

## Contents
<a name="API_RevisionLocation_Contents"></a>

 ** appSpecContent **   <a name="CodeDeploy-Type-RevisionLocation-appSpecContent"></a>
 The content of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML and stored as a RawString.
Type: [AppSpecContent](API_AppSpecContent.md) object
Required: No

 ** gitHubLocation **   <a name="CodeDeploy-Type-RevisionLocation-gitHubLocation"></a>
Information about the location of application artifacts stored in GitHub.
Type: [GitHubLocation](API_GitHubLocation.md) object
Required: No

 ** revisionType **   <a name="CodeDeploy-Type-RevisionLocation-revisionType"></a>
The type of application revision:
+ S3: An application revision stored in Amazon S3.
+ GitHub: An application revision stored in GitHub (EC2/On-premises deployments only).
+ String: A YAML-formatted or JSON-formatted string (AWS Lambda deployments only).
+ AppSpecContent: An `AppSpecContent` object that contains the contents of an AppSpec file for an AWS Lambda or Amazon ECS deployment. The content is formatted as JSON or YAML stored as a RawString.
Type: String
Valid Values: `S3 | GitHub | String | AppSpecContent | SystemsManagerPatchBaseline`
Required: No

 ** s3Location **   <a name="CodeDeploy-Type-RevisionLocation-s3Location"></a>
Information about the location of a revision stored in Amazon S3.
Type: [S3Location](API_S3Location.md) object
Required: No

 ** string **   <a name="CodeDeploy-Type-RevisionLocation-string"></a>
 *This member has been deprecated.*
Information about the location of an AWS Lambda deployment revision stored as a RawString.
Type: [RawString](API_RawString.md) object
Required: No

## See Also
<a name="API_RevisionLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/RevisionLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/RevisionLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/RevisionLocation)
