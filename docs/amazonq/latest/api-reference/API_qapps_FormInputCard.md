---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_FormInputCard.html
---

# FormInputCard
<a name="API_qapps_FormInputCard"></a>

A card in an Amazon Q App that allows the user to submit a response.

## Contents
<a name="API_qapps_FormInputCard_Contents"></a>

 ** dependencies **   <a name="qbusiness-Type-qapps_FormInputCard-dependencies"></a>
Any dependencies or requirements for the form input card.
Type: Array of strings
Required: Yes

 ** id **   <a name="qbusiness-Type-qapps_FormInputCard-id"></a>
The unique identifier of the form input card.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

 ** metadata **   <a name="qbusiness-Type-qapps_FormInputCard-metadata"></a>
The metadata that defines the form input card data.
Type: [FormInputCardMetadata](API_qapps_FormInputCardMetadata.md) object
Required: Yes

 ** title **   <a name="qbusiness-Type-qapps_FormInputCard-title"></a>
The title of the form input card.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `[^{}\\"<>]+`
Required: Yes

 ** type **   <a name="qbusiness-Type-qapps_FormInputCard-type"></a>
The type of the card.
Type: String
Valid Values: `text-input | q-query | file-upload | q-plugin | form-input`
Required: Yes

 ** computeMode **   <a name="qbusiness-Type-qapps_FormInputCard-computeMode"></a>
The compute mode of the form input card. This property determines whether individual participants of a data collection session can submit multiple response or one response. A compute mode of `append` shall allow participants to submit the same form multiple times with different values. A compute mode of `replace`code> shall overwrite the current value for each participant.
Type: String
Valid Values: `append | replace`
Required: No

## See Also
<a name="API_qapps_FormInputCard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/FormInputCard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/FormInputCard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/FormInputCard)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
