---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeCustomMetric.html
---

# DescribeCustomMetric
<a name="API_DescribeCustomMetric"></a>

**Note**
The AWS IoT Device Defender detect feature will no longer be available to new customers starting August 31, 2026. If you would like to use the detect feature, sign up prior to August 31, 2026. To learn about alternatives to AWS IoT Device Defender detect, see [AWS IoT Device Defender detect feature availability change](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-detect-availability-change.html). There is no change to AWS IoT Device Defender audit availability.

 Gets information about a Device Defender detect custom metric.

Requires permission to access the [DescribeCustomMetric](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DescribeCustomMetric_RequestSyntax"></a>

```
GET /custom-metric/{{metricName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeCustomMetric_RequestParameters"></a>

The request uses the following URI parameters.

 ** [metricName](#API_DescribeCustomMetric_RequestSyntax) **   <a name="iot-DescribeCustomMetric-request-uri-metricName"></a>
 The name of the custom metric.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_DescribeCustomMetric_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeCustomMetric_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationDate": number,
   "displayName": "string",
   "lastModifiedDate": number,
   "metricArn": "string",
   "metricName": "string",
   "metricType": "string"
}
```

## Response Elements
<a name="API_DescribeCustomMetric_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationDate](#API_DescribeCustomMetric_ResponseSyntax) **   <a name="iot-DescribeCustomMetric-response-creationDate"></a>
 The creation date of the custom metric in milliseconds since epoch.
Type: Timestamp

 ** [displayName](#API_DescribeCustomMetric_ResponseSyntax) **   <a name="iot-DescribeCustomMetric-response-displayName"></a>
 Field represents a friendly name in the console for the custom metric; doesn't have to be unique. Don't use this name as the metric identifier in the device metric report. Can be updated.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[\p{Graph}\x20]*`

 ** [lastModifiedDate](#API_DescribeCustomMetric_ResponseSyntax) **   <a name="iot-DescribeCustomMetric-response-lastModifiedDate"></a>
 The time the custom metric was last modified in milliseconds since epoch.
Type: Timestamp

 ** [metricArn](#API_DescribeCustomMetric_ResponseSyntax) **   <a name="iot-DescribeCustomMetric-response-metricArn"></a>
 The Amazon Resource Number (ARN) of the custom metric.
Type: String

 ** [metricName](#API_DescribeCustomMetric_ResponseSyntax) **   <a name="iot-DescribeCustomMetric-response-metricName"></a>
 The name of the custom metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

 ** [metricType](#API_DescribeCustomMetric_ResponseSyntax) **   <a name="iot-DescribeCustomMetric-response-metricType"></a>
 The type of the custom metric.
The type `number` only takes a single metric value as an input, but while submitting the metrics value in the DeviceMetrics report, it must be passed as an array with a single value.
Type: String
Valid Values: `string-list | ip-address-list | number-list | number`

## Errors
<a name="API_DescribeCustomMetric_Errors"></a>

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
<a name="API_DescribeCustomMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DescribeCustomMetric)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DescribeCustomMetric)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DescribeCustomMetric)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DescribeCustomMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DescribeCustomMetric)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DescribeCustomMetric)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DescribeCustomMetric)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DescribeCustomMetric)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DescribeCustomMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DescribeCustomMetric)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
