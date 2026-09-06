---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribePipelineDefinitionForExecution.html
---

# DescribePipelineDefinitionForExecution
<a name="API_DescribePipelineDefinitionForExecution"></a>

Describes the details of an execution's pipeline definition.

## Request Syntax
<a name="API_DescribePipelineDefinitionForExecution_RequestSyntax"></a>

```
{
   "PipelineExecutionArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribePipelineDefinitionForExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [PipelineExecutionArn](#API_DescribePipelineDefinitionForExecution_RequestSyntax) **   <a name="sagemaker-DescribePipelineDefinitionForExecution-request-PipelineExecutionArn"></a>
The Amazon Resource Name (ARN) of the pipeline execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:pipeline\/.*\/execution\/.*`
Required: Yes

## Response Syntax
<a name="API_DescribePipelineDefinitionForExecution_ResponseSyntax"></a>

```
{
   "CreationTime": number,
   "PipelineDefinition": "string"
}
```

## Response Elements
<a name="API_DescribePipelineDefinitionForExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreationTime](#API_DescribePipelineDefinitionForExecution_ResponseSyntax) **   <a name="sagemaker-DescribePipelineDefinitionForExecution-response-CreationTime"></a>
The time when the pipeline was created.
Type: Timestamp

 ** [PipelineDefinition](#API_DescribePipelineDefinitionForExecution_ResponseSyntax) **   <a name="sagemaker-DescribePipelineDefinitionForExecution-response-PipelineDefinition"></a>
The JSON pipeline definition.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1048576.
Pattern: `.*(?:[ \r\n\t].*)*`

## Errors
<a name="API_DescribePipelineDefinitionForExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribePipelineDefinitionForExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribePipelineDefinitionForExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribePipelineDefinitionForExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribePipelineDefinitionForExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribePipelineDefinitionForExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribePipelineDefinitionForExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribePipelineDefinitionForExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribePipelineDefinitionForExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribePipelineDefinitionForExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribePipelineDefinitionForExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribePipelineDefinitionForExecution)
