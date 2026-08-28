---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_PlayerConnectionEndpoint.html
---

# PlayerConnectionEndpoint
<a name="API_PlayerConnectionEndpoint"></a>

Network address(es) and port(s) for connecting to a game session.

## Contents
<a name="API_PlayerConnectionEndpoint_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** IpAddress **   <a name="gameliftservers-Type-PlayerConnectionEndpoint-IpAddress"></a>
IP address for connecting to the game session. When player gateway is enabled, this is a player gateway IP address. When player gateway is disabled, this is the game server IP address.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[0-9A-Fa-f\:\.]+`
Required: No

 ** Port **   <a name="gameliftservers-Type-PlayerConnectionEndpoint-Port"></a>
Port number for connecting to the game session. When player gateway is enabled, this is a player gateway port. When player gateway is disabled, this is the game server port.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 60000.
Required: No

## See Also
<a name="API_PlayerConnectionEndpoint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/PlayerConnectionEndpoint)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/PlayerConnectionEndpoint)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/PlayerConnectionEndpoint)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
