---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_ValidatePipeline.html
---

# ValidatePipeline
<a name="API_osis_ValidatePipeline"></a>

Checks whether an OpenSearch Ingestion pipeline configuration is valid prior to creation. For more information, see [Creating Amazon OpenSearch Ingestion pipelines](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/creating-pipeline.html).

## Request Syntax
<a name="API_osis_ValidatePipeline_RequestSyntax"></a>

```
POST /2022-01-01/osis/validatePipeline HTTP/1.1
Content-type: application/json

{
   "PipelineConfigurationBody": "{{string}}"
}
```

## URI Request Parameters
<a name="API_osis_ValidatePipeline_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_osis_ValidatePipeline_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [PipelineConfigurationBody](#API_osis_ValidatePipeline_RequestSyntax) **   <a name="opensearchservice-osis_ValidatePipeline-request-PipelineConfigurationBody"></a>
The pipeline configuration in YAML format. The command accepts the pipeline configuration as a string or within a .yaml file. If you provide the configuration as a string, each new line must be escaped with `\n`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100000.
Required: Yes

## Response Syntax
<a name="API_osis_ValidatePipeline_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Errors": [
      {
         "Message": "string"
      }
   ],
   "isValid": boolean
}
```

## Response Elements
<a name="API_osis_ValidatePipeline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Errors](#API_osis_ValidatePipeline_ResponseSyntax) **   <a name="opensearchservice-osis_ValidatePipeline-response-Errors"></a>
A list of errors if the configuration is invalid.
Type: Array of [ValidationMessage](API_osis_ValidationMessage.md) objects

 ** [isValid](#API_osis_ValidatePipeline_ResponseSyntax) **   <a name="opensearchservice-osis_ValidatePipeline-response-isValid"></a>
A boolean indicating whether or not the pipeline configuration is valid.
Type: Boolean

## Errors
<a name="API_osis_ValidatePipeline_Errors"></a>

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
<a name="API_osis_ValidatePipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/osis-2022-01-01/ValidatePipeline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/osis-2022-01-01/ValidatePipeline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/osis-2022-01-01/ValidatePipeline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/osis-2022-01-01/ValidatePipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/osis-2022-01-01/ValidatePipeline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/osis-2022-01-01/ValidatePipeline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/osis-2022-01-01/ValidatePipeline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/osis-2022-01-01/ValidatePipeline)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/osis-2022-01-01/ValidatePipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/osis-2022-01-01/ValidatePipeline)
