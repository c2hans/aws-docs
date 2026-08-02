---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_SignalInformation.html
---

# SignalInformation
<a name="API_SignalInformation"></a>

Information about a signal.

## Contents
<a name="API_SignalInformation_Contents"></a>

 ** name **   <a name="iotfleetwise-Type-SignalInformation-name"></a>
The name of the signal.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 150.
Pattern: `[\w|*|-]+(\.[\w|*|-]+)*`
Required: Yes

 ** dataPartitionId **   <a name="iotfleetwise-Type-SignalInformation-dataPartitionId"></a>
The ID of the data partition this signal is associated with.
The ID must match one of the IDs provided in `dataPartitions`. This is accomplished either by specifying a particular data partition ID or by using `default` for an established default partition. You can establish a default partition in the `DataPartition` data type.
If you upload a signal as a condition for a campaign's data partition, the same signal must be included in `signalsToCollect`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9]+`
Required: No

 ** maxSampleCount **   <a name="iotfleetwise-Type-SignalInformation-maxSampleCount"></a>
The maximum number of samples to collect.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 4294967295.
Required: No

 ** minimumSamplingIntervalMs **   <a name="iotfleetwise-Type-SignalInformation-minimumSamplingIntervalMs"></a>
The minimum duration of time (in milliseconds) between two triggering events to collect data.
If a signal changes often, you might want to collect data at a slower rate.
Type: Long
Valid Range: Minimum value of 0. Maximum value of 4294967295.
Required: No

## See Also
<a name="API_SignalInformation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/SignalInformation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/SignalInformation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/SignalInformation)
