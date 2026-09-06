---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_Repository.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# Repository
<a name="API_Repository"></a>

Detailed data of a linked repository—a repository that has been registered with AWS Proton.

## Contents
<a name="API_Repository_Contents"></a>

 ** arn **   <a name="proton-Type-Repository-arn"></a>
The Amazon Resource Name (ARN) of the linked repository.
Type: String
Required: Yes

 ** connectionArn **   <a name="proton-Type-Repository-connectionArn"></a>
The Amazon Resource Name (ARN) of your AWS CodeStar connection that connects AWS Proton to your repository provider account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:(aws|aws-cn|aws-us-gov):[a-zA-Z0-9-]+:[a-zA-Z0-9-]*:\d{12}:([\w+=,.@-]+[/:])*[\w+=,.@-]+`
Required: Yes

 ** name **   <a name="proton-Type-Repository-name"></a>
The repository name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*[A-Za-z0-9_.-].*/[A-Za-z0-9_.-].*`
Required: Yes

 ** provider **   <a name="proton-Type-Repository-provider"></a>
The repository provider.
Type: String
Valid Values: `GITHUB | GITHUB_ENTERPRISE | BITBUCKET`
Required: Yes

 ** encryptionKey **   <a name="proton-Type-Repository-encryptionKey"></a>
Your customer AWS KMS encryption key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:(aws|aws-cn|aws-us-gov):[a-zA-Z0-9-]+:[a-zA-Z0-9-]*:\d{12}:([\w+=,.@-]+[/:])*[\w+=,.@-]+`
Required: No

## See Also
<a name="API_Repository_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/Repository)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/Repository)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/Repository)
