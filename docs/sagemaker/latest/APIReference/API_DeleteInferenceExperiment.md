---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DeleteInferenceExperiment.html
---

# DeleteInferenceExperiment
<a name="API_DeleteInferenceExperiment"></a>

Deletes an inference experiment.

**Note**
 This operation does not delete your endpoint, variants, or any underlying resources. This operation only deletes the metadata of your experiment.

## Request Syntax
<a name="API_DeleteInferenceExperiment_RequestSyntax"></a>

```
{
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteInferenceExperiment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_DeleteInferenceExperiment_RequestSyntax) **   <a name="sagemaker-DeleteInferenceExperiment-request-Name"></a>
The name of the inference experiment you want to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`
Required: Yes

## Response Syntax
<a name="API_DeleteInferenceExperiment_ResponseSyntax"></a>

```
{
   "InferenceExperimentArn": "string"
}
```

## Response Elements
<a name="API_DeleteInferenceExperiment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [InferenceExperimentArn](#API_DeleteInferenceExperiment_ResponseSyntax) **   <a name="sagemaker-DeleteInferenceExperiment-response-InferenceExperimentArn"></a>
The ARN of the deleted inference experiment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:inference-experiment/.*`

## Errors
<a name="API_DeleteInferenceExperiment_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
There was a conflict when you attempted to modify a SageMaker entity such as an `Experiment` or `Artifact`.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DeleteInferenceExperiment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DeleteInferenceExperiment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DeleteInferenceExperiment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DeleteInferenceExperiment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DeleteInferenceExperiment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DeleteInferenceExperiment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DeleteInferenceExperiment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DeleteInferenceExperiment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DeleteInferenceExperiment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DeleteInferenceExperiment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DeleteInferenceExperiment)
