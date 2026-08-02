---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ComplianceExecutionSummary.html
---

# ComplianceExecutionSummary
<a name="API_ComplianceExecutionSummary"></a>

A summary of the call execution that includes an execution ID, the type of execution (for example, `Command`), and the date/time of the execution using a datetime object that is saved in the following format: `yyyy-MM-dd'T'HH:mm:ss'Z'`

## Contents
<a name="API_ComplianceExecutionSummary_Contents"></a>

 ** ExecutionTime **   <a name="systemsmanager-Type-ComplianceExecutionSummary-ExecutionTime"></a>
The time the execution ran as a datetime object that is saved in the following format: `yyyy-MM-dd'T'HH:mm:ss'Z'`
For State Manager associations, this timestamp represents when the compliance status was captured and reported by the Systems Manager service, not when the underlying association was actually executed on the managed node. To track actual association execution times, use the [DescribeAssociationExecutionTargets](API_DescribeAssociationExecutionTargets.md) command or check the association execution history in the Systems Manager console.
Type: Timestamp
Required: Yes

 ** ExecutionId **   <a name="systemsmanager-Type-ComplianceExecutionSummary-ExecutionId"></a>
An ID created by the system when `PutComplianceItems` was called. For example, `CommandID` is a valid execution ID. You can use this ID in subsequent calls.
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** ExecutionType **   <a name="systemsmanager-Type-ComplianceExecutionSummary-ExecutionType"></a>
The type of execution. For example, `Command` is a valid execution type.
Type: String
Length Constraints: Maximum length of 50.
Required: No

## See Also
<a name="API_ComplianceExecutionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/ComplianceExecutionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/ComplianceExecutionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/ComplianceExecutionSummary)
