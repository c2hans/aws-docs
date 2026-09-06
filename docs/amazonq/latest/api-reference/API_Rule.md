---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Rule.html
---

# Rule
<a name="API_Rule"></a>

Guardrail rules for an Amazon Q Business application. Amazon Q Business supports only one rule at a time.

## Contents
<a name="API_Rule_Contents"></a>

 ** ruleType **   <a name="qbusiness-Type-Rule-ruleType"></a>
The type of rule.
Type: String
Valid Values: `CONTENT_BLOCKER_RULE | CONTENT_RETRIEVAL_RULE`
Required: Yes

 ** excludedUsersAndGroups **   <a name="qbusiness-Type-Rule-excludedUsersAndGroups"></a>
Users and groups to be excluded from a rule.
Type: [UsersAndGroups](API_UsersAndGroups.md) object
Required: No

 ** includedUsersAndGroups **   <a name="qbusiness-Type-Rule-includedUsersAndGroups"></a>
Users and groups to be included in a rule.
Type: [UsersAndGroups](API_UsersAndGroups.md) object
Required: No

 ** ruleConfiguration **   <a name="qbusiness-Type-Rule-ruleConfiguration"></a>
The configuration information for a rule.
Type: [RuleConfiguration](API_RuleConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_Rule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/Rule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/Rule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/Rule)
