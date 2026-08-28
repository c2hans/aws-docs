---
source_url: https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_ActivatePipeline.html
---

# ActivatePipeline
<a name="API_ActivatePipeline"></a>

Validates the specified pipeline and starts processing pipeline tasks. If the pipeline does not pass validation, activation fails.

If you need to pause the pipeline to investigate an issue with a component, such as a data source or script, call [DeactivatePipeline](API_DeactivatePipeline.md).

To activate a finished pipeline, modify the end date for the pipeline and then activate it.

If you activate an on-demand pipeline that is already running, it will cancel all running objects and re-run the pipeline. StartTimestamp does not apply to on-demand pipelines.

## Request Syntax
<a name="API_ActivatePipeline_RequestSyntax"></a>

```
{
   "parameterValues": [
      {
         "id": "{{string}}",
         "stringValue": "{{string}}"
      }
   ],
   "pipelineId": "{{string}}",
   "startTimestamp": {{number}}
}
```

## Request Parameters
<a name="API_ActivatePipeline_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [parameterValues](#API_ActivatePipeline_RequestSyntax) **   <a name="DP-ActivatePipeline-request-parameterValues"></a>
A list of parameter values to pass to the pipeline at activation.
Type: Array of [ParameterValue](API_ParameterValue.md) objects
Required: No

 ** [pipelineId](#API_ActivatePipeline_RequestSyntax) **   <a name="DP-ActivatePipeline-request-pipelineId"></a>
The ID of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`
Required: Yes

 ** [startTimestamp](#API_ActivatePipeline_RequestSyntax) **   <a name="DP-ActivatePipeline-request-startTimestamp"></a>
The date and time to resume the pipeline. By default, the pipeline resumes from the last completed execution.
Type: Timestamp
Required: No

## Response Elements
<a name="API_ActivatePipeline_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_ActivatePipeline_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceError **
An internal service error occurred.
 ** message **
Description of the error message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request was not valid. Verify that your request was properly formatted, that the signature was generated with the correct credentials, and that you haven't exceeded any of the service limits for your account.
 ** message **
Description of the error message.
HTTP Status Code: 400

 ** PipelineDeletedException **
The specified pipeline has been deleted.
 ** message **
Description of the error message.
HTTP Status Code: 400

 ** PipelineNotFoundException **
The specified pipeline was not found. Verify that you used the correct user and account identifiers.
 ** message **
Description of the error message.
HTTP Status Code: 400

## Examples
<a name="API_ActivatePipeline_Examples"></a>

### Example
<a name="API_ActivatePipeline_Example_1"></a>

This example illustrates one usage of ActivatePipeline.

#### Sample Request
<a name="API_ActivatePipeline_Example_1_Request"></a>

```

POST / HTTP/1.1
Content-Type: application/x-amz-json-1.1
X-Amz-Target: DataPipeline.ActivatePipeline
Content-Length: 39
Host: datapipeline.us-east-1.amazonaws.com
X-Amz-Date: Mon, 12 Nov 2012 17:49:52 GMT
Authorization: AuthParams

{"pipelineId": "df-06372391ZG65EXAMPLE"}
```

#### Sample Response
<a name="API_ActivatePipeline_Example_1_Response"></a>

```

HTTP/1.1 200
x-amzn-RequestId: ee19d5bf-074e-11e2-af6f-6bc7a6be60d9
Content-Type: application/x-amz-json-1.1
Content-Length: 2
Date: Mon, 12 Nov 2012 17:50:53 GMT

{}
```

## See Also
<a name="API_ActivatePipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datapipeline-2012-10-29/ActivatePipeline)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datapipeline-2012-10-29/ActivatePipeline)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datapipeline-2012-10-29/ActivatePipeline)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datapipeline-2012-10-29/ActivatePipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datapipeline-2012-10-29/ActivatePipeline)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datapipeline-2012-10-29/ActivatePipeline)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datapipeline-2012-10-29/ActivatePipeline)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datapipeline-2012-10-29/ActivatePipeline)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datapipeline-2012-10-29/ActivatePipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datapipeline-2012-10-29/ActivatePipeline)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Pipeline. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datapipeline` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
