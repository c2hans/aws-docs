---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateLabelingJob.html
---

# CreateLabelingJob
<a name="API_CreateLabelingJob"></a>

Creates a job that uses workers to label the data objects in your input dataset. You can use the labeled data to train machine learning models.

You can select your workforce from one of three providers:
+ A private workforce that you create. It can include employees, contractors, and outside experts. Use a private workforce when want the data to stay within your organization or when a specific set of skills is required.
+ One or more vendors that you select from the AWS Marketplace. Vendors provide expertise in specific areas.
+ The Amazon Mechanical Turk workforce. This is the largest workforce, but it should only be used for public data or data that has been stripped of any personally identifiable information.

You can also use *automated data labeling* to reduce the number of data objects that need to be labeled by a human. Automated data labeling uses *active learning* to determine if a data object can be labeled by machine or if it needs to be sent to a human worker. For more information, see [Using Automated Data Labeling](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-automated-labeling.html).

The data objects to be labeled are contained in an Amazon S3 bucket. You create a *manifest file* that describes the location of each object. For more information, see [Using Input and Output Data](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-data.html).

The output can be used as the manifest file for another labeling job or as training data for your machine learning models.

You can use this operation to create a static labeling job or a streaming labeling job. A static labeling job stops if all data objects in the input manifest file identified in `ManifestS3Uri` have been labeled. A streaming labeling job runs perpetually until it is manually stopped, or remains idle for 10 days. You can send new data objects to an active (`InProgress`) streaming labeling job in real time. To learn how to create a static labeling job, see [Create a Labeling Job (API) ](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-create-labeling-job-api.html) in the Amazon SageMaker Developer Guide. To learn how to create a streaming labeling job, see [Create a Streaming Labeling Job](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-streaming-create-job.html).

## Request Syntax
<a name="API_CreateLabelingJob_RequestSyntax"></a>

