---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_PlayerGatewayConfiguration.html
---

# PlayerGatewayConfiguration
<a name="API_PlayerGatewayConfiguration"></a>

Configuration settings for player gateway. Use these settings to specify advanced options for how player gateway handles connections.

## Contents
<a name="API_PlayerGatewayConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** GameServerIpProtocolSupported **   <a name="gameliftservers-Type-PlayerGatewayConfiguration-GameServerIpProtocolSupported"></a>
The IP protocol that your game servers support for player connections through player gateway. If the value is set to `IPv4`, GameLift will install and execute a lightweight IP translation software on fleet instances to receive and transform incoming IPv6 traffic to IPv4. If the value is set to `DUAL_STACK`, the lightweight IP translation software will not be installed on fleet instances. `DUAL_STACK` provides slightly better performance than `IPv4`.
Type: String
Valid Values: `IPv4 | DUAL_STACK`
Required: No

## See Also
<a name="API_PlayerGatewayConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/PlayerGatewayConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/PlayerGatewayConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/PlayerGatewayConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
