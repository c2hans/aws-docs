---
source_url: https://docs.aws.amazon.com/social-messaging/latest/APIReference/API_GetWhatsAppCallPermission.html
---

# GetWhatsAppCallPermission
<a name="API_GetWhatsAppCallPermission"></a>

Retrieves the current calling permission for a WhatsApp end user, along with the calling actions the business is allowed to take with that user. Provide the destination phone number or the business-scoped user ID to identify the end user.

## Request Syntax
<a name="API_GetWhatsAppCallPermission_RequestSyntax"></a>

```
POST /v1/whatsapp/call/permission/get HTTP/1.1
Content-type: application/json

{
   "destinationPhoneNumber": "{{string}}",
   "endUserBsuid": "{{string}}",
   "originationPhoneNumberId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetWhatsAppCallPermission_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetWhatsAppCallPermission_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [destinationPhoneNumber](#API_GetWhatsAppCallPermission_RequestSyntax) **   <a name="Social-GetWhatsAppCallPermission-request-destinationPhoneNumber"></a>
The end user's phone number, in E.164 format, for which to retrieve the calling permission.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `\+[1-9]\d{1,14}`
Required: No

 ** [endUserBsuid](#API_GetWhatsAppCallPermission_RequestSyntax) **   <a name="Social-GetWhatsAppCallPermission-request-endUserBsuid"></a>
The business-scoped user identifier (BSUID) of the end user for which to retrieve the calling permission.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [originationPhoneNumberId](#API_GetWhatsAppCallPermission_RequestSyntax) **   <a name="Social-GetWhatsAppCallPermission-request-originationPhoneNumberId"></a>
The unique identifier of the business phone number for which to retrieve the calling permission. The phone number identifiers are formatted as `phone-number-id-01234567890123456789012345678901`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 115.
Pattern: `.*(^phone-number-id-.*$)|(^arn:.*:phone-number-id/[0-9a-zA-Z]+$).*`
Required: Yes

## Response Syntax
<a name="API_GetWhatsAppCallPermission_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "actions": [
      {
         "actionName": "string",
         "canPerformAction": boolean,
         "limits": [
            {
               "currentUsage": number,
               "limitExpirationTime": number,
               "maxAllowed": number,
               "timePeriod": "string"
            }
         ]
      }
   ],
   "permission": {
      "expirationTime": number,
      "status": "string"
   }
}
```

## Response Elements
<a name="API_GetWhatsAppCallPermission_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [actions](#API_GetWhatsAppCallPermission_ResponseSyntax) **   <a name="Social-GetWhatsAppCallPermission-response-actions"></a>
The calling actions the business can take with the end user, and any limits that apply to each action.
Type: Array of [WhatsAppCallPermissionAction](API_WhatsAppCallPermissionAction.md) objects

 ** [permission](#API_GetWhatsAppCallPermission_ResponseSyntax) **   <a name="Social-GetWhatsAppCallPermission-response-permission"></a>
The current calling permission state for the end user.
Type: [WhatsAppCallPermission](API_WhatsAppCallPermission.md) object

## Errors
<a name="API_GetWhatsAppCallPermission_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedByMetaException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** DependencyException **
Thrown when performing an action because a dependency would be broken.
HTTP Status Code: 502

 ** InternalServiceException **
The request processing has failed because of an unknown error, exception, or failure.
HTTP Status Code: 500

 ** InvalidParametersException **
One or more parameters provided to the action are not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource was not found.
HTTP Status Code: 404

 ** ThrottledRequestException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request contains an invalid parameter value.
HTTP Status Code: 400

## See Also
<a name="API_GetWhatsAppCallPermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/socialmessaging-2024-01-01/GetWhatsAppCallPermission)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/socialmessaging-2024-01-01/GetWhatsAppCallPermission)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/socialmessaging-2024-01-01/GetWhatsAppCallPermission)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/socialmessaging-2024-01-01/GetWhatsAppCallPermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/socialmessaging-2024-01-01/GetWhatsAppCallPermission)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/socialmessaging-2024-01-01/GetWhatsAppCallPermission)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/socialmessaging-2024-01-01/GetWhatsAppCallPermission)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/socialmessaging-2024-01-01/GetWhatsAppCallPermission)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/socialmessaging-2024-01-01/GetWhatsAppCallPermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/socialmessaging-2024-01-01/GetWhatsAppCallPermission)
