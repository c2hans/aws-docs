---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_StartOTelEnrichment.html
---

# StartOTelEnrichment
<a name="API_StartOTelEnrichment"></a>

Enables enrichment and PromQL access for CloudWatch vended metrics for [supported AWS resources](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/UsingResourceTagsForTelemetry.html) in the account. Once enabled, metrics that contain a resource identifier dimension (for example, EC2 `CPUUtilization` with an `InstanceId` dimension) are enriched with resource ARN and resource tag labels and become queryable using PromQL.

Before calling this operation, you must enable resource tags on telemetry for your account. For more information, see [Enable resource tags on telemetry](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/EnableResourceTagsOnTelemetry.html).

Optionally, `IncludeFilters` and `ExcludeFilters` limit enrichment to a subset of the account's metrics. These filters are stored only when this operation starts enrichment. Calling `StartOTelEnrichment` for an account where enrichment is already running has no effect and does not modify the filters that are applied. To change them, use [UpdateOTelEnrichment](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UpdateOTelEnrichment.html).

## Request Parameters
<a name="API_StartOTelEnrichment_RequestParameters"></a>

 ** ExcludeFilters **
The metric namespaces, and the metric names, to leave unenriched. If this parameter is omitted, nothing is excluded.
Amazon CloudWatch applies `ExcludeFilters` after `IncludeFilters`, so a metric that both parameters match is not enriched.
A maximum of 100 filters is allowed across `IncludeFilters` and `ExcludeFilters` combined.
Type: Array of [OTelEnrichmentMetricSelector](API_OTelEnrichmentMetricSelector.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** IncludeFilters **
The metric namespaces, and the metric names, to enrich. If this parameter is omitted, every namespace that Amazon CloudWatch supports for enrichment is in scope.
A maximum of 100 filters is allowed across `IncludeFilters` and `ExcludeFilters` combined.
Type: Array of [OTelEnrichmentMetricSelector](API_OTelEnrichmentMetricSelector.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

## Response Elements
<a name="API_StartOTelEnrichment_ResponseElements"></a>

The following elements are returned by the service.

 ** CreatedAt **
The date and time that enrichment started for the account.
Type: Timestamp

 ** ExcludeFilters **
The exclude filters that are stored for the account.
Type: Array of [OTelEnrichmentMetricSelector](API_OTelEnrichmentMetricSelector.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** IncludeFilters **
The include filters that are stored for the account.
Type: Array of [OTelEnrichmentMetricSelector](API_OTelEnrichmentMetricSelector.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** UpdatedAt **
The date and time that the enrichment configuration for the account was last stored.
Type: Timestamp

## Errors
<a name="API_StartOTelEnrichment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ValidationError **
The request failed validation. One or more input parameters do not satisfy the constraints that the operation requires.
HTTP Status Code: 400

## See Also
<a name="API_StartOTelEnrichment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/StartOTelEnrichment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/StartOTelEnrichment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/StartOTelEnrichment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/StartOTelEnrichment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/StartOTelEnrichment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/StartOTelEnrichment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/StartOTelEnrichment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/StartOTelEnrichment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/StartOTelEnrichment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/StartOTelEnrichment)
