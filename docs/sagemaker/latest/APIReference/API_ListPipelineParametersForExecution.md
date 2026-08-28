---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListPipelineParametersForExecution.html
---

# ListPipelineParametersForExecution
<a name="API_ListPipelineParametersForExecution"></a>

Gets a list of parameters for a pipeline execution.

## Request Syntax
<a name="API_ListPipelineParametersForExecution_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "PipelineExecutionArn": "{{string}}"
}
```

## Request Parameters
<a name="API_ListPipelineParametersForExecution_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_ListPipelineParametersForExecution_RequestSyntax) **   <a name="sagemaker-ListPipelineParametersForExecution-request-MaxResults"></a>
The maximum number of parameters to return in the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListPipelineParametersForExecution_RequestSyntax) **   <a name="sagemaker-ListPipelineParametersForExecution-request-NextToken"></a>
If the result of the previous `ListPipelineParametersForExecution` request was truncated, the response includes a `NextToken`. To retrieve the next set of parameters, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`
Required: No

 ** [PipelineExecutionArn](#API_ListPipelineParametersForExecution_RequestSyntax) **   <a name="sagemaker-ListPipelineParametersForExecution-request-PipelineExecutionArn"></a>
The Amazon Resource Name (ARN) of the pipeline execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:pipeline\/.*\/execution\/.*`
Required: Yes

## Response Syntax
<a name="API_ListPipelineParametersForExecution_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "PipelineParameters": [
      {
         "Name": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPipelineParametersForExecution_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListPipelineParametersForExecution_ResponseSyntax) **   <a name="sagemaker-ListPipelineParametersForExecution-response-NextToken"></a>
If the result of the previous `ListPipelineParametersForExecution` request was truncated, the response includes a `NextToken`. To retrieve the next set of parameters, use the token in the next request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `.*`

 ** [PipelineParameters](#API_ListPipelineParametersForExecution_ResponseSyntax) **   <a name="sagemaker-ListPipelineParametersForExecution-response-PipelineParameters"></a>
Contains a list of pipeline parameters. This list can be empty.
Type: Array of [Parameter](API_Parameter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

## Errors
<a name="API_ListPipelineParametersForExecution_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_ListPipelineParametersForExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/ListPipelineParametersForExecution)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/ListPipelineParametersForExecution)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ListPipelineParametersForExecution)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/ListPipelineParametersForExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ListPipelineParametersForExecution)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/ListPipelineParametersForExecution)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/ListPipelineParametersForExecution)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/ListPipelineParametersForExecution)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/ListPipelineParametersForExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ListPipelineParametersForExecution)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
