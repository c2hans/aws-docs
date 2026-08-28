---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_OperationFailureDetails.html
---

# OperationFailureDetails
<a name="API_OperationFailureDetails"></a>

Provides a description of the operation failure.

## Contents
<a name="API_OperationFailureDetails_Contents"></a>

 ** ErrorInfo **   <a name="APIReference-Type-OperationFailureDetails-ErrorInfo"></a>
A description of the error that caused an operation to fail.
Type: [ErrorInfo](API_ErrorInfo.md) object
Required: No

 ** RollbackOperationId **   <a name="APIReference-Type-OperationFailureDetails-RollbackOperationId"></a>
The rollback operation ID of the system-rollback operation that executed due to failure in the current operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_OperationFailureDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/OperationFailureDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/OperationFailureDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/OperationFailureDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Service for Apache Flink (formerly Amazon Kinesis Data Analytics for Apache Flink). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managed-flink` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
