---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_ReplicationTaskAssessmentResult.html
---

# ReplicationTaskAssessmentResult
<a name="API_ReplicationTaskAssessmentResult"></a>

 The task assessment report in JSON format.

## Contents
<a name="API_ReplicationTaskAssessmentResult_Contents"></a>

 ** AssessmentResults **   <a name="DMS-Type-ReplicationTaskAssessmentResult-AssessmentResults"></a>
 The task assessment results in JSON format.
The response object only contains this field if you provide [DescribeReplicationTaskAssessmentResults:ReplicationTaskArn](API_DescribeReplicationTaskAssessmentResults.md#DMS-DescribeReplicationTaskAssessmentResults-request-ReplicationTaskArn) in the request.
Type: String
Required: No

 ** AssessmentResultsFile **   <a name="DMS-Type-ReplicationTaskAssessmentResult-AssessmentResultsFile"></a>
 The file containing the results of the task assessment.
Type: String
Required: No

 ** AssessmentStatus **   <a name="DMS-Type-ReplicationTaskAssessmentResult-AssessmentStatus"></a>
 The status of the task assessment.
Type: String
Required: No

 ** ReplicationTaskArn **   <a name="DMS-Type-ReplicationTaskAssessmentResult-ReplicationTaskArn"></a>
The Amazon Resource Name (ARN) of the replication task.
Type: String
Required: No

 ** ReplicationTaskIdentifier **   <a name="DMS-Type-ReplicationTaskAssessmentResult-ReplicationTaskIdentifier"></a>
 The replication task identifier of the task on which the task assessment was run.
Type: String
Required: No

 ** ReplicationTaskLastAssessmentDate **   <a name="DMS-Type-ReplicationTaskAssessmentResult-ReplicationTaskLastAssessmentDate"></a>
The date the task assessment was completed.
Type: Timestamp
Required: No

 ** S3ObjectUrl **   <a name="DMS-Type-ReplicationTaskAssessmentResult-S3ObjectUrl"></a>
 The URL of the S3 object containing the task assessment results.
The response object only contains this field if you provide [DescribeReplicationTaskAssessmentResults:ReplicationTaskArn](API_DescribeReplicationTaskAssessmentResults.md#DMS-DescribeReplicationTaskAssessmentResults-request-ReplicationTaskArn) in the request.
Type: String
Required: No

## See Also
<a name="API_ReplicationTaskAssessmentResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/ReplicationTaskAssessmentResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/ReplicationTaskAssessmentResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/ReplicationTaskAssessmentResult)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
