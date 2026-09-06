---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_StartImportLabelsTaskRun.html
---

# StartImportLabelsTaskRun
<a name="API_StartImportLabelsTaskRun"></a>

Enables you to provide additional labels (examples of truth) to be used to teach the machine learning transform and improve its quality. This API operation is generally used as part of the active learning workflow that starts with the `StartMLLabelingSetGenerationTaskRun` call and that ultimately results in improving the quality of your machine learning transform.

After the `StartMLLabelingSetGenerationTaskRun` finishes, AWS Glue machine learning will have generated a series of questions for humans to answer. (Answering these questions is often called 'labeling' in the machine learning workflows). In the case of the `FindMatches` transform, these questions are of the form, “What is the correct way to group these rows together into groups composed entirely of matching records?” After the labeling process is finished, users upload their answers/labels with a call to `StartImportLabelsTaskRun`. After `StartImportLabelsTaskRun` finishes, all future runs of the machine learning transform use the new and improved labels and perform a higher-quality transformation.

By default, `StartMLLabelingSetGenerationTaskRun` continually learns from and combines all labels that you upload unless you set `Replace` to true. If you set `Replace` to true, `StartImportLabelsTaskRun` deletes and forgets all previously uploaded labels and learns only from the exact set that you upload. Replacing labels can be helpful if you realize that you previously uploaded incorrect labels, and you believe that they are having a negative effect on your transform quality.

You can check on the status of your task run by calling the `GetMLTaskRun` operation.

## Request Syntax
<a name="API_StartImportLabelsTaskRun_RequestSyntax"></a>

```
{
   "InputS3Path": "{{string}}",
   "ReplaceAllLabels": {{boolean}},
   "TransformId": "{{string}}"
}
```

## Request Parameters
<a name="API_StartImportLabelsTaskRun_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [InputS3Path](#API_StartImportLabelsTaskRun_RequestSyntax) **   <a name="Glue-StartImportLabelsTaskRun-request-InputS3Path"></a>
The Amazon Simple Storage Service (Amazon S3) path from where you import the labels.
Type: String
Required: Yes

 ** [ReplaceAllLabels](#API_StartImportLabelsTaskRun_RequestSyntax) **   <a name="Glue-StartImportLabelsTaskRun-request-ReplaceAllLabels"></a>
Indicates whether to overwrite your existing labels.
Type: Boolean
Required: No

 ** [TransformId](#API_StartImportLabelsTaskRun_RequestSyntax) **   <a name="Glue-StartImportLabelsTaskRun-request-TransformId"></a>
The unique identifier of the machine learning transform.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_StartImportLabelsTaskRun_ResponseSyntax"></a>

```
{
   "TaskRunId": "string"
}
```

## Response Elements
<a name="API_StartImportLabelsTaskRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TaskRunId](#API_StartImportLabelsTaskRun_ResponseSyntax) **   <a name="Glue-StartImportLabelsTaskRun-response-TaskRunId"></a>
The unique identifier for the task run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_StartImportLabelsTaskRun_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** ResourceNumberLimitExceededException **
A resource numerical limit was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_StartImportLabelsTaskRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/StartImportLabelsTaskRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/StartImportLabelsTaskRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/StartImportLabelsTaskRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/StartImportLabelsTaskRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/StartImportLabelsTaskRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/StartImportLabelsTaskRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/StartImportLabelsTaskRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/StartImportLabelsTaskRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/StartImportLabelsTaskRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/StartImportLabelsTaskRun)
