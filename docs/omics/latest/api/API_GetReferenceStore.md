---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_GetReferenceStore.html
---

# GetReferenceStore
<a name="API_GetReferenceStore"></a>

Gets information about a reference store.

## Request Syntax
<a name="API_GetReferenceStore_RequestSyntax"></a>

```
GET /referencestore/{{id}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetReferenceStore_RequestParameters"></a>

The request uses the following URI parameters.

 ** [id](#API_GetReferenceStore_RequestSyntax) **   <a name="omics-GetReferenceStore-request-uri-id"></a>
The store's ID.
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`
Required: Yes

## Request Body
<a name="API_GetReferenceStore_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetReferenceStore_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "creationTime": "string",
   "description": "string",
   "id": "string",
   "name": "string",
   "sseConfig": {
      "keyArn": "string",
      "type": "string"
   }
}
```

## Response Elements
<a name="API_GetReferenceStore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_GetReferenceStore_ResponseSyntax) **   <a name="omics-GetReferenceStore-response-arn"></a>
The store's ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `arn:.+`

 ** [creationTime](#API_GetReferenceStore_ResponseSyntax) **   <a name="omics-GetReferenceStore-response-creationTime"></a>
When the store was created.
Type: Timestamp

 ** [description](#API_GetReferenceStore_ResponseSyntax) **   <a name="omics-GetReferenceStore-response-description"></a>
The store's description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [id](#API_GetReferenceStore_ResponseSyntax) **   <a name="omics-GetReferenceStore-response-id"></a>
The store's ID.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 36.
Pattern: `[0-9]+`

 ** [name](#API_GetReferenceStore_ResponseSyntax) **   <a name="omics-GetReferenceStore-response-name"></a>
The store's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[\p{L}||\p{M}||\p{Z}||\p{S}||\p{N}||\p{P}]+`

 ** [sseConfig](#API_GetReferenceStore_ResponseSyntax) **   <a name="omics-GetReferenceStore-response-sseConfig"></a>
The store's server-side encryption (SSE) settings.
Type: [SseConfig](API_SseConfig.md) object

## Errors
<a name="API_GetReferenceStore_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

 ** RequestTimeoutException **
The request timed out.
HTTP Status Code: 408

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
<a name="API_GetReferenceStore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/GetReferenceStore)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/GetReferenceStore)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/GetReferenceStore)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/GetReferenceStore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/GetReferenceStore)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/GetReferenceStore)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/GetReferenceStore)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/GetReferenceStore)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/GetReferenceStore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/GetReferenceStore)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
