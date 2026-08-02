---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_LifecyclePolicyRuleAction.html
---

# LifecyclePolicyRuleAction
<a name="API_LifecyclePolicyRuleAction"></a>

The type of action to be taken.

## Contents
<a name="API_LifecyclePolicyRuleAction_Contents"></a>

 ** targetStorageClass **   <a name="ECR-Type-LifecyclePolicyRuleAction-targetStorageClass"></a>
The target storage class for the action. This is only present when the `type` is `TRANSITION.`
Type: String
Valid Values: `ARCHIVE`
Required: No

 ** type **   <a name="ECR-Type-LifecyclePolicyRuleAction-type"></a>
The type of action to be taken.
Type: String
Valid Values: `EXPIRE | TRANSITION`
Required: No

## See Also
<a name="API_LifecyclePolicyRuleAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/LifecyclePolicyRuleAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/LifecyclePolicyRuleAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/LifecyclePolicyRuleAction)
