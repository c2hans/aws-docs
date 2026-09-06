---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetCrawlerMetrics.html
---

# GetCrawlerMetrics
<a name="API_GetCrawlerMetrics"></a>

Retrieves metrics about specified crawlers.

## Request Syntax
<a name="API_GetCrawlerMetrics_RequestSyntax"></a>

```
{
   "CrawlerNameList": [ "{{string}}" ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_GetCrawlerMetrics_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CrawlerNameList](#API_GetCrawlerMetrics_RequestSyntax) **   <a name="Glue-GetCrawlerMetrics-request-CrawlerNameList"></a>
A list of the names of crawlers about which to retrieve metrics.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [MaxResults](#API_GetCrawlerMetrics_RequestSyntax) **   <a name="Glue-GetCrawlerMetrics-request-MaxResults"></a>
The maximum size of a list to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [NextToken](#API_GetCrawlerMetrics_RequestSyntax) **   <a name="Glue-GetCrawlerMetrics-request-NextToken"></a>
A continuation token, if this is a continuation call.
Type: String
Required: No

## Response Syntax
<a name="API_GetCrawlerMetrics_ResponseSyntax"></a>

```
{
   "CrawlerMetricsList": [
      {
         "CrawlerName": "string",
         "LastRuntimeSeconds": number,
         "MedianRuntimeSeconds": number,
         "StillEstimating": boolean,
         "TablesCreated": number,
         "TablesDeleted": number,
         "TablesUpdated": number,
         "TimeLeftSeconds": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_GetCrawlerMetrics_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CrawlerMetricsList](#API_GetCrawlerMetrics_ResponseSyntax) **   <a name="Glue-GetCrawlerMetrics-response-CrawlerMetricsList"></a>
A list of metrics for the specified crawler.
Type: Array of [CrawlerMetrics](API_CrawlerMetrics.md) objects

 ** [NextToken](#API_GetCrawlerMetrics_ResponseSyntax) **   <a name="Glue-GetCrawlerMetrics-response-NextToken"></a>
A continuation token, if the returned list does not contain the last metric available.
Type: String

## Errors
<a name="API_GetCrawlerMetrics_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_GetCrawlerMetrics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetCrawlerMetrics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetCrawlerMetrics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetCrawlerMetrics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetCrawlerMetrics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetCrawlerMetrics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetCrawlerMetrics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetCrawlerMetrics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetCrawlerMetrics)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetCrawlerMetrics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetCrawlerMetrics)