```
{
   "HumanTaskConfig": {
      "AnnotationConsolidationConfig": {
         "AnnotationConsolidationLambdaArn": "{{string}}"
      },
      "MaxConcurrentTaskCount": {{number}},
      "NumberOfHumanWorkersPerDataObject": {{number}},
      "PreHumanTaskLambdaArn": "{{string}}",
      "PublicWorkforceTaskPrice": {
         "AmountInUsd": {
            "Cents": {{number}},
            "Dollars": {{number}},
            "TenthFractionsOfACent": {{number}}
         }
      },
      "TaskAvailabilityLifetimeInSeconds": {{number}},
      "TaskDescription": "{{string}}",
      "TaskKeywords": [ "{{string}}" ],
      "TaskTimeLimitInSeconds": {{number}},
      "TaskTitle": "{{string}}",
      "UiConfig": {
         "HumanTaskUiArn": "{{string}}",
         "UiTemplateS3Uri": "{{string}}"
      },
      "WorkteamArn": "{{string}}"
   },
   "InputConfig": {
      "DataAttributes": {
         "ContentClassifiers": [ "{{string}}" ]
      },
      "DataSource": {
         "S3DataSource": {
            "ManifestS3Uri": "{{string}}"
         },
         "SnsDataSource": {
            "SnsTopicArn": "{{string}}"
         }
      }
   },
   "LabelAttributeName": "{{string}}",
   "LabelCategoryConfigS3Uri": "{{string}}",
   "LabelingJobAlgorithmsConfig": {
      "InitialActiveLearningModelArn": "{{string}}",
      "LabelingJobAlgorithmSpecificationArn": "{{string}}",
      "LabelingJobResourceConfig": {
         "VolumeKmsKeyId": "{{string}}",
         "VpcConfig": {
            "SecurityGroupIds": [ "{{string}}" ],
            "Subnets": [ "{{string}}" ]
         }
      }
   },
   "LabelingJobName": "{{string}}",
   "OutputConfig": {
      "KmsKeyId": "{{string}}",
      "S3OutputPath": "{{string}}",
      "SnsTopicArn": "{{string}}"
   },
   "RoleArn": "{{string}}",
   "StoppingConditions": {
      "MaxHumanLabeledObjectCount": {{number}},
      "MaxPercentageOfInputDatasetLabeled": {{number}}
   },
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateLabelingJob_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [HumanTaskConfig](#API_CreateLabelingJob_RequestSyntax) **   <a name="sagemaker-CreateLabelingJob-request-HumanTaskConfig"></a>
Configures the labeling task and how it is presented to workers; including, but not limited to price, keywords, and batch size (task count).
Type: [HumanTaskConfig](API_HumanTaskConfig.md) object
Required: Yes

 ** [InputConfig](#API_CreateLabelingJob_RequestSyntax) **   <a name="sagemaker-CreateLabelingJob-request-InputConfig"></a>
Input data for the labeling job, such as the Amazon S3 location of the data objects and the location of the manifest file that describes the data objects.
You must specify at least one of the following: `S3DataSource` or `SnsDataSource`.
+ Use `SnsDataSource` to specify an SNS input topic for a streaming labeling job. If you do not specify and SNS input topic ARN, Ground Truth will create a one-time labeling job that stops after all data objects in the input manifest file have been labeled.
+ Use `S3DataSource` to specify an input manifest file for both streaming and one-time labeling jobs. Adding an `S3DataSource` is optional if you use `SnsDataSource` to create a streaming labeling job.
If you use the Amazon Mechanical Turk workforce, your input data should not include confidential information, personal information or protected health information. Use `ContentClassifiers` to specify that your data is free of personally identifiable information and adult content.
Type: [LabelingJobInputConfig](API_LabelingJobInputConfig.md) object
Required: Yes

 ** [LabelAttributeName](#API_CreateLabelingJob_RequestSyntax) **   <a name="sagemaker-CreateLabelingJob-request-LabelAttributeName"></a>
The attribute name to use for the label in the output manifest file. This is the key for the key/value pair formed with the label that a worker assigns to the object. The `LabelAttributeName` must meet the following requirements.
+ The name can't end with "-metadata".
+ If you are using one of the [built-in task types](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-task-types.html) or one of the following, the attribute name *must* end with "-ref".
  + Image semantic segmentation (`SemanticSegmentation)` and adjustment (`AdjustmentSemanticSegmentation`) labeling jobs for this task type. One exception is that verification (`VerificationSemanticSegmentation`) *must not* end with -"ref".
  + Video frame object detection (`VideoObjectDetection`), and adjustment and verification (`AdjustmentVideoObjectDetection`) labeling jobs for this task type.
  + Video frame object tracking (`VideoObjectTracking`), and adjustment and verification (`AdjustmentVideoObjectTracking`) labeling jobs for this task type.
  + 3D point cloud semantic segmentation (`3DPointCloudSemanticSegmentation`), and adjustment and verification (`Adjustment3DPointCloudSemanticSegmentation`) labeling jobs for this task type.
  + 3D point cloud object tracking (`3DPointCloudObjectTracking`), and adjustment and verification (`Adjustment3DPointCloudObjectTracking`) labeling jobs for this task type.

If you are creating an adjustment or verification labeling job, you must use a *different* `LabelAttributeName` than the one used in the original labeling job. The original labeling job is the Ground Truth labeling job that produced the labels that you want verified or adjusted. To learn more about adjustment and verification labeling jobs, see [Verify and Adjust Labels](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-verification-data.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,126}`
Required: Yes

 ** [LabelCategoryConfigS3Uri](#API_CreateLabelingJob_RequestSyntax) **   <a name="sagemaker-CreateLabelingJob-request-LabelCategoryConfigS3Uri"></a>
The S3 URI of the file, referred to as a *label category configuration file*, that defines the categories used to label the data objects.
For 3D point cloud and video frame task types, you can add label category attributes and frame attributes to your label category configuration file. To learn how, see [Create a Labeling Category Configuration File for 3D Point Cloud Labeling Jobs](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-point-cloud-label-category-config.html).
For named entity recognition jobs, in addition to `"labels"`, you must provide worker instructions in the label category configuration file using the `"instructions"` parameter: `"instructions": {"shortInstruction":"<h1>Add header</h1><p>Add Instructions</p>", "fullInstruction":"<p>Add additional instructions.</p>"}`. For details and an example, see [Create a Named Entity Recognition Labeling Job (API) ](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-named-entity-recg.html#sms-creating-ner-api).
For all other [built-in task types](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-task-types.html) and [custom tasks](https://docs.aws.amazon.com/sagemaker/latest/dg/sms-custom-templates.html), your label category configuration file must be a JSON file in the following format. Identify the labels you want to use by replacing `label_1`, `label_2`,`...`,`label_n` with your label categories.
 `{ `
 `"document-version": "2018-11-28",`
 `"labels": [{"label": "label_1"},{"label": "label_2"},...{"label": "label_n"}]`
 `}`
Note the following about the label category configuration file:
+ For image classification and text classification (single and multi-label) you must specify at least two label categories. For all other task types, the minimum number of label categories required is one.
+ Each label category must be unique, you cannot specify duplicate label categories.
+ If you create a 3D point cloud or video frame adjustment or verification labeling job, you must include `auditLabelAttributeName` in the label category configuration. Use this parameter to enter the [`LabelAttributeName`](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CreateLabelingJob.html#sagemaker-CreateLabelingJob-request-LabelAttributeName) of the labeling job you want to adjust or verify annotations of.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: No

 ** [LabelingJobAlgorithmsConfig](#API_CreateLabelingJob_RequestSyntax) **   <a name="sagemaker-CreateLabelingJob-request-LabelingJobAlgorithmsConfig"></a>
Configures the information required to perform automated data labeling.
Type: [LabelingJobAlgorithmsConfig](API_LabelingJobAlgorithmsConfig.md) object
Required: No

 ** [LabelingJobName](#API_CreateLabelingJob_RequestSyntax) **   <a name="sagemaker-CreateLabelingJob-request-LabelingJobName"></a>
The name of the labeling job. This name is used to identify the job in a list of labeling jobs. Labeling job names must be unique within an AWS account and region. `LabelingJobName` is not case sensitive. For example, Example-job and example-job are considered the same labeling job name by Ground Truth.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
Required: Yes

 ** [OutputConfig](#API_CreateLabelingJob_RequestSyntax) **   <a name="sagemaker-CreateLabelingJob-request-OutputConfig"></a>
The location of the output data and the AWS Key Management Service key ID for the key used to encrypt the output data, if any.
Type: [LabelingJobOutputConfig](API_LabelingJobOutputConfig.md) object
Required: Yes

 ** [RoleArn](#API_CreateLabelingJob_RequestSyntax) **   <a name="sagemaker-CreateLabelingJob-request-RoleArn"></a>
The Amazon Resource Number (ARN) that Amazon SageMaker assumes to perform tasks on your behalf during data labeling. You must grant this role the necessary permissions so that Amazon SageMaker can successfully complete data labeling.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: Yes

 ** [StoppingConditions](#API_CreateLabelingJob_RequestSyntax) **   <a name="sagemaker-CreateLabelingJob-request-StoppingConditions"></a>
A set of conditions for stopping the labeling job. If any of the conditions are met, the job is automatically stopped. You can use these conditions to control the cost of data labeling.
Type: [LabelingJobStoppingConditions](API_LabelingJobStoppingConditions.md) object
Required: No

 ** [Tags](#API_CreateLabelingJob_RequestSyntax) **   <a name="sagemaker-CreateLabelingJob-request-Tags"></a>
An array of key/value pairs. For more information, see [Using Cost Allocation Tags](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/cost-alloc-tags.html#allocation-what) in the * AWS Billing and Cost Management User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

## Response Syntax
<a name="API_CreateLabelingJob_ResponseSyntax"></a>

```
{
   "LabelingJobArn": "string"
}
```

## Response Elements
<a name="API_CreateLabelingJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LabelingJobArn](#API_CreateLabelingJob_ResponseSyntax) **   <a name="sagemaker-CreateLabelingJob-response-LabelingJobArn"></a>
The Amazon Resource Name (ARN) of the labeling job. You use this ARN to identify the labeling job.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:labeling-job/.*`

## Errors
<a name="API_CreateLabelingJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceInUse **
Resource being accessed is in use.
HTTP Status Code: 400

 ** ResourceLimitExceeded **
 You have exceeded an SageMaker resource limit. For example, you might have too many training jobs created.
HTTP Status Code: 400

## See Also
<a name="API_CreateLabelingJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/CreateLabelingJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/CreateLabelingJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CreateLabelingJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/CreateLabelingJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CreateLabelingJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/CreateLabelingJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/CreateLabelingJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/CreateLabelingJob)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/CreateLabelingJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CreateLabelingJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
