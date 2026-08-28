---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_ResolutionTechniques.html
---

# ResolutionTechniques
<a name="API_ResolutionTechniques"></a>

An object which defines the `resolutionType` and the `ruleBasedProperties`.

## Contents
<a name="API_ResolutionTechniques_Contents"></a>

 ** resolutionType **   <a name="API-Type-ResolutionTechniques-resolutionType"></a>
The type of matching workflow to create. Specify one of the following types:
+  `RULE_MATCHING`: Match records using configurable rule-based criteria
+  `ML_MATCHING`: Match records using machine learning models
+  `PROVIDER`: Match records using a third-party matching provider
Type: String
Valid Values: `RULE_MATCHING | ML_MATCHING | PROVIDER`
Required: Yes

 ** enableRealTimeMatching **   <a name="API-Type-ResolutionTechniques-enableRealTimeMatching"></a>
Specifies whether real-time matching is enabled for the rule-based matching workflow. When you enable real-time matching, you can use the `GenerateMatchId` operation with the workflow.
Type: Boolean
Required: No

 ** providerProperties **   <a name="API-Type-ResolutionTechniques-providerProperties"></a>
The properties of the provider service.
Type: [ProviderProperties](API_ProviderProperties.md) object
Required: No

 ** ruleBasedProperties **   <a name="API-Type-ResolutionTechniques-ruleBasedProperties"></a>
An object which defines the list of matching rules to run and has a field `rules`, which is a list of rule objects.
Type: [RuleBasedProperties](API_RuleBasedProperties.md) object
Required: No

 ** ruleConditionProperties **   <a name="API-Type-ResolutionTechniques-ruleConditionProperties"></a>
An object containing the `rules` for a matching workflow.
Type: [RuleConditionProperties](API_RuleConditionProperties.md) object
Required: No

## See Also
<a name="API_ResolutionTechniques_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/ResolutionTechniques)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/ResolutionTechniques)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/ResolutionTechniques)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
