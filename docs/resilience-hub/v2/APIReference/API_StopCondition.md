---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_StopCondition.html
---

# StopCondition
<a name="API_StopCondition"></a>

A CloudWatch alarm that automatically stops a test run if it breaches its threshold.

## Contents
<a name="API_StopCondition_Contents"></a>

 ** source **   <a name="ngresiliencehub-Type-StopCondition-source"></a>
The source of the stop condition.
Type: String
Valid Values: `aws:cloudwatch:alarm | none`
Required: Yes

 ** value **   <a name="ngresiliencehub-Type-StopCondition-value"></a>
The value of the stop condition, such as the ARN of the CloudWatch alarm.
Type: String
Required: Yes

## See Also
<a name="API_StopCondition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/StopCondition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/StopCondition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/StopCondition)
