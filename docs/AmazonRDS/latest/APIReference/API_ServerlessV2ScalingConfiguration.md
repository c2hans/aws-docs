---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_ServerlessV2ScalingConfiguration.html
---

# ServerlessV2ScalingConfiguration
<a name="API_ServerlessV2ScalingConfiguration"></a>

Contains the scaling configuration of an Aurora Serverless v2 DB cluster.

For more information, see [Using Amazon Aurora Serverless v2](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/aurora-serverless-v2.html) in the *Amazon Aurora User Guide*.

## Contents
<a name="API_ServerlessV2ScalingConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** MaxCapacity **
The maximum number of Aurora capacity units (ACUs) for a DB instance in an Aurora Serverless v2 cluster. You can specify ACU values in half-step increments, such as 32, 32.5, 33, and so on. The largest value that you can use is 256 for recent Aurora versions, or 128 for older versions. You can check the attributes of your engine version or platform version to determine the specific maximum capacity supported.
Type: Double
Required: No

 ** MinCapacity **
The minimum number of Aurora capacity units (ACUs) for a DB instance in an Aurora Serverless v2 cluster. You can specify ACU values in half-step increments, such as 8, 8.5, 9, and so on. For Aurora versions that support the Aurora Serverless v2 auto-pause feature, the smallest value that you can use is 0. For versions that don't support Aurora Serverless v2 auto-pause, the smallest value that you can use is 0.5.
Type: Double
Required: No

 ** SecondsUntilAutoPause **
Specifies the number of seconds an Aurora Serverless v2 DB instance must be idle before Aurora attempts to automatically pause it.
Specify a value between 300 seconds (five minutes) and 86,400 seconds (one day). The default is 300 seconds.
Type: Integer
Required: No

## See Also
<a name="API_ServerlessV2ScalingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rds-2014-10-31/ServerlessV2ScalingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rds-2014-10-31/ServerlessV2ScalingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rds-2014-10-31/ServerlessV2ScalingConfiguration)
