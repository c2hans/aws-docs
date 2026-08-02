---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationFormValidationFinding.html
---

# EvaluationFormValidationFinding
<a name="API_EvaluationFormValidationFinding"></a>

Information about a finding from the evaluation form validation process. Each finding identifies a structural issue or quality improvement opportunity for the evaluation form.

## Contents
<a name="API_EvaluationFormValidationFinding_Contents"></a>

 ** Description **   <a name="connect-Type-EvaluationFormValidationFinding-Description"></a>
A description of the validation issue.
Type: String
Required: Yes

 ** IssueCode **   <a name="connect-Type-EvaluationFormValidationFinding-IssueCode"></a>
A code that identifies the type of validation issue found.
Type: String
Required: Yes

 ** Severity **   <a name="connect-Type-EvaluationFormValidationFinding-Severity"></a>
The severity of the finding. Valid values: `WARNING`, `ERROR`.
Type: String
Valid Values: `WARNING | ERROR`
Required: Yes

 ** Items **   <a name="connect-Type-EvaluationFormValidationFinding-Items"></a>
A list of evaluation form items affected by this finding.
Type: Array of [EvaluationFormValidationFindingItem](API_EvaluationFormValidationFindingItem.md) objects
Required: No

 ** Suggestion **   <a name="connect-Type-EvaluationFormValidationFinding-Suggestion"></a>
A suggested fix for the validation issue.
Type: String
Required: No

## See Also
<a name="API_EvaluationFormValidationFinding_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationFormValidationFinding)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationFormValidationFinding)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationFormValidationFinding)
