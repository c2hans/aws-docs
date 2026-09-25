---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoveryPlanExecutionStepConfiguration.html
---

# RecoveryPlanExecutionStepConfiguration
<a name="API_RecoveryPlanExecutionStepConfiguration"></a>

Type-specific configuration for an execution step response. Mirrors `RecoveryPlanStepConfiguration` but uses execution-enriched server shapes.

## Contents
<a name="API_RecoveryPlanExecutionStepConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** executionServerStepConfiguration **   <a name="drs-Type-RecoveryPlanExecutionStepConfiguration-executionServerStepConfiguration"></a>
Configuration for a `SERVER` type execution step.
Type: [ExecutionServerStepConfiguration](API_ExecutionServerStepConfiguration.md) object
Required: No

 ** waitStepConfiguration **   <a name="drs-Type-RecoveryPlanExecutionStepConfiguration-waitStepConfiguration"></a>
Configuration for a `WAIT` type step.
Type: [WaitStepConfiguration](API_WaitStepConfiguration.md) object
Required: No

## See Also
<a name="API_RecoveryPlanExecutionStepConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/RecoveryPlanExecutionStepConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/RecoveryPlanExecutionStepConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/RecoveryPlanExecutionStepConfiguration)
