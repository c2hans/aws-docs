---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateDimension.html
---

# UpdateDimension
<a name="API_UpdateDimension"></a>

**Note**
The AWS IoT Device Defender detect feature will no longer be available to new customers starting August 31, 2026. If you would like to use the detect feature, sign up prior to August 31, 2026. To learn about alternatives to AWS IoT Device Defender detect, see [AWS IoT Device Defender detect feature availability change](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-detect-availability-change.html). There is no change to AWS IoT Device Defender audit availability.

Updates the definition for a dimension. You cannot change the type of a dimension after it is created (you can delete it and recreate it).

Requires permission to access the [UpdateDimension](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_UpdateDimension_RequestSyntax"></a>

```
PATCH /dimensions/{{name}} HTTP/1.1
Content-type: application/json

{
   "stringValues": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_UpdateDimension_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_UpdateDimension_RequestSyntax) **   <a name="iot-UpdateDimension-request-uri-name"></a>
A unique identifier for the dimension. Choose something that describes the type and value to make it easy to remember what it does.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_UpdateDimension_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [stringValues](#API_UpdateDimension_RequestSyntax) **   <a name="iot-UpdateDimension-request-stringValues"></a>
Specifies the value or list of values for the dimension. For `TOPIC_FILTER` dimensions, this is a pattern used to match the MQTT topic (for example, "admin/\#").
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## Response Syntax
<a name="API_UpdateDimension_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "creationDate": number,
   "lastModifiedDate": number,
   "name": "string",
   "stringValues": [ "string" ],
   "type": "string"
}
```

## Response Elements
<a name="API_UpdateDimension_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_UpdateDimension_ResponseSyntax) **   <a name="iot-UpdateDimension-response-arn"></a>
The Amazon Resource Name (ARN)of the created dimension.
Type: String

 ** [creationDate](#API_UpdateDimension_ResponseSyntax) **   <a name="iot-UpdateDimension-response-creationDate"></a>
The date and time, in milliseconds since epoch, when the dimension was initially created.
Type: Timestamp

 ** [lastModifiedDate](#API_UpdateDimension_ResponseSyntax) **   <a name="iot-UpdateDimension-response-lastModifiedDate"></a>
The date and time, in milliseconds since epoch, when the dimension was most recently updated.
Type: Timestamp

 ** [name](#API_UpdateDimension_ResponseSyntax) **   <a name="iot-UpdateDimension-response-name"></a>
A unique identifier for the dimension.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`

 ** [stringValues](#API_UpdateDimension_ResponseSyntax) **   <a name="iot-UpdateDimension-response-stringValues"></a>
The value or list of values used to scope the dimension. For example, for topic filters, this is the pattern used to match the MQTT topic name.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [type](#API_UpdateDimension_ResponseSyntax) **   <a name="iot-UpdateDimension-response-type"></a>
The type of the dimension.
Type: String
Valid Values: `TOPIC_FILTER`

## Errors
<a name="API_UpdateDimension_Errors"></a>

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
<a name="API_UpdateDimension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/UpdateDimension)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/UpdateDimension)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/UpdateDimension)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/UpdateDimension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/UpdateDimension)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/UpdateDimension)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/UpdateDimension)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/UpdateDimension)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/UpdateDimension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/UpdateDimension)
