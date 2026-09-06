---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_InputSerialization.html
---

# InputSerialization
<a name="API_InputSerialization"></a>

Describes the serialization format of the object.

## Contents
<a name="API_InputSerialization_Contents"></a>

 ** CompressionType **   <a name="AmazonS3-Type-InputSerialization-CompressionType"></a>
Specifies object's compression format. Valid values: NONE, GZIP, BZIP2. Default Value: NONE.
Type: String
Valid Values: `NONE | GZIP | BZIP2`
Required: No

 ** CSV **   <a name="AmazonS3-Type-InputSerialization-CSV"></a>
Describes the serialization of a CSV-encoded object.
Type: [CSVInput](API_CSVInput.md) data type
Required: No

 ** JSON **   <a name="AmazonS3-Type-InputSerialization-JSON"></a>
Specifies JSON as object's input serialization format.
Type: [JSONInput](API_JSONInput.md) data type
Required: No

 ** Parquet **   <a name="AmazonS3-Type-InputSerialization-Parquet"></a>
Specifies Parquet as object's input serialization format.
Type: [ParquetInput](API_ParquetInput.md) data type
Required: No

## See Also
<a name="API_InputSerialization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3-2006-03-01/InputSerialization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3-2006-03-01/InputSerialization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3-2006-03-01/InputSerialization)
