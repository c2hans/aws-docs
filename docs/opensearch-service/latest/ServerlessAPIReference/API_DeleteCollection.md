---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_DeleteCollection.html
---

# DeleteCollection
<a name="API_DeleteCollection"></a>

Deletes an OpenSearch Serverless collection. For more information, see [Creating and managing Amazon OpenSearch Serverless collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html).

## Request Syntax
<a name="API_DeleteCollection_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "id": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteCollection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_DeleteCollection_RequestSyntax) **   <a name="opensearchserverless-DeleteCollection-request-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [id](#API_DeleteCollection_RequestSyntax) **   <a name="opensearchserverless-DeleteCollection-request-id"></a>
The unique identifier of the collection. For example, `1iu5usc406kd`. The ID is part of the collection endpoint. You can also retrieve it using the [ListCollections](https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_ListCollections.html) API.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-z0-9]{3,40}`
Required: Yes

## Response Syntax
<a name="API_DeleteCollection_ResponseSyntax"></a>

```
{
   "deleteCollectionDetail": {
      "deletionProtection": "string",
      "id": "string",
      "name": "string",
      "status": "string"
   }
}
```

## Response Elements
<a name="API_DeleteCollection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [deleteCollectionDetail](#API_DeleteCollection_ResponseSyntax) **   <a name="opensearchserverless-DeleteCollection-response-deleteCollectionDetail"></a>
Details of the deleted collection.
Type: [DeleteCollectionDetail](API_DeleteCollectionDetail.md) object

## Errors
<a name="API_DeleteCollection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE\_FAILED state.
HTTP Status Code: 400

 ** InternalServerException **
Thrown when an error internal to the service occurs while processing a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Thrown when accessing or deleting a resource that does not exist.
HTTP Status Code: 400

 ** ValidationException **
Thrown when the HTTP request contains invalid input or is missing required input.
HTTP Status Code: 400

## Examples
<a name="API_DeleteCollection_Examples"></a>

### Delete a collection
<a name="API_DeleteCollection_Example_1"></a>

The following example deletes a collection.

#### Sample Request
<a name="API_DeleteCollection_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: aoss.<region>.<domain>
Accept-Encoding: identity
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.0
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: OpenSearchServerless.DeleteCollection

{
  "id": "07tjusf2h91cunochc",
  "clientToken": "f576fe66-8dd5-11ec-b909-0242ac120004"
}
```

#### Sample Response
<a name="API_DeleteCollection_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
x-amz-crc32: <Checksum>
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
   "deleteCollectionDetail":{
      "id":"07tjusf2h91cunochc",
      "name":"my-collection",
      "status":"DELETING"
   }
}
```

## See Also
<a name="API_DeleteCollection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/DeleteCollection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/DeleteCollection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/DeleteCollection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/DeleteCollection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/DeleteCollection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/DeleteCollection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/DeleteCollection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/DeleteCollection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/DeleteCollection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/DeleteCollection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
