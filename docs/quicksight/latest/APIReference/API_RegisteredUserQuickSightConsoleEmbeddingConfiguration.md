---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_RegisteredUserQuickSightConsoleEmbeddingConfiguration.html
---

# RegisteredUserQuickSightConsoleEmbeddingConfiguration
<a name="API_RegisteredUserQuickSightConsoleEmbeddingConfiguration"></a>

Information about the Amazon Quick Sight console that you want to embed.

## Contents
<a name="API_RegisteredUserQuickSightConsoleEmbeddingConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FeatureConfigurations **   <a name="QS-Type-RegisteredUserQuickSightConsoleEmbeddingConfiguration-FeatureConfigurations"></a>
The embedding configuration of an embedded Amazon Quick Sight console.
Type: [RegisteredUserConsoleFeatureConfigurations](API_RegisteredUserConsoleFeatureConfigurations.md) object
Required: No

 ** InitialPath **   <a name="QS-Type-RegisteredUserQuickSightConsoleEmbeddingConfiguration-InitialPath"></a>
The initial URL path for the Amazon Quick Sight console. `InitialPath` is required.
The entry point URL is constrained to the following paths:
+  `/start`
+  `/start/analyses`
+  `/start/dashboards`
+  `/start/favorites`
+  `/dashboards/DashboardId`. *DashboardId* is the actual ID key from the Amazon Quick Sight console URL of the dashboard.
+  `/analyses/AnalysisId`. *AnalysisId* is the actual ID key from the Amazon Quick Sight console URL of the analysis.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

## See Also
<a name="API_RegisteredUserQuickSightConsoleEmbeddingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/RegisteredUserQuickSightConsoleEmbeddingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/RegisteredUserQuickSightConsoleEmbeddingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/RegisteredUserQuickSightConsoleEmbeddingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
