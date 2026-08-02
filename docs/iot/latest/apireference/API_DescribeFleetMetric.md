---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeFleetMetric.html
---

# DescribeFleetMetric
<a name="API_DescribeFleetMetric"></a>

Gets information about the specified fleet metric.

Requires permission to access the [DescribeFleetMetric](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DescribeFleetMetric_RequestSyntax"></a>

```
GET /fleet-metric/{{metricName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeFleetMetric_RequestParameters"></a>

The request uses the following URI parameters.

 ** [metricName](#API_DescribeFleetMetric_RequestSyntax) **   <a name="iot-DescribeFleetMetric-request-uri-metricName"></a>
The name of the fleet metric to describe.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_\-\.]+`
Required: Yes

## Request Body
<a name="API_DescribeFleetMetric_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeFleetMetric_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "aggregationField": "string",
   "aggregationType": {
      "name": "string",
      "values": [ "string" ]
   },
   "creationDate": number,
   "description": "string",
   "indexName": "string",
   "lastModifiedDate": number,
   "metricArn": "string",
   "metricName": "string",
   "period": number,
   "queryString": "string",
   "queryVersion": "string",
   "unit": "string",
   "version": number
}
```

## Response Elements
<a name="API_DescribeFleetMetric_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [aggregationField](#API_DescribeFleetMetric_ResponseSyntax) **   <a name="iot-DescribeFleetMetric-response-aggregationField"></a>
The field to aggregate.
Type: String
Length Constraints: Minimum length of 1.

 ** [aggregationType](#API_DescribeFleetMetric_ResponseSyntax) **   <a name="iot-DescribeFleetMetric-response-aggregationType"></a>
The type of the aggregation query.
Type: [AggregationType](API_AggregationType.md) object

 ** [creationDate](#API_DescribeFleetMetric_ResponseSyntax) **   <a name="iot-DescribeFleetMetric-response-creationDate"></a>
The date when the fleet metric is created.
Type: Timestamp

 ** [description](#API_DescribeFleetMetric_ResponseSyntax) **   <a name="iot-DescribeFleetMetric-response-description"></a>
The fleet metric description.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `[\p{Graph}\x20]*`

 ** [indexName](#API_DescribeFleetMetric_ResponseSyntax) **   <a name="iot-DescribeFleetMetric-response-indexName"></a>
The name of the index to search.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

 ** [lastModifiedDate](#API_DescribeFleetMetric_ResponseSyntax) **   <a name="iot-DescribeFleetMetric-response-lastModifiedDate"></a>
The date when the fleet metric is last modified.
Type: Timestamp

 ** [metricArn](#API_DescribeFleetMetric_ResponseSyntax) **   <a name="iot-DescribeFleetMetric-response-metricArn"></a>
The ARN of the fleet metric to describe.
Type: String

 ** [metricName](#API_DescribeFleetMetric_ResponseSyntax) **   <a name="iot-DescribeFleetMetric-response-metricName"></a>
The name of the fleet metric to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_\-\.]+`

 ** [period](#API_DescribeFleetMetric_ResponseSyntax) **   <a name="iot-DescribeFleetMetric-response-period"></a>
The time in seconds between fleet metric emissions. Range [60(1 min), 86400(1 day)] and must be multiple of 60.
Type: Integer
Valid Range: Minimum value of 60. Maximum value of 86400.

 ** [queryString](#API_DescribeFleetMetric_ResponseSyntax) **   <a name="iot-DescribeFleetMetric-response-queryString"></a>
The search query string.
Type: String
Length Constraints: Minimum length of 1.

 ** [queryVersion](#API_DescribeFleetMetric_ResponseSyntax) **   <a name="iot-DescribeFleetMetric-response-queryVersion"></a>
The query version.
Type: String

 ** [unit](#API_DescribeFleetMetric_ResponseSyntax) **   <a name="iot-DescribeFleetMetric-response-unit"></a>
Used to support unit transformation such as milliseconds to seconds. The unit must be supported by [CW metric](https://docs.aws.amazon.com/AmazonCloudWatch/latest/APIReference/API_MetricDatum.html).
Type: String
Valid Values: `Seconds | Microseconds | Milliseconds | Bytes | Kilobytes | Megabytes | Gigabytes | Terabytes | Bits | Kilobits | Megabits | Gigabits | Terabits | Percent | Count | Bytes/Second | Kilobytes/Second | Megabytes/Second | Gigabytes/Second | Terabytes/Second | Bits/Second | Kilobits/Second | Megabits/Second | Gigabits/Second | Terabits/Second | Count/Second | None`

 ** [version](#API_DescribeFleetMetric_ResponseSyntax) **   <a name="iot-DescribeFleetMetric-response-version"></a>
The version of the fleet metric.
Type: Long

## Errors
<a name="API_DescribeFleetMetric_Errors"></a>

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
<a name="API_DescribeFleetMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DescribeFleetMetric)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DescribeFleetMetric)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DescribeFleetMetric)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DescribeFleetMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DescribeFleetMetric)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DescribeFleetMetric)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DescribeFleetMetric)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DescribeFleetMetric)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DescribeFleetMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DescribeFleetMetric)
