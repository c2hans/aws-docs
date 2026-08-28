---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_GetAnnotationStore.html
---

# GetAnnotationStore
<a name="API_GetAnnotationStore"></a>

**Important**
 AWS HealthOmics variant stores and annotation stores are no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS HealthOmics variant store and annotation store availability change](https://docs.aws.amazon.com/omics/latest/dev/variant-store-availability-change.html).

Gets information about an annotation store.

## Request Syntax
<a name="API_GetAnnotationStore_RequestSyntax"></a>

```
GET /annotationStore/{{name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAnnotationStore_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_GetAnnotationStore_RequestSyntax) **   <a name="omics-GetAnnotationStore-request-uri-name"></a>
The store's name.
Required: Yes

## Request Body
<a name="API_GetAnnotationStore_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAnnotationStore_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationTime": "string",
   "description": "string",
   "id": "string",
   "name": "string",
   "numVersions": number,
   "reference": { ... },
   "sseConfig": {
      "keyArn": "string",
      "type": "string"
   },
   "status": "string",
   "statusMessage": "string",
   "storeArn": "string",
   "storeFormat": "string",
   "storeOptions": { ... },
   "storeSizeBytes": number,
   "tags": {
      "string" : "string"
   },
   "updateTime": "string"
}
```

## Response Elements
<a name="API_GetAnnotationStore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_GetAnnotationStore_ResponseSyntax) **   <a name="omics-GetAnnotationStore-response-creationTime"></a>
When the store was created.
Type: Timestamp

 ** [description](#API_GetAnnotationStore_ResponseSyntax) **   <a name="omics-GetAnnotationStore-response-description"></a>
The store's description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [id](#API_GetAnnotationStore_ResponseSyntax) **   <a name="omics-GetAnnotationStore-response-id"></a>
The store's ID.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [name](#API_GetAnnotationStore_ResponseSyntax) **   <a name="omics-GetAnnotationStore-response-name"></a>
The store's name.
Type: String

 ** [numVersions](#API_GetAnnotationStore_ResponseSyntax) **   <a name="omics-GetAnnotationStore-response-numVersions"></a>
 An integer indicating how many versions of an annotation store exist.
Type: Integer

 ** [reference](#API_GetAnnotationStore_ResponseSyntax) **   <a name="omics-GetAnnotationStore-response-reference"></a>
The store's genome reference.
Type: [ReferenceItem](API_ReferenceItem.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [sseConfig](#API_GetAnnotationStore_ResponseSyntax) **   <a name="omics-GetAnnotationStore-response-sseConfig"></a>
The store's server-side encryption (SSE) settings.
Type: [SseConfig](API_SseConfig.md) object

 ** [status](#API_GetAnnotationStore_ResponseSyntax) **   <a name="omics-GetAnnotationStore-response-status"></a>
The store's status.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | FAILED`

 ** [statusMessage](#API_GetAnnotationStore_ResponseSyntax) **   <a name="omics-GetAnnotationStore-response-statusMessage"></a>
A status message.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [storeArn](#API_GetAnnotationStore_ResponseSyntax) **   <a name="omics-GetAnnotationStore-response-storeArn"></a>
The store's ARN.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:([^: ]*):([^: ]*):([^: ]*):([0-9]{12}):([^: ]*)`

 ** [storeFormat](#API_GetAnnotationStore_ResponseSyntax) **   <a name="omics-GetAnnotationStore-response-storeFormat"></a>
The store's annotation file format.
Type: String
Valid Values: `GFF | TSV | VCF`

 ** [storeOptions](#API_GetAnnotationStore_ResponseSyntax) **   <a name="omics-GetAnnotationStore-response-storeOptions"></a>
The store's parsing options.
Type: [StoreOptions](API_StoreOptions.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [storeSizeBytes](#API_GetAnnotationStore_ResponseSyntax) **   <a name="omics-GetAnnotationStore-response-storeSizeBytes"></a>
The store's size in bytes.
Type: Long

 ** [tags](#API_GetAnnotationStore_ResponseSyntax) **   <a name="omics-GetAnnotationStore-response-tags"></a>
The store's tags.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [updateTime](#API_GetAnnotationStore_ResponseSyntax) **   <a name="omics-GetAnnotationStore-response-updateTime"></a>
When the store was updated.
Type: Timestamp

## Errors
<a name="API_GetAnnotationStore_Errors"></a>

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
<a name="API_GetAnnotationStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/GetAnnotationStore)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/GetAnnotationStore)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/GetAnnotationStore)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/GetAnnotationStore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/GetAnnotationStore)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/GetAnnotationStore)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/GetAnnotationStore)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/GetAnnotationStore)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/GetAnnotationStore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/GetAnnotationStore)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
