---
source_url: https://docs.aws.amazon.com/sesmailmanager/latest/APIReference/API_TrafficPolicy.html
---

# TrafficPolicy
<a name="API_TrafficPolicy"></a>

The structure of a traffic policy resource which is a container for policy statements.

## Contents
<a name="API_TrafficPolicy_Contents"></a>

 ** DefaultAction **   <a name="sesmailmanager-Type-TrafficPolicy-DefaultAction"></a>
Default action instructs the traﬃc policy to either Allow or Deny (block) messages that fall outside of (or not addressed by) the conditions of your policy statements
Type: String
Valid Values: `ALLOW | DENY`
Required: Yes

 ** TrafficPolicyId **   <a name="sesmailmanager-Type-TrafficPolicy-TrafficPolicyId"></a>
The identifier of the traffic policy resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** TrafficPolicyName **   <a name="sesmailmanager-Type-TrafficPolicy-TrafficPolicyName"></a>
A user-friendly name of the traffic policy resource.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `[A-Za-z0-9_\-]+`
Required: Yes

## See Also
<a name="API_TrafficPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mailmanager-2023-10-17/TrafficPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mailmanager-2023-10-17/TrafficPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mailmanager-2023-10-17/TrafficPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SES Mail Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sesmailmanager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
