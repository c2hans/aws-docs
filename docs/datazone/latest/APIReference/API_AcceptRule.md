---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_AcceptRule.html
---

# AcceptRule
<a name="API_AcceptRule"></a>

Specifies the rule and the threshold under which a prediction can be accepted.

## Contents
<a name="API_AcceptRule_Contents"></a>

 ** rule **   <a name="datazone-Type-AcceptRule-rule"></a>
Specifies whether you want to accept the top prediction for all targets or none.
Type: String
Valid Values: `ALL | NONE`
Required: No

 ** threshold **   <a name="datazone-Type-AcceptRule-threshold"></a>
The confidence score that specifies the condition at which a prediction can be accepted.
Type: Float
Required: No

## See Also
<a name="API_AcceptRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/AcceptRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/AcceptRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/AcceptRule)
