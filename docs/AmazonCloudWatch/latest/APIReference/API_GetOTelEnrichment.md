---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_GetOTelEnrichment.html
---

# GetOTelEnrichment
<a name="API_GetOTelEnrichment"></a>

Returns the current status of vended metric enrichment for the account, including whether CloudWatch vended metrics are enriched with resource ARN and resource tag labels and queryable using PromQL. For the list of supported resources, see [Supported AWS infrastructure metrics](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/UsingResourceTagsForTelemetry.html).

## Response Syntax
<a name="API_GetOTelEnrichment_ResponseSyntax"></a>

```
{
   "CreatedAt": number,
   "ExcludeFilters": [
      {
         "MetricNames": [ "string" ],
         "Namespace": "string"
      }
   ],
   "IncludeFilters": [
      {
         "MetricNames": [ "string" ],
         "Namespace": "string"
      }
   ],
   "Status": "string",
   "UpdatedAt": number
}
```

## Response Elements
<a name="API_GetOTelEnrichment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedAt](#API_GetOTelEnrichment_ResponseSyntax) **   <a name="ACW-GetOTelEnrichment-response-CreatedAt"></a>
The date and time that enrichment started for the account. This parameter is omitted when enrichment is stopped.
Type: Timestamp

 ** [ExcludeFilters](#API_GetOTelEnrichment_ResponseSyntax) **   <a name="ACW-GetOTelEnrichment-response-ExcludeFilters"></a>
The metric namespaces, and the metric names, that are left unenriched. This parameter is omitted when enrichment is stopped, and when enrichment is running with no exclude filters, which means that nothing is excluded.
Type: Array of [OTelEnrichmentMetricSelector](API_OTelEnrichmentMetricSelector.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [IncludeFilters](#API_GetOTelEnrichment_ResponseSyntax) **   <a name="ACW-GetOTelEnrichment-response-IncludeFilters"></a>
The metric namespaces, and the metric names, that are enriched. This parameter is omitted when enrichment is stopped, and when enrichment is running with no include filters, which means that every supported namespace is in scope.
Type: Array of [OTelEnrichmentMetricSelector](API_OTelEnrichmentMetricSelector.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [Status](#API_GetOTelEnrichment_ResponseSyntax) **   <a name="ACW-GetOTelEnrichment-response-Status"></a>
The status of OTel enrichment for the account. Valid values are `Running` (enrichment is enabled) and `Stopped` (enrichment is disabled).
Type: String
Valid Values: `Running | Stopped`

 ** [UpdatedAt](#API_GetOTelEnrichment_ResponseSyntax) **   <a name="ACW-GetOTelEnrichment-response-UpdatedAt"></a>
The date and time that the enrichment configuration for the account was last stored.
Type: Timestamp

## Errors
<a name="API_GetOTelEnrichment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetOTelEnrichment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/monitoring-2010-08-01/GetOTelEnrichment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/monitoring-2010-08-01/GetOTelEnrichment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/monitoring-2010-08-01/GetOTelEnrichment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/monitoring-2010-08-01/GetOTelEnrichment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/monitoring-2010-08-01/GetOTelEnrichment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/monitoring-2010-08-01/GetOTelEnrichment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/monitoring-2010-08-01/GetOTelEnrichment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/monitoring-2010-08-01/GetOTelEnrichment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/monitoring-2010-08-01/GetOTelEnrichment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/monitoring-2010-08-01/GetOTelEnrichment)
