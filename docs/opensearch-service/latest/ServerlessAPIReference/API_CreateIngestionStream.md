---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateIngestionStream.html
---

# CreateIngestionStream
<a name="API_CreateIngestionStream"></a>

Creates an ingestion stream that continuously ingests data from an Amazon S3 bucket into an index in an OpenSearch Serverless collection. An ingestion stream processes Amazon S3 event notifications delivered to an Amazon SQS queue and ingests new objects as they arrive. The stream continues to ingest data until you delete it. To perform a one-time bulk ingestion instead, use `CreateIngestionJob`.

## Request Syntax
<a name="API_CreateIngestionStream_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "collectionId": "{{string}}",
   "failureIndexName": "{{string}}",
   "indexName": "{{string}}",
   "ingestionStreamName": "{{string}}",
   "roleArn": "{{string}}",
   "source": {
      "s3": {
         "buckets": [
            {
               "bucket": "{{string}}",
               "bucketOwnerAccountId": "{{string}}",
               "initialScan": "{{string}}"
            }
         ],
         "sqsArn": "{{string}}"
      }
   },
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateIngestionStream_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateIngestionStream_RequestSyntax) **   <a name="opensearchserverless-CreateIngestionStream-request-clientToken"></a>
Unique, case-sensitive identifier to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [collectionId](#API_CreateIngestionStream_RequestSyntax) **   <a name="opensearchserverless-CreateIngestionStream-request-collectionId"></a>
The unique identifier of the collection to ingest data into.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-z0-9]{3,40}`
Required: Yes

 ** [failureIndexName](#API_CreateIngestionStream_RequestSyntax) **   <a name="opensearchserverless-CreateIngestionStream-request-failureIndexName"></a>
The name of the index where documents that fail to be ingested are recorded.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-z0-9.][a-z0-9._-]*`
Required: No

 ** [indexName](#API_CreateIngestionStream_RequestSyntax) **   <a name="opensearchserverless-CreateIngestionStream-request-indexName"></a>
The name of the index to ingest documents into.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-z0-9.][a-z0-9._-]*`
Required: Yes

 ** [ingestionStreamName](#API_CreateIngestionStream_RequestSyntax) **   <a name="opensearchserverless-CreateIngestionStream-request-ingestionStreamName"></a>
The name of the ingestion stream. The name must be unique within the collection.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]*`
Required: Yes

 ** [roleArn](#API_CreateIngestionStream_RequestSyntax) **   <a name="opensearchserverless-CreateIngestionStream-request-roleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that OpenSearch Serverless assumes to read data from the source. The role must be in the same account as the collection.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:aws|aws-cn|aws-us-gov|aws-iso|aws-iso-b|aws-iso-c|aws-iso-d|aws-iso-e):iam::\d{12}:role/.+`
Required: Yes

 ** [source](#API_CreateIngestionStream_RequestSyntax) **   <a name="opensearchserverless-CreateIngestionStream-request-source"></a>
The Amazon S3 source to ingest data from, including the Amazon SQS queue that receives S3 event notifications.
Type: [IngestionStreamSource](API_IngestionStreamSource.md) object
Required: Yes

 ** [tags](#API_CreateIngestionStream_RequestSyntax) **   <a name="opensearchserverless-CreateIngestionStream-request-tags"></a>
An arbitrary set of tags (key–value pairs) to associate with the ingestion stream.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateIngestionStream_ResponseSyntax"></a>

```
{
   "ingestionStreamDetail": {
      "activeAlerts": [
         {
            "code": "string",
            "message": "string"
         }
      ],
      "arn": "string",
      "collectionId": "string",
      "createdAt": number,
      "failureIndexName": "string",
      "failureReasons": [
         {
            "code": "string",
            "message": "string"
         }
      ],
      "indexName": "string",
      "ingestionStreamId": "string",
      "ingestionStreamName": "string",
      "revision": number,
      "roleArn": "string",
      "source": {
         "s3": {
            "buckets": [
               {
                  "bucket": "string",
                  "bucketOwnerAccountId": "string",
                  "initialScan": "string"
               }
            ],
            "sqsArn": "string"
         }
      },
      "state": "string",
      "statistics": {
         "s3": {
            "objectsDiscovered": number,
            "objectsFailed": number,
            "objectsIngested": number
         }
      },
      "status": "string",
      "updatedAt": number
   }
}
```

## Response Elements
<a name="API_CreateIngestionStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ingestionStreamDetail](#API_CreateIngestionStream_ResponseSyntax) **   <a name="opensearchserverless-CreateIngestionStream-response-ingestionStreamDetail"></a>
Details about the created ingestion stream.
Type: [IngestionStreamDetail](API_IngestionStreamDetail.md) object

## Errors
<a name="API_CreateIngestionStream_Errors"></a>

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

 ** ServiceQuotaExceededException **
Thrown when you attempt to create more resources than the service allows based on service quotas.
HTTP Status Code: 400

 ** ValidationException **
Thrown when the HTTP request contains invalid input or is missing required input.
HTTP Status Code: 400

## See Also
<a name="API_CreateIngestionStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/CreateIngestionStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/CreateIngestionStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/CreateIngestionStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/CreateIngestionStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/CreateIngestionStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/CreateIngestionStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/CreateIngestionStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/CreateIngestionStream)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/CreateIngestionStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/CreateIngestionStream)
