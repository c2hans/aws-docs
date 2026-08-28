---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_GameServerGroupAutoScalingPolicy.html
---

# GameServerGroupAutoScalingPolicy
<a name="API_GameServerGroupAutoScalingPolicy"></a>

Configuration settings for intelligent automatic scaling that uses target tracking. These settings are used to add an Auto Scaling policy when creating the corresponding Auto Scaling group. After the Auto Scaling group is created, all updates to Auto Scaling policies, including changing this policy and adding or removing other policies, is done directly on the Auto Scaling group.

## Contents
<a name="API_GameServerGroupAutoScalingPolicy_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** TargetTrackingConfiguration **   <a name="gameliftservers-Type-GameServerGroupAutoScalingPolicy-TargetTrackingConfiguration"></a>
Settings for a target-based scaling policy applied to Auto Scaling group. These settings are used to create a target-based policy that tracks the Amazon GameLift Servers FleetIQ metric `"PercentUtilizedGameServers"` and specifies a target value for the metric. As player usage changes, the policy triggers to adjust the game server group capacity so that the metric returns to the target value.
Type: [TargetTrackingConfiguration](API_TargetTrackingConfiguration.md) object
Required: Yes

 ** EstimatedInstanceWarmup **   <a name="gameliftservers-Type-GameServerGroupAutoScalingPolicy-EstimatedInstanceWarmup"></a>
Length of time, in seconds, it takes for a new instance to start new game server processes and register with Amazon GameLift Servers FleetIQ. Specifying a warm-up time can be useful, particularly with game servers that take a long time to start up, because it avoids prematurely starting new instances.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_GameServerGroupAutoScalingPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/GameServerGroupAutoScalingPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/GameServerGroupAutoScalingPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/GameServerGroupAutoScalingPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
