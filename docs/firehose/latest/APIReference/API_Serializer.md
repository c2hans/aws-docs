---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_Serializer.html
---

# Serializer
<a name="API_Serializer"></a>

The serializer that you want Firehose to use to convert data to the target format before writing it to Amazon S3. Firehose supports two types of serializers: the ORC SerDe and the Parquet SerDe.

## Contents
<a name="API_Serializer_Contents"></a>

 ** OrcSerDe **   <a name="Firehose-Type-Serializer-OrcSerDe"></a>
A serializer to use for converting data to the ORC format before storing it in Amazon S3. For more information, see [Apache ORC](https://orc.apache.org/docs/).
Type: [OrcSerDe](API_OrcSerDe.md) object
Required: No

 ** ParquetSerDe **   <a name="Firehose-Type-Serializer-ParquetSerDe"></a>
A serializer to use for converting data to the Parquet format before storing it in Amazon S3. For more information, see [Apache Parquet](https://parquet.apache.org/docs/contribution-guidelines/).
Type: [ParquetSerDe](API_ParquetSerDe.md) object
Required: No

## See Also
<a name="API_Serializer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/Serializer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/Serializer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/Serializer)
