---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_GetIngestionStream.html
---

# GetIngestionStream
<a name="API_GetIngestionStream"></a>

Returns information about an ingestion stream, including its configuration, status, and processing state.

## Request Syntax
<a name="API_GetIngestionStream_RequestSyntax"></a>

```
{
   "collectionId": "{{string}}",
   "ingestionStreamId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetIngestionStream_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [collectionId](#API_GetIngestionStream_RequestSyntax) **   <a name="opensearchserverless-GetIngestionStream-request-collectionId"></a>
The unique identifier of the collection that the ingestion stream belongs to.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-z0-9]{3,40}`
Required: Yes

 ** [ingestionStreamId](#API_GetIngestionStream_RequestSyntax) **   <a name="opensearchserverless-GetIngestionStream-request-ingestionStreamId"></a>
The unique identifier of the ingestion stream to retrieve.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_GetIngestionStream_ResponseSyntax"></a>

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
<a name="API_GetIngestionStream_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ingestionStreamDetail](#API_GetIngestionStream_ResponseSyntax) **   <a name="opensearchserverless-GetIngestionStream-response-ingestionStreamDetail"></a>
Details about the requested ingestion stream.
Type: [IngestionStreamDetail](API_IngestionStreamDetail.md) object

## Errors
<a name="API_GetIngestionStream_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Thrown when an error internal to the service occurs while processing a request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Thrown when accessing or deleting a resource that does not exist.
HTTP Status Code: 400

 ** ValidationException **
Thrown when the HTTP request contains invalid input or is missing required input.
HTTP Status Code: 400

## See Also
<a name="API_GetIngestionStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/GetIngestionStream)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/GetIngestionStream)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/GetIngestionStream)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/GetIngestionStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/GetIngestionStream)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/GetIngestionStream)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/GetIngestionStream)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/GetIngestionStream)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/GetIngestionStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/GetIngestionStream)
