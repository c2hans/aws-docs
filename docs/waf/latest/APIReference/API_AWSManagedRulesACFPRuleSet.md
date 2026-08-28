---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_AWSManagedRulesACFPRuleSet.html
---

# AWSManagedRulesACFPRuleSet
<a name="API_AWSManagedRulesACFPRuleSet"></a>

Details for your use of the account creation fraud prevention managed rule group, `AWSManagedRulesACFPRuleSet`. This configuration is used in `ManagedRuleGroupConfig`.

For additional information about this and the other intelligent threat mitigation rule groups, see [Intelligent threat mitigation in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-managed-protections) and [AWS Managed Rules rule groups list](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-list) in the * AWS WAF Developer Guide*.

## Contents
<a name="API_AWSManagedRulesACFPRuleSet_Contents"></a>

 ** CreationPath **   <a name="WAF-Type-AWSManagedRulesACFPRuleSet-CreationPath"></a>
The path of the account creation endpoint for your application. This is the page on your website that accepts the completed registration form for a new user. This page must accept `POST` requests.
For example, for the URL `https://example.com/web/newaccount`, you would provide the path `/web/newaccount`. Account creation page paths that start with the path that you provide are considered a match. For example `/web/newaccount` matches the account creation paths `/web/newaccount`, `/web/newaccount/`, `/web/newaccountPage`, and `/web/newaccount/thisPage`, but doesn't match the path `/home/web/newaccount` or `/website/newaccount`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: Yes

 ** RegistrationPagePath **   <a name="WAF-Type-AWSManagedRulesACFPRuleSet-RegistrationPagePath"></a>
The path of the account registration endpoint for your application. This is the page on your website that presents the registration form to new users.
This page must accept `GET` text/html requests.
For example, for the URL `https://example.com/web/registration`, you would provide the path `/web/registration`. Registration page paths that start with the path that you provide are considered a match. For example `/web/registration` matches the registration paths `/web/registration`, `/web/registration/`, `/web/registrationPage`, and `/web/registration/thisPage`, but doesn't match the path `/home/web/registration` or `/website/registration`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `.*\S.*`
Required: Yes

 ** RequestInspection **   <a name="WAF-Type-AWSManagedRulesACFPRuleSet-RequestInspection"></a>
The criteria for inspecting account creation requests, used by the ACFP rule group to validate and track account creation attempts.
Type: [RequestInspectionACFP](API_RequestInspectionACFP.md) object
Required: Yes

 ** EnableRegexInPath **   <a name="WAF-Type-AWSManagedRulesACFPRuleSet-EnableRegexInPath"></a>
Allow the use of regular expressions in the registration page path and the account creation path.
Type: Boolean
Required: No

 ** ResponseInspection **   <a name="WAF-Type-AWSManagedRulesACFPRuleSet-ResponseInspection"></a>
The criteria for inspecting responses to account creation requests, used by the ACFP rule group to track account creation success rates.
Response inspection is available only in web ACLs that protect Amazon CloudFront distributions.
The ACFP rule group evaluates the responses that your protected resources send back to client account creation attempts, keeping count of successful and failed attempts from each IP address and client session. Using this information, the rule group labels and mitigates requests from client sessions and IP addresses that have had too many successful account creation attempts in a short amount of time.
Type: [ResponseInspection](API_ResponseInspection.md) object
Required: No

## See Also
<a name="API_AWSManagedRulesACFPRuleSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/AWSManagedRulesACFPRuleSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/AWSManagedRulesACFPRuleSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/AWSManagedRulesACFPRuleSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
