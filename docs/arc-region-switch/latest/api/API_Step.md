---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_Step.html
---

# Step
<a name="API_Step"></a>

Represents a step in a Region switch plan workflow. Each step performs a specific action during the Region switch process.

## Contents
<a name="API_Step_Contents"></a>

 ** executionBlockConfiguration **   <a name="regionswitch-Type-Step-executionBlockConfiguration"></a>
The configuration for an execution block in a workflow.
Type: [ExecutionBlockConfiguration](API_ExecutionBlockConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** executionBlockType **   <a name="regionswitch-Type-Step-executionBlockType"></a>
The type of an execution block in a workflow.
Type: String
Valid Values: `CustomActionLambda | ManualApproval | AuroraGlobalDatabase | EC2AutoScaling | ARCRoutingControl | ARCRegionSwitchPlan | Parallel | ECSServiceScaling | EKSResourceScaling | Route53HealthCheck | DocumentDb | RdsPromoteReadReplica | RdsCreateCrossRegionReplica | LambdaEventSourceMapping | AuroraServerlessScaling | AuroraProvisionedScaling | NeptuneGlobalDatabase`
Required: Yes

 ** name **   <a name="regionswitch-Type-Step-name"></a>
The name of a step in a workflow.
Type: String
Required: Yes

 ** description **   <a name="regionswitch-Type-Step-description"></a>
The description of a step in a workflow.
Type: String
Required: No

## See Also
<a name="API_Step_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/Step)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/Step)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/Step)
