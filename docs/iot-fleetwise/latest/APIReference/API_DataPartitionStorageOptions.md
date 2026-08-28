---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_DataPartitionStorageOptions.html
---

# DataPartitionStorageOptions
<a name="API_DataPartitionStorageOptions"></a>

Size, time, and location options for the data partition.

## Contents
<a name="API_DataPartitionStorageOptions_Contents"></a>

 ** maximumSize **   <a name="iotfleetwise-Type-DataPartitionStorageOptions-maximumSize"></a>
The maximum storage size of the data stored in the data partition.
Newer data overwrites older data when the partition reaches the maximum size.
Type: [StorageMaximumSize](API_StorageMaximumSize.md) object
Required: Yes

 ** minimumTimeToLive **   <a name="iotfleetwise-Type-DataPartitionStorageOptions-minimumTimeToLive"></a>
The amount of time that data in this partition will be kept on disk.
+ After the designated amount of time passes, the data can be removed, but it's not guaranteed to be removed.
+ Before the time expires, data in this partition can still be deleted if the partition reaches its configured maximum size.
+ Newer data will overwrite older data when the partition reaches the maximum size.
Type: [StorageMinimumTimeToLive](API_StorageMinimumTimeToLive.md) object
Required: Yes

 ** storageLocation **   <a name="iotfleetwise-Type-DataPartitionStorageOptions-storageLocation"></a>
The folder name for the data partition under the campaign storage folder.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

## See Also
<a name="API_DataPartitionStorageOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/DataPartitionStorageOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/DataPartitionStorageOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/DataPartitionStorageOptions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
