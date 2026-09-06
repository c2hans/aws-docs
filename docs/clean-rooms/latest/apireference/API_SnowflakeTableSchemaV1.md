---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_SnowflakeTableSchemaV1.html
---

# SnowflakeTableSchemaV1
<a name="API_SnowflakeTableSchemaV1"></a>

 The Snowflake table schema.

## Contents
<a name="API_SnowflakeTableSchemaV1_Contents"></a>

 ** columnName **   <a name="API-Type-SnowflakeTableSchemaV1-columnName"></a>
 The column name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-z0-9_](([a-z0-9_ ]+-)*([a-z0-9_ ]+))?`
Required: Yes

 ** columnType **   <a name="API-Type-SnowflakeTableSchemaV1-columnType"></a>
 The column's data type. Supported data types: `ARRAY`, `BIGINT`, `BOOLEAN`, `CHAR`, `DATE`, `DECIMAL`, `DOUBLE`, `DOUBLE PRECISION`, `FLOAT`, `FLOAT4`, `INT`, `INTEGER`, `MAP`, `NUMERIC`, `NUMBER`, `REAL`, `SMALLINT`, `STRING`, `TIMESTAMP`, `TIMESTAMP_LTZ`, `TIMESTAMP_NTZ`, `DATETIME`, `TINYINT`, `VARCHAR`, `TEXT`, `CHARACTER`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: Yes

## See Also
<a name="API_SnowflakeTableSchemaV1_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/SnowflakeTableSchemaV1)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/SnowflakeTableSchemaV1)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/SnowflakeTableSchemaV1)
