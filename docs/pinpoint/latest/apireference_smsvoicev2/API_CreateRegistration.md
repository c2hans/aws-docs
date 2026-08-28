---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateRegistration.html
---

# CreateRegistration
<a name="API_CreateRegistration"></a>

Creates a new registration based on the **RegistrationType** field.

## Request Syntax
<a name="API_CreateRegistration_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "RegistrationType": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateRegistration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_CreateRegistration_RequestSyntax) **   <a name="pinpoint-CreateRegistration-request-ClientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you don't specify a client token, a randomly generated token is used for the request to ensure idempotency.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** [RegistrationType](#API_CreateRegistration_RequestSyntax) **   <a name="pinpoint-CreateRegistration-request-RegistrationType"></a>
The type of registration form to create. The list of **RegistrationTypes** can be found using the [DescribeRegistrationTypeDefinitions](API_DescribeRegistrationTypeDefinitions.md) action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_]+`
Required: Yes

 ** [Tags](#API_CreateRegistration_RequestSyntax) **   <a name="pinpoint-CreateRegistration-request-Tags"></a>
An array of tags (key and value pairs) to associate with the registration.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: No

## Response Syntax
<a name="API_CreateRegistration_ResponseSyntax"></a>

```
{
   "AdditionalAttributes": {
      "string" : "string"
   },
   "CreatedTimestamp": number,
   "CurrentVersionNumber": number,
   "RegistrationArn": "string",
   "RegistrationId": "string",
   "RegistrationStatus": "string",
   "RegistrationType": "string",
   "Tags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_CreateRegistration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AdditionalAttributes](#API_CreateRegistration_ResponseSyntax) **   <a name="pinpoint-CreateRegistration-response-AdditionalAttributes"></a>
Metadata about a given registration which is specific to that registration type.
Type: String to string map

 ** [CreatedTimestamp](#API_CreateRegistration_ResponseSyntax) **   <a name="pinpoint-CreateRegistration-response-CreatedTimestamp"></a>
The time when the registration was created, in [UNIX epoch time](https://www.epochconverter.com/) format.
Type: Timestamp

 ** [CurrentVersionNumber](#API_CreateRegistration_ResponseSyntax) **   <a name="pinpoint-CreateRegistration-response-CurrentVersionNumber"></a>
The current version number of the registration.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 100000.

 ** [RegistrationArn](#API_CreateRegistration_ResponseSyntax) **   <a name="pinpoint-CreateRegistration-response-RegistrationArn"></a>
The Amazon Resource Name (ARN) for the registration.
Type: String

 ** [RegistrationId](#API_CreateRegistration_ResponseSyntax) **   <a name="pinpoint-CreateRegistration-response-RegistrationId"></a>
The unique identifier for the registration.
Type: String

 ** [RegistrationStatus](#API_CreateRegistration_ResponseSyntax) **   <a name="pinpoint-CreateRegistration-response-RegistrationStatus"></a>
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

 ** [RegistrationType](#API_CreateRegistration_ResponseSyntax) **   <a name="pinpoint-CreateRegistration-response-RegistrationType"></a>
The type of registration form to create. The list of **RegistrationTypes** can be found using the [DescribeRegistrationTypeDefinitions](API_DescribeRegistrationTypeDefinitions.md) action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_]+`

 ** [Tags](#API_CreateRegistration_ResponseSyntax) **   <a name="pinpoint-CreateRegistration-response-Tags"></a>
An array of tags (key and value pairs) to associate with the registration.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

## Errors
<a name="API_CreateRegistration_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
 ** Reason **
The reason for the exception.
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
<a name="API_CreateRegistration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/CreateRegistration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/CreateRegistration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/CreateRegistration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/CreateRegistration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/CreateRegistration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/CreateRegistration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/CreateRegistration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/CreateRegistration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/CreateRegistration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/CreateRegistration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
