---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_UpdateMLTransform.html
---

# UpdateMLTransform
<a name="API_UpdateMLTransform"></a>

Updates an existing machine learning transform. Call this operation to tune the algorithm parameters to achieve better results.

After calling this operation, you can call the `StartMLEvaluationTaskRun` operation to assess how well your new parameters achieved your goals (such as improving the quality of your machine learning transform, or making it more cost-effective).

## Request Syntax
<a name="API_UpdateMLTransform_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "GlueVersion": "{{string}}",
   "MaxCapacity": {{number}},
   "MaxRetries": {{number}},
   "Name": "{{string}}",
   "NumberOfWorkers": {{number}},
   "Parameters": {
      "FindMatchesParameters": {
         "AccuracyCostTradeoff": {{number}},
         "EnforceProvidedLabels": {{boolean}},
         "PrecisionRecallTradeoff": {{number}},
         "PrimaryKeyColumnName": "{{string}}"
      },
      "TransformType": "{{string}}"
   },
   "Role": "{{string}}",
   "Timeout": {{number}},
   "TransformId": "{{string}}",
   "WorkerType": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateMLTransform_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateMLTransform_RequestSyntax) **   <a name="Glue-UpdateMLTransform-request-Description"></a>
A description of the transform. The default is an empty string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** [GlueVersion](#API_UpdateMLTransform_RequestSyntax) **   <a name="Glue-UpdateMLTransform-request-GlueVersion"></a>
This value determines which version of AWS Glue this machine learning transform is compatible with. Glue 1.0 is recommended for most customers. If the value is not set, the Glue compatibility defaults to Glue 0.9. For more information, see [AWS Glue Versions](https://docs.aws.amazon.com/glue/latest/dg/release-notes.html#release-notes-versions) in the developer guide.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(\w+\.)+\w+$`
Required: No

 ** [MaxCapacity](#API_UpdateMLTransform_RequestSyntax) **   <a name="Glue-UpdateMLTransform-request-MaxCapacity"></a>
The number of AWS Glue data processing units (DPUs) that are allocated to task runs for this transform. You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the [AWS Glue pricing page](https://aws.amazon.com/glue/pricing/).
When the `WorkerType` field is set to a value other than `Standard`, the `MaxCapacity` field is set automatically and becomes read-only.
Type: Double
Required: No

 ** [MaxRetries](#API_UpdateMLTransform_RequestSyntax) **   <a name="Glue-UpdateMLTransform-request-MaxRetries"></a>
The maximum number of times to retry a task for this transform after a task run fails.
Type: Integer
Required: No

 ** [Name](#API_UpdateMLTransform_RequestSyntax) **   <a name="Glue-UpdateMLTransform-request-Name"></a>
The unique name that you gave the transform when you created it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [NumberOfWorkers](#API_UpdateMLTransform_RequestSyntax) **   <a name="Glue-UpdateMLTransform-request-NumberOfWorkers"></a>
The number of workers of a defined `workerType` that are allocated when this task runs.
Type: Integer
Required: No

 ** [Parameters](#API_UpdateMLTransform_RequestSyntax) **   <a name="Glue-UpdateMLTransform-request-Parameters"></a>
The configuration parameters that are specific to the transform type (algorithm) used. Conditionally dependent on the transform type.
Type: [TransformParameters](API_TransformParameters.md) object
Required: No

 ** [Role](#API_UpdateMLTransform_RequestSyntax) **   <a name="Glue-UpdateMLTransform-request-Role"></a>
The name or Amazon Resource Name (ARN) of the IAM role with the required permissions.
Type: String
Required: No

 ** [Timeout](#API_UpdateMLTransform_RequestSyntax) **   <a name="Glue-UpdateMLTransform-request-Timeout"></a>
The timeout for a task run for this transform in minutes. This is the maximum time that a task run for this transform can consume resources before it is terminated and enters `TIMEOUT` status. The default is 2,880 minutes (48 hours).
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [TransformId](#API_UpdateMLTransform_RequestSyntax) **   <a name="Glue-UpdateMLTransform-request-TransformId"></a>
A unique identifier that was generated when the transform was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [WorkerType](#API_UpdateMLTransform_RequestSyntax) **   <a name="Glue-UpdateMLTransform-request-WorkerType"></a>
The type of predefined worker that is allocated when this task runs. Accepts a value of Standard, G.1X, or G.2X.
+ For the `Standard` worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.
+ For the `G.1X` worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and 1 executor per worker.
+ For the `G.2X` worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk, and 1 executor per worker.
Type: String
Valid Values: `Standard | G.1X | G.2X | G.025X | G.4X | G.8X | Z.2X`
Required: No

## Response Syntax
<a name="API_UpdateMLTransform_ResponseSyntax"></a>

```
{
   "TransformId": "string"
}
```

## Response Elements
<a name="API_UpdateMLTransform_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TransformId](#API_UpdateMLTransform_ResponseSyntax) **   <a name="Glue-UpdateMLTransform-response-TransformId"></a>
The unique identifier for the transform that was updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_UpdateMLTransform_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
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
<a name="API_UpdateMLTransform_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/UpdateMLTransform)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/UpdateMLTransform)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/UpdateMLTransform)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/UpdateMLTransform)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/UpdateMLTransform)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/UpdateMLTransform)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/UpdateMLTransform)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/UpdateMLTransform)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/UpdateMLTransform)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/UpdateMLTransform)
