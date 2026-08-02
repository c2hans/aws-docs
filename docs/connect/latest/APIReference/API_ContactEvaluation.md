---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ContactEvaluation.html
---

# ContactEvaluation
<a name="API_ContactEvaluation"></a>

Information about the contact evaluations where the key is the FormId, which is a unique identifier for the form.

## Contents
<a name="API_ContactEvaluation_Contents"></a>

 ** DeleteTimestamp **   <a name="connect-Type-ContactEvaluation-DeleteTimestamp"></a>
The date and time when the evaluation was deleted, in UTC time.
Type: Timestamp
Required: No

 ** EndTimestamp **   <a name="connect-Type-ContactEvaluation-EndTimestamp"></a>
The date and time when the evaluation was submitted, in UTC time.
Type: Timestamp
Required: No

 ** EvaluationArn **   <a name="connect-Type-ContactEvaluation-EvaluationArn"></a>
The Amazon Resource Name for the evaluation form. It is always present.
Type: String
Required: No

 ** ExportLocation **   <a name="connect-Type-ContactEvaluation-ExportLocation"></a>
The path where evaluation was exported.
Type: String
Required: No

 ** FormId **   <a name="connect-Type-ContactEvaluation-FormId"></a>
The `FormId` of the contact evaluation.
Type: String
Required: No

 ** StartTimestamp **   <a name="connect-Type-ContactEvaluation-StartTimestamp"></a>
The date and time when the evaluation was started, in UTC time.
Type: Timestamp
Required: No

 ** Status **   <a name="connect-Type-ContactEvaluation-Status"></a>
The status of the evaluation.
Type: String
Valid Values: `COMPLETE | IN_PROGRESS | DELETED`
Required: No

## See Also
<a name="API_ContactEvaluation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ContactEvaluation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ContactEvaluation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ContactEvaluation)
