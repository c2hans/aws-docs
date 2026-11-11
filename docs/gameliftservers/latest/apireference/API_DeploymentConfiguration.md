---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DeploymentConfiguration.html
---

# DeploymentConfiguration
<a name="API_DeploymentConfiguration"></a>

Set of rules for processing a deployment for a container fleet update. For how Amazon GameLift Servers validates and rolls out a deployment, see [Container fleet deployments](https://docs.aws.amazon.com/gameliftservers/latest/developerguide/containers-deployment-validation.html).

## Contents
<a name="API_DeploymentConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ImpairmentStrategy **   <a name="gameliftservers-Type-DeploymentConfiguration-ImpairmentStrategy"></a>
Determines what actions to take if a deployment fails validation. If the fleet is multi-location, this strategy applies across all fleet locations.
+  `ROLLBACK` -- Returns all of the fleet's containers to the last successful deployment.
+  `MAINTAIN` -- Keeps the containers that failed validation in place so that you can inspect them, and returns all other containers to the last successful deployment. Use this option when you're deploying a container image that you want to be able to debug on failure.
Default value: `MAINTAIN`
Type: String
Valid Values: `MAINTAIN | ROLLBACK`
Required: No

 ** MinimumHealthyPercentage **   <a name="gameliftservers-Type-DeploymentConfiguration-MinimumHealthyPercentage"></a>
Sets the minimum percentage of the fleet's game server container groups to keep healthy during deployment activity. A low value favors deployment speed; a high value favors game server availability. For example, if the fleet runs 20 game server container groups and this value is 75, Amazon GameLift Servers keeps at least 15 of them healthy, so it replaces no more than 5 at a time.
Default value: 75
Type: Integer
Valid Range: Minimum value of 30. Maximum value of 75.
Required: No

 ** ProtectionStrategy **   <a name="gameliftservers-Type-DeploymentConfiguration-ProtectionStrategy"></a>
Determines how fleet deployment activity affects active game sessions on the fleet. A protected game session can't be terminated while it's active; a fleet sets the default protection for its new game sessions with `NewGameSessionProtectionPolicy`.
+  `WITH_PROTECTION` -- The deployment honors game session protection, and delays actions that would interrupt a protected active game session until the game session ends.
+  `IGNORE_PROTECTION` -- The deployment replaces containers regardless of game session activity, including active game sessions. This option is useful during development and testing.
This setting also affects how long deployment validation can take. When the fleet's `NewGameSessionProtectionPolicy` is `FullProtection` and the deployment uses `WITH_PROTECTION`, validation waits for protected game sessions to end.
Default value: `WITH_PROTECTION`
Type: String
Valid Values: `WITH_PROTECTION | IGNORE_PROTECTION`
Required: No

## See Also
<a name="API_DeploymentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DeploymentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DeploymentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DeploymentConfiguration)
