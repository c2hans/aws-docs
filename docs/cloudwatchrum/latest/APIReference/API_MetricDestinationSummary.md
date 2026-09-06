---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_MetricDestinationSummary.html
---

# MetricDestinationSummary
<a name="API_MetricDestinationSummary"></a>

A structure that displays information about one destination that CloudWatch RUM sends extended metrics to.

## Contents
<a name="API_MetricDestinationSummary_Contents"></a>

 ** Destination **   <a name="cloudwatchrum-Type-MetricDestinationSummary-Destination"></a>
Specifies whether the destination is `CloudWatch` or `Evidently`.
Type: String
Valid Values: `CloudWatch | Evidently`
Required: No

 ** DestinationArn **   <a name="cloudwatchrum-Type-MetricDestinationSummary-DestinationArn"></a>
If the destination is `Evidently`, this specifies the ARN of the Evidently experiment that receives the metrics.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `.*arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`
Required: No

 ** IamRoleArn **   <a name="cloudwatchrum-Type-MetricDestinationSummary-IamRoleArn"></a>
This field appears only when the destination is `Evidently`. It specifies the ARN of the IAM role that is used to write to the Evidently experiment that receives the metrics.
Type: String
Pattern: `.*arn:[^:]*:[^:]*:[^:]*:[^:]*:.*`
Required: No

## See Also
<a name="API_MetricDestinationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/MetricDestinationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/MetricDestinationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/MetricDestinationSummary)
