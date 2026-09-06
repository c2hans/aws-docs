---
source_url: https://docs.aws.amazon.com/inspector/v1/APIReference/API_RulesPackage.html
---

# RulesPackage
<a name="API_RulesPackage"></a>

Contains information about an Amazon Inspector Classic rules package. This data type is used as the response element in the [DescribeRulesPackages](API_DescribeRulesPackages.md) action.

## Contents
<a name="API_RulesPackage_Contents"></a>

 ** arn **   <a name="Inspector-Type-RulesPackage-arn"></a>
The ARN of the rules package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** name **   <a name="Inspector-Type-RulesPackage-name"></a>
The name of the rules package.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

 ** provider **   <a name="Inspector-Type-RulesPackage-provider"></a>
The provider of the rules package.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

 ** version **   <a name="Inspector-Type-RulesPackage-version"></a>
The version ID of the rules package.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: Yes

 ** description **   <a name="Inspector-Type-RulesPackage-description"></a>
The description of the rules package.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 20000.
Required: No

## See Also
<a name="API_RulesPackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector-2016-02-16/RulesPackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector-2016-02-16/RulesPackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector-2016-02-16/RulesPackage)
