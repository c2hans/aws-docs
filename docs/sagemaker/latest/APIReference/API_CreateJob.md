---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateJob.html
---

# CreateJob
<a name="API_CreateJob"></a>

Creates a model customization job in Amazon SageMaker. A job runs a workload based on the job category and configuration you provide. You specify the job category, a schema-versioned configuration document, and an IAM role that grants Amazon SageMaker permission to access resources on your behalf.

Use the `AgentRFT` category to fine-tune a model using multi-turn reinforcement learning with reward signals. Use the `AgentRFTEvaluation` category to evaluate a fine-tuned or base model by running multi-turn rollouts against a held-out prompt dataset and computing metrics such as pass@k and mean reward.

Before creating a job, call `ListJobSchemaVersions` and `DescribeJobSchemaVersion` to retrieve the configuration schema for your job category. The `JobConfigDocument` must conform to the schema specified by `JobConfigSchemaVersion`.

The following operations are related to `CreateJob`:
+  `DescribeJob`
+  `ListJobs`
+  `StopJob`
+  `DeleteJob`
+  `ListJobSchemaVersions`
+  `DescribeJobSchemaVersion`

## Request Syntax
<a name="API_CreateJob_RequestSyntax"></a>

```
{
   "JobCategory": "{{string}}",
   "JobConfigDocument": "{{string}}",
   "JobConfigSchemaVersion": "{{string}}",
   "JobName": "{{string}}",
   "RoleArn": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [JobCategory](#API_CreateJob_RequestSyntax) **   <a name="sagemaker-CreateJob-request-JobCategory"></a>
The category of the job. The category determines the type of workload that the job runs.
Type: String
Valid Values: `AgentRFT | AgentRFTEvaluation`
Required: Yes

 ** [JobConfigDocument](#API_CreateJob_RequestSyntax) **   <a name="sagemaker-CreateJob-request-JobConfigDocument"></a>
The JSON configuration document for the job. The document must conform to the schema specified by `JobConfigSchemaVersion`. Use `DescribeJobSchemaVersion` to retrieve the schema for validation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 262144.
Required: Yes

 ** [JobConfigSchemaVersion](#API_CreateJob_RequestSyntax) **   <a name="sagemaker-CreateJob-request-JobConfigSchemaVersion"></a>
The version of the configuration schema to use for the job configuration document. Use `ListJobSchemaVersions` to get available schema versions for a job category.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 16.
Pattern: `\d+\.\d+\.\d+`
Required: Yes

 ** [JobName](#API_CreateJob_RequestSyntax) **   <a name="sagemaker-CreateJob-request-JobName"></a>
The name of the job. The name must be unique within your account and AWS Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [RoleArn](#API_CreateJob_RequestSyntax) **   <a name="sagemaker-CreateJob-request-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that Amazon SageMaker assumes to perform the job. The role must have the necessary permissions to access the resources required by the job configuration.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [Tags](#API_CreateJob_RequestSyntax) **   <a name="sagemaker-CreateJob-request-Tags"></a>
An array of key-value pairs to apply to the job as tags. For more information, see [Tagging AWS Resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html).
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateJob_ResponseSyntax"></a>

```
{
   "JobArn": "string"
}
```

## Response Elements
<a name="API_CreateJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [JobArn](#API_CreateJob_ResponseSyntax) **   <a name="sagemaker-CreateJob-response-JobArn"></a>
The Amazon Resource Name (ARN) of the job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:(aws[a-z\-]*):sagemaker:[a-z0-9\-]+:[0-9]{12}:job/[a-zA-Z0-9]+/[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`

## Errors
<a name="API_CreateJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_CreateJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateJob)
