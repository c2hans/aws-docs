---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/ServerlessAPIReference/API_GetIngestionJob.html
---

# GetIngestionJob
<a name="API_GetIngestionJob"></a>

Returns information about an ingestion job, including its configuration, status, and processing state.

## Request Syntax
<a name="API_GetIngestionJob_RequestSyntax"></a>

```
{
   "collectionId": "{{string}}",
   "ingestionJobId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetIngestionJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [collectionId](#API_GetIngestionJob_RequestSyntax) **   <a name="opensearchserverless-GetIngestionJob-request-collectionId"></a>
The unique identifier of the collection that the ingestion job belongs to.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 40.
Pattern: `[a-z0-9]{3,40}`
Required: Yes

 ** [ingestionJobId](#API_GetIngestionJob_RequestSyntax) **   <a name="opensearchserverless-GetIngestionJob-request-ingestionJobId"></a>
The unique identifier of the ingestion job to retrieve.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 64.
Pattern: `[a-z0-9]+`
Required: Yes

## Response Syntax
<a name="API_GetIngestionJob_ResponseSyntax"></a>

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
<a name="API_GetIngestionJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ingestionJobDetail](#API_GetIngestionJob_ResponseSyntax) **   <a name="opensearchserverless-GetIngestionJob-response-ingestionJobDetail"></a>
Details about the requested ingestion job.
Type: [IngestionJobDetail](API_IngestionJobDetail.md) object

## Errors
<a name="API_GetIngestionJob_Errors"></a>

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
<a name="API_GetIngestionJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearchserverless-2021-11-01/GetIngestionJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearchserverless-2021-11-01/GetIngestionJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearchserverless-2021-11-01/GetIngestionJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearchserverless-2021-11-01/GetIngestionJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearchserverless-2021-11-01/GetIngestionJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearchserverless-2021-11-01/GetIngestionJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearchserverless-2021-11-01/GetIngestionJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearchserverless-2021-11-01/GetIngestionJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearchserverless-2021-11-01/GetIngestionJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearchserverless-2021-11-01/GetIngestionJob)
