---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_TimestreamAction.html
---

# TimestreamAction
<a name="API_TimestreamAction"></a>

The Timestream rule action writes attributes (measures) from an MQTT message into an Amazon Timestream table. For more information, see the [Timestream](https://docs.aws.amazon.com/iot/latest/developerguide/timestream-rule-action.html) topic rule action documentation.

## Contents
<a name="API_TimestreamAction_Contents"></a>

 ** databaseName **   <a name="iot-Type-TimestreamAction-databaseName"></a>
The name of an Amazon Timestream database.
Type: String
Required: Yes

 ** dimensions **   <a name="iot-Type-TimestreamAction-dimensions"></a>
Metadata attributes of the time series that are written in each measure record.
Type: Array of [TimestreamDimension](API_TimestreamDimension.md) objects
Array Members: Minimum number of 1 item. Maximum number of 128 items.
Required: Yes

 ** roleArn **   <a name="iot-Type-TimestreamAction-roleArn"></a>
The ARN of the role that grants permission to write to the Amazon Timestream database table.
Type: String
Required: Yes

 ** tableName **   <a name="iot-Type-TimestreamAction-tableName"></a>
The name of the database table into which to write the measure records.
Type: String
Required: Yes

 ** timestamp **   <a name="iot-Type-TimestreamAction-timestamp"></a>
Specifies an application-defined value to replace the default value assigned to the Timestream record's timestamp in the `time` column.
You can use this property to specify the value and the precision of the Timestream record's timestamp. You can specify a value from the message payload or a value computed by a substitution template.
If omitted, the topic rule action assigns the timestamp, in milliseconds, at the time it processed the rule.
Type: [TimestreamTimestamp](API_TimestreamTimestamp.md) object
Required: No

## See Also
<a name="API_TimestreamAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/TimestreamAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/TimestreamAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/TimestreamAction)
