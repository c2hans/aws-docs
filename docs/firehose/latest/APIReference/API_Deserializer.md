---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_Deserializer.html
---

# Deserializer
<a name="API_Deserializer"></a>

The deserializer you want Firehose to use for converting the input data from JSON. Firehose then serializes the data to its final format using the [Serializer](API_Serializer.md). Firehose supports two types of deserializers: the [Apache Hive JSON SerDe](https://cwiki.apache.org/confluence/display/Hive/LanguageManual+DDL#LanguageManualDDL-JSON) and the [OpenX JSON SerDe](https://github.com/rcongiu/Hive-JSON-Serde).

## Contents
<a name="API_Deserializer_Contents"></a>

 ** HiveJsonSerDe **   <a name="Firehose-Type-Deserializer-HiveJsonSerDe"></a>
The native Hive / HCatalog JsonSerDe. Used by Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the OpenX SerDe.
Type: [HiveJsonSerDe](API_HiveJsonSerDe.md) object
Required: No

 ** OpenXJsonSerDe **   <a name="Firehose-Type-Deserializer-OpenXJsonSerDe"></a>
The OpenX SerDe. Used by Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the native Hive / HCatalog JsonSerDe.
Type: [OpenXJsonSerDe](API_OpenXJsonSerDe.md) object
Required: No

## See Also
<a name="API_Deserializer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/Deserializer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/Deserializer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/Deserializer)
