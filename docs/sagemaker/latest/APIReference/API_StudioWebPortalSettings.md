---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_StudioWebPortalSettings.html
---

# StudioWebPortalSettings
<a name="API_StudioWebPortalSettings"></a>

Studio settings. If these settings are applied on a user level, they take priority over the settings applied on a domain level.

## Contents
<a name="API_StudioWebPortalSettings_Contents"></a>

 ** ExecutionRoleSessionNameMode **   <a name="sagemaker-Type-StudioWebPortalSettings-ExecutionRoleSessionNameMode"></a>
The execution role session name mode. If this value is set to `USER_IDENTITY`, the session name of the execution role corresponds to the user's identity. For IAM domains, the session name is the IAM session name used to generate the presigned URL. For IAM Identity Center domains, the session name is the username of the associated IAM Identity Center user. If this value is set to `STATIC` or is not set, the session name defaults to `SageMaker`.
Type: String
Valid Values: `STATIC | USER_IDENTITY`
Required: No

 ** HiddenAppTypes **   <a name="sagemaker-Type-StudioWebPortalSettings-HiddenAppTypes"></a>
The [Applications supported in Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-apps.html) that are hidden from the Studio left navigation pane.
Type: Array of strings
Valid Values: `JupyterServer | KernelGateway | DetailedProfiler | TensorBoard | CodeEditor | JupyterLab | RStudioServerPro | RSessionGateway | Canvas`
Required: No

 ** HiddenInstanceTypes **   <a name="sagemaker-Type-StudioWebPortalSettings-HiddenInstanceTypes"></a>
 The instance types you are hiding from the Studio user interface.
