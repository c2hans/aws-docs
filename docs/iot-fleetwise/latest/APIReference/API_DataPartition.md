---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_DataPartition.html
---

# DataPartition
<a name="API_DataPartition"></a>

The configuration for signal data storage and upload options. You can only specify these options when the campaign's spooling mode is `TO_DISK`.

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

## Contents
<a name="API_DataPartition_Contents"></a>

 ** id **   <a name="iotfleetwise-Type-DataPartition-id"></a>
The ID of the data partition. The data partition ID must be unique within a campaign. You can establish a data partition as the default partition for a campaign by using `default` as the ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9]+`
Required: Yes

 ** storageOptions **   <a name="iotfleetwise-Type-DataPartition-storageOptions"></a>
The storage options for a data partition.
Type: [DataPartitionStorageOptions](API_DataPartitionStorageOptions.md) object
Required: Yes

 ** uploadOptions **   <a name="iotfleetwise-Type-DataPartition-uploadOptions"></a>
The upload options for the data partition.
Type: [DataPartitionUploadOptions](API_DataPartitionUploadOptions.md) object
Required: No

## See Also
<a name="API_DataPartition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/DataPartition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/DataPartition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/DataPartition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
