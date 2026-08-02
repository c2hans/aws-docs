---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_GitConfig.html
---

# GitConfig
<a name="API_GitConfig"></a>

Specifies configuration details for a Git repository in your AWS account.

## Contents
<a name="API_GitConfig_Contents"></a>

 ** RepositoryUrl **   <a name="sagemaker-Type-GitConfig-RepositoryUrl"></a>
The URL where the Git repository is located.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 1024.
Pattern: `https://([^/]+)/?.{3,1016}`
Required: Yes

 ** Branch **   <a name="sagemaker-Type-GitConfig-Branch"></a>
The default branch for the Git repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[^ ~^:?*\[]+`
Required: No

 ** SecretArn **   <a name="sagemaker-Type-GitConfig-SecretArn"></a>
The Amazon Resource Name (ARN) of the AWS Secrets Manager secret that contains the credentials used to access the git repository. The secret must have a staging label of `AWSCURRENT` and must be in the following format:
 `{"username": UserName, "password": Password}`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:secretsmanager:[a-z0-9\-]*:[0-9]{12}:secret:.*`
Required: No

## See Also
<a name="API_GitConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/GitConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/GitConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/GitConfig)
