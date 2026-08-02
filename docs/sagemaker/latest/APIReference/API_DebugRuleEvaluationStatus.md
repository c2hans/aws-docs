---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DebugRuleEvaluationStatus.html
---

# DebugRuleEvaluationStatus
<a name="API_DebugRuleEvaluationStatus"></a>

Information about the status of the rule evaluation.

## Contents
<a name="API_DebugRuleEvaluationStatus_Contents"></a>

 ** LastModifiedTime **   <a name="sagemaker-Type-DebugRuleEvaluationStatus-LastModifiedTime"></a>
Timestamp when the rule evaluation status was last modified.
Type: Timestamp
Required: No

 ** RuleConfigurationName **   <a name="sagemaker-Type-DebugRuleEvaluationStatus-RuleConfigurationName"></a>
The name of the rule configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*`
Required: No

 ** RuleEvaluationJobArn **   <a name="sagemaker-Type-DebugRuleEvaluationStatus-RuleEvaluationJobArn"></a>
The Amazon Resource Name (ARN) of the rule evaluation job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:processing-job/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: No

 ** RuleEvaluationStatus **   <a name="sagemaker-Type-DebugRuleEvaluationStatus-RuleEvaluationStatus"></a>
Status of the rule evaluation.
Type: String
Valid Values: `InProgress | NoIssuesFound | IssuesFound | Error | Stopping | Stopped`
Required: No

 ** StatusDetails **   <a name="sagemaker-Type-DebugRuleEvaluationStatus-StatusDetails"></a>
Details from the rule evaluation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

## See Also
<a name="API_DebugRuleEvaluationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DebugRuleEvaluationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DebugRuleEvaluationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DebugRuleEvaluationStatus)
