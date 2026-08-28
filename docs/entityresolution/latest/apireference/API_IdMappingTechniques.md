---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_IdMappingTechniques.html
---

# IdMappingTechniques
<a name="API_IdMappingTechniques"></a>

An object which defines the ID mapping technique and any additional configurations.

## Contents
<a name="API_IdMappingTechniques_Contents"></a>

 ** idMappingType **   <a name="API-Type-IdMappingTechniques-idMappingType"></a>
The type of ID mapping.
Type: String
Valid Values: `PROVIDER | RULE_BASED`
Required: Yes

 ** providerProperties **   <a name="API-Type-IdMappingTechniques-providerProperties"></a>
An object which defines any additional configurations required by the provider service.
Type: [ProviderProperties](API_ProviderProperties.md) object
Required: No

 ** ruleBasedProperties **   <a name="API-Type-IdMappingTechniques-ruleBasedProperties"></a>
 An object which defines any additional configurations required by rule-based matching.
Type: [IdMappingRuleBasedProperties](API_IdMappingRuleBasedProperties.md) object
Required: No

## See Also
<a name="API_IdMappingTechniques_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/IdMappingTechniques)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/IdMappingTechniques)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/IdMappingTechniques)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
