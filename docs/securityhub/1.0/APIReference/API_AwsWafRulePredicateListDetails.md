---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsWafRulePredicateListDetails.html
---

# AwsWafRulePredicateListDetails
<a name="API_AwsWafRulePredicateListDetails"></a>

Provides details about the `ByteMatchSet`, `IPSet`, `SqlInjectionMatchSet`, `XssMatchSet`, `RegexMatchSet`, `GeoMatchSet`, and `SizeConstraintSet` objects that you want to add to a rule and, for each object, indicates whether you want to negate the settings.

## Contents
<a name="API_AwsWafRulePredicateListDetails_Contents"></a>

 ** DataId **   <a name="securityhub-Type-AwsWafRulePredicateListDetails-DataId"></a>
A unique identifier for a predicate in a rule, such as `ByteMatchSetId` or `IPSetId`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Negated **   <a name="securityhub-Type-AwsWafRulePredicateListDetails-Negated"></a>
Specifies if you want AWS WAF to allow, block, or count requests based on the settings in the `ByteMatchSet`, `IPSet`, `SqlInjectionMatchSet`, `XssMatchSet`, `RegexMatchSet`, `GeoMatchSet`, or `SizeConstraintSet`.
Type: Boolean
Required: No

 ** Type **   <a name="securityhub-Type-AwsWafRulePredicateListDetails-Type"></a>
The type of predicate in a rule, such as `ByteMatch` or `IPSet`.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsWafRulePredicateListDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsWafRulePredicateListDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsWafRulePredicateListDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsWafRulePredicateListDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
