---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_CreateRegistrationVersion.html
---

# CreateRegistrationVersion
<a name="API_CreateRegistrationVersion"></a>

Create a new version of the registration and increase the **VersionNumber**. The previous version of the registration becomes read-only.

## Request Syntax
<a name="API_CreateRegistrationVersion_RequestSyntax"></a>

```
{
   "RegistrationId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateRegistrationVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RegistrationId](#API_CreateRegistrationVersion_RequestSyntax) **   <a name="pinpoint-CreateRegistrationVersion-request-RegistrationId"></a>
The unique identifier for the registration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Response Syntax
<a name="API_CreateRegistrationVersion_ResponseSyntax"></a>

```
{
   "RegistrationArn": "string",
   "RegistrationId": "string",
   "RegistrationVersionStatus": "string",
   "RegistrationVersionStatusHistory": {
      "ApprovedTimestamp": number,
      "ArchivedTimestamp": number,
      "AwsReviewingTimestamp": number,
      "DeniedTimestamp": number,
      "DiscardedTimestamp": number,
      "DraftTimestamp": number,
      "RequiresAuthenticationTimestamp": number,
      "ReviewingTimestamp": number,
      "RevokedTimestamp": number,
      "SubmittedTimestamp": number
   },
   "VersionNumber": number
}
```

## Response Elements
<a name="API_CreateRegistrationVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [RegistrationArn](#API_CreateRegistrationVersion_ResponseSyntax) **   <a name="pinpoint-CreateRegistrationVersion-response-RegistrationArn"></a>
The Amazon Resource Name (ARN) for the registration.
Type: String

 ** [RegistrationId](#API_CreateRegistrationVersion_ResponseSyntax) **   <a name="pinpoint-CreateRegistrationVersion-response-RegistrationId"></a>
The unique identifier for the registration.
Type: String

 ** [RegistrationVersionStatus](#API_CreateRegistrationVersion_ResponseSyntax) **   <a name="pinpoint-CreateRegistrationVersion-response-RegistrationVersionStatus"></a>
The status of the registration.
+  `APPROVED`: Your registration has been approved.
+  `ARCHIVED`: Your previously approved registration version moves into this status when a more recently submitted version is approved.
+  `DENIED`: You must fix your registration and resubmit it.
+  `DISCARDED`: You've abandon this version of their registration to start over with a new version.
+  `DRAFT`: The initial status of a registration version after it’s created.
+  `REQUIRES_AUTHENTICATION`: You need to complete email authentication.
+  `REVIEWING`: Your registration has been accepted and is being reviewed.
+  `REVOKED`: Your previously approved registration has been revoked.
+  `SUBMITTED`: Your registration has been submitted.
Type: String
Valid Values: `DRAFT | SUBMITTED | AWS_REVIEWING | REVIEWING | REQUIRES_AUTHENTICATION | APPROVED | DISCARDED | DENIED | REVOKED | ARCHIVED | REQUIRES_OFFLINE_REVIEW`

 ** [RegistrationVersionStatusHistory](#API_CreateRegistrationVersion_ResponseSyntax) **   <a name="pinpoint-CreateRegistrationVersion-response-RegistrationVersionStatusHistory"></a>
A **RegistrationVersionStatusHistory** object that contains timestamps for the registration.
Type: [RegistrationVersionStatusHistory](API_RegistrationVersionStatusHistory.md) object

 ** [VersionNumber](#API_CreateRegistrationVersion_ResponseSyntax) **   <a name="pinpoint-CreateRegistrationVersion-response-VersionNumber"></a>
The new version number of the registration.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 100000.

## Errors
<a name="API_CreateRegistrationVersion_Errors"></a>

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
<a name="API_CreateRegistrationVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/CreateRegistrationVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
