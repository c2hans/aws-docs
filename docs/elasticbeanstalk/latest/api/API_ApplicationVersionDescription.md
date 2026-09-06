---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ApplicationVersionDescription.html
---

# ApplicationVersionDescription
<a name="API_ApplicationVersionDescription"></a>

Describes the properties of an application version.

## Contents
<a name="API_ApplicationVersionDescription_Contents"></a>

 ** ApplicationName **
The name of the application to which the application version belongs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** ApplicationVersionArn **
The Amazon Resource Name (ARN) of the application version.
Type: String
Required: No

 ** BuildArn **
Reference to the artifact from the AWS CodeBuild build.
Type: String
Required: No

 ** DateCreated **
The creation date of the application version.
Type: Timestamp
Required: No

 ** DateUpdated **
The last modified date of the application version.
Type: Timestamp
Required: No

 ** Description **
The description of the application version.
Type: String
Length Constraints: Maximum length of 200.
Required: No

 ** SourceBuildInformation **
If the version's source code was retrieved from AWS CodeCommit, the location of the source code for the application version.
Type: [SourceBuildInformation](API_SourceBuildInformation.md) object
Required: No

 ** SourceBundle **
The storage location of the application version's source bundle in Amazon S3.
Type: [S3Location](API_S3Location.md) object
Required: No

 ** Status **
The processing status of the application version. Reflects the state of the application version during its creation. Many of the values are only applicable if you specified `True` for the `Process` parameter of the `CreateApplicationVersion` action. The following list describes the possible values.
+  `Unprocessed` – Application version wasn't pre-processed or validated. Elastic Beanstalk will validate configuration files during deployment of the application version to an environment.
+  `Processing` – Elastic Beanstalk is currently processing the application version.
+  `Building` – Application version is currently undergoing an AWS CodeBuild build.
+  `Processed` – Elastic Beanstalk was successfully pre-processed and validated.
+  `Failed` – Either the AWS CodeBuild build failed or configuration files didn't pass validation. This application version isn't usable.
Type: String
Valid Values: `Processed | Unprocessed | Failed | Processing | Building`
Required: No

 ** VersionLabel **
A unique identifier for the application version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

## See Also
<a name="API_ApplicationVersionDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/ApplicationVersionDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/ApplicationVersionDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/ApplicationVersionDescription)
