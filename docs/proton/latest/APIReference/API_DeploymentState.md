---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_DeploymentState.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# DeploymentState
<a name="API_DeploymentState"></a>

The detailed data about the current state of the deployment.

## Contents
<a name="API_DeploymentState_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** component **   <a name="proton-Type-DeploymentState-component"></a>
The state of the component associated with the deployment.
Type: [ComponentState](API_ComponentState.md) object
Required: No

 ** environment **   <a name="proton-Type-DeploymentState-environment"></a>
The state of the environment associated with the deployment.
Type: [EnvironmentState](API_EnvironmentState.md) object
Required: No

 ** serviceInstance **   <a name="proton-Type-DeploymentState-serviceInstance"></a>
The state of the service instance associated with the deployment.
Type: [ServiceInstanceState](API_ServiceInstanceState.md) object
Required: No

 ** servicePipeline **   <a name="proton-Type-DeploymentState-servicePipeline"></a>
The state of the service pipeline associated with the deployment.
Type: [ServicePipelineState](API_ServicePipelineState.md) object
Required: No

## See Also
<a name="API_DeploymentState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/DeploymentState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/DeploymentState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/DeploymentState)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
