---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_TrainedModelsConfigurationPolicy.html
---

# TrainedModelsConfigurationPolicy
<a name="API_TrainedModelsConfigurationPolicy"></a>

The configuration policy for the trained models.

## Contents
<a name="API_TrainedModelsConfigurationPolicy_Contents"></a>

 ** containerLogs **   <a name="API-Type-TrainedModelsConfigurationPolicy-containerLogs"></a>
The container for the logs of the trained model.
Type: Array of [LogsConfigurationPolicy](API_LogsConfigurationPolicy.md) objects
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: No

 ** containerMetrics **   <a name="API-Type-TrainedModelsConfigurationPolicy-containerMetrics"></a>
The container for the metrics of the trained model.
Type: [MetricsConfigurationPolicy](API_MetricsConfigurationPolicy.md) object
Required: No

 ** maxArtifactSize **   <a name="API-Type-TrainedModelsConfigurationPolicy-maxArtifactSize"></a>
The maximum size limit for trained model artifacts as defined in the configuration policy. This setting helps enforce consistent size limits across trained models in the collaboration.
Type: [TrainedModelArtifactMaxSize](API_TrainedModelArtifactMaxSize.md) object
Required: No

## See Also
<a name="API_TrainedModelsConfigurationPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/TrainedModelsConfigurationPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/TrainedModelsConfigurationPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/TrainedModelsConfigurationPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
