---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_UpdateCollection.html
---

# UpdateCollection
<a name="API_UpdateCollection"></a>

Updates an OpenSearch Serverless collection.

## Request Syntax
<a name="API_UpdateCollection_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "deletionProtection": "{{string}}",
   "description": "{{string}}",
   "id": "{{string}}",
   "vectorOptions": {
      "ServerlessVectorAcceleration": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateCollection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateCollection_RequestSyntax) **   <a name="opensearchserverless-UpdateCollection-request-clientToken"></a>
Unique, case-sensitive identifier to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [deletionProtection](#API_UpdateCollection_RequestSyntax) **   <a name="opensearchserverless-UpdateCollection-request-deletionProtection"></a>
Indicates whether to enable or disable deletion protection for the collection. When set to `ENABLED`, the collection cannot be deleted.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [description](#API_UpdateCollection_RequestSyntax) **   <a name="opensearchserverless-UpdateCollection-request-description"></a>
A description of the collection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** [id](#API_UpdateCollection_RequestSyntax) **   <a name="opensearchserverless-UpdateCollection-request-id"></a>
The unique identifier of the collection.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-z0-9]{3,40}`
Required: Yes

 ** [vectorOptions](#API_UpdateCollection_RequestSyntax) **   <a name="opensearchserverless-UpdateCollection-request-vectorOptions"></a>
Configuration options for vector search capabilities in the collection.
Type: [VectorOptions](API_VectorOptions.md) object
Required: No

## Response Syntax
<a name="API_UpdateCollection_ResponseSyntax"></a>

```
{
   "updateCollectionDetail": {
      "arn": "string",
      "createdDate": number,
      "deletionProtection": "string",
      "description": "string",
      "id": "string",
      "lastModifiedDate": number,
      "name": "string",
      "status": "string",
      "type": "string",
      "vectorOptions": {
         "ServerlessVectorAcceleration": "string"
      }
   }
}
```

## Response Elements
<a name="API_UpdateCollection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [updateCollectionDetail](#API_UpdateCollection_ResponseSyntax) **   <a name="opensearchserverless-UpdateCollection-response-updateCollectionDetail"></a>
Details about the updated collection.
Type: [UpdateCollectionDetail](API_UpdateCollectionDetail.md) object

## Errors
<a name="API_UpdateCollection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE\_FAILED state.
HTTP Status Code: 400

 ** InternalServerException **
Thrown when an error internal to the service occurs while processing a request.
HTTP Status Code: 500

 ** ValidationException **
Thrown when the HTTP request contains invalid input or is missing required input.
HTTP Status Code: 400

## See Also
<a name="API_UpdateCollection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/UpdateCollection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/UpdateCollection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/UpdateCollection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/UpdateCollection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/UpdateCollection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/UpdateCollection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/UpdateCollection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/UpdateCollection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/UpdateCollection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/UpdateCollection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
