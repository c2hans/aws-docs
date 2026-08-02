---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/awswaf.html
---

# Data retrieval APIs for AWS WAF
<a name="awswaf"></a>

AWS WAF provides the following APIs for data retrieval.

****

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="waf-GetByteMatchSet"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetByteMatchSet.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetByteMatchSet.html) | Retrieve a ByteMatchSet | Read |
| <a name="waf-GetChangeToken"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetChangeToken.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetChangeToken.html) | Retrieve a change token to use in create, update, and delete requests | Read |
| <a name="waf-GetChangeTokenStatus"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetChangeTokenStatus.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetChangeTokenStatus.html) | Retrieve the status of a change token | Read |
| <a name="waf-GetGeoMatchSet"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetGeoMatchSet.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetGeoMatchSet.html) | Retrieve a GeoMatchSet | Read |
| <a name="waf-GetIPSet"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetIPSet.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetIPSet.html) | Retrieve an IPSet | Read |
| <a name="waf-GetLoggingConfiguration"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetLoggingConfiguration.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetLoggingConfiguration.html) | Retrieve a LoggingConfiguration for a web ACL | Read |
| <a name="waf-GetPermissionPolicy"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetPermissionPolicy.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetPermissionPolicy.html) | Retrieve an IAM policy for a rule group | Read |
| <a name="waf-GetRateBasedRule"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetRateBasedRule.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetRateBasedRule.html) | Retrieve a RateBasedRule | Read |
| <a name="waf-GetRateBasedRuleManagedKeys"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetRateBasedRuleManagedKeys.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetRateBasedRuleManagedKeys.html) | Retrieve the array of IP addresses that are currently being blocked by a RateBasedRule | Read |
| <a name="waf-GetRegexMatchSet"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetRegexMatchSet.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetRegexMatchSet.html) | Retrieve a RegexMatchSet | Read |
| <a name="waf-GetRegexPatternSet"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetRegexPatternSet.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetRegexPatternSet.html) | Retrieve a RegexPatternSet | Read |
| <a name="waf-GetRule"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetRule.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetRule.html) | Retrieve a Rule | Read |
| <a name="waf-GetRuleGroup"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetRuleGroup.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetRuleGroup.html) | Retrieve a RuleGroup | Read |
| <a name="waf-GetSampledRequests"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetSampledRequests.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetSampledRequests.html) | Retrieve detailed information about a sample set of web requests | Read |
| <a name="waf-GetSizeConstraintSet"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetSizeConstraintSet.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetSizeConstraintSet.html) | Retrieve a SizeConstraintSet | Read |
| <a name="waf-GetSqlInjectionMatchSet"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetSqlInjectionMatchSet.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetSqlInjectionMatchSet.html) | Retrieve an SqlInjectionMatchSet | Read |
| <a name="waf-GetWebACL"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetWebACL.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetWebACL.html) | Retrieve a WebACL | Read |
| <a name="waf-GetXssMatchSet"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetXssMatchSet.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_GetXssMatchSet.html) | Retrieve an XssMatchSet | Read |
| <a name="waf-ListActivatedRulesInRuleGroup"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListActivatedRulesInRuleGroup.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListActivatedRulesInRuleGroup.html) | Retrieve an array of ActivatedRule objects | List |
| <a name="waf-ListByteMatchSets"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListByteMatchSets.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListByteMatchSets.html) | Retrieve an array of ByteMatchSetSummary objects | List |
| <a name="waf-ListGeoMatchSets"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListGeoMatchSets.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListGeoMatchSets.html) | Retrieve an array of GeoMatchSetSummary objects | List |
| <a name="waf-ListIPSets"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListIPSets.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListIPSets.html) | Retrieve an array of IPSetSummary objects | List |
| <a name="waf-ListLoggingConfigurations"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListLoggingConfigurations.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListLoggingConfigurations.html) | Retrieve an array of LoggingConfiguration objects | List |
| <a name="waf-ListRateBasedRules"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListRateBasedRules.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListRateBasedRules.html) | Retrieve an array of RuleSummary objects | List |
| <a name="waf-ListRegexMatchSets"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListRegexMatchSets.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListRegexMatchSets.html) | Retrieve an array of RegexMatchSetSummary objects | List |
| <a name="waf-ListRegexPatternSets"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListRegexPatternSets.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListRegexPatternSets.html) | Retrieve an array of RegexPatternSetSummary objects | List |
| <a name="waf-ListRuleGroups"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListRuleGroups.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListRuleGroups.html) | Retrieve an array of RuleGroup objects | List |
| <a name="waf-ListRules"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListRules.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListRules.html) | Retrieve an array of RuleSummary objects | List |
| <a name="waf-ListSizeConstraintSets"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListSizeConstraintSets.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListSizeConstraintSets.html) | Retrieve an array of SizeConstraintSetSummary objects | List |
| <a name="waf-ListSqlInjectionMatchSets"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListSqlInjectionMatchSets.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListSqlInjectionMatchSets.html) | Retrieve an array of SqlInjectionMatchSet objects | List |
| <a name="waf-ListSubscribedRuleGroups"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListSubscribedRuleGroups.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListSubscribedRuleGroups.html) | Retrieve an array of RuleGroup objects that you are subscribed to | List |
| <a name="waf-ListTagsForResource"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListTagsForResource.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListTagsForResource.html) | Retrieve the tags for a resource | Read |
| <a name="waf-ListWebACLs"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListWebACLs.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListWebACLs.html) | Retrieve an array of WebACLSummary objects | List |
| <a name="waf-ListXssMatchSets"></a>[https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListXssMatchSets.html](https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_ListXssMatchSets.html) | Retrieve an array of XssMatchSet objects | List |
