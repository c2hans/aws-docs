---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_NamespaceRuleBasedProperties.html
---

# NamespaceRuleBasedProperties
<a name="API_NamespaceRuleBasedProperties"></a>

 The rule-based properties of an ID namespace. These properties define how the ID namespace can be used in an ID mapping workflow.

## Contents
<a name="API_NamespaceRuleBasedProperties_Contents"></a>

 ** attributeMatchingModel **   <a name="API-Type-NamespaceRuleBasedProperties-attributeMatchingModel"></a>
The comparison type. You can either choose `ONE_TO_ONE` or `MANY_TO_MANY` as the `attributeMatchingModel`.
If you choose `ONE_TO_ONE`, the system can only match attributes if the sub-types are an exact match. For example, for the `Email` attribute type, the system will only consider it a match if the value of the `Email` field of Profile A matches the value of the `Email` field of Profile B.
If you choose `MANY_TO_MANY`, the system can match attributes across the sub-types of an attribute type. For example, if the value of the `Email` field of Profile A matches the value of `BusinessEmail` field of Profile B, the two profiles are matched on the `Email` attribute type.
Type: String
Valid Values: `ONE_TO_ONE | MANY_TO_MANY`
Required: No

 ** recordMatchingModels **   <a name="API-Type-NamespaceRuleBasedProperties-recordMatchingModels"></a>
 The type of matching record that is allowed to be used in an ID mapping workflow.
If the value is set to `ONE_SOURCE_TO_ONE_TARGET`, only one record in the source is matched to one record in the target.
If the value is set to `MANY_SOURCE_TO_ONE_TARGET`, all matching records in the source are matched to one record in the target.
Type: Array of strings
Valid Values: `ONE_SOURCE_TO_ONE_TARGET | MANY_SOURCE_TO_ONE_TARGET`
Required: No

 ** ruleDefinitionTypes **   <a name="API-Type-NamespaceRuleBasedProperties-ruleDefinitionTypes"></a>
 The sets of rules you can use in an ID mapping workflow. The limitations specified for the source and target must be compatible.
Type: Array of strings
Valid Values: `SOURCE | TARGET`
Required: No

 ** rules **   <a name="API-Type-NamespaceRuleBasedProperties-rules"></a>
 The rules for the ID namespace.
Type: Array of [Rule](API_Rule.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: No

## See Also
<a name="API_NamespaceRuleBasedProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/NamespaceRuleBasedProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/NamespaceRuleBasedProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/NamespaceRuleBasedProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
