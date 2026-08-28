---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ApplicationOperationInfoDetails.html
---

# ApplicationOperationInfoDetails
<a name="API_ApplicationOperationInfoDetails"></a>

A description of the application operation that provides information about the updates that were made to the application.

## Contents
<a name="API_ApplicationOperationInfoDetails_Contents"></a>

 ** EndTime **   <a name="APIReference-Type-ApplicationOperationInfoDetails-EndTime"></a>
The timestamp that indicates when the operation finished.
Type: Timestamp
Required: Yes

 ** Operation **   <a name="APIReference-Type-ApplicationOperationInfoDetails-Operation"></a>
The type of operation that is performed on an application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** OperationStatus **   <a name="APIReference-Type-ApplicationOperationInfoDetails-OperationStatus"></a>
The status of the operation.
Type: String
Valid Values: `IN_PROGRESS | CANCELLED | SUCCESSFUL | FAILED`
Required: Yes

 ** StartTime **   <a name="APIReference-Type-ApplicationOperationInfoDetails-StartTime"></a>
The timestamp that indicates when the operation was created.
Type: Timestamp
Required: Yes

 ** ApplicationVersionChangeDetails **   <a name="APIReference-Type-ApplicationOperationInfoDetails-ApplicationVersionChangeDetails"></a>
Contains information about the version changes that the operation applied to the application.
Type: [ApplicationVersionChangeDetails](API_ApplicationVersionChangeDetails.md) object
Required: No

 ** OperationFailureDetails **   <a name="APIReference-Type-ApplicationOperationInfoDetails-OperationFailureDetails"></a>
Provides a description of the operation failure.
Type: [OperationFailureDetails](API_OperationFailureDetails.md) object
Required: No

## See Also
<a name="API_ApplicationOperationInfoDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ApplicationOperationInfoDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ApplicationOperationInfoDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ApplicationOperationInfoDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
