---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_DeletePipelineEndpoint.html
---

# DeletePipelineEndpoint
<a name="API_osis_DeletePipelineEndpoint"></a>

Deletes a VPC endpoint for an OpenSearch Ingestion pipeline.

## Request Syntax
<a name="API_osis_DeletePipelineEndpoint_RequestSyntax"></a>

```
DELETE /2022-01-01/osis/deletePipelineEndpoint/{{EndpointId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_osis_DeletePipelineEndpoint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [EndpointId](#API_osis_DeletePipelineEndpoint_RequestSyntax) **   <a name="opensearchservice-osis_DeletePipelineEndpoint-request-uri-EndpointId"></a>
The unique identifier of the pipeline endpoint to delete.
Length Constraints: Minimum length of 3. Maximum length of 512.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]+$`
Required: Yes

## Request Body
<a name="API_osis_DeletePipelineEndpoint_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_osis_DeletePipelineEndpoint_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_osis_DeletePipelineEndpoint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_osis_DeletePipelineEndpoint_Errors"></a>

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

 ** ValidationException **
An exception for missing or invalid input fields.
HTTP Status Code: 400

## See Also
<a name="API_osis_DeletePipelineEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/osis-2022-01-01/DeletePipelineEndpoint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/osis-2022-01-01/DeletePipelineEndpoint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/osis-2022-01-01/DeletePipelineEndpoint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/osis-2022-01-01/DeletePipelineEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/osis-2022-01-01/DeletePipelineEndpoint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/osis-2022-01-01/DeletePipelineEndpoint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/osis-2022-01-01/DeletePipelineEndpoint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/osis-2022-01-01/DeletePipelineEndpoint)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/osis-2022-01-01/DeletePipelineEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/osis-2022-01-01/DeletePipelineEndpoint)
