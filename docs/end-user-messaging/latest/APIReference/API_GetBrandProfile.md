---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_GetBrandProfile.html
---

# GetBrandProfile
<a name="API_GetBrandProfile"></a>

Retrieves the metadata for a brand profile, including its name, status, deletion protection setting, and timestamps. To retrieve the attributes of the profile, use the ListBrandProfileAttributes operation.

## Request Syntax
<a name="API_GetBrandProfile_RequestSyntax"></a>

```
GET /v1/brand-profiles/{{brandProfileId+}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetBrandProfile_RequestParameters"></a>

The request uses the following URI parameters.

 ** [brandProfileId](#API_GetBrandProfile_RequestSyntax) **   <a name="endusermessaging-GetBrandProfile-request-uri-brandProfileId"></a>
The unique identifier of the brand profile. You can specify either the bare ID or the full Amazon Resource Name (ARN).
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Request Body
<a name="API_GetBrandProfile_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetBrandProfile_ResponseSyntax"></a>

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
<a name="API_GetBrandProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [brandProfileArn](#API_GetBrandProfile_ResponseSyntax) **   <a name="endusermessaging-GetBrandProfile-response-brandProfileArn"></a>
The Amazon Resource Name (ARN) of the brand profile.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 256.
Pattern: `arn:[A-Za-z0-9_:/-]+`

 ** [brandProfileId](#API_GetBrandProfile_ResponseSyntax) **   <a name="endusermessaging-GetBrandProfile-response-brandProfileId"></a>
The unique identifier of the brand profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`

 ** [brandProfileName](#API_GetBrandProfile_ResponseSyntax) **   <a name="endusermessaging-GetBrandProfile-response-brandProfileName"></a>
The name of the brand profile. The name can contain alphanumeric characters, underscores, hyphens, and spaces.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9_ -]*[A-Za-z0-9_-][A-Za-z0-9_ -]*`

 ** [createdAt](#API_GetBrandProfile_ResponseSyntax) **   <a name="endusermessaging-GetBrandProfile-response-createdAt"></a>
The time when the resource was created, in Unix epoch time.
Type: Timestamp

 ** [deletionProtectionEnabled](#API_GetBrandProfile_ResponseSyntax) **   <a name="endusermessaging-GetBrandProfile-response-deletionProtectionEnabled"></a>
Specifies whether deletion protection is enabled. When enabled, the resource cannot be deleted until deletion protection is turned off.
Type: Boolean

 ** [status](#API_GetBrandProfile_ResponseSyntax) **   <a name="endusermessaging-GetBrandProfile-response-status"></a>
The current lifecycle status of the brand profile.
Type: String
Valid Values: `ACTIVE | BLOCKED | PAUSED | CANCELLED | FAILED`

 ** [updatedAt](#API_GetBrandProfile_ResponseSyntax) **   <a name="endusermessaging-GetBrandProfile-response-updatedAt"></a>
The time when the resource was last updated, in Unix epoch time.
Type: Timestamp

## Errors
<a name="API_GetBrandProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_GetBrandProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/endusermessaging-2026-09-21/GetBrandProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/endusermessaging-2026-09-21/GetBrandProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/GetBrandProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/endusermessaging-2026-09-21/GetBrandProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/GetBrandProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/endusermessaging-2026-09-21/GetBrandProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/endusermessaging-2026-09-21/GetBrandProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/endusermessaging-2026-09-21/GetBrandProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/endusermessaging-2026-09-21/GetBrandProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/GetBrandProfile)
