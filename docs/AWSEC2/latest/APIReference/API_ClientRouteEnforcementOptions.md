---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ClientRouteEnforcementOptions.html
---

# ClientRouteEnforcementOptions
<a name="API_ClientRouteEnforcementOptions"></a>

Client Route Enforcement is a feature of Client VPN that helps enforce administrator defined routes on devices connected through the VPN. This feature helps improve your security posture by ensuring that network traffic originating from a connected client is not inadvertently sent outside the VPN tunnel.

Client Route Enforcement works by monitoring the route table of a connected device for routing policy changes to the VPN connection. If the feature detects any VPN routing policy modifications, it will automatically force an update to the route table, reverting it back to the expected route configurations.

## Contents
<a name="API_ClientRouteEnforcementOptions_Contents"></a>

 ** Enforced **
Enable or disable Client Route Enforcement. The state can either be `true` (enabled) or `false` (disabled). The default is `false`.
Valid values: `true | false`
Default value: `false`
Type: Boolean
Required: No

## See Also
<a name="API_ClientRouteEnforcementOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ClientRouteEnforcementOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ClientRouteEnforcementOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ClientRouteEnforcementOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
