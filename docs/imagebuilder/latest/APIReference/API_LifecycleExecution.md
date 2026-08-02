---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_LifecycleExecution.html
---

# LifecycleExecution
<a name="API_LifecycleExecution"></a>

Contains metadata from a runtime instance of a lifecycle policy.

## Contents
<a name="API_LifecycleExecution_Contents"></a>

 ** endTime **   <a name="imagebuilder-Type-LifecycleExecution-endTime"></a>
The timestamp when the lifecycle runtime instance completed.
Type: Timestamp
Required: No

 ** lifecycleExecutionId **   <a name="imagebuilder-Type-LifecycleExecution-lifecycleExecutionId"></a>
Identifies the lifecycle policy runtime instance.
Type: String
Pattern: `^lce-[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$`
Required: No

 ** lifecyclePolicyArn **   <a name="imagebuilder-Type-LifecycleExecution-lifecyclePolicyArn"></a>
The Amazon Resource Name (ARN) of the lifecycle policy that ran.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `^arn:aws(?:-[a-z]+)*:imagebuilder:[a-z]{2,}(?:-[a-z]+)+-[0-9]+:(?:[0-9]{12}|aws):lifecycle-policy/[a-z0-9-_]+$`
Required: No

 ** resourcesImpactedSummary **   <a name="imagebuilder-Type-LifecycleExecution-resourcesImpactedSummary"></a>
Contains information about associated resources that are identified for action by the runtime instance of the lifecycle policy.
Type: [LifecycleExecutionResourcesImpactedSummary](API_LifecycleExecutionResourcesImpactedSummary.md) object
Required: No

 ** startTime **   <a name="imagebuilder-Type-LifecycleExecution-startTime"></a>
The timestamp when the lifecycle runtime instance started.
Type: Timestamp
Required: No

 ** state **   <a name="imagebuilder-Type-LifecycleExecution-state"></a>
Runtime state that reports if the policy action ran successfully, failed, or was skipped.
Type: [LifecycleExecutionState](API_LifecycleExecutionState.md) object
Required: No

## See Also
<a name="API_LifecycleExecution_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/LifecycleExecution)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/LifecycleExecution)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/LifecycleExecution)
