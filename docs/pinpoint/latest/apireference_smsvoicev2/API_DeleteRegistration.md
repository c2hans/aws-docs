---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_DeleteRegistration.html
---

# DeleteRegistration
<a name="API_DeleteRegistration"></a>

Permanently delete an existing registration from your account.

## Request Syntax
<a name="API_DeleteRegistration_RequestSyntax"></a>

```
{
   "RegistrationId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteRegistration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RegistrationId](#API_DeleteRegistration_RequestSyntax) **   <a name="pinpoint-DeleteRegistration-request-RegistrationId"></a>
The unique identifier for the registration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Response Syntax
<a name="API_DeleteRegistration_ResponseSyntax"></a>

```
{
   "AdditionalAttributes": {
      "string" : "string"
   },
   "ApprovedVersionNumber": number,
   "CreatedTimestamp": number,
   "CurrentVersionNumber": number,
   "LatestDeniedVersionNumber": number,
   "RegistrationArn": "string",
   "RegistrationId": "string",
   "RegistrationStatus": "string",
   "RegistrationType": "string"
}
```

## Response Elements
<a name="API_DeleteRegistration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AdditionalAttributes](#API_DeleteRegistration_ResponseSyntax) **   <a name="pinpoint-DeleteRegistration-response-AdditionalAttributes"></a>
Metadata about a given registration which is specific to that registration type.
Type: String to string map

 ** [ApprovedVersionNumber](#API_DeleteRegistration_ResponseSyntax) **   <a name="pinpoint-DeleteRegistration-response-ApprovedVersionNumber"></a>
The version number of the registration that was approved.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 100000.

 ** [CreatedTimestamp](#API_DeleteRegistration_ResponseSyntax) **   <a name="pinpoint-DeleteRegistration-response-CreatedTimestamp"></a>
The time when the registration was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp

 ** [CurrentVersionNumber](#API_DeleteRegistration_ResponseSyntax) **   <a name="pinpoint-DeleteRegistration-response-CurrentVersionNumber"></a>
The current version number of the registration.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 100000.

 ** [LatestDeniedVersionNumber](#API_DeleteRegistration_ResponseSyntax) **   <a name="pinpoint-DeleteRegistration-response-LatestDeniedVersionNumber"></a>
The latest version number of the registration that was denied.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 100000.

 ** [RegistrationArn](#API_DeleteRegistration_ResponseSyntax) **   <a name="pinpoint-DeleteRegistration-response-RegistrationArn"></a>
The Amazon Resource Name (ARN) for the registration.
Type: String

 ** [RegistrationId](#API_DeleteRegistration_ResponseSyntax) **   <a name="pinpoint-DeleteRegistration-response-RegistrationId"></a>
The unique identifier for the registration.
Type: String

 ** [RegistrationStatus](#API_DeleteRegistration_ResponseSyntax) **   <a name="pinpoint-DeleteRegistration-response-RegistrationStatus"></a>
The status of the registration.
+  `CLOSED`: The phone number or sender ID has been deleted and you must also delete the registration for the number.
+  `CREATED`: Your registration is created but not submitted.
+  `COMPLETE`: Your registration has been approved and your origination identity has been created.
+  `DELETED`: The registration has been deleted.
+  `PROVISIONING`: Your registration has been approved and your origination identity is being created.
+  `REQUIRES_AUTHENTICATION`: You need to complete email authentication.
+  `REQUIRES_UPDATES`: You must fix your registration and resubmit it.
+  `REVIEWING`: Your registration has been accepted and is being reviewed.
+  `SUBMITTED`: Your registration has been submitted and is awaiting review.
Type: String
Valid Values: `CREATED | SUBMITTED | AWS_REVIEWING | REVIEWING | REQUIRES_AUTHENTICATION | PROVISIONING | COMPLETE | REQUIRES_UPDATES | CLOSED | DELETED`

 ** [RegistrationType](#API_DeleteRegistration_ResponseSyntax) **   <a name="pinpoint-DeleteRegistration-response-RegistrationType"></a>
The type of registration form. The list of **RegistrationTypes** can be found using the [DescribeRegistrationTypeDefinitions](API_DescribeRegistrationTypeDefinitions.md) action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_]+`

## Errors
<a name="API_DeleteRegistration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because you don't have sufficient permissions to access the resource.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

 ** ConflictException **
Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time or it could be that the requested action isn't valid for the current state or configuration of the resource.
 ** Reason **
The reason for the exception.
 ** ResourceId **
The unique identifier of the request.
 ** ResourceType **
The type of resource that caused the exception.
HTTP Status Code: 400

 ** InternalServerException **
The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.
 ** RequestId **
The unique identifier of the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
A requested resource couldn't be found.
 ** ResourceId **
The unique identifier of the resource.
 ** ResourceType **
The type of resource that caused the exception.
HTTP Status Code: 400

 ** ThrottlingException **
An error that occurred because too many requests were sent during a certain amount of time.
HTTP Status Code: 400

 ** ValidationException **
A validation exception for a field.
 ** Fields **
The field that failed validation.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_DeleteRegistration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/DeleteRegistration)
