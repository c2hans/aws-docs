---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_AwsJobRateIncreaseCriteria.html
---

# AwsJobRateIncreaseCriteria
<a name="API_AwsJobRateIncreaseCriteria"></a>

The criteria to initiate the increase in rate of rollout for a job.

## Contents
<a name="API_AwsJobRateIncreaseCriteria_Contents"></a>

 ** numberOfNotifiedThings **   <a name="iot-Type-AwsJobRateIncreaseCriteria-numberOfNotifiedThings"></a>
When this number of things have been notified, it will initiate an increase in the rollout rate.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** numberOfSucceededThings **   <a name="iot-Type-AwsJobRateIncreaseCriteria-numberOfSucceededThings"></a>
When this number of things have succeeded in their job execution, it will initiate an increase in the rollout rate.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_AwsJobRateIncreaseCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/AwsJobRateIncreaseCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/AwsJobRateIncreaseCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/AwsJobRateIncreaseCriteria)
