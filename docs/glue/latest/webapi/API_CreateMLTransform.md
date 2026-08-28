---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_CreateMLTransform.html
---

# CreateMLTransform
<a name="API_CreateMLTransform"></a>

Creates an AWS Glue machine learning transform. This operation creates the transform and all the necessary parameters to train it.

Call this operation as the first step in the process of using a machine learning transform (such as the `FindMatches` transform) for deduplicating data. You can provide an optional `Description`, in addition to the parameters that you want to use for your algorithm.

You must also specify certain parameters for the tasks that AWS Glue runs on your behalf as part of learning from your data and creating a high-quality machine learning transform. These parameters include `Role`, and optionally, `AllocatedCapacity`, `Timeout`, and `MaxRetries`. For more information, see [Jobs](https://docs.aws.amazon.com/glue/latest/dg/aws-glue-api-jobs-job.html).

## Request Syntax
<a name="API_CreateMLTransform_RequestSyntax"></a>

```
{
   "Description": "{{string}}",
   "GlueVersion": "{{string}}",
   "InputRecordTables": [
      {
         "AdditionalOptions": {
            "{{string}}" : "{{string}}"
         },
         "CatalogId": "{{string}}",
         "ConnectionName": "{{string}}",
         "DatabaseName": "{{string}}",
         "TableName": "{{string}}"
      }
   ],
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
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "Timeout": {{number}},
   "TransformEncryption": {
      "MlUserDataEncryption": {
         "KmsKeyId": "{{string}}",
         "MlUserDataEncryptionMode": "{{string}}"
      },
      "TaskRunSecurityConfigurationName": "{{string}}"
   },
   "WorkerType": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateMLTransform_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Description](#API_CreateMLTransform_RequestSyntax) **   <a name="Glue-CreateMLTransform-request-Description"></a>
A description of the machine learning transform that is being defined. The default is an empty string.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`
Required: No

 ** [GlueVersion](#API_CreateMLTransform_RequestSyntax) **   <a name="Glue-CreateMLTransform-request-GlueVersion"></a>
This value determines which version of AWS Glue this machine learning transform is compatible with. Glue 1.0 is recommended for most customers. If the value is not set, the Glue compatibility defaults to Glue 0.9. For more information, see [AWS Glue Versions](https://docs.aws.amazon.com/glue/latest/dg/release-notes.html#release-notes-versions) in the developer guide.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(\w+\.)+\w+$`
Required: No

 ** [InputRecordTables](#API_CreateMLTransform_RequestSyntax) **   <a name="Glue-CreateMLTransform-request-InputRecordTables"></a>
A list of AWS Glue table definitions used by the transform.
Type: Array of [GlueTable](API_GlueTable.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: Yes

 ** [MaxCapacity](#API_CreateMLTransform_RequestSyntax) **   <a name="Glue-CreateMLTransform-request-MaxCapacity"></a>
The number of AWS Glue data processing units (DPUs) that are allocated to task runs for this transform. You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the [AWS Glue pricing page](https://aws.amazon.com/glue/pricing/).
 `MaxCapacity` is a mutually exclusive option with `NumberOfWorkers` and `WorkerType`.
+ If either `NumberOfWorkers` or `WorkerType` is set, then `MaxCapacity` cannot be set.
+ If `MaxCapacity` is set then neither `NumberOfWorkers` or `WorkerType` can be set.
+ If `WorkerType` is set, then `NumberOfWorkers` is required (and vice versa).
+  `MaxCapacity` and `NumberOfWorkers` must both be at least 1.
When the `WorkerType` field is set to a value other than `Standard`, the `MaxCapacity` field is set automatically and becomes read-only.
When the `WorkerType` field is set to a value other than `Standard`, the `MaxCapacity` field is set automatically and becomes read-only.
Type: Double
Required: No

 ** [MaxRetries](#API_CreateMLTransform_RequestSyntax) **   <a name="Glue-CreateMLTransform-request-MaxRetries"></a>
The maximum number of times to retry a task for this transform after a task run fails.
Type: Integer
Required: No

 ** [Name](#API_CreateMLTransform_RequestSyntax) **   <a name="Glue-CreateMLTransform-request-Name"></a>
The unique name that you give the transform when you create it.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** [NumberOfWorkers](#API_CreateMLTransform_RequestSyntax) **   <a name="Glue-CreateMLTransform-request-NumberOfWorkers"></a>
The number of workers of a defined `workerType` that are allocated when this task runs.
If `WorkerType` is set, then `NumberOfWorkers` is required (and vice versa).
Type: Integer
Required: No

 ** [Parameters](#API_CreateMLTransform_RequestSyntax) **   <a name="Glue-CreateMLTransform-request-Parameters"></a>
The algorithmic parameters that are specific to the transform type used. Conditionally dependent on the transform type.
Type: [TransformParameters](API_TransformParameters.md) object
Required: Yes

 ** [Role](#API_CreateMLTransform_RequestSyntax) **   <a name="Glue-CreateMLTransform-request-Role"></a>
The name or Amazon Resource Name (ARN) of the IAM role with the required permissions. The required permissions include both AWS Glue service role permissions to AWS Glue resources, and Amazon S3 permissions required by the transform.
+ This role needs AWS Glue service role permissions to allow access to resources in AWS Glue. See [Attach a Policy to IAM Users That Access AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/attach-policy-iam-user.html).
+ This role needs permission to your Amazon Simple Storage Service (Amazon S3) sources, targets, temporary directory, scripts, and any libraries used by the task run for this transform.
Type: String
Required: Yes

 ** [Tags](#API_CreateMLTransform_RequestSyntax) **   <a name="Glue-CreateMLTransform-request-Tags"></a>
The tags to use with this machine learning transform. You may use tags to limit access to the machine learning transform. For more information about tags in AWS Glue, see [AWS Tags in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/monitor-tags.html) in the developer guide.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [Timeout](#API_CreateMLTransform_RequestSyntax) **   <a name="Glue-CreateMLTransform-request-Timeout"></a>
The timeout of the task run for this transform in minutes. This is the maximum time that a task run for this transform can consume resources before it is terminated and enters `TIMEOUT` status. The default is 2,880 minutes (48 hours).
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [TransformEncryption](#API_CreateMLTransform_RequestSyntax) **   <a name="Glue-CreateMLTransform-request-TransformEncryption"></a>
The encryption-at-rest settings of the transform that apply to accessing user data. Machine learning transforms can access user data encrypted in Amazon S3 using KMS.
Type: [TransformEncryption](API_TransformEncryption.md) object
Required: No

 ** [WorkerType](#API_CreateMLTransform_RequestSyntax) **   <a name="Glue-CreateMLTransform-request-WorkerType"></a>
The type of predefined worker that is allocated when this task runs. Accepts a value of Standard, G.1X, or G.2X.
+ For the `Standard` worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.
+ For the `G.1X` worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and 1 executor per worker.
+ For the `G.2X` worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk, and 1 executor per worker.
 `MaxCapacity` is a mutually exclusive option with `NumberOfWorkers` and `WorkerType`.
+ If either `NumberOfWorkers` or `WorkerType` is set, then `MaxCapacity` cannot be set.
+ If `MaxCapacity` is set then neither `NumberOfWorkers` or `WorkerType` can be set.
+ If `WorkerType` is set, then `NumberOfWorkers` is required (and vice versa).
+  `MaxCapacity` and `NumberOfWorkers` must both be at least 1.
Type: String
Valid Values: `Standard | G.1X | G.2X | G.025X | G.4X | G.8X | Z.2X`
Required: No

## Response Syntax
<a name="API_CreateMLTransform_ResponseSyntax"></a>

```
{
   "TransformId": "string"
}
```

## Response Elements
<a name="API_CreateMLTransform_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TransformId](#API_CreateMLTransform_ResponseSyntax) **   <a name="Glue-CreateMLTransform-response-TransformId"></a>
A unique identifier that is generated for the transform.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

## Errors
<a name="API_CreateMLTransform_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** AlreadyExistsException **
A resource to be created or added already exists.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** IdempotentParameterMismatchException **
The same unique identifier was associated with two different records.
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
<a name="API_CreateMLTransform_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/CreateMLTransform)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/CreateMLTransform)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/CreateMLTransform)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/CreateMLTransform)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/CreateMLTransform)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/CreateMLTransform)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/CreateMLTransform)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/CreateMLTransform)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/CreateMLTransform)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/CreateMLTransform)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
