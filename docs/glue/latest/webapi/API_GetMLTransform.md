---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetMLTransform.html
---

# GetMLTransform
<a name="API_GetMLTransform"></a>

Gets an AWS Glue machine learning transform artifact and all its corresponding metadata. Machine learning transforms are a special type of transform that use machine learning to learn the details of the transformation to be performed by learning from examples provided by humans. These transformations are then saved by AWS Glue. You can retrieve their metadata by calling `GetMLTransform`.

## Request Syntax
<a name="API_GetMLTransform_RequestSyntax"></a>

```
{
   "TransformId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetMLTransform_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TransformId](#API_GetMLTransform_RequestSyntax) **   <a name="Glue-GetMLTransform-request-TransformId"></a>
The unique identifier of the transform, generated at the time that the transform was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

## Response Syntax
<a name="API_GetMLTransform_ResponseSyntax"></a>

```
{
   "CreatedOn": number,
   "Description": "string",
   "EvaluationMetrics": {
      "FindMatchesMetrics": {
         "AreaUnderPRCurve": number,
         "ColumnImportances": [
            {
               "ColumnName": "string",
               "Importance": number
            }
         ],
         "ConfusionMatrix": {
            "NumFalseNegatives": number,
            "NumFalsePositives": number,
            "NumTrueNegatives": number,
            "NumTruePositives": number
         },
         "F1": number,
         "Precision": number,
         "Recall": number
      },
      "TransformType": "string"
   },
   "GlueVersion": "string",
   "InputRecordTables": [
      {
         "AdditionalOptions": {
            "string" : "string"
         },
         "CatalogId": "string",
         "ConnectionName": "string",
         "DatabaseName": "string",
         "TableName": "string"
      }
   ],
   "LabelCount": number,
   "LastModifiedOn": number,
   "MaxCapacity": number,
   "MaxRetries": number,
   "Name": "string",
   "NumberOfWorkers": number,
   "Parameters": {
      "FindMatchesParameters": {
         "AccuracyCostTradeoff": number,
         "EnforceProvidedLabels": boolean,
         "PrecisionRecallTradeoff": number,
         "PrimaryKeyColumnName": "string"
      },
      "TransformType": "string"
   },
   "Role": "string",
   "Schema": [
      {
         "DataType": "string",
         "Name": "string"
      }
   ],
   "Status": "string",
   "Timeout": number,
   "TransformEncryption": {
      "MlUserDataEncryption": {
         "KmsKeyId": "string",
         "MlUserDataEncryptionMode": "string"
      },
      "TaskRunSecurityConfigurationName": "string"
   },
   "TransformId": "string",
   "WorkerType": "string"
}
```

## Response Elements
<a name="API_GetMLTransform_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedOn](#API_GetMLTransform_ResponseSyntax) **   <a name="Glue-GetMLTransform-response-CreatedOn"></a>
The date and time when the transform was created.
Type: Timestamp

 ** [Description](#API_GetMLTransform_ResponseSyntax) **   <a name="Glue-GetMLTransform-response-Description"></a>
A description of the transform.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\r\n\t]*`

 ** [EvaluationMetrics](#API_GetMLTransform_ResponseSyntax) **   <a name="Glue-GetMLTransform-response-EvaluationMetrics"></a>
The latest evaluation metrics.
Type: [EvaluationMetrics](API_EvaluationMetrics.md) object

 ** [GlueVersion](#API_GetMLTransform_ResponseSyntax) **   <a name="Glue-GetMLTransform-response-GlueVersion"></a>
This value determines which version of AWS Glue this machine learning transform is compatible with. Glue 1.0 is recommended for most customers. If the value is not set, the Glue compatibility defaults to Glue 0.9. For more information, see [AWS Glue Versions](https://docs.aws.amazon.com/glue/latest/dg/release-notes.html#release-notes-versions) in the developer guide.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(\w+\.)+\w+$`

 ** [InputRecordTables](#API_GetMLTransform_ResponseSyntax) **   <a name="Glue-GetMLTransform-response-InputRecordTables"></a>
A list of AWS Glue table definitions used by the transform.
Type: Array of [GlueTable](API_GlueTable.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.

 ** [LabelCount](#API_GetMLTransform_ResponseSyntax) **   <a name="Glue-GetMLTransform-response-LabelCount"></a>
The number of labels available for this transform.
Type: Integer

 ** [LastModifiedOn](#API_GetMLTransform_ResponseSyntax) **   <a name="Glue-GetMLTransform-response-LastModifiedOn"></a>
The date and time when the transform was last modified.
Type: Timestamp

 ** [MaxCapacity](#API_GetMLTransform_ResponseSyntax) **   <a name="Glue-GetMLTransform-response-MaxCapacity"></a>
The number of AWS Glue data processing units (DPUs) that are allocated to task runs for this transform. You can allocate from 2 to 100 DPUs; the default is 10. A DPU is a relative measure of processing power that consists of 4 vCPUs of compute capacity and 16 GB of memory. For more information, see the [AWS Glue pricing page](https://aws.amazon.com/glue/pricing/).
When the `WorkerType` field is set to a value other than `Standard`, the `MaxCapacity` field is set automatically and becomes read-only.
Type: Double

 ** [MaxRetries](#API_GetMLTransform_ResponseSyntax) **   <a name="Glue-GetMLTransform-response-MaxRetries"></a>
The maximum number of times to retry a task for this transform after a task run fails.
Type: Integer

 ** [Name](#API_GetMLTransform_ResponseSyntax) **   <a name="Glue-GetMLTransform-response-Name"></a>
The unique name given to the transform when it was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [NumberOfWorkers](#API_GetMLTransform_ResponseSyntax) **   <a name="Glue-GetMLTransform-response-NumberOfWorkers"></a>
The number of workers of a defined `workerType` that are allocated when this task runs.
Type: Integer

 ** [Parameters](#API_GetMLTransform_ResponseSyntax) **   <a name="Glue-GetMLTransform-response-Parameters"></a>
The configuration parameters that are specific to the algorithm used.
Type: [TransformParameters](API_TransformParameters.md) object

 ** [Role](#API_GetMLTransform_ResponseSyntax) **   <a name="Glue-GetMLTransform-response-Role"></a>
The name or Amazon Resource Name (ARN) of the IAM role with the required permissions.
Type: String

 ** [Schema](#API_GetMLTransform_ResponseSyntax) **   <a name="Glue-GetMLTransform-response-Schema"></a>
The `Map<Column, Type>` object that represents the schema that this transform accepts. Has an upper bound of 100 columns.
Type: Array of [SchemaColumn](API_SchemaColumn.md) objects
Array Members: Maximum number of 100 items.

 ** [Status](#API_GetMLTransform_ResponseSyntax) **   <a name="Glue-GetMLTransform-response-Status"></a>
The last known status of the transform (to indicate whether it can be used or not). One of "NOT\_READY", "READY", or "DELETING".
Type: String
Valid Values: `NOT_READY | READY | DELETING`

 ** [Timeout](#API_GetMLTransform_ResponseSyntax) **   <a name="Glue-GetMLTransform-response-Timeout"></a>
The timeout for a task run for this transform in minutes. This is the maximum time that a task run for this transform can consume resources before it is terminated and enters `TIMEOUT` status. The default is 2,880 minutes (48 hours).
Type: Integer
Valid Range: Minimum value of 1.

 ** [TransformEncryption](#API_GetMLTransform_ResponseSyntax) **   <a name="Glue-GetMLTransform-response-TransformEncryption"></a>
The encryption-at-rest settings of the transform that apply to accessing user data. Machine learning transforms can access user data encrypted in Amazon S3 using KMS.
Type: [TransformEncryption](API_TransformEncryption.md) object

 ** [TransformId](#API_GetMLTransform_ResponseSyntax) **   <a name="Glue-GetMLTransform-response-TransformId"></a>
The unique identifier of the transform, generated at the time that the transform was created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`

 ** [WorkerType](#API_GetMLTransform_ResponseSyntax) **   <a name="Glue-GetMLTransform-response-WorkerType"></a>
The type of predefined worker that is allocated when this task runs. Accepts a value of Standard, G.1X, or G.2X.
+ For the `Standard` worker type, each worker provides 4 vCPU, 16 GB of memory and a 50GB disk, and 2 executors per worker.
+ For the `G.1X` worker type, each worker provides 4 vCPU, 16 GB of memory and a 64GB disk, and 1 executor per worker.
+ For the `G.2X` worker type, each worker provides 8 vCPU, 32 GB of memory and a 128GB disk, and 1 executor per worker.
Type: String
Valid Values: `Standard | G.1X | G.2X | G.025X | G.4X | G.8X | Z.2X`

## Errors
<a name="API_GetMLTransform_Errors"></a>

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

## See Also
<a name="API_GetMLTransform_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetMLTransform)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetMLTransform)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetMLTransform)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetMLTransform)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetMLTransform)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetMLTransform)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetMLTransform)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetMLTransform)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetMLTransform)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetMLTransform)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
