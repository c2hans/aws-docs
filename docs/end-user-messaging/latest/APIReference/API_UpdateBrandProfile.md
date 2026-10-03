---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_UpdateBrandProfile.html
---

# UpdateBrandProfile
<a name="API_UpdateBrandProfile"></a>

Updates the name or the deletion protection setting of a brand profile. To change the information that is stored in the profile, use the brand profile attribute operations.

## Request Syntax
<a name="API_UpdateBrandProfile_RequestSyntax"></a>

```
PUT /v1/brand-profiles/{{brandProfileId+}} HTTP/1.1
Content-type: application/json

{
   "brandProfileName": "{{string}}",
   "deletionProtectionEnabled": {{boolean}}
}
```

## URI Request Parameters
<a name="API_UpdateBrandProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [brandProfileId](#API_UpdateBrandProfile_RequestSyntax) **   <a name="endusermessaging-UpdateBrandProfile-request-uri-brandProfileId"></a>
The unique identifier of the brand profile. You can specify either the bare ID or the full Amazon Resource Name (ARN).
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Request Body
<a name="API_UpdateBrandProfile_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [brandProfileName](#API_UpdateBrandProfile_RequestSyntax) **   <a name="endusermessaging-UpdateBrandProfile-request-brandProfileName"></a>
The name of the brand profile. The name can contain alphanumeric characters, underscores, hyphens, and spaces.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_ -]*[A-Za-z0-9_-][A-Za-z0-9_ -]*`
Required: No

 ** [deletionProtectionEnabled](#API_UpdateBrandProfile_RequestSyntax) **   <a name="endusermessaging-UpdateBrandProfile-request-deletionProtectionEnabled"></a>
Specifies whether deletion protection is enabled. When enabled, the resource cannot be deleted until deletion protection is turned off.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdateBrandProfile_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
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
<a name="API_UpdateBrandProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [brandProfileArn](#API_UpdateBrandProfile_ResponseSyntax) **   <a name="endusermessaging-UpdateBrandProfile-response-brandProfileArn"></a>
The Amazon Resource Name (ARN) of the brand profile.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 256.
Pattern: `arn:[A-Za-z0-9_:/-]+`

 ** [brandProfileId](#API_UpdateBrandProfile_ResponseSyntax) **   <a name="endusermessaging-UpdateBrandProfile-response-brandProfileId"></a>
The unique identifier of the brand profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`

 ** [brandProfileName](#API_UpdateBrandProfile_ResponseSyntax) **   <a name="endusermessaging-UpdateBrandProfile-response-brandProfileName"></a>
The name of the brand profile. The name can contain alphanumeric characters, underscores, hyphens, and spaces.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_ -]*[A-Za-z0-9_-][A-Za-z0-9_ -]*`

 ** [createdAt](#API_UpdateBrandProfile_ResponseSyntax) **   <a name="endusermessaging-UpdateBrandProfile-response-createdAt"></a>
The time when the resource was created, in Unix epoch time.
Type: Timestamp

 ** [deletionProtectionEnabled](#API_UpdateBrandProfile_ResponseSyntax) **   <a name="endusermessaging-UpdateBrandProfile-response-deletionProtectionEnabled"></a>
Specifies whether deletion protection is enabled. When enabled, the resource cannot be deleted until deletion protection is turned off.
Type: Boolean

 ** [status](#API_UpdateBrandProfile_ResponseSyntax) **   <a name="endusermessaging-UpdateBrandProfile-response-status"></a>
The current lifecycle status of the brand profile.
Type: String
Valid Values: `ACTIVE | BLOCKED | PAUSED | CANCELLED | FAILED`

 ** [updatedAt](#API_UpdateBrandProfile_ResponseSyntax) **   <a name="endusermessaging-UpdateBrandProfile-response-updatedAt"></a>
The time when the resource was last updated, in Unix epoch time.
Type: Timestamp

## Errors
<a name="API_UpdateBrandProfile_Errors"></a>

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

 ** ResourceNotFoundException **
The request references a resource that does not exist. Verify that the resource identifier is correct and try your request again.
 ** resourceId **
The identifier of the resource that could not be found.
 ** resourceType **
The type of the resource that could not be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied because it exceeded the allowed request rate.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by the service. Check your request parameters and retry the request.
HTTP Status Code: 400

## See Also
<a name="API_UpdateBrandProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/endusermessaging-2026-09-21/UpdateBrandProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/endusermessaging-2026-09-21/UpdateBrandProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/UpdateBrandProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/endusermessaging-2026-09-21/UpdateBrandProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/UpdateBrandProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/endusermessaging-2026-09-21/UpdateBrandProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/endusermessaging-2026-09-21/UpdateBrandProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/endusermessaging-2026-09-21/UpdateBrandProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/endusermessaging-2026-09-21/UpdateBrandProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/UpdateBrandProfile)
