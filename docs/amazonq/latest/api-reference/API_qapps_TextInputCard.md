---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_TextInputCard.html
---

# TextInputCard
<a name="API_qapps_TextInputCard"></a>

A card in an Amazon Q App that allows the user to input text.

## Contents
<a name="API_qapps_TextInputCard_Contents"></a>

 ** dependencies **   <a name="qbusiness-Type-qapps_TextInputCard-dependencies"></a>
Any dependencies or requirements for the text input card.
Type: Array of strings
Required: Yes

 ** id **   <a name="qbusiness-Type-qapps_TextInputCard-id"></a>
The unique identifier of the text input card.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

 ** title **   <a name="qbusiness-Type-qapps_TextInputCard-title"></a>
The title or label of the text input card.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `[^{}\\"<>]+`
Required: Yes

 ** type **   <a name="qbusiness-Type-qapps_TextInputCard-type"></a>
The type of the card.
Type: String
Valid Values: `text-input | q-query | file-upload | q-plugin | form-input`
Required: Yes

 ** defaultValue **   <a name="qbusiness-Type-qapps_TextInputCard-defaultValue"></a>
The default value to pre-populate in the text input field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** placeholder **   <a name="qbusiness-Type-qapps_TextInputCard-placeholder"></a>
The placeholder text to display in the text input field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

## See Also
<a name="API_qapps_TextInputCard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/TextInputCard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/TextInputCard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/TextInputCard)
