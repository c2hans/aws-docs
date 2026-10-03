---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_DeleteBrandProfileAttribute.html
---

# DeleteBrandProfileAttribute
<a name="API_DeleteBrandProfileAttribute"></a>

Deletes a brand profile attribute. If the attribute stores media, this operation also deletes the associated media.

## Request Syntax
<a name="API_DeleteBrandProfileAttribute_RequestSyntax"></a>

```
DELETE /v1/brand-profiles/{{brandProfileId}}/attributes/{{attributeName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteBrandProfileAttribute_RequestParameters"></a>

The request uses the following URI parameters.

 ** [attributeName](#API_DeleteBrandProfileAttribute_RequestSyntax) **   <a name="endusermessaging-DeleteBrandProfileAttribute-request-uri-attributeName"></a>
The name of the brand profile attribute. The name is unique within a brand profile.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_ -]*[A-Za-z0-9_-][A-Za-z0-9_ -]*`
Required: Yes

 ** [brandProfileId](#API_DeleteBrandProfileAttribute_RequestSyntax) **   <a name="endusermessaging-DeleteBrandProfileAttribute-request-uri-brandProfileId"></a>
The unique identifier of the brand profile. You can specify either the bare ID or the full Amazon Resource Name (ARN).
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Request Body
<a name="API_DeleteBrandProfileAttribute_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteBrandProfileAttribute_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "attributeName": "string",
   "brandProfileId": "string"
}
```

## Response Elements
<a name="API_DeleteBrandProfileAttribute_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [attributeName](#API_DeleteBrandProfileAttribute_ResponseSyntax) **   <a name="endusermessaging-DeleteBrandProfileAttribute-response-attributeName"></a>
The name of the brand profile attribute. The name is unique within a brand profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_ -]*[A-Za-z0-9_-][A-Za-z0-9_ -]*`

 ** [brandProfileId](#API_DeleteBrandProfileAttribute_ResponseSyntax) **   <a name="endusermessaging-DeleteBrandProfileAttribute-response-brandProfileId"></a>
The unique identifier of the brand profile.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`

## Errors
<a name="API_DeleteBrandProfileAttribute_Errors"></a>

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
<a name="API_DeleteBrandProfileAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/endusermessaging-2026-09-21/DeleteBrandProfileAttribute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/endusermessaging-2026-09-21/DeleteBrandProfileAttribute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/DeleteBrandProfileAttribute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/endusermessaging-2026-09-21/DeleteBrandProfileAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/DeleteBrandProfileAttribute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/endusermessaging-2026-09-21/DeleteBrandProfileAttribute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/endusermessaging-2026-09-21/DeleteBrandProfileAttribute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/endusermessaging-2026-09-21/DeleteBrandProfileAttribute)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/endusermessaging-2026-09-21/DeleteBrandProfileAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/DeleteBrandProfileAttribute)
