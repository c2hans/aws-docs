---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_VersionToPublish.html
---

# VersionToPublish
<a name="API_VersionToPublish"></a>

A version of the named managed rule group, that the rule group's vendor publishes for use by customers.

**Note**
This is intended for use only by vendors of managed rule sets. Vendors are AWS and AWS Marketplace sellers.
Vendors, you can use the managed rule set APIs to provide controlled rollout of your versioned managed rule group offerings for your customers. The APIs are `ListManagedRuleSets`, `GetManagedRuleSet`, `PutManagedRuleSetVersions`, and `UpdateManagedRuleSetVersionExpiryDate`.

## Contents
<a name="API_VersionToPublish_Contents"></a>

 ** AssociatedRuleGroupArn **   <a name="WAF-Type-VersionToPublish-AssociatedRuleGroupArn"></a>
The Amazon Resource Name (ARN) of the vendor's rule group that's used in the published managed rule group version.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

 ** ForecastedLifetime **   <a name="WAF-Type-VersionToPublish-ForecastedLifetime"></a>
The amount of time the vendor expects this version of the managed rule group to last, in days.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_VersionToPublish_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/VersionToPublish)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/VersionToPublish)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/VersionToPublish)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
