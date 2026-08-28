---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_SecurityHubPolicy.html
---

# SecurityHubPolicy
<a name="API_SecurityHubPolicy"></a>

 An object that defines how AWS Security Hub CSPM is configured. The configuration policy includes whether Security Hub CSPM is enabled or disabled, a list of enabled security standards, a list of enabled or disabled security controls, and a list of custom parameter values for specified controls. If you provide a list of security controls that are enabled in the configuration policy, Security Hub CSPM disables all other controls (including newly released controls). If you provide a list of security controls that are disabled in the configuration policy, Security Hub CSPM enables all other controls (including newly released controls).

## Contents
<a name="API_SecurityHubPolicy_Contents"></a>

 ** EnabledStandardIdentifiers **   <a name="securityhub-Type-SecurityHubPolicy-EnabledStandardIdentifiers"></a>
 A list that defines which security standards are enabled in the configuration policy.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** SecurityControlsConfiguration **   <a name="securityhub-Type-SecurityHubPolicy-SecurityControlsConfiguration"></a>
 An object that defines which security controls are enabled in the configuration policy. The enablement status of a control is aligned across all of the enabled standards in an account.
Type: [SecurityControlsConfiguration](API_SecurityControlsConfiguration.md) object
Required: No

 ** ServiceEnabled **   <a name="securityhub-Type-SecurityHubPolicy-ServiceEnabled"></a>
 Indicates whether Security Hub CSPM is enabled in the policy.
Type: Boolean
Required: No

## See Also
<a name="API_SecurityHubPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/SecurityHubPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/SecurityHubPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/SecurityHubPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
