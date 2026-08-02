---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/latest/APIReference/API_ModifyRule.html
---

# ModifyRule
<a name="API_ModifyRule"></a>

Replaces the specified properties of the specified rule. Any properties that you do not specify are unchanged.

To add an item to a list, remove an item from a list, or update an item in a list, you must provide the entire list. For example, to add an action, specify a list with the current actions plus the new action.

To modify the actions for the default rule, use [ModifyListener](API_ModifyListener.md).

## Request Parameters
<a name="API_ModifyRule_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **Actions.member.N**
The actions.
Type: Array of [Action](API_Action.md) objects
Required: No

 **Conditions.member.N**
The conditions.
Type: Array of [RuleCondition](API_RuleCondition.md) objects
Required: No

 ** ResetTransforms **
Indicates whether to remove all transforms from the rule. If you specify `ResetTransforms`, you can't specify `Transforms`.
Type: Boolean
Required: No

 ** RuleArn **
The Amazon Resource Name (ARN) of the rule.
Type: String
Required: Yes

 **Transforms.member.N**
The transforms to apply to requests that match this rule. You can add one host header rewrite transform and one URL rewrite transform. If you specify `Transforms`, you can't specify `ResetTransforms`.
Type: Array of [RuleTransform](API_RuleTransform.md) objects
Required: No

## Response Elements
<a name="API_ModifyRule_ResponseElements"></a>

The following element is returned by the service.

 **Rules.member.N**
Information about the modified rule.
Type: Array of [Rule](API_Rule.md) objects

## Errors
<a name="API_ModifyRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** IncompatibleProtocols **
The specified configuration is not valid with this protocol.
HTTP Status Code: 400

 ** InvalidLoadBalancerAction **
The requested action is not valid.
HTTP Status Code: 400

 ** OperationNotPermitted **
This operation is not allowed.
HTTP Status Code: 400

 ** RuleNotFound **
The specified rule does not exist.
HTTP Status Code: 400

 ** TargetGroupAssociationLimit **
You've reached the limit on the number of load balancers per target group.
HTTP Status Code: 400

 ** TargetGroupNotFound **
The specified target group does not exist.
HTTP Status Code: 400

 ** TooManyActions **
You've reached the limit on the number of actions per rule.
HTTP Status Code: 400

 ** TooManyRegistrationsForTargetId **
You've reached the limit on the number of times a target can be registered with a load balancer.
HTTP Status Code: 400

 ** TooManyTargets **
You've reached the limit on the number of targets.
HTTP Status Code: 400

 ** TooManyUniqueTargetGroupsPerLoadBalancer **
You've reached the limit on the number of unique target groups per load balancer across all listeners. If a target group is used by multiple actions for a load balancer, it is counted as only one use.
HTTP Status Code: 400

 ** UnsupportedProtocol **
The specified protocol is not supported.
HTTP Status Code: 400

## See Also
<a name="API_ModifyRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticloadbalancingv2-2015-12-01/ModifyRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticloadbalancingv2-2015-12-01/ModifyRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancingv2-2015-12-01/ModifyRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticloadbalancingv2-2015-12-01/ModifyRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancingv2-2015-12-01/ModifyRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticloadbalancingv2-2015-12-01/ModifyRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticloadbalancingv2-2015-12-01/ModifyRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticloadbalancingv2-2015-12-01/ModifyRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticloadbalancingv2-2015-12-01/ModifyRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancingv2-2015-12-01/ModifyRule)