Type: Array of strings
Valid Values: `system | ml.t3.micro | ml.t3.small | ml.t3.medium | ml.t3.large | ml.t3.xlarge | ml.t3.2xlarge | ml.m5.large | ml.m5.xlarge | ml.m5.2xlarge | ml.m5.4xlarge | ml.m5.8xlarge | ml.m5.12xlarge | ml.m5.16xlarge | ml.m5.24xlarge | ml.m5d.large | ml.m5d.xlarge | ml.m5d.2xlarge | ml.m5d.4xlarge | ml.m5d.8xlarge | ml.m5d.12xlarge | ml.m5d.16xlarge | ml.m5d.24xlarge | ml.c5.large | ml.c5.xlarge | ml.c5.2xlarge | ml.c5.4xlarge | ml.c5.9xlarge | ml.c5.12xlarge | ml.c5.18xlarge | ml.c5.24xlarge | ml.p3.2xlarge | ml.p3.8xlarge | ml.p3.16xlarge | ml.p3dn.24xlarge | ml.g4dn.xlarge | ml.g4dn.2xlarge | ml.g4dn.4xlarge | ml.g4dn.8xlarge | ml.g4dn.12xlarge | ml.g4dn.16xlarge | ml.r5.large | ml.r5.xlarge | ml.r5.2xlarge | ml.r5.4xlarge | ml.r5.8xlarge | ml.r5.12xlarge | ml.r5.16xlarge | ml.r5.24xlarge | ml.g5.xlarge | ml.g5.2xlarge | ml.g5.4xlarge | ml.g5.8xlarge | ml.g5.16xlarge | ml.g5.12xlarge | ml.g5.24xlarge | ml.g5.48xlarge | ml.g6.xlarge | ml.g6.2xlarge | ml.g6.4xlarge | ml.g6.8xlarge | ml.g6.12xlarge | ml.g6.16xlarge | ml.g6.24xlarge | ml.g6.48xlarge | ml.g6e.xlarge | ml.g6e.2xlarge | ml.g6e.4xlarge | ml.g6e.8xlarge | ml.g6e.12xlarge | ml.g6e.16xlarge | ml.g6e.24xlarge | ml.g6e.48xlarge | ml.geospatial.interactive | ml.p4d.24xlarge | ml.p4de.24xlarge | ml.trn1.2xlarge | ml.trn1.32xlarge | ml.trn1n.32xlarge | ml.p5.48xlarge | ml.p5en.48xlarge | ml.p6-b200.48xlarge | ml.m6i.large | ml.m6i.xlarge | ml.m6i.2xlarge | ml.m6i.4xlarge | ml.m6i.8xlarge | ml.m6i.12xlarge | ml.m6i.16xlarge | ml.m6i.24xlarge | ml.m6i.32xlarge | ml.m7i.large | ml.m7i.xlarge | ml.m7i.2xlarge | ml.m7i.4xlarge | ml.m7i.8xlarge | ml.m7i.12xlarge | ml.m7i.16xlarge | ml.m7i.24xlarge | ml.m7i.48xlarge | ml.c6i.large | ml.c6i.xlarge | ml.c6i.2xlarge | ml.c6i.4xlarge | ml.c6i.8xlarge | ml.c6i.12xlarge | ml.c6i.16xlarge | ml.c6i.24xlarge | ml.c6i.32xlarge | ml.c7i.large | ml.c7i.xlarge | ml.c7i.2xlarge | ml.c7i.4xlarge | ml.c7i.8xlarge | ml.c7i.12xlarge | ml.c7i.16xlarge | ml.c7i.24xlarge | ml.c7i.48xlarge | ml.r6i.large | ml.r6i.xlarge | ml.r6i.2xlarge | ml.r6i.4xlarge | ml.r6i.8xlarge | ml.r6i.12xlarge | ml.r6i.16xlarge | ml.r6i.24xlarge | ml.r6i.32xlarge | ml.r7i.large | ml.r7i.xlarge | ml.r7i.2xlarge | ml.r7i.4xlarge | ml.r7i.8xlarge | ml.r7i.12xlarge | ml.r7i.16xlarge | ml.r7i.24xlarge | ml.r7i.48xlarge | ml.m6id.large | ml.m6id.xlarge | ml.m6id.2xlarge | ml.m6id.4xlarge | ml.m6id.8xlarge | ml.m6id.12xlarge | ml.m6id.16xlarge | ml.m6id.24xlarge | ml.m6id.32xlarge | ml.c6id.large | ml.c6id.xlarge | ml.c6id.2xlarge | ml.c6id.4xlarge | ml.c6id.8xlarge | ml.c6id.12xlarge | ml.c6id.16xlarge | ml.c6id.24xlarge | ml.c6id.32xlarge | ml.r6id.large | ml.r6id.xlarge | ml.r6id.2xlarge | ml.r6id.4xlarge | ml.r6id.8xlarge | ml.r6id.12xlarge | ml.r6id.16xlarge | ml.r6id.24xlarge | ml.r6id.32xlarge | ml.p5.4xlarge | ml.g7.2xlarge | ml.g7.4xlarge | ml.g7.8xlarge | ml.g7.12xlarge | ml.g7.24xlarge | ml.g7.48xlarge | ml.g7e.2xlarge | ml.g7e.4xlarge | ml.g7e.8xlarge | ml.g7e.12xlarge | ml.g7e.24xlarge | ml.g7e.48xlarge`
Required: No

 ** HiddenMlTools **   <a name="sagemaker-Type-StudioWebPortalSettings-HiddenMlTools"></a>
The machine learning tools that are hidden from the Studio left navigation pane.
Type: Array of strings
Valid Values: `DataWrangler | FeatureStore | EmrClusters | AutoMl | Experiments | Training | ModelEvaluation | Pipelines | Models | JumpStart | InferenceRecommender | Endpoints | Projects | InferenceOptimization | PerformanceEvaluation | LakeraGuard | Comet | DeepchecksLLMEvaluation | Fiddler | HyperPodClusters | RunningInstances | Datasets | Evaluators`
Required: No

 ** HiddenSageMakerImageVersionAliases **   <a name="sagemaker-Type-StudioWebPortalSettings-HiddenSageMakerImageVersionAliases"></a>
 The version aliases you are hiding from the Studio user interface.
Type: Array of [HiddenSageMakerImage](API_HiddenSageMakerImage.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

## See Also
<a name="API_StudioWebPortalSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/StudioWebPortalSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/StudioWebPortalSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/StudioWebPortalSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
