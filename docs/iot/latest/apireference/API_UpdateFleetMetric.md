---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateFleetMetric.html
---

# UpdateFleetMetric
<a name="API_UpdateFleetMetric"></a>

Updates the data for a fleet metric.

Requires permission to access the [UpdateFleetMetric](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_UpdateFleetMetric_RequestSyntax"></a>

```
PATCH /fleet-metric/{{metricName}} HTTP/1.1
Content-type: application/json

{
   "aggregationField": "{{string}}",
   "aggregationType": {
      "name": "{{string}}",
      "values": [ "{{string}}" ]
   },
   "description": "{{string}}",
   "expectedVersion": {{number}},
   "indexName": "{{string}}",
   "period": {{number}},
   "queryString": "{{string}}",
   "queryVersion": "{{string}}",
   "unit": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateFleetMetric_RequestParameters"></a>

The request uses the following URI parameters.

 ** [metricName](#API_UpdateFleetMetric_RequestSyntax) **   <a name="iot-UpdateFleetMetric-request-uri-metricName"></a>
The name of the fleet metric to update.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_\-\.]+`
Required: Yes

## Request Body
<a name="API_UpdateFleetMetric_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [aggregationField](#API_UpdateFleetMetric_RequestSyntax) **   <a name="iot-UpdateFleetMetric-request-aggregationField"></a>
The field to aggregate.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [aggregationType](#API_UpdateFleetMetric_RequestSyntax) **   <a name="iot-UpdateFleetMetric-request-aggregationType"></a>
The type of the aggregation query.
Type: [AggregationType](API_AggregationType.md) object
Required: No

 ** [description](#API_UpdateFleetMetric_RequestSyntax) **   <a name="iot-UpdateFleetMetric-request-description"></a>
The description of the fleet metric.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `[\p{Graph}\x20]*`
Required: No

 ** [expectedVersion](#API_UpdateFleetMetric_RequestSyntax) **   <a name="iot-UpdateFleetMetric-request-expectedVersion"></a>
The expected version of the fleet metric record in the registry.
Type: Long
Required: No

 ** [indexName](#API_UpdateFleetMetric_RequestSyntax) **   <a name="iot-UpdateFleetMetric-request-indexName"></a>
The name of the index to search.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

 ** [period](#API_UpdateFleetMetric_RequestSyntax) **   <a name="iot-UpdateFleetMetric-request-period"></a>
The time in seconds between fleet metric emissions. Range [60(1 min), 86400(1 day)] and must be multiple of 60.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 86400.
Required: No

 ** [queryString](#API_UpdateFleetMetric_RequestSyntax) **   <a name="iot-UpdateFleetMetric-request-queryString"></a>
The search query string.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [queryVersion](#API_UpdateFleetMetric_RequestSyntax) **   <a name="iot-UpdateFleetMetric-request-queryVersion"></a>
The version of the query.
Type: String
Required: No

 ** [unit](#API_UpdateFleetMetric_RequestSyntax) **   <a name="iot-UpdateFleetMetric-request-unit"></a>
Used to support unit transformation such as milliseconds to seconds. The unit must be supported by [CW metric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html).
Type: String
Valid Values: `Seconds | Microseconds | Milliseconds | Bytes | Kilobytes | Megabytes | Gigabytes | Terabytes | Bits | Kilobits | Megabits | Gigabits | Terabits | Percent | Count | Bytes/Second | Kilobytes/Second | Megabytes/Second | Gigabytes/Second | Terabytes/Second | Bits/Second | Kilobits/Second | Megabits/Second | Gigabits/Second | Terabits/Second | Count/Second | None`
Required: No

## Response Syntax
<a name="API_UpdateFleetMetric_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateFleetMetric_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateFleetMetric_Errors"></a>

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

 ** VersionConflictException **
An exception thrown when the version of an entity specified with the `expectedVersion` parameter does not match the latest version in the system.
 ** message **
The message for the exception.
HTTP Status Code: 409

## See Also
<a name="API_UpdateFleetMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/UpdateFleetMetric)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/UpdateFleetMetric)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/UpdateFleetMetric)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/UpdateFleetMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/UpdateFleetMetric)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/UpdateFleetMetric)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/UpdateFleetMetric)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/UpdateFleetMetric)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/UpdateFleetMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/UpdateFleetMetric)
