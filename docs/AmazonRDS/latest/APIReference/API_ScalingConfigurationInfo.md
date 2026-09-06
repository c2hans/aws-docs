---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ScalingConfigurationInfo.html
---

# ScalingConfigurationInfo
<a name="API_ScalingConfigurationInfo"></a>

The scaling configuration for an Aurora DB cluster in `serverless` DB engine mode.

For more information, see [Using Amazon Aurora Serverless v1](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless.html) in the *Amazon Aurora User Guide*.

## Contents
<a name="API_ScalingConfigurationInfo_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AutoPause **
Indicates whether automatic pause is allowed for the Aurora DB cluster in `serverless` DB engine mode.
When the value is set to false for an Aurora Serverless v1 DB cluster, the DB cluster automatically resumes.
Type: Boolean
Required: No

 ** MaxCapacity **
The maximum capacity for an Aurora DB cluster in `serverless` DB engine mode.
Type: Integer
Required: No

 ** MinCapacity **
The minimum capacity for an Aurora DB cluster in `serverless` DB engine mode.
Type: Integer
Required: No

 ** SecondsBeforeTimeout **
The number of seconds before scaling times out. What happens when an attempted scaling action times out is determined by the `TimeoutAction` setting.
Type: Integer
Required: No

 ** SecondsUntilAutoPause **
The remaining amount of time, in seconds, before the Aurora DB cluster in `serverless` mode is paused. A DB cluster can be paused only when it's idle (it has no connections).
Type: Integer
Required: No

 ** TimeoutAction **
The action that occurs when Aurora times out while attempting to change the capacity of an Aurora Serverless v1 cluster. The value is either `ForceApplyCapacityChange` or `RollbackCapacityChange`.
 `ForceApplyCapacityChange`, the default, sets the capacity to the specified value as soon as possible.
 `RollbackCapacityChange` ignores the capacity change if a scaling point isn't found in the timeout period.
Type: String
Required: No

## See Also
<a name="API_ScalingConfigurationInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ScalingConfigurationInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ScalingConfigurationInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ScalingConfigurationInfo)
