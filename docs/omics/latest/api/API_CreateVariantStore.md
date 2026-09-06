---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_CreateVariantStore.html
---

# CreateVariantStore
<a name="API_CreateVariantStore"></a>

**Important**
 AWS HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS HealthOmics variant store and annotation store availability change](https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html).

Creates a variant store.

## Request Syntax
<a name="API_CreateVariantStore_RequestSyntax"></a>

```
POST /variantStore HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "name": "{{string}}",
   "reference": { ... },
   "sseConfig": {
      "keyArn": "{{string}}",
      "type": "{{string}}"
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateVariantStore_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateVariantStore_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateVariantStore_RequestSyntax) **   <a name="omics-CreateVariantStore-request-description"></a>
A description for the store.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [name](#API_CreateVariantStore_RequestSyntax) **   <a name="omics-CreateVariantStore-request-name"></a>
A name for the store.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `([a-z]){1}([a-z0-9_]){2,254}`
Required: No

 ** [reference](#API_CreateVariantStore_RequestSyntax) **   <a name="omics-CreateVariantStore-request-reference"></a>
The genome reference for the store's variants.
Type: [ReferenceItem](API_ReferenceItem.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [sseConfig](#API_CreateVariantStore_RequestSyntax) **   <a name="omics-CreateVariantStore-request-sseConfig"></a>
Server-side encryption (SSE) settings for the store.
Type: [SseConfig](API_SseConfig.md) object
Required: No

 ** [tags](#API_CreateVariantStore_RequestSyntax) **   <a name="omics-CreateVariantStore-request-tags"></a>
Tags for the store.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateVariantStore_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationTime": "string",
   "id": "string",
   "name": "string",
   "reference": { ... },
   "status": "string"
}
```

## Response Elements
<a name="API_CreateVariantStore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_CreateVariantStore_ResponseSyntax) **   <a name="omics-CreateVariantStore-response-creationTime"></a>
When the store was created.
Type: Timestamp

 ** [id](#API_CreateVariantStore_ResponseSyntax) **   <a name="omics-CreateVariantStore-response-id"></a>
The store's ID.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [name](#API_CreateVariantStore_ResponseSyntax) **   <a name="omics-CreateVariantStore-response-name"></a>
The store's name.
Type: String

 ** [reference](#API_CreateVariantStore_ResponseSyntax) **   <a name="omics-CreateVariantStore-response-reference"></a>
The store's genome reference.
Type: [ReferenceItem](API_ReferenceItem.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [status](#API_CreateVariantStore_ResponseSyntax) **   <a name="omics-CreateVariantStore-response-status"></a>
The store's status.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | FAILED`

## Errors
<a name="API_CreateVariantStore_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request cannot be applied to the target resource in its current state.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The target resource was not found in the current Region.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateVariantStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/CreateVariantStore)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/CreateVariantStore)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/CreateVariantStore)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/CreateVariantStore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/CreateVariantStore)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/CreateVariantStore)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/CreateVariantStore)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/CreateVariantStore)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/CreateVariantStore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/CreateVariantStore)
