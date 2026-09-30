---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_UpdateOTelEnrichment.html
---

# UpdateOTelEnrichment
<a name="API_UpdateOTelEnrichment"></a>

Replaces the filters that determine which CloudWatch vended metrics are enriched with resource ARN and resource tag labels for the account. Enrichment must already be running for the account. If it is not, this operation returns a `ResourceNotFoundException`. To start enrichment, use [StartOTelEnrichment](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_StartOTelEnrichment.html).

The filters in the request completely replace the stored filters; they are not merged with them. `IncludeFilters` and `ExcludeFilters` are replaced as a pair, so a request that specifies only `IncludeFilters` also clears the stored `ExcludeFilters`, and a request that specifies neither clears both.

## Request Parameters
<a name="API_UpdateOTelEnrichment_RequestParameters"></a>

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
<a name="API_UpdateOTelEnrichment_ResponseElements"></a>

The following elements are returned by the service.

 ** CreatedAt **
The date and time that enrichment started for the account.
Type: Timestamp

 ** ExcludeFilters **
The exclude filters that are stored for the account after the replacement. This parameter is omitted when the request cleared the exclude filters, which means that nothing is excluded.
Type: Array of [OTelEnrichmentMetricSelector](API_OTelEnrichmentMetricSelector.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** IncludeFilters **
The include filters that are stored for the account after the replacement. This parameter is omitted when the request cleared the include filters, which means that every supported namespace is in scope.
Type: Array of [OTelEnrichmentMetricSelector](API_OTelEnrichmentMetricSelector.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** UpdatedAt **
The date and time that the enrichment configuration for the account was last stored.
Type: Timestamp

## Errors
<a name="API_UpdateOTelEnrichment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFoundException **
The named resource does not exist.
HTTP Status Code: 404

 ** ValidationError **
The request failed validation. One or more input parameters do not satisfy the constraints that the operation requires.
HTTP Status Code: 400

## See Also
<a name="API_UpdateOTelEnrichment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/UpdateOTelEnrichment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/UpdateOTelEnrichment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/UpdateOTelEnrichment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/UpdateOTelEnrichment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/UpdateOTelEnrichment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/UpdateOTelEnrichment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/UpdateOTelEnrichment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/UpdateOTelEnrichment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/UpdateOTelEnrichment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/UpdateOTelEnrichment)
