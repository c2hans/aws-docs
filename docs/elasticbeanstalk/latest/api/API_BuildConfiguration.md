---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_BuildConfiguration.html
---

# BuildConfiguration
<a name="API_BuildConfiguration"></a>

Settings for an AWS CodeBuild build.

## Contents
<a name="API_BuildConfiguration_Contents"></a>

 ** CodeBuildServiceRole **
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that enables AWS CodeBuild to interact with dependent AWS service on behalf of the AWS account.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** Image **
The ID of the Docker image to use for this build project.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** ArtifactName **
The name of the artifact of the CodeBuild build. If provided, Elastic Beanstalk stores the build artifact in the S3 location *S3-bucket*/resources/*application-name*/codebuild/codebuild-*version-label*-*artifact-name*.zip. If not provided, Elastic Beanstalk stores the build artifact in the S3 location *S3-bucket*/resources/*application-name*/codebuild/codebuild-*version-label*.zip.
Type: String
Required: No

 ** ComputeType **
Information about the compute resources the build project will use.
+  `BUILD_GENERAL1_SMALL: Use up to 3 GB memory and 2 vCPUs for builds`
+  `BUILD_GENERAL1_MEDIUM: Use up to 7 GB memory and 4 vCPUs for builds`
+  `BUILD_GENERAL1_LARGE: Use up to 15 GB memory and 8 vCPUs for builds`
Type: String
Valid Values: `BUILD_GENERAL1_SMALL | BUILD_GENERAL1_MEDIUM | BUILD_GENERAL1_LARGE`
Required: No

 ** TimeoutInMinutes **
How long in minutes, from 5 to 480 (8 hours), for AWS CodeBuild to wait until timing out any related build that does not get marked as completed. The default is 60 minutes.
Type: Integer
Required: No

## See Also
<a name="API_BuildConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/BuildConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/BuildConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/BuildConfiguration)
