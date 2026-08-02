---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_ListBatchJobDefinitions.html
---

# ListBatchJobDefinitions
<a name="API_ListBatchJobDefinitions"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Lists all the available batch job definitions based on the batch job resources uploaded during the application creation. You can use the batch job definitions in the list to start a batch job.

## Request Syntax
<a name="API_ListBatchJobDefinitions_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/batch-job-definitions?maxResults={{maxResults}}&nextToken={{nextToken}}&prefix={{prefix}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListBatchJobDefinitions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_ListBatchJobDefinitions_RequestSyntax) **   <a name="m2-ListBatchJobDefinitions-request-uri-applicationId"></a>
The identifier of the application.
Pattern: `\S{1,80}`
Required: Yes

 ** [maxResults](#API_ListBatchJobDefinitions_RequestSyntax) **   <a name="m2-ListBatchJobDefinitions-request-uri-maxResults"></a>
The maximum number of batch job definitions to return.
Valid Range: Minimum value of 1. Maximum value of 2000.

 ** [nextToken](#API_ListBatchJobDefinitions_RequestSyntax) **   <a name="m2-ListBatchJobDefinitions-request-uri-nextToken"></a>
A pagination token returned from a previous call to this operation. This specifies the next item to return. To return to the beginning of the list, exclude this parameter.
Pattern: `\S{1,2000}`

 ** [prefix](#API_ListBatchJobDefinitions_RequestSyntax) **   <a name="m2-ListBatchJobDefinitions-request-uri-prefix"></a>
If the batch job definition is a FileBatchJobDefinition, the prefix allows you to search on the file names of FileBatchJobDefinitions.

## Request Body
<a name="API_ListBatchJobDefinitions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListBatchJobDefinitions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "batchJobDefinitions": [
      { ... }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListBatchJobDefinitions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [batchJobDefinitions](#API_ListBatchJobDefinitions_ResponseSyntax) **   <a name="m2-ListBatchJobDefinitions-response-batchJobDefinitions"></a>
The list of batch job definitions.
Type: Array of [BatchJobDefinition](API_BatchJobDefinition.md) objects

 ** [nextToken](#API_ListBatchJobDefinitions_ResponseSyntax) **   <a name="m2-ListBatchJobDefinitions-response-nextToken"></a>
If there are more items to return, this contains a token that is passed to a subsequent call to this operation to retrieve the next set of items.
Type: String
Pattern: `\S{1,2000}`

## Errors
<a name="API_ListBatchJobDefinitions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The account or role doesn't have the right permissions to make the request.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred during the processing of the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
 ** resourceId **
The ID of the missing resource.
 ** resourceType **
The type of the missing resource.
HTTP Status Code: 404

 ** ThrottlingException **
The number of requests made exceeds the limit.
 ** quotaCode **
The identifier of the throttled request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
 ** serviceCode **
The identifier of the service that the throttled request was made to.
HTTP Status Code: 429

 ** ValidationException **
One or more parameters provided in the request is not valid.
 ** fieldList **
The list of fields that failed service validation.
 ** reason **
The reason why it failed service validation.
HTTP Status Code: 400

## See Also
<a name="API_ListBatchJobDefinitions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/m2-2021-04-28/ListBatchJobDefinitions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/m2-2021-04-28/ListBatchJobDefinitions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/ListBatchJobDefinitions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/m2-2021-04-28/ListBatchJobDefinitions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/ListBatchJobDefinitions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/m2-2021-04-28/ListBatchJobDefinitions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/m2-2021-04-28/ListBatchJobDefinitions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/m2-2021-04-28/ListBatchJobDefinitions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/m2-2021-04-28/ListBatchJobDefinitions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/ListBatchJobDefinitions)
