---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_TargetConfiguration.html
---

# TargetConfiguration
<a name="API_TargetConfiguration"></a>

Settings for a target-based scaling policy. A target-based policy tracks a particular fleet metric specifies a target value for the metric. As player usage changes, the policy triggers Amazon GameLift Servers to adjust capacity so that the metric returns to the target value. The target configuration specifies settings as needed for the target based policy, including the target value.

## Contents
<a name="API_TargetConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** TargetValue **   <a name="gameliftservers-Type-TargetConfiguration-TargetValue"></a>
Desired value to use with a target-based scaling policy. The value must be relevant for whatever metric the scaling policy is using. For example, in a policy using the metric PercentAvailableGameSessions, the target value should be the preferred size of the fleet's buffer (the percent of capacity that should be idle and ready for new game sessions).
Type: Double
Required: Yes

## See Also
<a name="API_TargetConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/TargetConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/TargetConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/TargetConfiguration)
