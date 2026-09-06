---
source_url: https://docs.aws.amazon.com/apprunner/latest/api/API_AuthenticationConfiguration.html
---

# AuthenticationConfiguration
<a name="API_AuthenticationConfiguration"></a>

Describes resources needed to authenticate access to some source repositories. The specific resource depends on the repository provider.

## Contents
<a name="API_AuthenticationConfiguration_Contents"></a>

 ** AccessRoleArn **   <a name="apprunner-Type-AuthenticationConfiguration-AccessRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that grants the App Runner service access to a source repository. It's required for ECR image repositories (but not for ECR Public repositories).
Type: String
Length Constraints: Minimum length of 29. Maximum length of 1024.
Pattern: `arn:(aws|aws-us-gov|aws-cn|aws-iso|aws-iso-b):iam::[0-9]{12}:(role|role\/service-role)\/[\w+=,.@\-/]{1,1000}`
Required: No

 ** ConnectionArn **   <a name="apprunner-Type-AuthenticationConfiguration-ConnectionArn"></a>
The Amazon Resource Name (ARN) of the App Runner connection that enables the App Runner service to connect to a source repository. It's required for GitHub code repositories.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws(-[\w]+)*:[a-z0-9-\\.]{0,63}:[a-z0-9-\\.]{0,63}:[0-9]{12}:(\w|\/|-){1,1011}`
Required: No

## See Also
<a name="API_AuthenticationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/apprunner-2020-05-15/AuthenticationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/apprunner-2020-05-15/AuthenticationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/apprunner-2020-05-15/AuthenticationConfiguration)
