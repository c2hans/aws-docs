---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_GetPipelineBlueprint.html
---

# GetPipelineBlueprint
<a name="API_osis_GetPipelineBlueprint"></a>

Retrieves information about a specific blueprint for OpenSearch Ingestion. Blueprints are templates for the configuration needed for a `CreatePipeline` request. For more information, see [Using blueprints to create a pipeline](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/creating-pipeline.html#pipeline-blueprint).

## Request Syntax
<a name="API_osis_GetPipelineBlueprint_RequestSyntax"></a>

```
GET /2022-01-01/osis/getPipelineBlueprint/{{BlueprintName}}?format={{Format}} HTTP/1.1
```

## URI Request Parameters
<a name="API_osis_GetPipelineBlueprint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [BlueprintName](#API_osis_GetPipelineBlueprint_RequestSyntax) **   <a name="opensearchservice-osis_GetPipelineBlueprint-request-uri-BlueprintName"></a>
The name of the blueprint to retrieve.
Required: Yes

 ** [Format](#API_osis_GetPipelineBlueprint_RequestSyntax) **   <a name="opensearchservice-osis_GetPipelineBlueprint-request-uri-Format"></a>
The format format of the blueprint to retrieve.
Pattern: `(YAML|JSON)`

## Request Body
<a name="API_osis_GetPipelineBlueprint_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_osis_GetPipelineBlueprint_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Blueprint": {
      "BlueprintName": "string",
      "DisplayDescription": "string",
      "DisplayName": "string",
      "PipelineConfigurationBody": "string",
      "Service": "string",
      "UseCase": "string"
   },
   "Format": "string"
}
```

## Response Elements
<a name="API_osis_GetPipelineBlueprint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Blueprint](#API_osis_GetPipelineBlueprint_ResponseSyntax) **   <a name="opensearchservice-osis_GetPipelineBlueprint-response-Blueprint"></a>
The requested blueprint in YAML format.
Type: [PipelineBlueprint](API_osis_PipelineBlueprint.md) object

 ** [Format](#API_osis_GetPipelineBlueprint_ResponseSyntax) **   <a name="opensearchservice-osis_GetPipelineBlueprint-response-Format"></a>
The format of the blueprint.
Type: String

## Errors
<a name="API_osis_GetPipelineBlueprint_Errors"></a>

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
<a name="API_osis_GetPipelineBlueprint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/osis-2022-01-01/GetPipelineBlueprint)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/osis-2022-01-01/GetPipelineBlueprint)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/osis-2022-01-01/GetPipelineBlueprint)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/osis-2022-01-01/GetPipelineBlueprint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/osis-2022-01-01/GetPipelineBlueprint)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/osis-2022-01-01/GetPipelineBlueprint)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/osis-2022-01-01/GetPipelineBlueprint)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/osis-2022-01-01/GetPipelineBlueprint)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/osis-2022-01-01/GetPipelineBlueprint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/osis-2022-01-01/GetPipelineBlueprint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
