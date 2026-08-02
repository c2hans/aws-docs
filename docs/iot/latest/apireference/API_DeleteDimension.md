---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteDimension.html
---

# DeleteDimension
<a name="API_DeleteDimension"></a>

**Note**
The AWS IoT Device Defender detect feature will no longer be available to new customers starting August 31, 2026. If you would like to use the detect feature, sign up prior to August 31, 2026. To learn about alternatives to AWS IoT Device Defender detect, see [AWS IoT Device Defender detect feature availability change](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-detect-availability-change.html). There is no change to AWS IoT Device Defender audit availability.

Removes the specified dimension from your AWS accounts.

Requires permission to access the [DeleteDimension](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DeleteDimension_RequestSyntax"></a>

```
DELETE /dimensions/{{name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteDimension_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_DeleteDimension_RequestSyntax) **   <a name="iot-DeleteDimension-request-uri-name"></a>
The unique identifier for the dimension that you want to delete.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

## Request Body
<a name="API_DeleteDimension_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteDimension_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteDimension_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteDimension_Errors"></a>

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

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_DeleteDimension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DeleteDimension)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DeleteDimension)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DeleteDimension)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DeleteDimension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DeleteDimension)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DeleteDimension)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DeleteDimension)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DeleteDimension)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DeleteDimension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DeleteDimension)
