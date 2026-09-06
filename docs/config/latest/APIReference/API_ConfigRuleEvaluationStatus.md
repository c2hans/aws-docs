---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ConfigRuleEvaluationStatus.html
---

# ConfigRuleEvaluationStatus
<a name="API_ConfigRuleEvaluationStatus"></a>

Status information for your AWS Config Managed rules and AWS Config Custom Policy rules. The status includes information such as the last time the rule ran, the last time it failed, and the related error for the last failure.

This operation does not return status information about AWS Config Custom Lambda rules.

## Contents
<a name="API_ConfigRuleEvaluationStatus_Contents"></a>

 ** ConfigRuleArn **   <a name="config-Type-ConfigRuleEvaluationStatus-ConfigRuleArn"></a>
The Amazon Resource Name (ARN) of the AWS Config rule.
Type: String
Required: No

 ** ConfigRuleId **   <a name="config-Type-ConfigRuleEvaluationStatus-ConfigRuleId"></a>
The ID of the AWS Config rule.
Type: String
Required: No

 ** ConfigRuleName **   <a name="config-Type-ConfigRuleEvaluationStatus-ConfigRuleName"></a>
The name of the AWS Config rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[A-Za-z0-9_-]+`
Required: No

 ** FirstActivatedTime **   <a name="config-Type-ConfigRuleEvaluationStatus-FirstActivatedTime"></a>
The time that you first activated the AWS Config rule.
Type: Timestamp
Required: No

 ** FirstEvaluationStarted **   <a name="config-Type-ConfigRuleEvaluationStatus-FirstEvaluationStarted"></a>
Indicates whether AWS Config has evaluated your resources against the rule at least once.
+  `true` - AWS Config has evaluated your AWS resources against the rule at least once.
+  `false` - AWS Config has not finished evaluating your AWS resources against the rule at least once.
Type: Boolean
Required: No

 ** LastDeactivatedTime **   <a name="config-Type-ConfigRuleEvaluationStatus-LastDeactivatedTime"></a>
The time that you last turned off the AWS Config rule.
Type: Timestamp
Required: No

 ** LastDebugLogDeliveryStatus **   <a name="config-Type-ConfigRuleEvaluationStatus-LastDebugLogDeliveryStatus"></a>
The status of the last attempted delivery of a debug log for your AWS Config Custom Policy rules. Either `Successful` or `Failed`.
Type: String
Required: No

 ** LastDebugLogDeliveryStatusReason **   <a name="config-Type-ConfigRuleEvaluationStatus-LastDebugLogDeliveryStatusReason"></a>
The reason AWS Config was not able to deliver a debug log. This is for the last failed attempt to retrieve a debug log for your AWS Config Custom Policy rules.
Type: String
Required: No

 ** LastDebugLogDeliveryTime **   <a name="config-Type-ConfigRuleEvaluationStatus-LastDebugLogDeliveryTime"></a>
The time AWS Config last attempted to deliver a debug log for your AWS Config Custom Policy rules.
Type: Timestamp
Required: No

 ** LastErrorCode **   <a name="config-Type-ConfigRuleEvaluationStatus-LastErrorCode"></a>
The error code that AWS Config returned when the rule last failed.
Type: String
Required: No

 ** LastErrorMessage **   <a name="config-Type-ConfigRuleEvaluationStatus-LastErrorMessage"></a>
The error message that AWS Config returned when the rule last failed.
Type: String
Required: No

 ** LastFailedEvaluationTime **   <a name="config-Type-ConfigRuleEvaluationStatus-LastFailedEvaluationTime"></a>
The time that AWS Config last failed to evaluate your AWS resources against the rule.
Type: Timestamp
Required: No

 ** LastFailedInvocationTime **   <a name="config-Type-ConfigRuleEvaluationStatus-LastFailedInvocationTime"></a>
The time that AWS Config last failed to invoke the AWS Config rule to evaluate your AWS resources.
Type: Timestamp
Required: No

 ** LastSuccessfulEvaluationTime **   <a name="config-Type-ConfigRuleEvaluationStatus-LastSuccessfulEvaluationTime"></a>
The time that AWS Config last successfully evaluated your AWS resources against the rule.
Type: Timestamp
Required: No

 ** LastSuccessfulInvocationTime **   <a name="config-Type-ConfigRuleEvaluationStatus-LastSuccessfulInvocationTime"></a>
The time that AWS Config last successfully invoked the AWS Config rule to evaluate your AWS resources.
Type: Timestamp
Required: No

## See Also
<a name="API_ConfigRuleEvaluationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ConfigRuleEvaluationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ConfigRuleEvaluationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ConfigRuleEvaluationStatus)
