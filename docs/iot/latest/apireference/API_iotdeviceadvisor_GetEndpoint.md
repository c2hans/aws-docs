---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_GetEndpoint.html
---

# GetEndpoint
<a name="API_iotdeviceadvisor_GetEndpoint"></a>

Gets information about an Device Advisor endpoint.

## Request Syntax
<a name="API_iotdeviceadvisor_GetEndpoint_RequestSyntax"></a>

```
GET /endpoint?authenticationMethod={{authenticationMethod}}&certificateArn={{certificateArn}}&deviceRoleArn={{deviceRoleArn}}&thingArn={{thingArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_iotdeviceadvisor_GetEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [authenticationMethod](#API_iotdeviceadvisor_GetEndpoint_RequestSyntax) **   <a name="iot-iotdeviceadvisor_GetEndpoint-request-uri-authenticationMethod"></a>
The authentication method used during the device connection.
Valid Values: `X509ClientCertificate | SignatureVersion4`

 ** [certificateArn](#API_iotdeviceadvisor_GetEndpoint_RequestSyntax) **   <a name="iot-iotdeviceadvisor_GetEndpoint-request-uri-certificateArn"></a>
The certificate ARN of the device. This is an optional parameter.
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [deviceRoleArn](#API_iotdeviceadvisor_GetEndpoint_RequestSyntax) **   <a name="iot-iotdeviceadvisor_GetEndpoint-request-uri-deviceRoleArn"></a>
The device role ARN of the device. This is an optional parameter.
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [thingArn](#API_iotdeviceadvisor_GetEndpoint_RequestSyntax) **   <a name="iot-iotdeviceadvisor_GetEndpoint-request-uri-thingArn"></a>
The thing ARN of the device. This is an optional parameter.
Length Constraints: Minimum length of 20. Maximum length of 2048.

## Request Body
<a name="API_iotdeviceadvisor_GetEndpoint_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_iotdeviceadvisor_GetEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "endpoint": "string"
}
```

## Response Elements
<a name="API_iotdeviceadvisor_GetEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [endpoint](#API_iotdeviceadvisor_GetEndpoint_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_GetEndpoint-response-endpoint"></a>
The response of an Device Advisor endpoint.
Type: String
Length Constraints: Minimum length of 45. Maximum length of 75.

## Errors
<a name="API_iotdeviceadvisor_GetEndpoint_Errors"></a>

 ** InternalServerException **
Sends an Internal Failure exception.
 ** message **
Sends an Internal Failure Exception message.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Sends a Resource Not Found exception.
 ** message **
Sends a Resource Not Found Exception message.
HTTP Status Code: 404

 ** ValidationException **
Sends a validation exception.
 ** message **
Sends a Validation Exception message.
HTTP Status Code: 400

## See Also
<a name="API_iotdeviceadvisor_GetEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotdeviceadvisor-2020-09-18/GetEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotdeviceadvisor-2020-09-18/GetEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotdeviceadvisor-2020-09-18/GetEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotdeviceadvisor-2020-09-18/GetEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotdeviceadvisor-2020-09-18/GetEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotdeviceadvisor-2020-09-18/GetEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotdeviceadvisor-2020-09-18/GetEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotdeviceadvisor-2020-09-18/GetEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotdeviceadvisor-2020-09-18/GetEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotdeviceadvisor-2020-09-18/GetEndpoint)
