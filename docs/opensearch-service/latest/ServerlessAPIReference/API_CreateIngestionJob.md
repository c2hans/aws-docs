---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_CreateIngestionJob.html
---

# CreateIngestionJob
<a name="API_CreateIngestionJob"></a>

Creates an ingestion job that performs a one-time bulk ingestion of data from an Amazon S3 bucket into an index in an OpenSearch Serverless collection. An ingestion job scans the source bucket, indexes the documents it finds, and then completes. To continuously ingest new data as it arrives, use `CreateIngestionStream` instead.

## Request Syntax
<a name="API_CreateIngestionJob_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "collectionId": "{{string}}",
   "failureIndexName": "{{string}}",
   "indexName": "{{string}}",
   "ingestionJobName": "{{string}}",
   "source": {
      "s3": {
         "bucket": "{{string}}",
         "bucketOwnerAccountId": "{{string}}",
         "keyPrefix": "{{string}}"
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
<a name="API_CreateIngestionJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateIngestionJob_RequestSyntax) **   <a name="opensearchserverless-CreateIngestionJob-request-clientToken"></a>
Unique, case-sensitive identifier to ensure idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** [collectionId](#API_CreateIngestionJob_RequestSyntax) **   <a name="opensearchserverless-CreateIngestionJob-request-collectionId"></a>
The unique identifier of the collection to ingest data into.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-z0-9]{3,40}`
Required: Yes

 ** [failureIndexName](#API_CreateIngestionJob_RequestSyntax) **   <a name="opensearchserverless-CreateIngestionJob-request-failureIndexName"></a>
The name of the index where documents that fail to be ingested are recorded.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-z0-9.][a-z0-9._-]*`
Required: No

 ** [indexName](#API_CreateIngestionJob_RequestSyntax) **   <a name="opensearchserverless-CreateIngestionJob-request-indexName"></a>
The name of the index to ingest documents into.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-z0-9.][a-z0-9._-]*`
Required: Yes

 ** [ingestionJobName](#API_CreateIngestionJob_RequestSyntax) **   <a name="opensearchserverless-CreateIngestionJob-request-ingestionJobName"></a>
The name of the ingestion job. The name must be unique within the collection.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 32.
Pattern: `[a-z][a-z0-9-]*`
Required: Yes

 ** [source](#API_CreateIngestionJob_RequestSyntax) **   <a name="opensearchserverless-CreateIngestionJob-request-source"></a>
The Amazon S3 source to ingest data from.
Type: [IngestionJobSource](API_IngestionJobSource.md) object
Required: Yes

 ** [tags](#API_CreateIngestionJob_RequestSyntax) **   <a name="opensearchserverless-CreateIngestionJob-request-tags"></a>
An arbitrary set of tags (key–value pairs) to associate with the ingestion job.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateIngestionJob_ResponseSyntax"></a>

```
{
   "ingestionJobDetail": {
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
      "ingestionJobId": "string",
      "ingestionJobName": "string",
      "revision": number,
      "source": {
         "s3": {
            "bucket": "string",
            "bucketOwnerAccountId": "string",
            "keyPrefix": "string"
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
<a name="API_CreateIngestionJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ingestionJobDetail](#API_CreateIngestionJob_ResponseSyntax) **   <a name="opensearchserverless-CreateIngestionJob-response-ingestionJobDetail"></a>
Details about the created ingestion job.
Type: [IngestionJobDetail](API_IngestionJobDetail.md) object

## Errors
<a name="API_CreateIngestionJob_Errors"></a>

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
<a name="API_CreateIngestionJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/CreateIngestionJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/CreateIngestionJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/CreateIngestionJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/CreateIngestionJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/CreateIngestionJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/CreateIngestionJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/CreateIngestionJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/CreateIngestionJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/CreateIngestionJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/CreateIngestionJob)
