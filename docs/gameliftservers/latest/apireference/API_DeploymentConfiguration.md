---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_DeploymentConfiguration.html
---

# DeploymentConfiguration
<a name="API_DeploymentConfiguration"></a>

Set of rules for processing a deployment for a container fleet update.

## Contents
<a name="API_DeploymentConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ImpairmentStrategy **   <a name="gameliftservers-Type-DeploymentConfiguration-ImpairmentStrategy"></a>
Determines what actions to take if a deployment fails. If the fleet is multi-location, this strategy applies across all fleet locations. With a rollback strategy, updated fleet instances are rolled back to the last successful deployment. Alternatively, you can maintain a few impaired containers for the purpose of debugging, while all other tasks return to the last successful deployment.
Type: String
Valid Values: `MAINTAIN | ROLLBACK`
Required: No

 ** MinimumHealthyPercentage **   <a name="gameliftservers-Type-DeploymentConfiguration-MinimumHealthyPercentage"></a>
Sets a minimum level of healthy tasks to maintain during deployment activity.
Type: Integer
Valid Range: Minimum value of 30. Maximum value of 75.
Required: No

 ** ProtectionStrategy **   <a name="gameliftservers-Type-DeploymentConfiguration-ProtectionStrategy"></a>
Determines how fleet deployment activity affects active game sessions on the fleet. With protection, a deployment honors game session protection, and delays actions that would interrupt a protected active game session until the game session ends. Without protection, deployment activity can shut down all running tasks, including active game sessions, regardless of game session protection.
Type: String
Valid Values: `WITH_PROTECTION | IGNORE_PROTECTION`
Required: No

## See Also
<a name="API_DeploymentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/DeploymentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/DeploymentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/DeploymentConfiguration)
