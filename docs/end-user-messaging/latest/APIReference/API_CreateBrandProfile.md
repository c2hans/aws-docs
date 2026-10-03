---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_CreateBrandProfile.html
---

# CreateBrandProfile
<a name="API_CreateBrandProfile"></a>

Creates a brand profile. A brand profile is a lightweight container that holds your brand identity information as flexible attributes. After you create a brand profile, use the CreateBrandProfileAttributes operation to add company information, addresses, compliance documents, and logos.

## Request Syntax
<a name="API_CreateBrandProfile_RequestSyntax"></a>

```
POST /v1/brand-profiles HTTP/1.1
Content-type: application/json

{
   "brandProfileName": "{{string}}",
   "clientToken": "{{string}}",
   "deletionProtectionEnabled": {{boolean}},
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_CreateBrandProfile_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateBrandProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [brandProfileName](#API_CreateBrandProfile_RequestSyntax) **   <a name="endusermessaging-CreateBrandProfile-request-brandProfileName"></a>
The name of the brand profile. The name can contain alphanumeric characters, underscores, hyphens, and spaces.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_ -]*[A-Za-z0-9_-][A-Za-z0-9_ -]*`
Required: Yes

 ** [clientToken](#API_CreateBrandProfile_RequestSyntax) **   <a name="endusermessaging-CreateBrandProfile-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you do not specify a client token, the AWS SDK automatically generates one.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [deletionProtectionEnabled](#API_CreateBrandProfile_RequestSyntax) **   <a name="endusermessaging-CreateBrandProfile-request-deletionProtectionEnabled"></a>
Specifies whether deletion protection is enabled. When enabled, the resource cannot be deleted until deletion protection is turned off.
Type: Boolean
Required: No

 ** [tags](#API_CreateBrandProfile_RequestSyntax) **   <a name="endusermessaging-CreateBrandProfile-request-tags"></a>
An array of key and value pair tags that are associated with the resource.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateBrandProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "attributesCreated": number,
   "brandProfileArn": "string",
   "brandProfileId": "string",
   "brandProfileName": "string",
   "createdAt": number,
   "deletionProtectionEnabled": boolean,
   "status": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_CreateBrandProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [attributesCreated](#API_CreateBrandProfile_ResponseSyntax) **   <a name="endusermessaging-CreateBrandProfile-response-attributesCreated"></a>
The number of default attributes that were created for the brand profile.
Type: Integer

 ** [brandProfileArn](#API_CreateBrandProfile_ResponseSyntax) **   <a name="endusermessaging-CreateBrandProfile-response-brandProfileArn"></a>
The Amazon Resource Name (ARN) of the brand profile.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 256.
Pattern: `arn:[A-Za-z0-9_:/-]+`

 ** [brandProfileId](#API_CreateBrandProfile_ResponseSyntax) **   <a name="endusermessaging-CreateBrandProfile-response-brandProfileId"></a>
The unique identifier of the brand profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`

 ** [brandProfileName](#API_CreateBrandProfile_ResponseSyntax) **   <a name="endusermessaging-CreateBrandProfile-response-brandProfileName"></a>
The name of the brand profile. The name can contain alphanumeric characters, underscores, hyphens, and spaces.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_ -]*[A-Za-z0-9_-][A-Za-z0-9_ -]*`

 ** [createdAt](#API_CreateBrandProfile_ResponseSyntax) **   <a name="endusermessaging-CreateBrandProfile-response-createdAt"></a>
The time when the resource was created, in Unix epoch time.
Type: Timestamp

 ** [deletionProtectionEnabled](#API_CreateBrandProfile_ResponseSyntax) **   <a name="endusermessaging-CreateBrandProfile-response-deletionProtectionEnabled"></a>
Specifies whether deletion protection is enabled. When enabled, the resource cannot be deleted until deletion protection is turned off.
Type: Boolean

 ** [status](#API_CreateBrandProfile_ResponseSyntax) **   <a name="endusermessaging-CreateBrandProfile-response-status"></a>
The current lifecycle status of the brand profile.
Type: String
Valid Values: `ACTIVE | BLOCKED | PAUSED | CANCELLED | FAILED`

 ** [updatedAt](#API_CreateBrandProfile_ResponseSyntax) **   <a name="endusermessaging-CreateBrandProfile-response-updatedAt"></a>
The time when the resource was last updated, in Unix epoch time.
Type: Timestamp

## Errors
<a name="API_CreateBrandProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource.
 ** resourceId **
The identifier of the resource that the request conflicts with.
 ** resourceType **
The type of the resource that the request conflicts with.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred during the processing of the request.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request would exceed a service quota for your account.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied because it exceeded the allowed request rate.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service. Check your request parameters and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_CreateBrandProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/endusermessaging-2026-09-21/CreateBrandProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/endusermessaging-2026-09-21/CreateBrandProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/CreateBrandProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/endusermessaging-2026-09-21/CreateBrandProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/CreateBrandProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/endusermessaging-2026-09-21/CreateBrandProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/endusermessaging-2026-09-21/CreateBrandProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/endusermessaging-2026-09-21/CreateBrandProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/endusermessaging-2026-09-21/CreateBrandProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/CreateBrandProfile)
