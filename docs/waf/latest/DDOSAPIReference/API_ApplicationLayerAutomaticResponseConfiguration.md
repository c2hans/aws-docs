---
source_url: https://docs.aws.amazon.com/waf/latest/DDOSAPIReference/API_ApplicationLayerAutomaticResponseConfiguration.html
---

# ApplicationLayerAutomaticResponseConfiguration
<a name="API_ApplicationLayerAutomaticResponseConfiguration"></a>

The automatic application layer DDoS mitigation settings for a [Protection](API_Protection.md). This configuration determines whether Shield Advanced automatically manages rules in the web ACL in order to respond to application layer events that Shield Advanced determines to be DDoS attacks.

## Contents
<a name="API_ApplicationLayerAutomaticResponseConfiguration_Contents"></a>

 ** Action **   <a name="AWSShield-Type-ApplicationLayerAutomaticResponseConfiguration-Action"></a>
Specifies the action setting that Shield Advanced should use in the AWS WAF rules that it creates on behalf of the protected resource in response to DDoS attacks. You specify this as part of the configuration for the automatic application layer DDoS mitigation feature, when you enable or update automatic mitigation. Shield Advanced creates the AWS WAF rules in a Shield Advanced-managed rule group, inside the web ACL that you have associated with the resource.
Type: [ResponseAction](API_ResponseAction.md) object
Required: Yes

 ** Status **   <a name="AWSShield-Type-ApplicationLayerAutomaticResponseConfiguration-Status"></a>
Indicates whether automatic application layer DDoS mitigation is enabled for the protection.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: Yes

## See Also
<a name="API_ApplicationLayerAutomaticResponseConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/shield-2016-06-02/ApplicationLayerAutomaticResponseConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/shield-2016-06-02/ApplicationLayerAutomaticResponseConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/shield-2016-06-02/ApplicationLayerAutomaticResponseConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query waf` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
