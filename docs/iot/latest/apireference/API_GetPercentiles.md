---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_GetPercentiles.html
---

# GetPercentiles
<a name="API_GetPercentiles"></a>

Groups the aggregated values that match the query into percentile groupings. The default percentile groupings are: 1,5,25,50,75,95,99, although you can specify your own when you call `GetPercentiles`. This function returns a value for each percentile group specified (or the default percentile groupings). The percentile group "1" contains the aggregated field value that occurs in approximately one percent of the values that match the query. The percentile group "5" contains the aggregated field value that occurs in approximately five percent of the values that match the query, and so on. The result is an approximation, the more values that match the query, the more accurate the percentile values.

Requires permission to access the [GetPercentiles](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_GetPercentiles_RequestSyntax"></a>

```
POST /indices/percentiles HTTP/1.1
Content-type: application/json

{
   "aggregationField": "{{string}}",
   "indexName": "{{string}}",
   "percents": [ {{number}} ],
   "queryString": "{{string}}",
   "queryVersion": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetPercentiles_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetPercentiles_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [aggregationField](#API_GetPercentiles_RequestSyntax) **   <a name="iot-GetPercentiles-request-aggregationField"></a>
The field to aggregate.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [indexName](#API_GetPercentiles_RequestSyntax) **   <a name="iot-GetPercentiles-request-indexName"></a>
The name of the index to search.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

 ** [percents](#API_GetPercentiles_RequestSyntax) **   <a name="iot-GetPercentiles-request-percents"></a>
The percentile groups returned.
Type: Array of doubles
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [queryString](#API_GetPercentiles_RequestSyntax) **   <a name="iot-GetPercentiles-request-queryString"></a>
The search query string.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [queryVersion](#API_GetPercentiles_RequestSyntax) **   <a name="iot-GetPercentiles-request-queryVersion"></a>
The query version.
Type: String
Required: No

## Response Syntax
<a name="API_GetPercentiles_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "percentiles": [
      {
         "percent": number,
         "value": number
      }
   ]
}
```

## Response Elements
<a name="API_GetPercentiles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [percentiles](#API_GetPercentiles_ResponseSyntax) **   <a name="iot-GetPercentiles-response-percentiles"></a>
The percentile values of the aggregated fields.
Type: Array of [PercentPair](API_PercentPair.md) objects

## Errors
<a name="API_GetPercentiles_Errors"></a>

 ** IndexNotReadyException **
The index is not ready.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidAggregationException **
The aggregation is invalid.
HTTP Status Code: 400

 ** InvalidQueryException **
The query is invalid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_GetPercentiles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/GetPercentiles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/GetPercentiles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/GetPercentiles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/GetPercentiles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/GetPercentiles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/GetPercentiles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/GetPercentiles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/GetPercentiles)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/GetPercentiles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/GetPercentiles)
