---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_ExecutionStatus.html
---

# ExecutionStatus
<a name="API_DataExports_ExecutionStatus"></a>

The status of the execution.

## Contents
<a name="API_DataExports_ExecutionStatus_Contents"></a>

 ** CompletedAt **   <a name="awscostmanagement-Type-DataExports_ExecutionStatus-CompletedAt"></a>
The time when the execution was completed.
Type: Timestamp
Required: No

 ** CreatedAt **   <a name="awscostmanagement-Type-DataExports_ExecutionStatus-CreatedAt"></a>
The time when the execution was created.
Type: Timestamp
Required: No

 ** LastUpdatedAt **   <a name="awscostmanagement-Type-DataExports_ExecutionStatus-LastUpdatedAt"></a>
The time when the execution was last updated.
Type: Timestamp
Required: No

 ** StatusCode **   <a name="awscostmanagement-Type-DataExports_ExecutionStatus-StatusCode"></a>
The code for the status of the execution.
Type: String
Valid Values: `INITIATION_IN_PROCESS | QUERY_QUEUED | QUERY_IN_PROCESS | QUERY_FAILURE | DELIVERY_IN_PROCESS | DELIVERY_SUCCESS | DELIVERY_FAILURE`
Required: No

 ** StatusReason **   <a name="awscostmanagement-Type-DataExports_ExecutionStatus-StatusReason"></a>
The reason for the failed status.
Type: String
Valid Values: `INSUFFICIENT_PERMISSION | BILL_OWNER_CHANGED | INTERNAL_FAILURE | DEPRECATED`
Required: No

## See Also
<a name="API_DataExports_ExecutionStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-data-exports-2023-11-26/ExecutionStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-data-exports-2023-11-26/ExecutionStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-data-exports-2023-11-26/ExecutionStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
