---
source_url: https://docs.aws.amazon.com/cognito-user-identity-pools/latest/APIReference/API_AcrLevelConfigType.html
---

# AcrLevelConfigType
<a name="API_AcrLevelConfigType"></a>

The configuration for a single authentication context class reference (ACR) level in a user pool. Each entry in an `AcrConfiguration` map associates a level (`Level1` through `Level4`) with this configuration, which provides the custom name that Amazon Cognito reports for that level in the `acr` token claim.

## Contents
<a name="API_AcrLevelConfigType_Contents"></a>

 ** AcrValue **   <a name="CognitoUserPools-Type-AcrLevelConfigType-AcrValue"></a>
The custom name for this authentication context class reference (ACR) level. This value is the URI that Amazon Cognito reports in the `acr` token claim when a user meets this level. The name must be unique across all levels in the user pool, including default names.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\x21\x23-\x5B\x5D-\x7E]+`
Required: Yes

## See Also
<a name="API_AcrLevelConfigType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cognito-idp-2016-04-18/AcrLevelConfigType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cognito-idp-2016-04-18/AcrLevelConfigType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cognito-idp-2016-04-18/AcrLevelConfigType)
