---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_AthenaDatasetDefinition.html
---

# AthenaDatasetDefinition
<a name="API_AthenaDatasetDefinition"></a>

Configuration for Athena Dataset Definition input.

## Contents
<a name="API_AthenaDatasetDefinition_Contents"></a>

 ** Catalog **   <a name="sagemaker-Type-AthenaDatasetDefinition-Catalog"></a>
The name of the data catalog used in Athena query execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: Yes

 ** Database **   <a name="sagemaker-Type-AthenaDatasetDefinition-Database"></a>
The name of the database used in the Athena query execution.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`
Required: Yes

 ** OutputFormat **   <a name="sagemaker-Type-AthenaDatasetDefinition-OutputFormat"></a>
The data storage format for Athena query results.
Type: String
Valid Values: `PARQUET | ORC | AVRO | JSON | TEXTFILE`
Required: Yes

 ** OutputS3Uri **   <a name="sagemaker-Type-AthenaDatasetDefinition-OutputS3Uri"></a>
The location in Amazon S3 where Athena query results are stored.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `(https|s3)://([^/]+)/?(.*)`
Required: Yes

 ** QueryString **   <a name="sagemaker-Type-AthenaDatasetDefinition-QueryString"></a>
The SQL query statements, to be executed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `[\s\S]+`
Required: Yes

 ** KmsKeyId **   <a name="sagemaker-Type-AthenaDatasetDefinition-KmsKeyId"></a>
The AWS Key Management Service (AWS KMS) key that Amazon SageMaker uses to encrypt data generated from an Athena query execution.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[a-zA-Z0-9:/_-]*`
Required: No

 ** OutputCompression **   <a name="sagemaker-Type-AthenaDatasetDefinition-OutputCompression"></a>
The compression used for Athena query results.
Type: String
Valid Values: `GZIP | SNAPPY | ZLIB`
Required: No

 ** WorkGroup **   <a name="sagemaker-Type-AthenaDatasetDefinition-WorkGroup"></a>
The name of the workgroup in which the Athena query is being started.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9._-]+`
Required: No

## See Also
<a name="API_AthenaDatasetDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/AthenaDatasetDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/AthenaDatasetDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/AthenaDatasetDefinition)
