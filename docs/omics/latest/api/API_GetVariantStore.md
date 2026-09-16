---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_GetVariantStore.html
---

# GetVariantStore
<a name="API_GetVariantStore"></a>

**Important**
 AWS HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS HealthOmics variant store and annotation store availability change](https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html).

Gets information about a variant store.

## Request Syntax
<a name="API_GetVariantStore_RequestSyntax"></a>

```
GET /variantStore/{{name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetVariantStore_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_GetVariantStore_RequestSyntax) **   <a name="omics-GetVariantStore-request-uri-name"></a>
The store's name.
Required: Yes

## Request Body
<a name="API_GetVariantStore_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetVariantStore_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationTime": "string",
   "description": "string",
   "id": "string",
   "name": "string",
   "reference": { ... },
   "sseConfig": {
      "keyArn": "string",
      "type": "string"
   },
   "status": "string",
   "statusMessage": "string",
   "storeArn": "string",
   "storeSizeBytes": number,
   "tags": {
      "string" : "string"
   },
   "updateTime": "string"
}
```

## Response Elements
<a name="API_GetVariantStore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_GetVariantStore_ResponseSyntax) **   <a name="omics-GetVariantStore-response-creationTime"></a>
When the store was created.
Type: Timestamp

 ** [description](#API_GetVariantStore_ResponseSyntax) **   <a name="omics-GetVariantStore-response-description"></a>
The store's description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [id](#API_GetVariantStore_ResponseSyntax) **   <a name="omics-GetVariantStore-response-id"></a>
The store's ID.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [name](#API_GetVariantStore_ResponseSyntax) **   <a name="omics-GetVariantStore-response-name"></a>
The store's name.
Type: String

 ** [reference](#API_GetVariantStore_ResponseSyntax) **   <a name="omics-GetVariantStore-response-reference"></a>
The store's genome reference.
Type: [ReferenceItem](API_ReferenceItem.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [sseConfig](#API_GetVariantStore_ResponseSyntax) **   <a name="omics-GetVariantStore-response-sseConfig"></a>
The store's server-side encryption (SSE) settings.
Type: [SseConfig](API_SseConfig.md) object

 ** [status](#API_GetVariantStore_ResponseSyntax) **   <a name="omics-GetVariantStore-response-status"></a>
The store's status.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | FAILED`

 ** [statusMessage](#API_GetVariantStore_ResponseSyntax) **   <a name="omics-GetVariantStore-response-statusMessage"></a>
The store's status message.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [storeArn](#API_GetVariantStore_ResponseSyntax) **   <a name="omics-GetVariantStore-response-storeArn"></a>
The store's ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:([^: ]*):([^: ]*):([^: ]*):([0-9]{12}):([^: ]*)`

 ** [storeSizeBytes](#API_GetVariantStore_ResponseSyntax) **   <a name="omics-GetVariantStore-response-storeSizeBytes"></a>
The store's size in bytes.
Type: Long

 ** [tags](#API_GetVariantStore_ResponseSyntax) **   <a name="omics-GetVariantStore-response-tags"></a>
The store's tags.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [updateTime](#API_GetVariantStore_ResponseSyntax) **   <a name="omics-GetVariantStore-response-updateTime"></a>
When the store was updated.
Type: Timestamp

## Errors
<a name="API_GetVariantStore_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The target resource was not found in the current Region.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetVariantStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/GetVariantStore)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/GetVariantStore)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/GetVariantStore)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/GetVariantStore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/GetVariantStore)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/GetVariantStore)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/GetVariantStore)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/GetVariantStore)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/GetVariantStore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/GetVariantStore)
