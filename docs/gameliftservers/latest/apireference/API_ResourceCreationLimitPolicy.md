---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_ResourceCreationLimitPolicy.html
---

# ResourceCreationLimitPolicy
<a name="API_ResourceCreationLimitPolicy"></a>

A policy that puts limits on the number of game sessions that a player can create within a specified span of time. With this policy, you can control players' ability to consume available resources.

The policy is evaluated when a player tries to create a new game session. On receiving a `CreateGameSession` request, Amazon GameLift Servers checks that the player (identified by `CreatorId`) has created fewer than game session limit in the specified time period.

The purpose of this policy is to prevent a single player from consuming a large share of available hosting resources. For example, setting `NewGameSessionsPerCreator` to `4` and `PolicyPeriodInMinutes` to `10` limits each player to creating 4 game sessions every 10 minutes. Setting these values too high (for example, 200 game sessions every 1000 minutes) still allows a single player to rapidly consume resources. We recommend keeping these values small.

## Contents
<a name="API_ResourceCreationLimitPolicy_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** NewGameSessionsPerCreator **   <a name="gameliftservers-Type-ResourceCreationLimitPolicy-NewGameSessionsPerCreator"></a>
A policy that puts limits on the number of game sessions that a player can create within a specified span of time. With this policy, you can control players' ability to consume available resources.
The policy is evaluated when a player tries to create a new game session. On receiving a `CreateGameSession` request, Amazon GameLift Servers checks that the player (identified by `CreatorId`) has created fewer than game session limit in the specified time period.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** PolicyPeriodInMinutes **   <a name="gameliftservers-Type-ResourceCreationLimitPolicy-PolicyPeriodInMinutes"></a>
The time span used in evaluating the resource creation limit policy.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_ResourceCreationLimitPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/ResourceCreationLimitPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/ResourceCreationLimitPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/ResourceCreationLimitPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
