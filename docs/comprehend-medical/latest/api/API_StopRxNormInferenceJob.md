---
source_url: https://docs.aws.amazon.com/comprehend-medical/latest/api/API_StopRxNormInferenceJob.html
---

# StopRxNormInferenceJob
<a name="API_StopRxNormInferenceJob"></a>

Stops an InferRxNorm inference job in progress.

## Request Syntax
<a name="API_StopRxNormInferenceJob_RequestSyntax"></a>

```
{
   "JobId": "{{string}}"
}
```

## Request Parameters
<a name="API_StopRxNormInferenceJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobId](#API_StopRxNormInferenceJob_RequestSyntax) **   <a name="comprehendmedical-StopRxNormInferenceJob-request-JobId"></a>
The identifier of the job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`
Required: Yes

## Response Syntax
<a name="API_StopRxNormInferenceJob_ResponseSyntax"></a>

```
{
   "JobId": "string"
}
```

## Response Elements
<a name="API_StopRxNormInferenceJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobId](#API_StopRxNormInferenceJob_ResponseSyntax) **   <a name="comprehendmedical-StopRxNormInferenceJob-response-JobId"></a>
The identifier generated for the job. To get the status of job, use this identifier with the `DescribeRxNormInferenceJob` operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)$`

## Errors
<a name="API_StopRxNormInferenceJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
 An internal server error occurred. Retry your request.
HTTP Status Code: 500

 ** InvalidRequestException **
 The request that you made is invalid. Check your request to determine why it's invalid and then retry the request.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource identified by the specified Amazon Resource Name (ARN) was not found. Check the ARN and try your request again.
HTTP Status Code: 400

## See Also
<a name="API_StopRxNormInferenceJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/comprehendmedical-2018-10-30/StopRxNormInferenceJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/comprehendmedical-2018-10-30/StopRxNormInferenceJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehendmedical-2018-10-30/StopRxNormInferenceJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/comprehendmedical-2018-10-30/StopRxNormInferenceJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehendmedical-2018-10-30/StopRxNormInferenceJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/comprehendmedical-2018-10-30/StopRxNormInferenceJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/comprehendmedical-2018-10-30/StopRxNormInferenceJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/comprehendmedical-2018-10-30/StopRxNormInferenceJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/comprehendmedical-2018-10-30/StopRxNormInferenceJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehendmedical-2018-10-30/StopRxNormInferenceJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Comprehend Medical. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query comprehend-medical` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
