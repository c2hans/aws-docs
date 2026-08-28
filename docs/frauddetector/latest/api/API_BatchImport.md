---
source_url: https://docs.aws.amazon.com/frauddetector/latest/api/API_BatchImport.html
---

Amazon Fraud Detector is no longer be open to new customers as of November 7, 2025. For capabilities similar to Amazon Fraud Detector, explore Amazon SageMaker AI, AutoGluon, and AWS WAF.

# BatchImport
<a name="API_BatchImport"></a>

The batch import job details.

## Contents
<a name="API_BatchImport_Contents"></a>

 ** arn **   <a name="FraudDetector-Type-BatchImport-arn"></a>
The ARN of the batch import job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn\:aws[a-z-]{0,15}\:frauddetector\:[a-z0-9-]{3,20}\:[0-9]{12}\:[^\s]{2,128}$`
Required: No

 ** completionTime **   <a name="FraudDetector-Type-BatchImport-completionTime"></a>
Timestamp of when batch import job completed.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

 ** eventTypeName **   <a name="FraudDetector-Type-BatchImport-eventTypeName"></a>
The name of the event type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: No

 ** failedRecordsCount **   <a name="FraudDetector-Type-BatchImport-failedRecordsCount"></a>
The number of records that failed to import.
Type: Integer
Required: No

 ** failureReason **   <a name="FraudDetector-Type-BatchImport-failureReason"></a>
The reason batch import job failed.
Type: String
Required: No

 ** iamRoleArn **   <a name="FraudDetector-Type-BatchImport-iamRoleArn"></a>
The ARN of the IAM role to use for this job request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^arn\:aws[a-z-]{0,15}\:iam\:\:[0-9]{12}\:role\/[^\s]{2,64}$`
Required: No

 ** inputPath **   <a name="FraudDetector-Type-BatchImport-inputPath"></a>
The Amazon S3 location of your data file for batch import.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^s3:\/\/(.+)$`
Required: No

 ** jobId **   <a name="FraudDetector-Type-BatchImport-jobId"></a>
The ID of the batch import job.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[0-9a-z_-]+$`
Required: No

 ** outputPath **   <a name="FraudDetector-Type-BatchImport-outputPath"></a>
The Amazon S3 location of your output file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^s3:\/\/(.+)$`
Required: No

 ** processedRecordsCount **   <a name="FraudDetector-Type-BatchImport-processedRecordsCount"></a>
The number of records processed by batch import job.
Type: Integer
Required: No

 ** startTime **   <a name="FraudDetector-Type-BatchImport-startTime"></a>
Timestamp of when the batch import job started.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 30.
Required: No

 ** status **   <a name="FraudDetector-Type-BatchImport-status"></a>
The status of the batch import job.
Type: String
Valid Values: `IN_PROGRESS_INITIALIZING | IN_PROGRESS | CANCEL_IN_PROGRESS | CANCELED | COMPLETE | FAILED`
Required: No

 ** totalRecordsCount **   <a name="FraudDetector-Type-BatchImport-totalRecordsCount"></a>
The total number of records in the batch import job.
Type: Integer
Required: No

## See Also
<a name="API_BatchImport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/frauddetector-2019-11-15/BatchImport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/frauddetector-2019-11-15/BatchImport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/frauddetector-2019-11-15/BatchImport)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Fraud Detector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query frauddetector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
