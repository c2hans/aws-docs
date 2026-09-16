---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_RegisterThing.html
---

# RegisterThing
<a name="API_RegisterThing"></a>

Provisions a thing in the device registry. RegisterThing calls other AWS IoT control plane APIs. These calls might exceed your account level [AWS IoT Throttling Limits](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html#limits_iot) and cause throttle errors. Please contact [AWS Customer Support](https://console.aws.amazon.com/support/home) to raise your throttling limits if necessary.

Requires permission to access the [RegisterThing](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_RegisterThing_RequestSyntax"></a>

```
POST /things HTTP/1.1
Content-type: application/json

{
   "parameters": {
      "{{string}}" : "{{string}}"
   },
   "templateBody": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RegisterThing_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_RegisterThing_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [parameters](#API_RegisterThing_RequestSyntax) **   <a name="iot-RegisterThing-request-parameters"></a>
The parameters for provisioning a thing. See [Provisioning Templates](https://docs.aws.amazon.com/iot/latest/developerguide/provision-template.html) for more information.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 2048.
Key Pattern: `[\s\S]*`
Value Length Constraints: Minimum length of 0. Maximum length of 4096.
Value Pattern: `[\s\S]*`
Required: No

 ** [templateBody](#API_RegisterThing_RequestSyntax) **   <a name="iot-RegisterThing-request-templateBody"></a>
The provisioning template. See [Provisioning Devices That Have Device Certificates](https://docs.aws.amazon.com/iot/latest/developerguide/provision-w-cert.html) for more information.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.
Pattern: `[\s\S]*`
Required: Yes

## Response Syntax
<a name="API_RegisterThing_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "certificatePem": "string",
   "resourceArns": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_RegisterThing_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [certificatePem](#API_RegisterThing_ResponseSyntax) **   <a name="iot-RegisterThing-response-certificatePem"></a>
The certificate data, in PEM format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 65536.
Pattern: `[\s\S]*`

 ** [resourceArns](#API_RegisterThing_ResponseSyntax) **   <a name="iot-RegisterThing-response-resourceArns"></a>
ARNs for the generated resources.
Type: String to string map

## Errors
<a name="API_RegisterThing_Errors"></a>

 ** ConflictingResourceUpdateException **
A conflicting resource update exception. This exception is thrown when two pending updates cause a conflict.
 ** message **
The message for the exception.
HTTP Status Code: 409

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

 ** ResourceRegistrationFailureException **
The resource registration failed.
 ** message **
The message for the exception.
HTTP Status Code: 400

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
<a name="API_RegisterThing_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/RegisterThing)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/RegisterThing)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/RegisterThing)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/RegisterThing)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/RegisterThing)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/RegisterThing)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/RegisterThing)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/RegisterThing)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/RegisterThing)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/RegisterThing)
