---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DetachSecurityProfile.html
---

# DetachSecurityProfile
<a name="API_DetachSecurityProfile"></a>

**Note**
The AWS IoT Device Defender detect feature will no longer be available to new customers starting August 31, 2026. If you would like to use the detect feature, sign up prior to August 31, 2026. To learn about alternatives to AWS IoT Device Defender detect, see [AWS IoT Device Defender detect feature availability change](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-detect-availability-change.html). There is no change to AWS IoT Device Defender audit availability.

Disassociates a Device Defender security profile from a thing group or from this account.

Requires permission to access the [DetachSecurityProfile](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DetachSecurityProfile_RequestSyntax"></a>

```
DELETE /security-profiles/{{securityProfileName}}/targets?securityProfileTargetArn={{securityProfileTargetArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DetachSecurityProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [securityProfileName](#API_DetachSecurityProfile_RequestSyntax) **   <a name="iot-DetachSecurityProfile-request-uri-securityProfileName"></a>
The security profile that is detached.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

 ** [securityProfileTargetArn](#API_DetachSecurityProfile_RequestSyntax) **   <a name="iot-DetachSecurityProfile-request-uri-securityProfileTargetArn"></a>
The ARN of the thing group from which the security profile is detached.
Required: Yes

## Request Body
<a name="API_DetachSecurityProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DetachSecurityProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DetachSecurityProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DetachSecurityProfile_Errors"></a>

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
<a name="API_DetachSecurityProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DetachSecurityProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DetachSecurityProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DetachSecurityProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DetachSecurityProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DetachSecurityProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DetachSecurityProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DetachSecurityProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DetachSecurityProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DetachSecurityProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DetachSecurityProfile)
