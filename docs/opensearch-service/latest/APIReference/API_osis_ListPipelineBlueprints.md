---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_ListPipelineBlueprints.html
---

# ListPipelineBlueprints
<a name="API_osis_ListPipelineBlueprints"></a>

Retrieves a list of all available blueprints for Data Prepper. For more information, see [Using blueprints to create a pipeline](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/creating-pipeline.html#pipeline-blueprint).

## Request Syntax
<a name="API_osis_ListPipelineBlueprints_RequestSyntax"></a>

```
POST /2022-01-01/osis/listPipelineBlueprints HTTP/1.1
```

## URI Request Parameters
<a name="API_osis_ListPipelineBlueprints_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_osis_ListPipelineBlueprints_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_osis_ListPipelineBlueprints_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Blueprints": [
      {
         "BlueprintName": "string",
         "DisplayDescription": "string",
         "DisplayName": "string",
         "Service": "string",
         "UseCase": "string"
      }
   ]
}
```

## Response Elements
<a name="API_osis_ListPipelineBlueprints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Blueprints](#API_osis_ListPipelineBlueprints_ResponseSyntax) **   <a name="opensearchservice-osis_ListPipelineBlueprints-response-Blueprints"></a>
A list of available blueprints for Data Prepper.
Type: Array of [PipelineBlueprintSummary](API_osis_PipelineBlueprintSummary.md) objects

## Errors
<a name="API_osis_ListPipelineBlueprints_Errors"></a>

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

 ** InvalidPaginationTokenException **
An invalid pagination token provided in the request.
HTTP Status Code: 400

 ** ValidationException **
An exception for missing or invalid input fields.
HTTP Status Code: 400

## See Also
<a name="API_osis_ListPipelineBlueprints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/osis-2022-01-01/ListPipelineBlueprints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/osis-2022-01-01/ListPipelineBlueprints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/osis-2022-01-01/ListPipelineBlueprints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/osis-2022-01-01/ListPipelineBlueprints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/osis-2022-01-01/ListPipelineBlueprints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/osis-2022-01-01/ListPipelineBlueprints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/osis-2022-01-01/ListPipelineBlueprints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/osis-2022-01-01/ListPipelineBlueprints)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/osis-2022-01-01/ListPipelineBlueprints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/osis-2022-01-01/ListPipelineBlueprints)
