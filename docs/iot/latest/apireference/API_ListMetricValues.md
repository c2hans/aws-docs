---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ListMetricValues.html
---

# ListMetricValues
<a name="API_ListMetricValues"></a>

Lists the values reported for an AWS IoT Device Defender metric (device-side metric, cloud-side metric, or custom metric) by the given thing during the specified time period.

## Request Syntax
<a name="API_ListMetricValues_RequestSyntax"></a>

```
GET /metric-values?dimensionName={{dimensionName}}&dimensionValueOperator={{dimensionValueOperator}}&endTime={{endTime}}&maxResults={{maxResults}}&metricName={{metricName}}&nextToken={{nextToken}}&startTime={{startTime}}&thingName={{thingName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListMetricValues_RequestParameters"></a>

The request uses the following URI parameters.

 ** [dimensionName](#API_ListMetricValues_RequestSyntax) **   <a name="iot-ListMetricValues-request-uri-dimensionName"></a>
The dimension name.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

 ** [dimensionValueOperator](#API_ListMetricValues_RequestSyntax) **   <a name="iot-ListMetricValues-request-uri-dimensionValueOperator"></a>
The dimension value operator.
Valid Values: `IN | NOT_IN`

 ** [endTime](#API_ListMetricValues_RequestSyntax) **   <a name="iot-ListMetricValues-request-uri-endTime"></a>
The end of the time period for which metric values are returned.
Required: Yes

 ** [maxResults](#API_ListMetricValues_RequestSyntax) **   <a name="iot-ListMetricValues-request-uri-maxResults"></a>
The maximum number of results to return at one time.
Valid Range: Minimum value of 1. Maximum value of 250.

 ** [metricName](#API_ListMetricValues_RequestSyntax) **   <a name="iot-ListMetricValues-request-uri-metricName"></a>
The name of the security profile metric for which values are returned.
Required: Yes

 ** [nextToken](#API_ListMetricValues_RequestSyntax) **   <a name="iot-ListMetricValues-request-uri-nextToken"></a>
The token for the next set of results.

 ** [startTime](#API_ListMetricValues_RequestSyntax) **   <a name="iot-ListMetricValues-request-uri-startTime"></a>
The start of the time period for which metric values are returned.
Required: Yes

 ** [thingName](#API_ListMetricValues_RequestSyntax) **   <a name="iot-ListMetricValues-request-uri-thingName"></a>
The name of the thing for which security profile metric values are returned.
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

## Request Body
<a name="API_ListMetricValues_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListMetricValues_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "metricDatumList": [
      {
         "timestamp": number,
         "value": {
            "cidrs": [ "string" ],
            "count": number,
            "number": number,
            "numbers": [ number ],
            "ports": [ number ],
            "strings": [ "string" ]
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListMetricValues_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [metricDatumList](#API_ListMetricValues_ResponseSyntax) **   <a name="iot-ListMetricValues-response-metricDatumList"></a>
The data the thing reports for the metric during the specified time period.
Type: Array of [MetricDatum](API_MetricDatum.md) objects

 ** [nextToken](#API_ListMetricValues_ResponseSyntax) **   <a name="iot-ListMetricValues-response-nextToken"></a>
A token that can be used to retrieve the next set of results, or `null` if there are no additional results.
Type: String

## Errors
<a name="API_ListMetricValues_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

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

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListMetricValues_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/ListMetricValues)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/ListMetricValues)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ListMetricValues)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/ListMetricValues)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ListMetricValues)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/ListMetricValues)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/ListMetricValues)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/ListMetricValues)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/ListMetricValues)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ListMetricValues)
