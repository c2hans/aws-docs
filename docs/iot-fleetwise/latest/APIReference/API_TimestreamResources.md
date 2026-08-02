---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_TimestreamResources.html
---

# TimestreamResources
<a name="API_TimestreamResources"></a>

The registered Amazon Timestream resources that AWS IoT FleetWise edge agent software can transfer your vehicle data to.

## Contents
<a name="API_TimestreamResources_Contents"></a>

 ** timestreamDatabaseName **   <a name="iotfleetwise-Type-TimestreamResources-timestreamDatabaseName"></a>
The name of the registered Amazon Timestream database.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** timestreamTableName **   <a name="iotfleetwise-Type-TimestreamResources-timestreamTableName"></a>
The name of the registered Amazon Timestream database table.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

## See Also
<a name="API_TimestreamResources_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/TimestreamResources)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/TimestreamResources)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/TimestreamResources)
