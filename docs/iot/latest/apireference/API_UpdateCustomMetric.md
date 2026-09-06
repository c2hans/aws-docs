---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateCustomMetric.html
---

# UpdateCustomMetric
<a name="API_UpdateCustomMetric"></a>

**Note**
The AWS IoT Device Defender detect feature will no longer be available to new customers starting August 31, 2026. If you would like to use the detect feature, sign up prior to August 31, 2026. To learn about alternatives to AWS IoT Device Defender detect, see [AWS IoT Device Defender detect feature availability change](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-detect-availability-change.html). There is no change to AWS IoT Device Defender audit availability.

Updates a Device Defender detect custom metric.

Requires permission to access the [UpdateCustomMetric](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_UpdateCustomMetric_RequestSyntax"></a>

```
PATCH /custom-metric/{{metricName}} HTTP/1.1
Content-type: application/json

{
   "displayName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateCustomMetric_RequestParameters"></a>

The request uses the following URI parameters.

 ** [metricName](#API_UpdateCustomMetric_RequestSyntax) **   <a name="iot-UpdateCustomMetric-request-uri-metricName"></a>
 The name of the custom metric. Cannot be updated.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_UpdateCustomMetric_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [displayName](#API_UpdateCustomMetric_RequestSyntax) **   <a name="iot-UpdateCustomMetric-request-displayName"></a>
 Field represents a friendly name in the console for the custom metric, it doesn't have to be unique. Don't use this name as the metric identifier in the device metric report. Can be updated.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[\p{Graph}\x20]*`
Required: Yes

## Response Syntax
<a name="API_UpdateCustomMetric_ResponseSyntax"></a>

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
<a name="API_UpdateCustomMetric_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationDate](#API_UpdateCustomMetric_ResponseSyntax) **   <a name="iot-UpdateCustomMetric-response-creationDate"></a>
 The creation date of the custom metric in milliseconds since epoch.
Type: Timestamp

 ** [displayName](#API_UpdateCustomMetric_ResponseSyntax) **   <a name="iot-UpdateCustomMetric-response-displayName"></a>
 A friendly name in the console for the custom metric
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[\p{Graph}\x20]*`

 ** [lastModifiedDate](#API_UpdateCustomMetric_ResponseSyntax) **   <a name="iot-UpdateCustomMetric-response-lastModifiedDate"></a>
 The time the custom metric was last modified in milliseconds since epoch.
Type: Timestamp

 ** [metricArn](#API_UpdateCustomMetric_ResponseSyntax) **   <a name="iot-UpdateCustomMetric-response-metricArn"></a>
 The Amazon Resource Number (ARN) of the custom metric.
Type: String

 ** [metricName](#API_UpdateCustomMetric_ResponseSyntax) **   <a name="iot-UpdateCustomMetric-response-metricName"></a>
 The name of the custom metric.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

 ** [metricType](#API_UpdateCustomMetric_ResponseSyntax) **   <a name="iot-UpdateCustomMetric-response-metricType"></a>
 The type of the custom metric.
The type `number` only takes a single metric value as an input, but while submitting the metrics value in the DeviceMetrics report, it must be passed as an array with a single value.
Type: String
Valid Values: `string-list | ip-address-list | number-list | number`

## Errors
<a name="API_UpdateCustomMetric_Errors"></a>

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
<a name="API_UpdateCustomMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/UpdateCustomMetric)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/UpdateCustomMetric)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/UpdateCustomMetric)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/UpdateCustomMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/UpdateCustomMetric)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/UpdateCustomMetric)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/UpdateCustomMetric)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/UpdateCustomMetric)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/UpdateCustomMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/UpdateCustomMetric)
