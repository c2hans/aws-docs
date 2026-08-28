---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_RoutingStrategy.html
---

# RoutingStrategy
<a name="API_RoutingStrategy"></a>

The routing configuration for a fleet alias.

 **Related actions**

 [All APIs by task](https://docs.aws.amazon.com/gamelift/latest/developerguide/reference-awssdk.html#reference-awssdk-resources-fleets)

## Contents
<a name="API_RoutingStrategy_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** FleetId **   <a name="gameliftservers-Type-RoutingStrategy-FleetId"></a>
A unique identifier for the fleet that the alias points to. This value is the fleet ID, not the fleet ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+`
Required: No

 ** Message **   <a name="gameliftservers-Type-RoutingStrategy-Message"></a>
The message text to be used with a terminal routing strategy.
Type: String
Required: No

 ** Type **   <a name="gameliftservers-Type-RoutingStrategy-Type"></a>
The type of routing strategy for the alias.
Possible routing types include the following:
+  **SIMPLE** - The alias resolves to one specific fleet. Use this type when routing to active fleets.
+  **TERMINAL** - The alias does not resolve to a fleet but instead can be used to display a message to the user. A terminal alias throws a TerminalRoutingStrategyException with the message embedded.
Type: String
Valid Values: `SIMPLE | TERMINAL`
Required: No

## See Also
<a name="API_RoutingStrategy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/RoutingStrategy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/RoutingStrategy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/RoutingStrategy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
