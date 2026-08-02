---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_SessionSummary.html
---

# SessionSummary
<a name="API_SessionSummary"></a>

The summary of attributes associated with a session.

## Contents
<a name="API_SessionSummary_Contents"></a>

 ** applicationId **   <a name="emrserverless-Type-SessionSummary-applicationId"></a>
The ID of the application that the session belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

 ** arn **   <a name="emrserverless-Type-SessionSummary-arn"></a>
The Amazon Resource Name (ARN) of the session.
Type: String
Length Constraints: Minimum length of 60. Maximum length of 1024.
Pattern: `arn:(aws[a-zA-Z0-9-]*):emr-serverless:.+:(\d{12}):\/applications\/[0-9a-zA-Z]+\/sessions\/[0-9a-zA-Z]+`
Required: Yes

 ** createdAt **   <a name="emrserverless-Type-SessionSummary-createdAt"></a>
The date and time that the session was created.
Type: Timestamp
Required: Yes

 ** createdBy **   <a name="emrserverless-Type-SessionSummary-createdBy"></a>
The IAM principal that created the session.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z0-9-]*):(iam|sts)::(\d{12})?:[\w/+=,.@-]+`
Required: Yes

 ** executionRoleArn **   <a name="emrserverless-Type-SessionSummary-executionRoleArn"></a>
The Amazon Resource Name (ARN) of the execution role for the session.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z0-9-]*):iam::([0-9]{12}):(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)`
Required: Yes

 ** releaseLabel **   <a name="emrserverless-Type-SessionSummary-releaseLabel"></a>
The Amazon EMR release label associated with the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9._/-]+`
Required: Yes

 ** sessionId **   <a name="emrserverless-Type-SessionSummary-sessionId"></a>
The ID of the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

 ** state **   <a name="emrserverless-Type-SessionSummary-state"></a>
The state of the session.
Type: String
Valid Values: `SUBMITTED | STARTING | STARTED | IDLE | BUSY | FAILED | TERMINATING | TERMINATED`
Required: Yes

 ** stateDetails **   <a name="emrserverless-Type-SessionSummary-stateDetails"></a>
Additional details about the current state of the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.*\S.*`
Required: Yes

 ** updatedAt **   <a name="emrserverless-Type-SessionSummary-updatedAt"></a>
The date and time that the session was last updated.
Type: Timestamp
Required: Yes

 ** name **   <a name="emrserverless-Type-SessionSummary-name"></a>
The optional name of the session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_SessionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/SessionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/SessionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/SessionSummary)
