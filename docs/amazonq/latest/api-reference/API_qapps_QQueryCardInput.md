---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_qapps_QQueryCardInput.html
---

# QQueryCardInput
<a name="API_qapps_QQueryCardInput"></a>

The input shape for defining a query card in an Amazon Q App.

## Contents
<a name="API_qapps_QQueryCardInput_Contents"></a>

 ** id **   <a name="qbusiness-Type-qapps_QQueryCardInput-id"></a>
The unique identifier of the query card.
Type: String
Pattern: `[\da-f]{8}-[\da-f]{4}-[45][\da-f]{3}-[89ABab][\da-f]{3}-[\da-f]{12}`
Required: Yes

 ** prompt **   <a name="qbusiness-Type-qapps_QQueryCardInput-prompt"></a>
The prompt or instructions displayed for the query card.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50000.
Required: Yes

 ** title **   <a name="qbusiness-Type-qapps_QQueryCardInput-title"></a>
The title or label of the query card.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `[^{}\\"<>]+`
Required: Yes

 ** type **   <a name="qbusiness-Type-qapps_QQueryCardInput-type"></a>
The type of the card.
Type: String
Valid Values: `text-input | q-query | file-upload | q-plugin | form-input`
Required: Yes

 ** attributeFilter **   <a name="qbusiness-Type-qapps_QQueryCardInput-attributeFilter"></a>
Turns on filtering of responses based on document attributes or metadata fields.
Type: [AttributeFilter](API_qapps_AttributeFilter.md) object
Required: No

 ** outputSource **   <a name="qbusiness-Type-qapps_QQueryCardInput-outputSource"></a>
The source or type of output to generate for the query card.
Type: String
Valid Values: `approved-sources | llm`
Required: No

## See Also
<a name="API_qapps_QQueryCardInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qapps-2023-11-27/QQueryCardInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qapps-2023-11-27/QQueryCardInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qapps-2023-11-27/QQueryCardInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
