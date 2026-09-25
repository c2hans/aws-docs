---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_RecoveryPlanStepConfiguration.html
---

# RecoveryPlanStepConfiguration
<a name="API_RecoveryPlanStepConfiguration"></a>

Type-specific configuration for a Recovery Plan step. Exactly one member must be set.

## Contents
<a name="API_RecoveryPlanStepConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** serverStepConfiguration **   <a name="drs-Type-RecoveryPlanStepConfiguration-serverStepConfiguration"></a>
Configuration for a `SERVER` type step.
Type: [ServerStepConfiguration](API_ServerStepConfiguration.md) object
Required: No

 ** waitStepConfiguration **   <a name="drs-Type-RecoveryPlanStepConfiguration-waitStepConfiguration"></a>
Configuration for a `WAIT` type step.
Type: [WaitStepConfiguration](API_WaitStepConfiguration.md) object
Required: No

## See Also
<a name="API_RecoveryPlanStepConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/RecoveryPlanStepConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/RecoveryPlanStepConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/RecoveryPlanStepConfiguration)
