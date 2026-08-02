---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationForm.html
---

# EvaluationForm
<a name="API_EvaluationForm"></a>

Information about the evaluation form.

## Contents
<a name="API_EvaluationForm_Contents"></a>

 ** CreatedBy **   <a name="connect-Type-EvaluationForm-CreatedBy"></a>
The Amazon Resource Name (ARN) of the user who created the evaluation form.
Type: String
Required: Yes

 ** CreatedTime **   <a name="connect-Type-EvaluationForm-CreatedTime"></a>
The timestamp for when the evaluation form was created.
Type: Timestamp
Required: Yes

 ** EvaluationFormArn **   <a name="connect-Type-EvaluationForm-EvaluationFormArn"></a>
The Amazon Resource Name (ARN) for the evaluation form resource.
Type: String
Required: Yes

 ** EvaluationFormId **   <a name="connect-Type-EvaluationForm-EvaluationFormId"></a>
The unique identifier for the evaluation form.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** EvaluationFormVersion **   <a name="connect-Type-EvaluationForm-EvaluationFormVersion"></a>
A version of the evaluation form.
Type: Integer
Required: Yes

 ** Items **   <a name="connect-Type-EvaluationForm-Items"></a>
Items that are part of the evaluation form. The total number of sections and questions must not exceed 100 each. Questions must be contained in a section.
Type: Array of [EvaluationFormItem](API_EvaluationFormItem.md) objects
Required: Yes

 ** LastModifiedBy **   <a name="connect-Type-EvaluationForm-LastModifiedBy"></a>
The Amazon Resource Name (ARN) of the user who last updated the evaluation form.
Type: String
Required: Yes

 ** LastModifiedTime **   <a name="connect-Type-EvaluationForm-LastModifiedTime"></a>
The timestamp for when the evaluation form was last updated.
Type: Timestamp
Required: Yes

 ** Locked **   <a name="connect-Type-EvaluationForm-Locked"></a>
The flag indicating whether the evaluation form is locked for changes.
Type: Boolean
Required: Yes

 ** Status **   <a name="connect-Type-EvaluationForm-Status"></a>
The status of the evaluation form.
Type: String
Valid Values: `DRAFT | ACTIVE`
Required: Yes

 ** Title **   <a name="connect-Type-EvaluationForm-Title"></a>
A title of the evaluation form.
Type: String
Required: Yes

 ** AutoEvaluationConfiguration **   <a name="connect-Type-EvaluationForm-AutoEvaluationConfiguration"></a>
The automatic evaluation configuration of an evaluation form.
Type: [EvaluationFormAutoEvaluationConfiguration](API_EvaluationFormAutoEvaluationConfiguration.md) object
Required: No

 ** Description **   <a name="connect-Type-EvaluationForm-Description"></a>
The description of the evaluation form.
Type: String
Required: No

 ** LanguageConfiguration **   <a name="connect-Type-EvaluationForm-LanguageConfiguration"></a>
Configuration for language settings of this evaluation form.
Type: [EvaluationFormLanguageConfiguration](API_EvaluationFormLanguageConfiguration.md) object
Required: No

 ** LastValidationTime **   <a name="connect-Type-EvaluationForm-LastValidationTime"></a>
The timestamp when the most recent validation was started for this evaluation form.
Type: Timestamp
Required: No

 ** LatestValidationStatus **   <a name="connect-Type-EvaluationForm-LatestValidationStatus"></a>
The status of the most recent validation run for this evaluation form. Valid values: `IN_PROGRESS`, `COMPLETED`, `FAILED`.
Type: String
Valid Values: `IN_PROGRESS | COMPLETED | FAILED`
Required: No

 ** ReviewConfiguration **   <a name="connect-Type-EvaluationForm-ReviewConfiguration"></a>
Configuration for evaluation review settings of this evaluation form.
Type: [EvaluationReviewConfiguration](API_EvaluationReviewConfiguration.md) object
Required: No

 ** ScoringStrategy **   <a name="connect-Type-EvaluationForm-ScoringStrategy"></a>
A scoring strategy of the evaluation form.
Type: [EvaluationFormScoringStrategy](API_EvaluationFormScoringStrategy.md) object
Required: No

 ** Tags **   <a name="connect-Type-EvaluationForm-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** TargetConfiguration **   <a name="connect-Type-EvaluationForm-TargetConfiguration"></a>
Configuration that specifies the target for this evaluation form.
Type: [EvaluationFormTargetConfiguration](API_EvaluationFormTargetConfiguration.md) object
Required: No

## See Also
<a name="API_EvaluationForm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationForm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationForm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationForm)
