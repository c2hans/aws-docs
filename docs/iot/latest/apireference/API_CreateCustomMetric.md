---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreateCustomMetric.html
---

# CreateCustomMetric
<a name="API_CreateCustomMetric"></a>

**Note**
The AWS IoT Device Defender detect feature will no longer be available to new customers starting August 31, 2026. If you would like to use the detect feature, sign up prior to August 31, 2026. To learn about alternatives to AWS IoT Device Defender detect, see [AWS IoT Device Defender detect feature availability change](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-detect-availability-change.html). There is no change to AWS IoT Device Defender audit availability.

 Use this API to define a Custom Metric published by your devices to Device Defender.

Requires permission to access the [CreateCustomMetric](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_CreateCustomMetric_RequestSyntax"></a>

```
POST /custom-metric/{{metricName}} HTTP/1.1
Content-type: application/json

{
   "clientRequestToken": "{{string}}",
   "displayName": "{{string}}",
   "metricType": "{{string}}",
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateCustomMetric_RequestParameters"></a>

The request uses the following URI parameters.

 ** [metricName](#API_CreateCustomMetric_RequestSyntax) **   <a name="iot-CreateCustomMetric-request-uri-metricName"></a>
 The name of the custom metric. This will be used in the metric report submitted from the device/thing. The name can't begin with `aws:`. You can't change the name after you define it.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_CreateCustomMetric_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientRequestToken](#API_CreateCustomMetric_RequestSyntax) **   <a name="iot-CreateCustomMetric-request-clientRequestToken"></a>
Each custom metric must have a unique client request token. If you try to create a new custom metric that already exists with a different token, an exception occurs. If you omit this value, AWS SDKs will automatically generate a unique client request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: Yes

 ** [displayName](#API_CreateCustomMetric_RequestSyntax) **   <a name="iot-CreateCustomMetric-request-displayName"></a>
 The friendly name in the console for the custom metric. This name doesn't have to be unique. Don't use this name as the metric identifier in the device metric report. You can update the friendly name after you define it.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[\p{Graph}\x20]*`
Required: No

 ** [metricType](#API_CreateCustomMetric_RequestSyntax) **   <a name="iot-CreateCustomMetric-request-metricType"></a>
 The type of the custom metric.
The type `number` only takes a single metric value as an input, but when you submit the metrics value in the DeviceMetrics report, you must pass it as an array with a single value.
Type: String
Valid Values: `string-list | ip-address-list | number-list | number`
Required: Yes

 ** [tags](#API_CreateCustomMetric_RequestSyntax) **   <a name="iot-CreateCustomMetric-request-tags"></a>
 Metadata that can be used to manage the custom metric.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateCustomMetric_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "metricArn": "string",
   "metricName": "string"
}
```

## Response Elements
<a name="API_CreateCustomMetric_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [metricArn](#API_CreateCustomMetric_ResponseSyntax) **   <a name="iot-CreateCustomMetric-response-metricArn"></a>
 The Amazon Resource Number (ARN) of the custom metric. For example, `arn:aws-partition:iot:region:accountId:custommetric/metricName `
Type: String

 ** [metricName](#API_CreateCustomMetric_ResponseSyntax) **   <a name="iot-CreateCustomMetric-response-metricName"></a>
 The name of the custom metric to be used in the metric report.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

## Errors
<a name="API_CreateCustomMetric_Errors"></a>

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

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateCustomMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreateCustomMetric)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreateCustomMetric)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreateCustomMetric)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreateCustomMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreateCustomMetric)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreateCustomMetric)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreateCustomMetric)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreateCustomMetric)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreateCustomMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreateCustomMetric)
