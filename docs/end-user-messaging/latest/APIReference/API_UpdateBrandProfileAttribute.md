---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_UpdateBrandProfileAttribute.html
---

# UpdateBrandProfileAttribute
<a name="API_UpdateBrandProfileAttribute"></a>

Updates the value, description, or category of an existing brand profile attribute.

## Request Syntax
<a name="API_UpdateBrandProfileAttribute_RequestSyntax"></a>

```
PUT /v1/brand-profiles/{{brandProfileId}}/attributes/{{attributeName}} HTTP/1.1
Content-type: application/json

{
   "attachmentBody": {{blob}},
   "attributeValue": "{{string}}",
   "category": "{{string}}",
   "description": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateBrandProfileAttribute_RequestParameters"></a>

The request uses the following URI parameters.

 ** [attributeName](#API_UpdateBrandProfileAttribute_RequestSyntax) **   <a name="endusermessaging-UpdateBrandProfileAttribute-request-uri-attributeName"></a>
The name of the brand profile attribute. The name is unique within a brand profile.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_ -]*[A-Za-z0-9_-][A-Za-z0-9_ -]*`
Required: Yes

 ** [brandProfileId](#API_UpdateBrandProfileAttribute_RequestSyntax) **   <a name="endusermessaging-UpdateBrandProfileAttribute-request-uri-brandProfileId"></a>
The unique identifier of the brand profile. You can specify either the bare ID or the full Amazon Resource Name (ARN).
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Request Body
<a name="API_UpdateBrandProfileAttribute_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [attachmentBody](#API_UpdateBrandProfileAttribute_RequestSyntax) **   <a name="endusermessaging-UpdateBrandProfileAttribute-request-attachmentBody"></a>
The binary content for an attribute of type IMAGE or DOCUMENT. The content is base64-encoded when it is sent over the wire.
Type: Base64-encoded binary data object
Required: No

 ** [attributeValue](#API_UpdateBrandProfileAttribute_RequestSyntax) **   <a name="endusermessaging-UpdateBrandProfileAttribute-request-attributeValue"></a>
The text value of the attribute. This value applies to attributes of type TEXT.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** [category](#API_UpdateBrandProfileAttribute_RequestSyntax) **   <a name="endusermessaging-UpdateBrandProfileAttribute-request-category"></a>
The category of the attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** [description](#API_UpdateBrandProfileAttribute_RequestSyntax) **   <a name="endusermessaging-UpdateBrandProfileAttribute-request-description"></a>
A description of the attribute.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_UpdateBrandProfileAttribute_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "attributeName": "string",
   "attributeType": "string",
   "attributeValue": "string",
   "category": "string",
   "createdAt": number,
   "description": "string",
   "mediaContentType": "string",
   "mediaSizeBytes": number,
   "updatedAt": number
}
```

## Response Elements
<a name="API_UpdateBrandProfileAttribute_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [attributeName](#API_UpdateBrandProfileAttribute_ResponseSyntax) **   <a name="endusermessaging-UpdateBrandProfileAttribute-response-attributeName"></a>
The name of the brand profile attribute. The name is unique within a brand profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_ -]*[A-Za-z0-9_-][A-Za-z0-9_ -]*`

 ** [attributeType](#API_UpdateBrandProfileAttribute_ResponseSyntax) **   <a name="endusermessaging-UpdateBrandProfileAttribute-response-attributeType"></a>
The type of the attribute. TEXT stores an inline value. IMAGE and DOCUMENT store binary media that you upload.
Type: String
Valid Values: `TEXT | IMAGE | DOCUMENT`

 ** [attributeValue](#API_UpdateBrandProfileAttribute_ResponseSyntax) **   <a name="endusermessaging-UpdateBrandProfileAttribute-response-attributeValue"></a>
The text value of the attribute. This value applies to attributes of type TEXT.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.

 ** [category](#API_UpdateBrandProfileAttribute_ResponseSyntax) **   <a name="endusermessaging-UpdateBrandProfileAttribute-response-category"></a>
The category of the attribute.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [createdAt](#API_UpdateBrandProfileAttribute_ResponseSyntax) **   <a name="endusermessaging-UpdateBrandProfileAttribute-response-createdAt"></a>
The time when the resource was created, in Unix epoch time.
Type: Timestamp

 ** [description](#API_UpdateBrandProfileAttribute_ResponseSyntax) **   <a name="endusermessaging-UpdateBrandProfileAttribute-response-description"></a>
A description of the attribute.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [mediaContentType](#API_UpdateBrandProfileAttribute_ResponseSyntax) **   <a name="endusermessaging-UpdateBrandProfileAttribute-response-mediaContentType"></a>
The MIME content type of the attribute media.
Type: String

 ** [mediaSizeBytes](#API_UpdateBrandProfileAttribute_ResponseSyntax) **   <a name="endusermessaging-UpdateBrandProfileAttribute-response-mediaSizeBytes"></a>
The size of the attribute media, in bytes.
Type: Long

 ** [updatedAt](#API_UpdateBrandProfileAttribute_ResponseSyntax) **   <a name="endusermessaging-UpdateBrandProfileAttribute-response-updatedAt"></a>
The time when the resource was last updated, in Unix epoch time.
Type: Timestamp

## Errors
<a name="API_UpdateBrandProfileAttribute_Errors"></a>

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
<a name="API_UpdateBrandProfileAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/endusermessaging-2026-09-21/UpdateBrandProfileAttribute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/endusermessaging-2026-09-21/UpdateBrandProfileAttribute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/UpdateBrandProfileAttribute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/endusermessaging-2026-09-21/UpdateBrandProfileAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/UpdateBrandProfileAttribute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/endusermessaging-2026-09-21/UpdateBrandProfileAttribute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/endusermessaging-2026-09-21/UpdateBrandProfileAttribute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/endusermessaging-2026-09-21/UpdateBrandProfileAttribute)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/endusermessaging-2026-09-21/UpdateBrandProfileAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/UpdateBrandProfileAttribute)
