---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_TimestreamDimension.html
---

# TimestreamDimension
<a name="API_TimestreamDimension"></a>

Metadata attributes of the time series that are written in each measure record.

## Contents
<a name="API_TimestreamDimension_Contents"></a>

 ** name **   <a name="iot-Type-TimestreamDimension-name"></a>
The metadata dimension name. This is the name of the column in the Amazon Timestream database table record.
Dimensions cannot be named: `measure_name`, `measure_value`, or `time`. These names are reserved. Dimension names cannot start with `ts_` or `measure_value` and they cannot contain the colon (`:`) character.
Type: String
Required: Yes

 ** value **   <a name="iot-Type-TimestreamDimension-value"></a>
The value to write in this column of the database record.
Type: String
Required: Yes

## See Also
<a name="API_TimestreamDimension_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/TimestreamDimension)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/TimestreamDimension)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/TimestreamDimension)
