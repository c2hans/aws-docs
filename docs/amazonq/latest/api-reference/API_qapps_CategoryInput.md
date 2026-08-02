---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_CategoryInput.html
---

# CategoryInput
<a name="API_qapps_CategoryInput"></a>

A label that web experience users associate with a library item. Web experience users use Categories to tag and filter library items.

## Contents
<a name="API_qapps_CategoryInput_Contents"></a>

 ** id **   <a name="qbusiness-Type-qapps_CategoryInput-id"></a>
The unique identifier of the category.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

 ** title **   <a name="qbusiness-Type-qapps_CategoryInput-title"></a>
The name of the category.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[a-zA-Z0-9_]+( [a-zA-Z0-9_]+)*`
Required: Yes

 ** color **   <a name="qbusiness-Type-qapps_CategoryInput-color"></a>
The color of the category, represented as a hexadecimal value of either 3 or 6 digits.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 7.
Pattern: `#([A-Fa-f0-9]{3}|[A-Fa-f0-9]{6})`
Required: No

## See Also
<a name="API_qapps_CategoryInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/CategoryInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/CategoryInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/CategoryInput)
