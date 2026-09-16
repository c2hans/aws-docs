---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreateFleetMetric.html
---

# CreateFleetMetric
<a name="API_CreateFleetMetric"></a>

Creates a fleet metric.

Requires permission to access the [CreateFleetMetric](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_CreateFleetMetric_RequestSyntax"></a>

```
PUT /fleet-metric/{{metricName}} HTTP/1.1
Content-type: application/json

{
   "aggregationField": "{{string}}",
   "aggregationType": {
      "name": "{{string}}",
      "values": [ "{{string}}" ]
   },
   "description": "{{string}}",
   "indexName": "{{string}}",
   "period": {{number}},
   "queryString": "{{string}}",
   "queryVersion": "{{string}}",
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "unit": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateFleetMetric_RequestParameters"></a>

The request uses the following URI parameters.

 ** [metricName](#API_CreateFleetMetric_RequestSyntax) **   <a name="iot-CreateFleetMetric-request-uri-metricName"></a>
The name of the fleet metric to create.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_\-\.]+`
Required: Yes

## Request Body
<a name="API_CreateFleetMetric_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [aggregationField](#API_CreateFleetMetric_RequestSyntax) **   <a name="iot-CreateFleetMetric-request-aggregationField"></a>
The field to aggregate.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [aggregationType](#API_CreateFleetMetric_RequestSyntax) **   <a name="iot-CreateFleetMetric-request-aggregationType"></a>
The type of the aggregation query.
Type: [AggregationType](API_AggregationType.md) object
Required: Yes

 ** [description](#API_CreateFleetMetric_RequestSyntax) **   <a name="iot-CreateFleetMetric-request-description"></a>
The fleet metric description.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `[\p{Graph}\x20]*`
Required: No

 ** [indexName](#API_CreateFleetMetric_RequestSyntax) **   <a name="iot-CreateFleetMetric-request-indexName"></a>
The name of the index to search.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: No

 ** [period](#API_CreateFleetMetric_RequestSyntax) **   <a name="iot-CreateFleetMetric-request-period"></a>
The time in seconds between fleet metric emissions. Range [60(1 min), 86400(1 day)] and must be multiple of 60.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 86400.
Required: Yes

 ** [queryString](#API_CreateFleetMetric_RequestSyntax) **   <a name="iot-CreateFleetMetric-request-queryString"></a>
The search query string.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [queryVersion](#API_CreateFleetMetric_RequestSyntax) **   <a name="iot-CreateFleetMetric-request-queryVersion"></a>
The query version.
Type: String
Required: No

 ** [tags](#API_CreateFleetMetric_RequestSyntax) **   <a name="iot-CreateFleetMetric-request-tags"></a>
Metadata, which can be used to manage the fleet metric.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [unit](#API_CreateFleetMetric_RequestSyntax) **   <a name="iot-CreateFleetMetric-request-unit"></a>
Used to support unit transformation such as milliseconds to seconds. The unit must be supported by [CW metric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html). Default to null.
Type: String
Valid Values: `Seconds | Microseconds | Milliseconds | Bytes | Kilobytes | Megabytes | Gigabytes | Terabytes | Bits | Kilobits | Megabits | Gigabits | Terabits | Percent | Count | Bytes/Second | Kilobytes/Second | Megabytes/Second | Gigabytes/Second | Terabytes/Second | Bits/Second | Kilobits/Second | Megabits/Second | Gigabits/Second | Terabits/Second | Count/Second | None`
Required: No

## Response Syntax
<a name="API_CreateFleetMetric_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "metricArn": "string",
   "metricName": "string"
}
```

## Response Elements
<a name="API_CreateFleetMetric_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [metricArn](#API_CreateFleetMetric_ResponseSyntax) **   <a name="iot-CreateFleetMetric-response-metricArn"></a>
The Amazon Resource Name (ARN) of the new fleet metric.
Type: String

 ** [metricName](#API_CreateFleetMetric_ResponseSyntax) **   <a name="iot-CreateFleetMetric-response-metricName"></a>
The name of the fleet metric to create.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_\-\.]+`

## Errors
<a name="API_CreateFleetMetric_Errors"></a>

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

 ** LimitExceededException **
A limit has been exceeded.
 ** message **
The message for the exception.
HTTP Status Code: 410

 ** ResourceAlreadyExistsException **
The resource already exists.
 ** message **
The message for the exception.
 ** resourceArn **
The ARN of the resource that caused the exception.
 ** resourceId **
The ID of the resource that caused the exception.
HTTP Status Code: 409

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
<a name="API_CreateFleetMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreateFleetMetric)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreateFleetMetric)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreateFleetMetric)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreateFleetMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreateFleetMetric)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreateFleetMetric)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreateFleetMetric)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreateFleetMetric)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreateFleetMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreateFleetMetric)
