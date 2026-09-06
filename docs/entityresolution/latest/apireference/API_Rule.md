---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_Rule.html
---

# Rule
<a name="API_Rule"></a>

An object containing the `ruleName` and `matchingKeys`.

## Contents
<a name="API_Rule_Contents"></a>

 ** matchingKeys **   <a name="API-Type-Rule-matchingKeys"></a>
A list of `MatchingKeys`. The `MatchingKeys` must have been defined in the `SchemaMapping`. Two records are considered to match according to this rule if all of the `MatchingKeys` match.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 15 items.
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[a-zA-Z_0-9- ]*`
Required: Yes

 ** ruleName **   <a name="API-Type-Rule-ruleName"></a>
A name for the matching rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[a-zA-Z_0-9- ]*`
Required: Yes

## See Also
<a name="API_Rule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/Rule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/Rule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/Rule)
