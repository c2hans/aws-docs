---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_JobRunSummary.html
---

# JobRunSummary
<a name="API_JobRunSummary"></a>

The summary of attributes associated with a job run.

## Contents
<a name="API_JobRunSummary_Contents"></a>

 ** applicationId **   <a name="emrserverless-Type-JobRunSummary-applicationId"></a>
The ID of the application the job is running on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

 ** arn **   <a name="emrserverless-Type-JobRunSummary-arn"></a>
The ARN of the job run.
Type: String
Length Constraints: Minimum length of 60. Maximum length of 1024.
Pattern: `arn:(aws[a-zA-Z0-9-]*):emr-serverless:.+:(\d{12}):\/applications\/[0-9a-zA-Z]+\/jobruns\/[0-9a-zA-Z]+`
Required: Yes

 ** createdAt **   <a name="emrserverless-Type-JobRunSummary-createdAt"></a>
The date and time when the job run was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="emrserverless-Type-JobRunSummary-createdBy"></a>
The user who created the job run.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z0-9-]*):(iam|sts)::(\d{12})?:[\w/+=,.@-]+`
Required: Yes

 ** executionRole **   <a name="emrserverless-Type-JobRunSummary-executionRole"></a>
The execution role ARN of the job run.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z0-9-]*):iam::([0-9]{12}):(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)`
Required: Yes

 ** id **   <a name="emrserverless-Type-JobRunSummary-id"></a>
The ID of the job run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

 ** releaseLabel **   <a name="emrserverless-Type-JobRunSummary-releaseLabel"></a>
The Amazon EMR release associated with the application your job is running on.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9._/-]+`
Required: Yes

 ** state **   <a name="emrserverless-Type-JobRunSummary-state"></a>
The state of the job run.
Type: String
Valid Values: `SUBMITTED | PENDING | SCHEDULED | RUNNING | SUCCESS | FAILED | CANCELLING | CANCELLED | QUEUED`
Required: Yes

 ** stateDetails **   <a name="emrserverless-Type-JobRunSummary-stateDetails"></a>
The state details of the job run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: Yes

 ** updatedAt **   <a name="emrserverless-Type-JobRunSummary-updatedAt"></a>
The date and time when the job run was last updated.
Type: Timestamp
Required: Yes

 ** attempt **   <a name="emrserverless-Type-JobRunSummary-attempt"></a>
The attempt number of the job run execution.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** attemptCreatedAt **   <a name="emrserverless-Type-JobRunSummary-attemptCreatedAt"></a>
The date and time of when the job run attempt was created.
Type: Timestamp
Required: No

 ** attemptUpdatedAt **   <a name="emrserverless-Type-JobRunSummary-attemptUpdatedAt"></a>
The date and time of when the job run attempt was last updated.
Type: Timestamp
Required: No

 ** mode **   <a name="emrserverless-Type-JobRunSummary-mode"></a>
The mode of the job run.
Type: String
Valid Values: `BATCH | STREAMING`
Required: No

 ** name **   <a name="emrserverless-Type-JobRunSummary-name"></a>
The optional job run name. This doesn't have to be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

 ** type **   <a name="emrserverless-Type-JobRunSummary-type"></a>
The type of job run, such as Spark or Hive.
Type: String
Required: No

## See Also
<a name="API_JobRunSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/JobRunSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/JobRunSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/JobRunSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
