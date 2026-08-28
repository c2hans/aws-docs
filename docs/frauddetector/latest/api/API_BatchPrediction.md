---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_BatchPrediction.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# BatchPrediction
<a name="API_BatchPrediction"></a>

The batch prediction details.

## Contents
<a name="API_BatchPrediction_Contents"></a>

 ** arn **   <a name="FraudDetector-Type-BatchPrediction-arn"></a>
The ARN of batch prediction job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn\:aws[a-z-]{0,15}\:frauddetector\:[a-z0-9-]{3,20}\:[0-9]{12}\:[^\s]{2,128}$`
Required: No

 ** completionTime **   <a name="FraudDetector-Type-BatchPrediction-completionTime"></a>
Timestamp of when the batch prediction job completed.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

 ** detectorName **   <a name="FraudDetector-Type-BatchPrediction-detectorName"></a>
The name of the detector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: No

 ** detectorVersion **   <a name="FraudDetector-Type-BatchPrediction-detectorVersion"></a>
The detector version.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 7.
Pattern: `^[1-9][0-9]{0,3}\.[0-9]{1,2}$`
Required: No

 ** eventTypeName **   <a name="FraudDetector-Type-BatchPrediction-eventTypeName"></a>
The name of the event type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: No

 ** failureReason **   <a name="FraudDetector-Type-BatchPrediction-failureReason"></a>
The reason a batch prediction job failed.
Type: String
Required: No

 ** iamRoleArn **   <a name="FraudDetector-Type-BatchPrediction-iamRoleArn"></a>
The ARN of the IAM role to use for this job request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn\:aws[a-z-]{0,15}\:iam\:\:[0-9]{12}\:role\/[^\s]{2,64}$`
Required: No

 ** inputPath **   <a name="FraudDetector-Type-BatchPrediction-inputPath"></a>
The Amazon S3 location of your training file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^s3:\/\/(.+)$`
Required: No

 ** jobId **   <a name="FraudDetector-Type-BatchPrediction-jobId"></a>
The job ID for the batch prediction.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: No

 ** lastHeartbeatTime **   <a name="FraudDetector-Type-BatchPrediction-lastHeartbeatTime"></a>
Timestamp of most recent heartbeat indicating the batch prediction job was making progress.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

 ** outputPath **   <a name="FraudDetector-Type-BatchPrediction-outputPath"></a>
The Amazon S3 location of your output file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^s3:\/\/(.+)$`
Required: No

 ** processedRecordsCount **   <a name="FraudDetector-Type-BatchPrediction-processedRecordsCount"></a>
The number of records processed by the batch prediction job.
Type: Integer
Required: No

 ** startTime **   <a name="FraudDetector-Type-BatchPrediction-startTime"></a>
Timestamp of when the batch prediction job started.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

 ** status **   <a name="FraudDetector-Type-BatchPrediction-status"></a>
The batch prediction status.
Type: String
Valid Values: `IN_PROGRESS_INITIALIZING | IN_PROGRESS | CANCEL_IN_PROGRESS | CANCELED | COMPLETE | FAILED`
Required: No

 ** totalRecordsCount **   <a name="FraudDetector-Type-BatchPrediction-totalRecordsCount"></a>
The total number of records in the batch prediction job.
Type: Integer
Required: No

## See Also
<a name="API_BatchPrediction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/BatchPrediction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/BatchPrediction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/BatchPrediction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
