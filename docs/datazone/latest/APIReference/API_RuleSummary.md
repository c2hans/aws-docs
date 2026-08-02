---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_RuleSummary.html
---

# RuleSummary
<a name="API_RuleSummary"></a>

The summary of the rule.

## Contents
<a name="API_RuleSummary_Contents"></a>

 ** action **   <a name="datazone-Type-RuleSummary-action"></a>
The action of the rule.
Type: String
Valid Values: `CREATE_LISTING_CHANGE_SET | CREATE_SUBSCRIPTION_REQUEST`
Required: No

 ** identifier **   <a name="datazone-Type-RuleSummary-identifier"></a>
The ID of the rule.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

 ** lastUpdatedBy **   <a name="datazone-Type-RuleSummary-lastUpdatedBy"></a>
The timestamp at which the rule was last updated.
Type: String
Required: No

 ** name **   <a name="datazone-Type-RuleSummary-name"></a>
The name of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\w -]+`
Required: No

 ** revision **   <a name="datazone-Type-RuleSummary-revision"></a>
The revision of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ruleType **   <a name="datazone-Type-RuleSummary-ruleType"></a>
The type of the rule.
Type: String
Valid Values: `METADATA_FORM_ENFORCEMENT | GLOSSARY_TERM_ENFORCEMENT`
Required: No

 ** scope **   <a name="datazone-Type-RuleSummary-scope"></a>
The scope of the rule.
Type: [RuleScope](API_RuleScope.md) object
Required: No

 ** target **   <a name="datazone-Type-RuleSummary-target"></a>
The target of the rule.
Type: [RuleTarget](API_RuleTarget.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** targetType **   <a name="datazone-Type-RuleSummary-targetType"></a>
The target type of the rule.
Type: String
Valid Values: `DOMAIN_UNIT`
Required: No

 ** updatedAt **   <a name="datazone-Type-RuleSummary-updatedAt"></a>
The timestamp at which the rule was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_RuleSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/RuleSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/RuleSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/RuleSummary)
