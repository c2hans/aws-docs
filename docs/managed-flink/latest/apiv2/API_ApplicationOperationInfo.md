---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ApplicationOperationInfo.html
---

# ApplicationOperationInfo
<a name="API_ApplicationOperationInfo"></a>

A description of the aplication operation that provides information about the updates that were made to the application.

## Contents
<a name="API_ApplicationOperationInfo_Contents"></a>

 ** EndTime **   <a name="APIReference-Type-ApplicationOperationInfo-EndTime"></a>
The timestamp that indicates when the operation finished.
Type: Timestamp
Required: No

 ** Operation **   <a name="APIReference-Type-ApplicationOperationInfo-Operation"></a>
The type of operation that is performed on an application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** OperationId **   <a name="APIReference-Type-ApplicationOperationInfo-OperationId"></a>
The operation ID of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** OperationStatus **   <a name="APIReference-Type-ApplicationOperationInfo-OperationStatus"></a>
The status of the operation.
Type: String
Valid Values: `IN_PROGRESS | CANCELLED | SUCCESSFUL | FAILED`
Required: No

 ** StartTime **   <a name="APIReference-Type-ApplicationOperationInfo-StartTime"></a>
The timestamp that indicates when the operation was created.
Type: Timestamp
Required: No

## See Also
<a name="API_ApplicationOperationInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/ApplicationOperationInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/ApplicationOperationInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/ApplicationOperationInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
