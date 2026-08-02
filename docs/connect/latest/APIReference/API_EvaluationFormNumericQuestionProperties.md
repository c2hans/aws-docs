---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_EvaluationFormNumericQuestionProperties.html
---

# EvaluationFormNumericQuestionProperties
<a name="API_EvaluationFormNumericQuestionProperties"></a>

Information about properties for a numeric question in an evaluation form.

## Contents
<a name="API_EvaluationFormNumericQuestionProperties_Contents"></a>

 ** MaxValue **   <a name="connect-Type-EvaluationFormNumericQuestionProperties-MaxValue"></a>
The maximum answer value.
Type: Integer
Required: Yes

 ** MinValue **   <a name="connect-Type-EvaluationFormNumericQuestionProperties-MinValue"></a>
The minimum answer value.
Type: Integer
Required: Yes

 ** Automation **   <a name="connect-Type-EvaluationFormNumericQuestionProperties-Automation"></a>
The automation properties of the numeric question.
Type: [EvaluationFormNumericQuestionAutomation](API_EvaluationFormNumericQuestionAutomation.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** Options **   <a name="connect-Type-EvaluationFormNumericQuestionProperties-Options"></a>
The scoring options of the numeric question.
Type: Array of [EvaluationFormNumericQuestionOption](API_EvaluationFormNumericQuestionOption.md) objects
Required: No

## See Also
<a name="API_EvaluationFormNumericQuestionProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/EvaluationFormNumericQuestionProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/EvaluationFormNumericQuestionProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/EvaluationFormNumericQuestionProperties)
