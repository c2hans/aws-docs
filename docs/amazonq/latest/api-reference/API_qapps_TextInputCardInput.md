---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_TextInputCardInput.html
---

# TextInputCardInput
<a name="API_qapps_TextInputCardInput"></a>

The input shape for defining a text input card in an Amazon Q App.

## Contents
<a name="API_qapps_TextInputCardInput_Contents"></a>

 ** id **   <a name="qbusiness-Type-qapps_TextInputCardInput-id"></a>
The unique identifier of the text input card.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

 ** title **   <a name="qbusiness-Type-qapps_TextInputCardInput-title"></a>
The title or label of the text input card.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `[^{}\\"<>]+`
Required: Yes

 ** type **   <a name="qbusiness-Type-qapps_TextInputCardInput-type"></a>
The type of the card.
Type: String
Valid Values: `text-input | q-query | file-upload | q-plugin | form-input`
Required: Yes

 ** defaultValue **   <a name="qbusiness-Type-qapps_TextInputCardInput-defaultValue"></a>
The default value to pre-populate in the text input field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** placeholder **   <a name="qbusiness-Type-qapps_TextInputCardInput-placeholder"></a>
The placeholder text to display in the text input field.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

## See Also
<a name="API_qapps_TextInputCardInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/TextInputCardInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/TextInputCardInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/TextInputCardInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
