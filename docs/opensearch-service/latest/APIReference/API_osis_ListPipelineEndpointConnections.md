---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_ListPipelineEndpointConnections.html
---

# ListPipelineEndpointConnections
<a name="API_osis_ListPipelineEndpointConnections"></a>

Lists the pipeline endpoints connected to pipelines in your account.

## Request Syntax
<a name="API_osis_ListPipelineEndpointConnections_RequestSyntax"></a>

```
GET /2022-01-01/osis/listPipelineEndpointConnections?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_osis_ListPipelineEndpointConnections_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_osis_ListPipelineEndpointConnections_RequestSyntax) **   <a name="opensearchservice-osis_ListPipelineEndpointConnections-request-uri-MaxResults"></a>
The maximum number of pipeline endpoint connections to return in the response.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_osis_ListPipelineEndpointConnections_RequestSyntax) **   <a name="opensearchservice-osis_ListPipelineEndpointConnections-request-uri-NextToken"></a>
If your initial `ListPipelineEndpointConnections` operation returns a `nextToken`, you can include the returned `nextToken` in subsequent `ListPipelineEndpointConnections` operations, which returns results in the next page.
Length Constraints: Minimum length of 0. Maximum length of 3000.
Pattern: `^([\s\S]*)$`

## Request Body
<a name="API_osis_ListPipelineEndpointConnections_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_osis_ListPipelineEndpointConnections_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "PipelineEndpointConnections": [
      {
         "EndpointId": "string",
         "PipelineArn": "string",
         "Status": "string",
         "VpcEndpointOwner": "string"
      }
   ]
}
```

## Response Elements
<a name="API_osis_ListPipelineEndpointConnections_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_osis_ListPipelineEndpointConnections_ResponseSyntax) **   <a name="opensearchservice-osis_ListPipelineEndpointConnections-response-NextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 3000.
Pattern: `^([\s\S]*)$`

 ** [PipelineEndpointConnections](#API_osis_ListPipelineEndpointConnections_ResponseSyntax) **   <a name="opensearchservice-osis_ListPipelineEndpointConnections-response-PipelineEndpointConnections"></a>
A list of pipeline endpoint connections.
Type: Array of [PipelineEndpointConnection](API_osis_PipelineEndpointConnection.md) objects

## Errors
<a name="API_osis_ListPipelineEndpointConnections_Errors"></a>

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

 ** LimitExceededException **
You attempted to create more than the allowed number of tags.
HTTP Status Code: 409

 ** ValidationException **
An exception for missing or invalid input fields.
HTTP Status Code: 400

## See Also
<a name="API_osis_ListPipelineEndpointConnections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/osis-2022-01-01/ListPipelineEndpointConnections)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/osis-2022-01-01/ListPipelineEndpointConnections)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/osis-2022-01-01/ListPipelineEndpointConnections)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/osis-2022-01-01/ListPipelineEndpointConnections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/osis-2022-01-01/ListPipelineEndpointConnections)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/osis-2022-01-01/ListPipelineEndpointConnections)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/osis-2022-01-01/ListPipelineEndpointConnections)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/osis-2022-01-01/ListPipelineEndpointConnections)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/osis-2022-01-01/ListPipelineEndpointConnections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/osis-2022-01-01/ListPipelineEndpointConnections)
