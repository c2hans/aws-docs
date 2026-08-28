---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ProjectVersionDescription.html
---

# ProjectVersionDescription
<a name="API_ProjectVersionDescription"></a>

A description of a version of a Amazon Rekognition project version.

## Contents
<a name="API_ProjectVersionDescription_Contents"></a>

 ** BaseModelVersion **   <a name="rekognition-Type-ProjectVersionDescription-BaseModelVersion"></a>
The base detection model version used to create the project version.
Type: String
Required: No

 ** BillableTrainingTimeInSeconds **   <a name="rekognition-Type-ProjectVersionDescription-BillableTrainingTimeInSeconds"></a>
The duration, in seconds, that you were billed for a successful training of the model version. This value is only returned if the model version has been successfully trained.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** CreationTimestamp **   <a name="rekognition-Type-ProjectVersionDescription-CreationTimestamp"></a>
The Unix datetime for the date and time that training started.
Type: Timestamp
Required: No

 ** EvaluationResult **   <a name="rekognition-Type-ProjectVersionDescription-EvaluationResult"></a>
The training results. `EvaluationResult` is only returned if training is successful.
Type: [EvaluationResult](API_EvaluationResult.md) object
Required: No

 ** Feature **   <a name="rekognition-Type-ProjectVersionDescription-Feature"></a>
The feature that was customized.
Type: String
Valid Values: `CONTENT_MODERATION | CUSTOM_LABELS`
Required: No

 ** FeatureConfig **   <a name="rekognition-Type-ProjectVersionDescription-FeatureConfig"></a>
Feature specific configuration that was applied during training.
Type: [CustomizationFeatureConfig](API_CustomizationFeatureConfig.md) object
Required: No

 ** KmsKeyId **   <a name="rekognition-Type-ProjectVersionDescription-KmsKeyId"></a>
The identifer for the AWS Key Management Service key (AWS KMS key) that was used to encrypt the model during training.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,2048}$`
Required: No

 ** ManifestSummary **   <a name="rekognition-Type-ProjectVersionDescription-ManifestSummary"></a>
The location of the summary manifest. The summary manifest provides aggregate data validation results for the training and test datasets.
Type: [GroundTruthManifest](API_GroundTruthManifest.md) object
Required: No

 ** MaxInferenceUnits **   <a name="rekognition-Type-ProjectVersionDescription-MaxInferenceUnits"></a>
The maximum number of inference units Amazon Rekognition uses to auto-scale the model. Applies only to Custom Labels projects. For more information, see [StartProjectVersion](API_StartProjectVersion.md).
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** MinInferenceUnits **   <a name="rekognition-Type-ProjectVersionDescription-MinInferenceUnits"></a>
The minimum number of inference units used by the model. Applies only to Custom Labels projects. For more information, see [StartProjectVersion](API_StartProjectVersion.md).
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** OutputConfig **   <a name="rekognition-Type-ProjectVersionDescription-OutputConfig"></a>
The location where training results are saved.
Type: [OutputConfig](API_OutputConfig.md) object
Required: No

 ** ProjectVersionArn **   <a name="rekognition-Type-ProjectVersionDescription-ProjectVersionArn"></a>
The Amazon Resource Name (ARN) of the project version.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/version\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)`
Required: No

 ** SourceProjectVersionArn **   <a name="rekognition-Type-ProjectVersionDescription-SourceProjectVersionArn"></a>
If the model version was copied from a different project, `SourceProjectVersionArn` contains the ARN of the source model version.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `(^arn:[a-z\d-]+:rekognition:[a-z\d-]+:\d{12}:project\/[a-zA-Z0-9_.\-]{1,255}\/version\/[a-zA-Z0-9_.\-]{1,255}\/[0-9]+$)`
Required: No

 ** Status **   <a name="rekognition-Type-ProjectVersionDescription-Status"></a>
The current status of the model version.
Type: String
Valid Values: `TRAINING_IN_PROGRESS | TRAINING_COMPLETED | TRAINING_FAILED | STARTING | RUNNING | FAILED | STOPPING | STOPPED | DELETING | COPYING_IN_PROGRESS | COPYING_COMPLETED | COPYING_FAILED | DEPRECATED | EXPIRED`
Required: No

 ** StatusMessage **   <a name="rekognition-Type-ProjectVersionDescription-StatusMessage"></a>
A descriptive message for an error or warning that occurred.
Type: String
Required: No

 ** TestingDataResult **   <a name="rekognition-Type-ProjectVersionDescription-TestingDataResult"></a>
Contains information about the testing results.
Type: [TestingDataResult](API_TestingDataResult.md) object
Required: No

 ** TrainingDataResult **   <a name="rekognition-Type-ProjectVersionDescription-TrainingDataResult"></a>
Contains information about the training results.
Type: [TrainingDataResult](API_TrainingDataResult.md) object
Required: No

 ** TrainingEndTimestamp **   <a name="rekognition-Type-ProjectVersionDescription-TrainingEndTimestamp"></a>
The Unix date and time that training of the model ended.
Type: Timestamp
Required: No

 ** VersionDescription **   <a name="rekognition-Type-ProjectVersionDescription-VersionDescription"></a>
A user-provided description of the project version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9-_. ()':,;?]+`
Required: No

## See Also
<a name="API_ProjectVersionDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ProjectVersionDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/ProjectVersionDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/ProjectVersionDescription)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
