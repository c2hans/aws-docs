---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationFormSearchSummary.html
---

# EvaluationFormSearchSummary
<a name="API_EvaluationFormSearchSummary"></a>

Information about the returned evaluation forms.

## Contents
<a name="API_EvaluationFormSearchSummary_Contents"></a>

 ** CreatedBy **   <a name="connect-Type-EvaluationFormSearchSummary-CreatedBy"></a>
Who created the evaluation form.
Type: String
Required: Yes

 ** CreatedTime **   <a name="connect-Type-EvaluationFormSearchSummary-CreatedTime"></a>
When the evaluation form was created.
Type: Timestamp
Required: Yes

 ** EvaluationFormArn **   <a name="connect-Type-EvaluationFormSearchSummary-EvaluationFormArn"></a>
The Amazon Resource Name (ARN) for the evaluation form resource.
Type: String
Required: Yes

 ** EvaluationFormId **   <a name="connect-Type-EvaluationFormSearchSummary-EvaluationFormId"></a>
The unique identifier for the evaluation form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** LastModifiedBy **   <a name="connect-Type-EvaluationFormSearchSummary-LastModifiedBy"></a>
Who changed the evaluation form.
Type: String
Required: Yes

 ** LastModifiedTime **   <a name="connect-Type-EvaluationFormSearchSummary-LastModifiedTime"></a>
When the evaluation form was last changed.
Type: Timestamp
Required: Yes

 ** LatestVersion **   <a name="connect-Type-EvaluationFormSearchSummary-LatestVersion"></a>
Latest version of the evaluation form.
Type: Integer
Required: Yes

 ** Status **   <a name="connect-Type-EvaluationFormSearchSummary-Status"></a>
The status of the evaluation form.
Type: String
Valid Values: `DRAFT | ACTIVE`
Required: Yes

 ** Title **   <a name="connect-Type-EvaluationFormSearchSummary-Title"></a>
The title of the evaluation form.
Type: String
Required: Yes

 ** ActiveVersion **   <a name="connect-Type-EvaluationFormSearchSummary-ActiveVersion"></a>
Active version of the evaluation form.
Type: Integer
Required: No

 ** AutoEvaluationEnabled **   <a name="connect-Type-EvaluationFormSearchSummary-AutoEvaluationEnabled"></a>
Whether automated evaluation is enabled.
Type: Boolean
Required: No

 ** ContactInteractionType **   <a name="connect-Type-EvaluationFormSearchSummary-ContactInteractionType"></a>
The contact interaction type for this evaluation form.
Type: String
Valid Values: `AGENT | AUTOMATED | CUSTOMER`
Required: No

 ** Description **   <a name="connect-Type-EvaluationFormSearchSummary-Description"></a>
The description of the evaluation form.
Type: String
Required: No

 ** EvaluationFormLanguage **   <a name="connect-Type-EvaluationFormSearchSummary-EvaluationFormLanguage"></a>
The language of the evaluation form.
Type: String
Valid Values: `de-DE | en-US | es-ES | fr-FR | it-IT | pt-BR | ja-JP | ko-KR | zh-CN | ms-MY`
Required: No

 ** LastActivatedBy **   <a name="connect-Type-EvaluationFormSearchSummary-LastActivatedBy"></a>
The ID of user who last activated evaluation form.
Type: String
Required: No

 ** LastActivatedTime **   <a name="connect-Type-EvaluationFormSearchSummary-LastActivatedTime"></a>
When the evaluation format was last activated.
Type: Timestamp
Required: No

 ** Tags **   <a name="connect-Type-EvaluationFormSearchSummary-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_EvaluationFormSearchSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationFormSearchSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationFormSearchSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationFormSearchSummary)
