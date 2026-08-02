---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_DifferentialPrivacyColumn.html
---

# DifferentialPrivacyColumn
<a name="API_DifferentialPrivacyColumn"></a>

Specifies the name of the column that contains the unique identifier of your users, whose privacy you want to protect.

## Contents
<a name="API_DifferentialPrivacyColumn_Contents"></a>

 ** name **   <a name="API-Type-DifferentialPrivacyColumn-name"></a>
The name of the column, such as user\_id, that contains the unique identifier of your users, whose privacy you want to protect. If you want to turn on differential privacy for two or more tables in a collaboration, you must configure the same column as the user identifier column in both analysis rules.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
Required: Yes

## See Also
<a name="API_DifferentialPrivacyColumn_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/DifferentialPrivacyColumn)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/DifferentialPrivacyColumn)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/DifferentialPrivacyColumn)
