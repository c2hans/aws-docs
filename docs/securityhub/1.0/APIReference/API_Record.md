---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_Record.html
---

# Record
<a name="API_Record"></a>

An occurrence of sensitive data in an Apache Avro object container or an Apache Parquet file.

## Contents
<a name="API_Record_Contents"></a>

 ** JsonPath **   <a name="securityhub-Type-Record-JsonPath"></a>
The path, as a JSONPath expression, to the field in the record that contains the data. If the field name is longer than 20 characters, it is truncated. If the path is longer than 250 characters, it is truncated.
Type: String
Pattern: `.*\S.*`
Required: No

 ** RecordIndex **   <a name="securityhub-Type-Record-RecordIndex"></a>
The record index, starting from 0, for the record that contains the data.
Type: Long
Required: No

## See Also
<a name="API_Record_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/Record)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/Record)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/Record)
