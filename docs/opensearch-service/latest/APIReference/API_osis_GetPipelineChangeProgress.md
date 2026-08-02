---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_GetPipelineChangeProgress.html
---

# GetPipelineChangeProgress
<a name="API_osis_GetPipelineChangeProgress"></a>

Returns progress information for the current change happening on an OpenSearch Ingestion pipeline. Currently, this operation only returns information when a pipeline is being created.

For more information, see [Tracking the status of pipeline creation](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/creating-pipeline.html#get-pipeline-progress).

## Request Syntax
<a name="API_osis_GetPipelineChangeProgress_RequestSyntax"></a>

```
GET /2022-01-01/osis/getPipelineChangeProgress/{{PipelineName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_osis_GetPipelineChangeProgress_RequestParameters"></a>

The request uses the following URI parameters.

 ** [PipelineName](#API_osis_GetPipelineChangeProgress_RequestSyntax) **   <a name="opensearchservice-osis_GetPipelineChangeProgress-request-uri-PipelineName"></a>
The name of the pipeline.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

## Request Body
<a name="API_osis_GetPipelineChangeProgress_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_osis_GetPipelineChangeProgress_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ChangeProgressStatuses": [
      {
         "ChangeProgressStages": [
            {
               "Description": "string",
               "LastUpdatedAt": number,
               "Name": "string",
               "Status": "string"
            }
         ],
         "StartTime": number,
         "Status": "string",
         "TotalNumberOfStages": number
      }
   ]
}
```

## Response Elements
<a name="API_osis_GetPipelineChangeProgress_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeProgressStatuses](#API_osis_GetPipelineChangeProgress_ResponseSyntax) **   <a name="opensearchservice-osis_GetPipelineChangeProgress-response-ChangeProgressStatuses"></a>
The current status of the change happening on the pipeline.
Type: Array of [ChangeProgressStatus](API_osis_ChangeProgressStatus.md) objects

## Errors
<a name="API_osis_GetPipelineChangeProgress_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permissions to access the resource.
HTTP Status Code: 403

 ** DisabledOperationException **
Exception is thrown when an operation has been disabled.
HTTP Status Code: 409

 ** InternalException **
The request failed because of an unknown error, exception, or failure (the failure is internal to the service).
HTTP Status Code: 500

 ** ResourceNotFoundException **
You attempted to access or delete a resource that does not exist.
HTTP Status Code: 404

 ** ValidationException **
An exception for missing or invalid input fields.
HTTP Status Code: 400

## See Also
<a name="API_osis_GetPipelineChangeProgress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/osis-2022-01-01/GetPipelineChangeProgress)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/osis-2022-01-01/GetPipelineChangeProgress)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/osis-2022-01-01/GetPipelineChangeProgress)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/osis-2022-01-01/GetPipelineChangeProgress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/osis-2022-01-01/GetPipelineChangeProgress)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/osis-2022-01-01/GetPipelineChangeProgress)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/osis-2022-01-01/GetPipelineChangeProgress)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/osis-2022-01-01/GetPipelineChangeProgress)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/osis-2022-01-01/GetPipelineChangeProgress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/osis-2022-01-01/GetPipelineChangeProgress)
