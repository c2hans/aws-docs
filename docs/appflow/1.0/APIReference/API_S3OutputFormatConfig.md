---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_S3OutputFormatConfig.html
---

# S3OutputFormatConfig
<a name="API_S3OutputFormatConfig"></a>

 The configuration that determines how Amazon AppFlow should format the flow output data when Amazon S3 is used as the destination.

## Contents
<a name="API_S3OutputFormatConfig_Contents"></a>

 ** aggregationConfig **   <a name="appflow-Type-S3OutputFormatConfig-aggregationConfig"></a>
 The aggregation settings that you can use to customize the output format of your flow data.
Type: [AggregationConfig](API_AggregationConfig.md) object
Required: No

 ** fileType **   <a name="appflow-Type-S3OutputFormatConfig-fileType"></a>
 Indicates the file type that Amazon AppFlow places in the Amazon S3 bucket.
Type: String
Valid Values: `CSV | JSON | PARQUET`
Required: No

 ** prefixConfig **   <a name="appflow-Type-S3OutputFormatConfig-prefixConfig"></a>
 Determines the prefix that Amazon AppFlow applies to the folder name in the Amazon S3 bucket. You can name folders according to the flow frequency and date.
Type: [PrefixConfig](API_PrefixConfig.md) object
Required: No

 ** preserveSourceDataTyping **   <a name="appflow-Type-S3OutputFormatConfig-preserveSourceDataTyping"></a>
If your file output format is Parquet, use this parameter to set whether Amazon AppFlow preserves the data types in your source data when it writes the output to Amazon S3.
+  `true`: Amazon AppFlow preserves the data types when it writes to Amazon S3. For example, an integer or `1` in your source data is still an integer in your output.
+  `false`: Amazon AppFlow converts all of the source data into strings when it writes to Amazon S3. For example, an integer of `1` in your source data becomes the string `"1"` in the output.
Type: Boolean
Required: No

## See Also
<a name="API_S3OutputFormatConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/S3OutputFormatConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/S3OutputFormatConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/S3OutputFormatConfig)
