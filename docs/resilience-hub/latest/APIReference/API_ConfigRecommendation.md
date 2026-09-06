---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ConfigRecommendation.html
---

# ConfigRecommendation
<a name="API_ConfigRecommendation"></a>

Defines a recommendation configuration.

## Contents
<a name="API_ConfigRecommendation_Contents"></a>

 ** name **   <a name="resiliencehub-Type-ConfigRecommendation-name"></a>
The name of the recommendation configuration.
Type: String
Pattern: `[A-Za-z0-9][A-Za-z0-9_\-]{1,59}`
Required: Yes

 ** optimizationType **   <a name="resiliencehub-Type-ConfigRecommendation-optimizationType"></a>
The type of optimization.
Type: String
Valid Values: `LeastCost | LeastChange | BestAZRecovery | LeastErrors | BestAttainable | BestRegionRecovery`
Required: Yes

 ** referenceId **   <a name="resiliencehub-Type-ConfigRecommendation-referenceId"></a>
Reference identifier for the recommendation configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** appComponentName **   <a name="resiliencehub-Type-ConfigRecommendation-appComponentName"></a>
Name of the AppComponent.
Type: String
Pattern: `\S{1,255}`
Required: No

 ** compliance **   <a name="resiliencehub-Type-ConfigRecommendation-compliance"></a>
The current compliance against the resiliency policy before applying the configuration change.
Type: String to [DisruptionCompliance](API_DisruptionCompliance.md) object map
Valid Keys: `Software | Hardware | AZ | Region`
Required: No

 ** cost **   <a name="resiliencehub-Type-ConfigRecommendation-cost"></a>
The cost for the application.
Type: [Cost](API_Cost.md) object
Required: No

 ** description **   <a name="resiliencehub-Type-ConfigRecommendation-description"></a>
The optional description for an app.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** haArchitecture **   <a name="resiliencehub-Type-ConfigRecommendation-haArchitecture"></a>
The architecture type.
Type: String
Valid Values: `MultiSite | WarmStandby | PilotLight | BackupAndRestore | NoRecoveryPlan`
Required: No

 ** recommendationCompliance **   <a name="resiliencehub-Type-ConfigRecommendation-recommendationCompliance"></a>
The expected compliance against the resiliency policy after applying the configuration change.
Type: String to [RecommendationDisruptionCompliance](API_RecommendationDisruptionCompliance.md) object map
Valid Keys: `Software | Hardware | AZ | Region`
Required: No

 ** suggestedChanges **   <a name="resiliencehub-Type-ConfigRecommendation-suggestedChanges"></a>
List of the suggested configuration changes.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

## See Also
<a name="API_ConfigRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/ConfigRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/ConfigRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/ConfigRecommendation)
