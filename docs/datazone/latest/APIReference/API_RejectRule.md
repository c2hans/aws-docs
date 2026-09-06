---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_RejectRule.html
---

# RejectRule
<a name="API_RejectRule"></a>

Specifies the rule and the threshold under which a prediction can be rejected.

## Contents
<a name="API_RejectRule_Contents"></a>

 ** rule **   <a name="datazone-Type-RejectRule-rule"></a>
Specifies whether you want to reject the top prediction for all targets or none.
Type: String
Valid Values: `ALL | NONE`
Required: No

 ** threshold **   <a name="datazone-Type-RejectRule-threshold"></a>
The confidence score that specifies the condition at which a prediction can be rejected.
Type: Float
Required: No

## See Also
<a name="API_RejectRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/RejectRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/RejectRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/RejectRule)
