---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingTargets.html
---

# GetSamplingTargets
<a name="API_GetSamplingTargets"></a>

Requests a sampling quota for rules that the service is using to sample requests.

## Request Syntax
<a name="API_GetSamplingTargets_RequestSyntax"></a>

```
POST /SamplingTargets HTTP/1.1
Content-type: application/json

{
   "SamplingBoostStatisticsDocuments": [
      {
         "AnomalyCount": {{number}},
         "RuleName": "{{string}}",
         "SampledAnomalyCount": {{number}},
         "ServiceName": "{{string}}",
         "Timestamp": {{number}},
         "TotalCount": {{number}}
      }
   ],
   "SamplingStatisticsDocuments": [
      {
         "BorrowCount": {{number}},
         "ClientID": "{{string}}",
         "RequestCount": {{number}},
         "RuleName": "{{string}}",
         "SampledCount": {{number}},
         "Timestamp": {{number}}
      }
   ]
}
```

## URI Request Parameters
<a name="API_GetSamplingTargets_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetSamplingTargets_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [SamplingBoostStatisticsDocuments](#API_GetSamplingTargets_RequestSyntax) **   <a name="xray-GetSamplingTargets-request-SamplingBoostStatisticsDocuments"></a>
Information about rules that the service is using to boost sampling rate.
Type: Array of [SamplingBoostStatisticsDocument](API_SamplingBoostStatisticsDocument.md) objects
Array Members: Maximum number of 25 items.
Required: No

 ** [SamplingStatisticsDocuments](#API_GetSamplingTargets_RequestSyntax) **   <a name="xray-GetSamplingTargets-request-SamplingStatisticsDocuments"></a>
Information about rules that the service is using to sample requests.
Type: Array of [SamplingStatisticsDocument](API_SamplingStatisticsDocument.md) objects
Array Members: Maximum number of 25 items.
Required: Yes

## Response Syntax
<a name="API_GetSamplingTargets_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "LastRuleModification": number,
   "SamplingTargetDocuments": [
      {
         "FixedRate": number,
         "Interval": number,
         "ReservoirQuota": number,
         "ReservoirQuotaTTL": number,
         "RuleName": "string",
         "SamplingBoost": {
            "BoostRate": number,
            "BoostRateTTL": number
         }
      }
   ],
   "UnprocessedBoostStatistics": [
      {
         "ErrorCode": "string",
         "Message": "string",
         "RuleName": "string"
      }
   ],
   "UnprocessedStatistics": [
      {
         "ErrorCode": "string",
         "Message": "string",
         "RuleName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetSamplingTargets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LastRuleModification](#API_GetSamplingTargets_ResponseSyntax) **   <a name="xray-GetSamplingTargets-response-LastRuleModification"></a>
The last time a user changed the sampling rule configuration, in Unix time seconds. If the sampling rule configuration changed since the service last retrieved it, the service should call [GetSamplingRules](https://docs.aws.amazon.com/xray/latest/api/API_GetSamplingRules.html) to get the latest version.
Type: Timestamp

 ** [SamplingTargetDocuments](#API_GetSamplingTargets_ResponseSyntax) **   <a name="xray-GetSamplingTargets-response-SamplingTargetDocuments"></a>
Updated rules that the service should use to sample requests.
Type: Array of [SamplingTargetDocument](API_SamplingTargetDocument.md) objects

 ** [UnprocessedBoostStatistics](#API_GetSamplingTargets_ResponseSyntax) **   <a name="xray-GetSamplingTargets-response-UnprocessedBoostStatistics"></a>
Information about [SamplingBoostStatisticsDocument](https://docs.aws.amazon.com/xray/latest/api/API_SamplingBoostStatisticsDocument.html) that X-Ray could not process.
Type: Array of [UnprocessedStatistics](API_UnprocessedStatistics.md) objects

 ** [UnprocessedStatistics](#API_GetSamplingTargets_ResponseSyntax) **   <a name="xray-GetSamplingTargets-response-UnprocessedStatistics"></a>
Information about [SamplingStatisticsDocument](https://docs.aws.amazon.com/xray/latest/api/API_SamplingStatisticsDocument.html) that X-Ray could not process.
Type: Array of [UnprocessedStatistics](API_UnprocessedStatistics.md) objects

## Errors
<a name="API_GetSamplingTargets_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidRequestException **
The request is missing required parameters or has invalid parameters.
HTTP Status Code: 400

 ** ThrottledException **
The request exceeds the maximum number of requests per second.
HTTP Status Code: 429

## See Also
<a name="API_GetSamplingTargets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/xray-2016-04-12/GetSamplingTargets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/xray-2016-04-12/GetSamplingTargets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/GetSamplingTargets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/xray-2016-04-12/GetSamplingTargets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/GetSamplingTargets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/xray-2016-04-12/GetSamplingTargets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/xray-2016-04-12/GetSamplingTargets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/xray-2016-04-12/GetSamplingTargets)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/xray-2016-04-12/GetSamplingTargets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/GetSamplingTargets)
