---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_DataPartitionUploadOptions.html
---

# DataPartitionUploadOptions
<a name="API_DataPartitionUploadOptions"></a>

The upload options for the data partition. If upload options are specified, you must also specify storage options. See [DataPartitionStorageOptions](https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_DataPartitionStorageOptions.html).

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

## Contents
<a name="API_DataPartitionUploadOptions_Contents"></a>

 ** expression **   <a name="iotfleetwise-Type-DataPartitionUploadOptions-expression"></a>
The logical expression used to recognize what data to collect. For example, `$variable.`Vehicle.OutsideAirTemperature` >= 105.0`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

 ** conditionLanguageVersion **   <a name="iotfleetwise-Type-DataPartitionUploadOptions-conditionLanguageVersion"></a>
The version of the condition language. Defaults to the most recent condition language version.
Type: Integer
Valid Range: Fixed value of 1.
Required: No

## See Also
<a name="API_DataPartitionUploadOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/DataPartitionUploadOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/DataPartitionUploadOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/DataPartitionUploadOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
