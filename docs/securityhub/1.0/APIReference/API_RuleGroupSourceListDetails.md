---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_RuleGroupSourceListDetails.html
---

# RuleGroupSourceListDetails
<a name="API_RuleGroupSourceListDetails"></a>

Stateful inspection criteria for a domain list rule group.

## Contents
<a name="API_RuleGroupSourceListDetails_Contents"></a>

 ** GeneratedRulesType **   <a name="securityhub-Type-RuleGroupSourceListDetails-GeneratedRulesType"></a>
Indicates whether to allow or deny access to the domains listed in `Targets`.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Targets **   <a name="securityhub-Type-RuleGroupSourceListDetails-Targets"></a>
The domains that you want to inspect for in your traffic flows. You can provide full domain names, or use the '.' prefix as a wildcard. For example, `.example.com` matches all domains that end with `example.com`.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** TargetTypes **   <a name="securityhub-Type-RuleGroupSourceListDetails-TargetTypes"></a>
The protocols that you want to inspect. Specify `LS_SNI` for HTTPS. Specify `HTTP_HOST` for HTTP. You can specify either or both.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_RuleGroupSourceListDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/RuleGroupSourceListDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/RuleGroupSourceListDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/RuleGroupSourceListDetails)
