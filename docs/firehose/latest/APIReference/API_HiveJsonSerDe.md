---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_HiveJsonSerDe.html
---

# HiveJsonSerDe
<a name="API_HiveJsonSerDe"></a>

The native Hive / HCatalog JsonSerDe. Used by Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the OpenX SerDe.

## Contents
<a name="API_HiveJsonSerDe_Contents"></a>

 ** TimestampFormats **   <a name="Firehose-Type-HiveJsonSerDe-TimestampFormats"></a>
Indicates how you want Firehose to parse the date and timestamps that may be present in your input data JSON. To specify these format strings, follow the pattern syntax of JodaTime's DateTimeFormat format strings. For more information, see [Class DateTimeFormat](https://www.joda.org/joda-time/apidocs/org/joda/time/format/DateTimeFormat.html). You can also use the special value `millis` to parse timestamps in epoch milliseconds. If you don't specify a format, Firehose uses `java.sql.Timestamp::valueOf` by default.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^(?!\s*$).+`
Required: No

## See Also
<a name="API_HiveJsonSerDe_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/HiveJsonSerDe)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/HiveJsonSerDe)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/HiveJsonSerDe)
