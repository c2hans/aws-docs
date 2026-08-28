---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_PutVerificationStateOnViolation.html
---

# PutVerificationStateOnViolation
<a name="API_PutVerificationStateOnViolation"></a>

**Note**
The AWS IoT Device Defender detect feature will no longer be available to new customers starting August 31, 2026. If you would like to use the detect feature, sign up prior to August 31, 2026. To learn about alternatives to AWS IoT Device Defender detect, see [AWS IoT Device Defender detect feature availability change](https://docs.aws.amazon.com/iot-device-defender/latest/devguide/dd-detect-availability-change.html). There is no change to AWS IoT Device Defender audit availability.

Set a verification state and provide a description of that verification state on a violation (detect alarm).

## Request Syntax
<a name="API_PutVerificationStateOnViolation_RequestSyntax"></a>

```
POST /violations/verification-state/{{violationId}} HTTP/1.1
Content-type: application/json

{
   "verificationState": "{{string}}",
   "verificationStateDescription": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutVerificationStateOnViolation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [violationId](#API_PutVerificationStateOnViolation_RequestSyntax) **   <a name="iot-PutVerificationStateOnViolation-request-uri-violationId"></a>
The violation ID.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-]+`
Required: Yes

## Request Body
<a name="API_PutVerificationStateOnViolation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [verificationState](#API_PutVerificationStateOnViolation_RequestSyntax) **   <a name="iot-PutVerificationStateOnViolation-request-verificationState"></a>
The verification state of the violation.
Type: String
Valid Values: `FALSE_POSITIVE | BENIGN_POSITIVE | TRUE_POSITIVE | UNKNOWN`
Required: Yes

 ** [verificationStateDescription](#API_PutVerificationStateOnViolation_RequestSyntax) **   <a name="iot-PutVerificationStateOnViolation-request-verificationStateDescription"></a>
The description of the verification state of the violation (detect alarm).
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `[^\p{Cntrl}]*`
Required: No

## Response Syntax
<a name="API_PutVerificationStateOnViolation_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutVerificationStateOnViolation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutVerificationStateOnViolation_Errors"></a>

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
<a name="API_PutVerificationStateOnViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/PutVerificationStateOnViolation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/PutVerificationStateOnViolation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/PutVerificationStateOnViolation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/PutVerificationStateOnViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/PutVerificationStateOnViolation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/PutVerificationStateOnViolation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/PutVerificationStateOnViolation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/PutVerificationStateOnViolation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/PutVerificationStateOnViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/PutVerificationStateOnViolation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
