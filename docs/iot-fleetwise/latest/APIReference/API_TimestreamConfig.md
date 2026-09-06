---
source_url: https://docs.aws.amazon.com/iot-fleetwise/latest/APIReference/API_TimestreamConfig.html
---

# TimestreamConfig
<a name="API_TimestreamConfig"></a>

The Amazon Timestream table where the AWS IoT FleetWise campaign sends data. Timestream stores and organizes data to optimize query processing time and to reduce storage costs. For more information, see [Data modeling](https://docs.aws.amazon.com/timestream/latest/developerguide/data-modeling.html) in the *Amazon Timestream Developer Guide*.

## Contents
<a name="API_TimestreamConfig_Contents"></a>

 ** executionRoleArn **   <a name="iotfleetwise-Type-TimestreamConfig-executionRoleArn"></a>
The Amazon Resource Name (ARN) of the task execution role that grants AWS IoT FleetWise permission to deliver data to the Amazon Timestream table.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z0-9-]*):iam::(\d{12})?:(role((\u002F)|(\u002F[\u0021-\u007F]+\u002F))[\w+=,.@-]+)`
Required: Yes

 ** timestreamTableArn **   <a name="iotfleetwise-Type-TimestreamConfig-timestreamTableArn"></a>
The Amazon Resource Name (ARN) of the Amazon Timestream table.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z0-9-]*):timestream:[a-zA-Z0-9-]+:[0-9]{12}:database/[a-zA-Z0-9_.-]+/table/[a-zA-Z0-9_.-]+`
Required: Yes

## See Also
<a name="API_TimestreamConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotfleetwise-2021-06-17/TimestreamConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotfleetwise-2021-06-17/TimestreamConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotfleetwise-2021-06-17/TimestreamConfig)
