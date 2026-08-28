---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_PrivacyConfigurationPolicies.html
---

# PrivacyConfigurationPolicies
<a name="API_PrivacyConfigurationPolicies"></a>

Information about the privacy configuration policies for a configured model algorithm association.

## Contents
<a name="API_PrivacyConfigurationPolicies_Contents"></a>

 ** trainedModelExports **   <a name="API-Type-PrivacyConfigurationPolicies-trainedModelExports"></a>
Specifies who will receive the trained model export.
Type: [TrainedModelExportsConfigurationPolicy](API_TrainedModelExportsConfigurationPolicy.md) object
Required: No

 ** trainedModelInferenceJobs **   <a name="API-Type-PrivacyConfigurationPolicies-trainedModelInferenceJobs"></a>
Specifies who will receive the trained model inference jobs.
Type: [TrainedModelInferenceJobsConfigurationPolicy](API_TrainedModelInferenceJobsConfigurationPolicy.md) object
Required: No

 ** trainedModels **   <a name="API-Type-PrivacyConfigurationPolicies-trainedModels"></a>
Specifies who will receive the trained models.
Type: [TrainedModelsConfigurationPolicy](API_TrainedModelsConfigurationPolicy.md) object
Required: No

## See Also
<a name="API_PrivacyConfigurationPolicies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/PrivacyConfigurationPolicies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/PrivacyConfigurationPolicies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/PrivacyConfigurationPolicies)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
