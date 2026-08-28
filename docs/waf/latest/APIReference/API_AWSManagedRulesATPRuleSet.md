---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_AWSManagedRulesATPRuleSet.html
---

# AWSManagedRulesATPRuleSet
<a name="API_AWSManagedRulesATPRuleSet"></a>

Details for your use of the account takeover prevention managed rule group, `AWSManagedRulesATPRuleSet`. This configuration is used in `ManagedRuleGroupConfig`.

For additional information about this and the other intelligent threat mitigation rule groups, see [Intelligent threat mitigation in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-protections) and [AWS Managed Rules rule groups list](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-list) in the * AWS WAF Developer Guide*.

## Contents
<a name="API_AWSManagedRulesATPRuleSet_Contents"></a>

 ** LoginPath **   <a name="WAF-Type-AWSManagedRulesATPRuleSet-LoginPath"></a>
The path of the login endpoint for your application. For example, for the URL `https://example.com/web/login`, you would provide the path `/web/login`. Login paths that start with the path that you provide are considered a match. For example `/web/login` matches the login paths `/web/login`, `/web/login/`, `/web/loginPage`, and `/web/login/thisPage`, but doesn't match the login path `/home/web/login` or `/website/login`.
The rule group inspects only HTTP `POST` requests to your specified login endpoint.
Type: String
Required: Yes

 ** EnableRegexInPath **   <a name="WAF-Type-AWSManagedRulesATPRuleSet-EnableRegexInPath"></a>
Allow the use of regular expressions in the login page path.
Type: Boolean
Required: No

 ** RequestInspection **   <a name="WAF-Type-AWSManagedRulesATPRuleSet-RequestInspection"></a>
The criteria for inspecting login requests, used by the ATP rule group to validate credentials usage.
Type: [RequestInspection](API_RequestInspection.md) object
Required: No

 ** ResponseInspection **   <a name="WAF-Type-AWSManagedRulesATPRuleSet-ResponseInspection"></a>
The criteria for inspecting responses to login requests, used by the ATP rule group to track login failure rates.
Response inspection is available only in web ACLs that protect Amazon CloudFront distributions.
The ATP rule group evaluates the responses that your protected resources send back to client login attempts, keeping count of successful and failed attempts for each IP address and client session. Using this information, the rule group labels and mitigates requests from client sessions and IP addresses that have had too many failed login attempts in a short amount of time.
Type: [ResponseInspection](API_ResponseInspection.md) object
Required: No

## See Also
<a name="API_AWSManagedRulesATPRuleSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/AWSManagedRulesATPRuleSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/AWSManagedRulesATPRuleSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/AWSManagedRulesATPRuleSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
