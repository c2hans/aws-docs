---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_StartMLLabelingSetGenerationTaskRun.html
---

# StartMLLabelingSetGenerationTaskRun
<a name="API_StartMLLabelingSetGenerationTaskRun"></a>

Starts the active learning workflow for your machine learning transform to improve the transform's quality by generating label sets and adding labels.

When the `StartMLLabelingSetGenerationTaskRun` finishes, AWS Glue will have generated a "labeling set" or a set of questions for humans to answer.

In the case of the `FindMatches` transform, these questions are of the form, “What is the correct way to group these rows together into groups composed entirely of matching records?”

After the labeling process is finished, you can upload your labels with a call to `StartImportLabelsTaskRun`. After `StartImportLabelsTaskRun` finishes, all future runs of the machine learning transform will use the new and improved labels and perform a higher-quality transformation.

Note: The role used to write the generated labeling set to the `OutputS3Path` is the role associated with the Machine Learning Transform, specified in the `CreateMLTransform` API.

## Request Syntax
<a name="API_StartMLLabelingSetGenerationTaskRun_RequestSyntax"></a>

```
{
   "OutputS3Path": "{{string}}",
   "TransformId": "{{string}}"
}
```

## Request Parameters
<a name="API_StartMLLabelingSetGenerationTaskRun_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [OutputS3Path](#API_StartMLLabelingSetGenerationTaskRun_RequestSyntax) **   <a name="Glue-StartMLLabelingSetGenerationTaskRun-request-OutputS3Path"></a>
The Amazon Simple Storage Service (Amazon S3) path where you generate the labeling set.
Type: String
Required: Yes

 ** [TransformId](#API_StartMLLabelingSetGenerationTaskRun_RequestSyntax) **   <a name="Glue-StartMLLabelingSetGenerationTaskRun-request-TransformId"></a>
The unique identifier of the machine learning transform.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_StartMLLabelingSetGenerationTaskRun_ResponseSyntax"></a>

```
{
   "TaskRunId": "string"
}
```

## Response Elements
<a name="API_StartMLLabelingSetGenerationTaskRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TaskRunId](#API_StartMLLabelingSetGenerationTaskRun_ResponseSyntax) **   <a name="Glue-StartMLLabelingSetGenerationTaskRun-response-TaskRunId"></a>
The unique run identifier that is associated with this task run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_StartMLLabelingSetGenerationTaskRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentRunsExceededException **
Too many jobs are being run concurrently.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_StartMLLabelingSetGenerationTaskRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/StartMLLabelingSetGenerationTaskRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/StartMLLabelingSetGenerationTaskRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/StartMLLabelingSetGenerationTaskRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/StartMLLabelingSetGenerationTaskRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/StartMLLabelingSetGenerationTaskRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/StartMLLabelingSetGenerationTaskRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/StartMLLabelingSetGenerationTaskRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/StartMLLabelingSetGenerationTaskRun)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/StartMLLabelingSetGenerationTaskRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/StartMLLabelingSetGenerationTaskRun)
