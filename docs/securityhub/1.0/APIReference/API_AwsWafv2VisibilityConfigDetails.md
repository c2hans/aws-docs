---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsWafv2VisibilityConfigDetails.html
---

# AwsWafv2VisibilityConfigDetails
<a name="API_AwsWafv2VisibilityConfigDetails"></a>

 Defines and enables Amazon CloudWatch metrics and web request sample collection.

## Contents
<a name="API_AwsWafv2VisibilityConfigDetails_Contents"></a>

 ** CloudWatchMetricsEnabled **   <a name="securityhub-Type-AwsWafv2VisibilityConfigDetails-CloudWatchMetricsEnabled"></a>
 A boolean indicating whether the associated resource sends metrics to Amazon CloudWatch. For the list of available metrics, see [AWS WAF metrics and dimensions](https://docs.aws.amazon.com/waf/latest/developerguide/monitoring-cloudwatch.html#waf-metrics) in the * AWS WAF Developer Guide*.
Type: Boolean
Required: No

 ** MetricName **   <a name="securityhub-Type-AwsWafv2VisibilityConfigDetails-MetricName"></a>
 A name of the Amazon CloudWatch metric.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SampledRequestsEnabled **   <a name="securityhub-Type-AwsWafv2VisibilityConfigDetails-SampledRequestsEnabled"></a>
 A boolean indicating whether AWS WAF should store a sampling of the web requests that match the rules. You can view the sampled requests through the AWS WAF console.
Type: Boolean
Required: No

## See Also
<a name="API_AwsWafv2VisibilityConfigDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsWafv2VisibilityConfigDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsWafv2VisibilityConfigDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsWafv2VisibilityConfigDetails)
