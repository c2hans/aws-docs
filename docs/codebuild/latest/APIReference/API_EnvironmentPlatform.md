---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_EnvironmentPlatform.html
---

# EnvironmentPlatform
<a name="API_EnvironmentPlatform"></a>

A set of Docker images that are related by platform and are managed by AWS CodeBuild.

## Contents
<a name="API_EnvironmentPlatform_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** languages **   <a name="CodeBuild-Type-EnvironmentPlatform-languages"></a>
The list of programming languages that are available for the specified platform.
Type: Array of [EnvironmentLanguage](API_EnvironmentLanguage.md) objects
Required: No

 ** platform **   <a name="CodeBuild-Type-EnvironmentPlatform-platform"></a>
The platform's name.
Type: String
Valid Values: `DEBIAN | AMAZON_LINUX | UBUNTU | WINDOWS_SERVER`
Required: No

## See Also
<a name="API_EnvironmentPlatform_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/EnvironmentPlatform)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/EnvironmentPlatform)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/EnvironmentPlatform)
