---
source_url: https://docs.aws.amazon.com/end-user-messaging/latest/APIReference/API_CreateBrandProfileAttributes.html
---

# CreateBrandProfileAttributes
<a name="API_CreateBrandProfileAttributes"></a>

Creates up to 10 attributes for a brand profile in a single request. For attributes of type IMAGE or DOCUMENT, the response includes a presigned Amazon S3 URL that you use to upload the media. This operation is atomic: either all of the attributes are created, or none of them are.

## Request Syntax
<a name="API_CreateBrandProfileAttributes_RequestSyntax"></a>

```
POST /v1/brand-profiles/{{brandProfileId}}/attributes HTTP/1.1
Content-type: application/json

{
   "attributes": [
      {
         "attachmentBody": {{blob}},
         "attributeName": "{{string}}",
         "attributeType": "{{string}}",
         "attributeValue": "{{string}}",
         "category": "{{string}}",
         "description": "{{string}}"
      }
   ],
   "clientToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateBrandProfileAttributes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [brandProfileId](#API_CreateBrandProfileAttributes_RequestSyntax) **   <a name="endusermessaging-CreateBrandProfileAttributes-request-uri-brandProfileId"></a>
The unique identifier of the brand profile. You can specify either the bare ID or the full Amazon Resource Name (ARN).
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]+`
Required: Yes

## Request Body
<a name="API_CreateBrandProfileAttributes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [attributes](#API_CreateBrandProfileAttributes_RequestSyntax) **   <a name="endusermessaging-CreateBrandProfileAttributes-request-attributes"></a>
The brand profile attributes.
Type: Array of [BrandProfileAttributeInput](API_BrandProfileAttributeInput.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** [clientToken](#API_CreateBrandProfileAttributes_RequestSyntax) **   <a name="endusermessaging-CreateBrandProfileAttributes-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you do not specify a client token, the AWS SDK automatically generates one.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

## Response Syntax
<a name="API_CreateBrandProfileAttributes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "attributes": [
      {
         "attributeName": "string",
         "attributeType": "string",
         "mediaDownloadUrl": "string"
      }
   ]
}
```

## Response Elements
<a name="API_CreateBrandProfileAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [attributes](#API_CreateBrandProfileAttributes_ResponseSyntax) **   <a name="endusermessaging-CreateBrandProfileAttributes-response-attributes"></a>
The brand profile attributes.
Type: Array of [BrandProfileAttributeOutput](API_BrandProfileAttributeOutput.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.

## Errors
<a name="API_CreateBrandProfileAttributes_Errors"></a>

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
<a name="API_CreateBrandProfileAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/endusermessaging-2026-09-21/CreateBrandProfileAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/endusermessaging-2026-09-21/CreateBrandProfileAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/endusermessaging-2026-09-21/CreateBrandProfileAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/endusermessaging-2026-09-21/CreateBrandProfileAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/endusermessaging-2026-09-21/CreateBrandProfileAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/endusermessaging-2026-09-21/CreateBrandProfileAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/endusermessaging-2026-09-21/CreateBrandProfileAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/endusermessaging-2026-09-21/CreateBrandProfileAttributes)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/endusermessaging-2026-09-21/CreateBrandProfileAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/endusermessaging-2026-09-21/CreateBrandProfileAttributes)
