---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_TargetTrackingConfiguration.html
---

# TargetTrackingConfiguration
<a name="API_TargetTrackingConfiguration"></a>

Settings for a target-based scaling policy as part of a [GameServerGroupAutoScalingPolicy](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GameServerGroupAutoScalingPolicy.html) . These settings are used to create a target-based policy that tracks the Amazon GameLift Servers FleetIQ metric `"PercentUtilizedGameServers"` and specifies a target value for the metric. As player usage changes, the policy triggers to adjust the game server group capacity so that the metric returns to the target value.

## Contents
<a name="API_TargetTrackingConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** TargetValue **   <a name="gameliftservers-Type-TargetTrackingConfiguration-TargetValue"></a>
Desired value to use with a game server group target-based scaling policy.
Type: Double
Valid Range: Minimum value of 0.
Required: Yes

## See Also
<a name="API_TargetTrackingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/TargetTrackingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/TargetTrackingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/TargetTrackingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Servers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftservers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
