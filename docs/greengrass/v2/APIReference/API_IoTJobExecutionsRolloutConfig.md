---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_IoTJobExecutionsRolloutConfig.html
---

# IoTJobExecutionsRolloutConfig
<a name="API_IoTJobExecutionsRolloutConfig"></a>

Contains information about the rollout configuration for a job. This configuration defines the rate at which the job deploys a configuration to a fleet of target devices.

## Contents
<a name="API_IoTJobExecutionsRolloutConfig_Contents"></a>

 ** exponentialRate **   <a name="greengrassv2-Type-IoTJobExecutionsRolloutConfig-exponentialRate"></a>
The exponential rate to increase the job rollout rate.
Type: [IoTJobExponentialRolloutRate](API_IoTJobExponentialRolloutRate.md) object
Required: No

 ** maximumPerMinute **   <a name="greengrassv2-Type-IoTJobExecutionsRolloutConfig-maximumPerMinute"></a>
The maximum number of devices that receive a pending job notification, per minute.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

## See Also
<a name="API_IoTJobExecutionsRolloutConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/IoTJobExecutionsRolloutConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/IoTJobExecutionsRolloutConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/IoTJobExecutionsRolloutConfig)
