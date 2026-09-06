---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RuleMetadata.html
---

# RuleMetadata
<a name="API_RuleMetadata"></a>

Metadata about a rule. Rule metadata includes an ID, a name, a list of tags, and a short and long description. CodeGuru Reviewer uses rules to analyze code. A rule's recommendation is included in analysis results if code is detected that violates the rule.

## Contents
<a name="API_RuleMetadata_Contents"></a>

 ** LongDescription **   <a name="reviewer-Type-RuleMetadata-LongDescription"></a>
A long description of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^\S(.*\S)?$`
Required: No

 ** RuleId **   <a name="reviewer-Type-RuleMetadata-RuleId"></a>
The ID of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^\S+\/[a-zA-Z0-9-]+@v\d+\.\d+$`
Required: No

 ** RuleName **   <a name="reviewer-Type-RuleMetadata-RuleName"></a>
The name of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^\S(.*\S)?$`
Required: No

 ** RuleTags **   <a name="reviewer-Type-RuleMetadata-RuleTags"></a>
Tags that are associated with the rule.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^\S(.*\S)?$`
Required: No

 ** ShortDescription **   <a name="reviewer-Type-RuleMetadata-ShortDescription"></a>
A short description of the rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `^\S(.*\S)?$`
Required: No

## See Also
<a name="API_RuleMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/RuleMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/RuleMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/RuleMetadata)
