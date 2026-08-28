---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_RuleConditionProperties.html
---

# RuleConditionProperties
<a name="API_RuleConditionProperties"></a>

The properties of a rule condition that provides the ability to use more complex syntax.

## Contents
<a name="API_RuleConditionProperties_Contents"></a>

 ** rules **   <a name="API-Type-RuleConditionProperties-rules"></a>
 A list of rule objects, each of which have fields `ruleName` and `condition`.
Type: Array of [RuleCondition](API_RuleCondition.md) objects
Array Members: Minimum number of 1 item. Maximum number of 25 items.
Required: Yes

 ** matchingConfig **   <a name="API-Type-RuleConditionProperties-matchingConfig"></a>
An object that contains configuration settings for the matching process.
Type: [MatchingConfig](API_MatchingConfig.md) object
Required: No

## See Also
<a name="API_RuleConditionProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/RuleConditionProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/RuleConditionProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/RuleConditionProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Entity Resolution. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query entityresolution` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
