---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ClusterOrchestrator.html
---

# ClusterOrchestrator
<a name="API_ClusterOrchestrator"></a>

The type of orchestrator used for the SageMaker HyperPod cluster.

## Contents
<a name="API_ClusterOrchestrator_Contents"></a>

 ** Eks **   <a name="sagemaker-Type-ClusterOrchestrator-Eks"></a>
The Amazon EKS cluster used as the orchestrator for the SageMaker HyperPod cluster.
Type: [ClusterOrchestratorEksConfig](API_ClusterOrchestratorEksConfig.md) object
Required: No

 ** Slurm **   <a name="sagemaker-Type-ClusterOrchestrator-Slurm"></a>
The Slurm orchestrator configuration for the SageMaker HyperPod cluster.
Type: [ClusterOrchestratorSlurmConfig](API_ClusterOrchestratorSlurmConfig.md) object
Required: No

## See Also
<a name="API_ClusterOrchestrator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/ClusterOrchestrator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/ClusterOrchestrator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/ClusterOrchestrator)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
