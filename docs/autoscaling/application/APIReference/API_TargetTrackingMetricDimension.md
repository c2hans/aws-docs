---
source_url: https://docs.aws.amazon.com/autoscaling/application/APIReference/API_TargetTrackingMetricDimension.html
---

# TargetTrackingMetricDimension
<a name="API_TargetTrackingMetricDimension"></a>

Describes the dimension of a metric.

## Contents
<a name="API_TargetTrackingMetricDimension_Contents"></a>

 ** Name **   <a name="autoscaling-Type-TargetTrackingMetricDimension-Name"></a>
The name of the dimension.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

 ** Value **   <a name="autoscaling-Type-TargetTrackingMetricDimension-Value"></a>
The value of the dimension.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: Yes

## See Also
<a name="API_TargetTrackingMetricDimension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-autoscaling-2016-02-06/TargetTrackingMetricDimension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-autoscaling-2016-02-06/TargetTrackingMetricDimension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-autoscaling-2016-02-06/TargetTrackingMetricDimension)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Auto Scaling. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query autoscaling` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
