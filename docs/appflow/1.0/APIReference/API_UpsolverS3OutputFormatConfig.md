---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_UpsolverS3OutputFormatConfig.html
---

# UpsolverS3OutputFormatConfig
<a name="API_UpsolverS3OutputFormatConfig"></a>

 The configuration that determines how Amazon AppFlow formats the flow output data when Upsolver is used as the destination.

## Contents
<a name="API_UpsolverS3OutputFormatConfig_Contents"></a>

 ** prefixConfig **   <a name="appflow-Type-UpsolverS3OutputFormatConfig-prefixConfig"></a>
Specifies elements that Amazon AppFlow includes in the file and folder names in the flow destination.
Type: [PrefixConfig](API_PrefixConfig.md) object
Required: Yes

 ** aggregationConfig **   <a name="appflow-Type-UpsolverS3OutputFormatConfig-aggregationConfig"></a>
 The aggregation settings that you can use to customize the output format of your flow data.
Type: [AggregationConfig](API_AggregationConfig.md) object
Required: No

 ** fileType **   <a name="appflow-Type-UpsolverS3OutputFormatConfig-fileType"></a>
 Indicates the file type that Amazon AppFlow places in the Upsolver Amazon S3 bucket.
Type: String
Valid Values: `CSV | JSON | PARQUET`
Required: No

## See Also
<a name="API_UpsolverS3OutputFormatConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/UpsolverS3OutputFormatConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/UpsolverS3OutputFormatConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/UpsolverS3OutputFormatConfig)
