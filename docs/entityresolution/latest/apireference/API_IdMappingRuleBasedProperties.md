---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_IdMappingRuleBasedProperties.html
---

# IdMappingRuleBasedProperties
<a name="API_IdMappingRuleBasedProperties"></a>

 An object that defines the list of matching rules to run in an ID mapping workflow.

## Contents
<a name="API_IdMappingRuleBasedProperties_Contents"></a>

 ** attributeMatchingModel **   <a name="API-Type-IdMappingRuleBasedProperties-attributeMatchingModel"></a>
The comparison type. You can either choose `ONE_TO_ONE` or `MANY_TO_MANY` as the `attributeMatchingModel`.
If you choose `ONE_TO_ONE`, the system can only match attributes if the sub-types are an exact match. For example, for the `Email` attribute type, the system will only consider it a match if the value of the `Email` field of Profile A matches the value of the `Email` field of Profile B.
If you choose `MANY_TO_MANY`, the system can match attributes across the sub-types of an attribute type. For example, if the value of the `Email` field of Profile A matches the value of the `BusinessEmail` field of Profile B, the two profiles are matched on the `Email` attribute type.
Type: String
Valid Values: `ONE_TO_ONE | MANY_TO_MANY`
Required: Yes

 ** recordMatchingModel **   <a name="API-Type-IdMappingRuleBasedProperties-recordMatchingModel"></a>
 The type of matching record that is allowed to be used in an ID mapping workflow.
If the value is set to `ONE_SOURCE_TO_ONE_TARGET`, only one record in the source can be matched to the same record in the target.
If the value is set to `MANY_SOURCE_TO_ONE_TARGET`, multiple records in the source can be matched to one record in the target.
Type: String
Valid Values: `ONE_SOURCE_TO_ONE_TARGET | MANY_SOURCE_TO_ONE_TARGET`
Required: Yes

 ** ruleDefinitionType **   <a name="API-Type-IdMappingRuleBasedProperties-ruleDefinitionType"></a>
 The set of rules you can use in an ID mapping workflow. The limitations specified for the source or target to define the match rules must be compatible.
Type: String
Valid Values: `SOURCE | TARGET`
Required: Yes

 ** rules **   <a name="API-Type-IdMappingRuleBasedProperties-rules"></a>
 The rules that can be used for ID mapping.
Type: Array of [Rule](API_Rule.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: No

## See Also
<a name="API_IdMappingRuleBasedProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/IdMappingRuleBasedProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/IdMappingRuleBasedProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/IdMappingRuleBasedProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
