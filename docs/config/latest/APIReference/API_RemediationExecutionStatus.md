---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_RemediationExecutionStatus.html
---

# RemediationExecutionStatus
<a name="API_RemediationExecutionStatus"></a>

Provides details of the current status of the invoked remediation action for that resource.

## Contents
<a name="API_RemediationExecutionStatus_Contents"></a>

 ** InvocationTime **   <a name="config-Type-RemediationExecutionStatus-InvocationTime"></a>
Start time when the remediation was executed.
Type: Timestamp
Required: No

 ** LastUpdatedTime **   <a name="config-Type-RemediationExecutionStatus-LastUpdatedTime"></a>
The time when the remediation execution was last updated.
Type: Timestamp
Required: No

 ** ResourceKey **   <a name="config-Type-RemediationExecutionStatus-ResourceKey"></a>
The details that identify a resource within AWS Config, including the resource type and resource ID.
Type: [ResourceKey](API_ResourceKey.md) object
Required: No

 ** State **   <a name="config-Type-RemediationExecutionStatus-State"></a>
ENUM of the values.
Type: String
Valid Values: `QUEUED | IN_PROGRESS | SUCCEEDED | FAILED | UNKNOWN`
Required: No

 ** StepDetails **   <a name="config-Type-RemediationExecutionStatus-StepDetails"></a>
Details of every step.
Type: Array of [RemediationExecutionStep](API_RemediationExecutionStep.md) objects
Required: No

## See Also
<a name="API_RemediationExecutionStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/RemediationExecutionStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/RemediationExecutionStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/RemediationExecutionStatus)
