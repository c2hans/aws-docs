---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_AttachSecurityProfile.html
---

# AttachSecurityProfile
<a name="API_AttachSecurityProfile"></a>

**Note**
The AWS IoT Device Defender detect feature will no longer be available to new customers starting August 31, 2026. If you would like to use the detect feature, sign up prior to August 31, 2026. To learn about alternatives to AWS IoT Device Defender detect, see [AWS IoT Device Defender detect feature availability change](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-detect-availability-change.html). There is no change to AWS IoT Device Defender audit availability.

Associates a Device Defender security profile with a thing group or this account. Each thing group or account can have up to five security profiles associated with it.

Requires permission to access the [AttachSecurityProfile](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_AttachSecurityProfile_RequestSyntax"></a>

```
PUT /security-profiles/{{securityProfileName}}/targets?securityProfileTargetArn={{securityProfileTargetArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_AttachSecurityProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [securityProfileName](#API_AttachSecurityProfile_RequestSyntax) **   <a name="iot-AttachSecurityProfile-request-uri-securityProfileName"></a>
The security profile that is attached.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9:_-]+`
Required: Yes

 ** [securityProfileTargetArn](#API_AttachSecurityProfile_RequestSyntax) **   <a name="iot-AttachSecurityProfile-request-uri-securityProfileTargetArn"></a>
The ARN of the target (thing group) to which the security profile is attached.
Required: Yes

## Request Body
<a name="API_AttachSecurityProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_AttachSecurityProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_AttachSecurityProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AttachSecurityProfile_Errors"></a>

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

 ** VersionConflictException **
An exception thrown when the version of an entity specified with the `expectedVersion` parameter does not match the latest version in the system.
 ** message **
The message for the exception.
HTTP Status Code: 409

## See Also
<a name="API_AttachSecurityProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/AttachSecurityProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/AttachSecurityProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/AttachSecurityProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/AttachSecurityProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/AttachSecurityProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/AttachSecurityProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/AttachSecurityProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/AttachSecurityProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/AttachSecurityProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/AttachSecurityProfile)
