---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_ComponentRecommendation.html
---

# ComponentRecommendation
<a name="API_ComponentRecommendation"></a>

Defines recommendations for an AWS Resilience Hub AppComponent, returned as an object. This object contains component names, configuration recommendations, and recommendation statuses.

## Contents
<a name="API_ComponentRecommendation_Contents"></a>

 ** appComponentName **   <a name="resiliencehub-Type-ComponentRecommendation-appComponentName"></a>
Name of the AppComponent.
Type: String
Pattern: `\S{1,255}`
Required: Yes

 ** configRecommendations **   <a name="resiliencehub-Type-ComponentRecommendation-configRecommendations"></a>
List of recommendations.
Type: Array of [ConfigRecommendation](API_ConfigRecommendation.md) objects
Required: Yes

 ** recommendationStatus **   <a name="resiliencehub-Type-ComponentRecommendation-recommendationStatus"></a>
Status of the recommendation.
Type: String
Valid Values: `BreachedUnattainable | BreachedCanMeet | MetCanImprove | MissingPolicy`
Required: Yes

## See Also
<a name="API_ComponentRecommendation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/ComponentRecommendation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/ComponentRecommendation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/ComponentRecommendation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
