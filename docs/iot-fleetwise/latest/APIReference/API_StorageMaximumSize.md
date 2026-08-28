---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_StorageMaximumSize.html
---

# StorageMaximumSize
<a name="API_StorageMaximumSize"></a>

The maximum storage size for the data partition.

**Important**
 AWS IoT FleetWise is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS IoT FleetWise availability change](https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/iotfleetwise-availability-change.html).

## Contents
<a name="API_StorageMaximumSize_Contents"></a>

 ** unit **   <a name="iotfleetwise-Type-StorageMaximumSize-unit"></a>
The data type of the data to store.
Type: String
Valid Values: `MB | GB | TB`
Required: Yes

 ** value **   <a name="iotfleetwise-Type-StorageMaximumSize-value"></a>
The maximum amount of time to store data.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1073741824.
Required: Yes

## See Also
<a name="API_StorageMaximumSize_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/StorageMaximumSize)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/StorageMaximumSize)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/StorageMaximumSize)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT FleetWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-fleetwise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
