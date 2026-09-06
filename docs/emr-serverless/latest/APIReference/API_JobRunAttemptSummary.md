---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_JobRunAttemptSummary.html
---

# JobRunAttemptSummary
<a name="API_JobRunAttemptSummary"></a>

The summary of attributes associated with a job run attempt.

## Contents
<a name="API_JobRunAttemptSummary_Contents"></a>

 ** applicationId **   <a name="emrserverless-Type-JobRunAttemptSummary-applicationId"></a>
The ID of the application the job is running on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

 ** arn **   <a name="emrserverless-Type-JobRunAttemptSummary-arn"></a>
The Amazon Resource Name (ARN) of the job run.
Type: String
Length Constraints: Minimum length of 60. Maximum length of 1024.
Pattern: `arn:(aws[a-zA-Z0-9-]*):emr-serverless:.+:(\d{12}):\/applications\/[0-9a-zA-Z]+\/jobruns\/[0-9a-zA-Z]+`
Required: Yes

 ** createdAt **   <a name="emrserverless-Type-JobRunAttemptSummary-createdAt"></a>
The date and time when the job run attempt was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="emrserverless-Type-JobRunAttemptSummary-createdBy"></a>
The user who created the job run.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z0-9-]*):(iam|sts)::(\d{12})?:[\w/+=,.@-]+`
Required: Yes

 ** executionRole **   <a name="emrserverless-Type-JobRunAttemptSummary-executionRole"></a>
The Amazon Resource Name (ARN) of the execution role of the job run..
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z0-9-]*):iam::([0-9]{12}):(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)`
Required: Yes

 ** id **   <a name="emrserverless-Type-JobRunAttemptSummary-id"></a>
The ID of the job run attempt.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

 ** jobCreatedAt **   <a name="emrserverless-Type-JobRunAttemptSummary-jobCreatedAt"></a>
The date and time of when the job run was created.
Type: Timestamp
Required: Yes

 ** releaseLabel **   <a name="emrserverless-Type-JobRunAttemptSummary-releaseLabel"></a>
The Amazon EMR release label of the job run attempt.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9._/-]+`
Required: Yes

 ** state **   <a name="emrserverless-Type-JobRunAttemptSummary-state"></a>
The state of the job run attempt.
Type: String
Valid Values: `SUBMITTED | PENDING | SCHEDULED | RUNNING | SUCCESS | FAILED | CANCELLING | CANCELLED | QUEUED`
Required: Yes

 ** stateDetails **   <a name="emrserverless-Type-JobRunAttemptSummary-stateDetails"></a>
The state details of the job run attempt.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: Yes

 ** updatedAt **   <a name="emrserverless-Type-JobRunAttemptSummary-updatedAt"></a>
The date and time of when the job run attempt was last updated.
Type: Timestamp
Required: Yes

 ** attempt **   <a name="emrserverless-Type-JobRunAttemptSummary-attempt"></a>
The attempt number of the job run execution.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** mode **   <a name="emrserverless-Type-JobRunAttemptSummary-mode"></a>
The mode of the job run attempt.
Type: String
Valid Values: `BATCH | STREAMING`
Required: No

 ** name **   <a name="emrserverless-Type-JobRunAttemptSummary-name"></a>
The name of the job run attempt.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** type **   <a name="emrserverless-Type-JobRunAttemptSummary-type"></a>
The type of the job run, such as Spark or Hive.
Type: String
Required: No

## See Also
<a name="API_JobRunAttemptSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/JobRunAttemptSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/JobRunAttemptSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/JobRunAttemptSummary)
