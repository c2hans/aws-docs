---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateCollection.html
---

# CreateCollection
<a name="API_CreateCollection"></a>

Creates a new OpenSearch Serverless collection. For more information, see [Creating and managing Amazon OpenSearch Serverless collections](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-manage.html).

## Request Syntax
<a name="API_CreateCollection_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "collectionGroupName": "{{string}}",
   "deletionProtection": "{{string}}",
   "description": "{{string}}",
   "encryptionConfig": {
      "aWSOwnedKey": {{boolean}},
      "kmsKeyArn": "{{string}}"
   },
   "name": "{{string}}",
   "standbyReplicas": "{{string}}",
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "type": "{{string}}",
   "vectorOptions": {
      "ServerlessVectorAcceleration": "{{string}}"
   }
}
```

## Request Parameters
<a name="API_CreateCollection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateCollection_RequestSyntax) **   <a name="opensearchserverless-CreateCollection-request-clientToken"></a>
Unique, case-sensitive identifier to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [collectionGroupName](#API_CreateCollection_RequestSyntax) **   <a name="opensearchserverless-CreateCollection-request-collectionGroupName"></a>
The name of the collection group to associate with the collection.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]+`
Required: No

 ** [deletionProtection](#API_CreateCollection_RequestSyntax) **   <a name="opensearchserverless-CreateCollection-request-deletionProtection"></a>
Indicates whether to enable deletion protection for the collection. When set to `ENABLED`, the collection cannot be deleted.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [description](#API_CreateCollection_RequestSyntax) **   <a name="opensearchserverless-CreateCollection-request-description"></a>
Description of the collection.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Required: No

 ** [encryptionConfig](#API_CreateCollection_RequestSyntax) **   <a name="opensearchserverless-CreateCollection-request-encryptionConfig"></a>
Encryption settings for the collection.
Type: [EncryptionConfig](API_EncryptionConfig.md) object
Required: No

 ** [name](#API_CreateCollection_RequestSyntax) **   <a name="opensearchserverless-CreateCollection-request-name"></a>
Name of the collection.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 64.
Pattern: `[a-z][a-z0-9-]+`
Required: Yes

 ** [standbyReplicas](#API_CreateCollection_RequestSyntax) **   <a name="opensearchserverless-CreateCollection-request-standbyReplicas"></a>
Indicates whether standby replicas should be used for a collection.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

 ** [tags](#API_CreateCollection_RequestSyntax) **   <a name="opensearchserverless-CreateCollection-request-tags"></a>
An arbitrary set of tags (key–value pairs) to associate with the OpenSearch Serverless collection.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [type](#API_CreateCollection_RequestSyntax) **   <a name="opensearchserverless-CreateCollection-request-type"></a>
The type of collection.
Type: String
Valid Values: `SEARCH | TIMESERIES | VECTORSEARCH`
Required: No

 ** [vectorOptions](#API_CreateCollection_RequestSyntax) **   <a name="opensearchserverless-CreateCollection-request-vectorOptions"></a>
Configuration options for vector search capabilities in the collection.
Type: [VectorOptions](API_VectorOptions.md) object
Required: No

## Response Syntax
<a name="API_CreateCollection_ResponseSyntax"></a>

```
{
   "createCollectionDetail": {
      "arn": "string",
      "collectionGroupName": "string",
      "createdDate": number,
      "deletionProtection": "string",
      "description": "string",
      "id": "string",
      "kmsKeyArn": "string",
      "lastModifiedDate": number,
      "name": "string",
      "standbyReplicas": "string",
      "status": "string",
      "type": "string",
      "vectorOptions": {
         "ServerlessVectorAcceleration": "string"
      }
   }
}
```

## Response Elements
<a name="API_CreateCollection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createCollectionDetail](#API_CreateCollection_ResponseSyntax) **   <a name="opensearchserverless-CreateCollection-response-createCollectionDetail"></a>
Details about the collection.
Type: [CreateCollectionDetail](API_CreateCollectionDetail.md) object

## Errors
<a name="API_CreateCollection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
When creating a resource, thrown when a resource with the same name already exists or is being created. When deleting a resource, thrown when the resource is not in the ACTIVE, FAILED, or UPDATE\_FAILED state.
HTTP Status Code: 400

 ** InternalServerException **
Thrown when an error internal to the service occurs while processing a request.
HTTP Status Code: 500

 ** OcuLimitExceededException **
Thrown when the collection you're attempting to create results in a number of search or indexing OCUs that exceeds the account limit.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
Thrown when you attempt to create more resources than the service allows based on service quotas.
HTTP Status Code: 400

 ** ValidationException **
Thrown when the HTTP request contains invalid input or is missing required input.
HTTP Status Code: 400

## Examples
<a name="API_CreateCollection_Examples"></a>

### Create a collection
<a name="API_CreateCollection_Example_1"></a>

The following example creates a collection.

#### Sample Request
<a name="API_CreateCollection_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: aoss.<region>.<domain>
Accept-Encoding: identity
Content-Length: <PayloadSizeBytes>
User-Agent: <UserAgentString>
Content-Type: application/x-amz-json-1.0
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=<Headers>, Signature=<Signature>
X-Amz-Date: <Date>
X-Amz-Target: OpenSearchServerless.CreateCollection

{
  "name": "my-collection-name",
  "description": "collection-description",
  "clientToken": "f576fe66-8dd5-11ec-b909-0242ac120004",
  "type": "SEARCH"
}
```

#### Sample Response
<a name="API_CreateCollection_Example_1_Response"></a>

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
x-amz-crc32: <Checksum>
Content-Type: application/x-amz-json-1.0
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
   "createCollectionDetail":{
      "arn":"arn:aws:aoss:us-east-1:123456789012:collection/07tjusf2h91cunochc",
      "createdDate":1637012666117,
      "description":"collection-description",
      "kmsKeyArn": "auto",
      "type": "SEARCH",
      "id":"07tjusf2h91cunochc",
      "name":"my-collection-name",
      "status":"CREATING"
   }
}
```

## See Also
<a name="API_CreateCollection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/CreateCollection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/CreateCollection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/CreateCollection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/CreateCollection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/CreateCollection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/CreateCollection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/CreateCollection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/CreateCollection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/CreateCollection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/CreateCollection)
