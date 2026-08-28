---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_OpenXJsonSerDe.html
---

# OpenXJsonSerDe
<a name="API_OpenXJsonSerDe"></a>

The OpenX SerDe. Used by Firehose for deserializing data, which means converting it from the JSON format in preparation for serializing it to the Parquet or ORC format. This is one of two deserializers you can choose, depending on which one offers the functionality you need. The other option is the native Hive / HCatalog JsonSerDe.

## Contents
<a name="API_OpenXJsonSerDe_Contents"></a>

 ** CaseInsensitive **   <a name="Firehose-Type-OpenXJsonSerDe-CaseInsensitive"></a>
When set to `true`, which is the default, Firehose converts JSON keys to lowercase before deserializing them.
Type: Boolean
Required: No

 ** ColumnToJsonKeyMappings **   <a name="Firehose-Type-OpenXJsonSerDe-ColumnToJsonKeyMappings"></a>
Maps column names to JSON keys that aren't identical to the column names. This is useful when the JSON contains keys that are Hive keywords. For example, `timestamp` is a Hive keyword. If you have a JSON key named `timestamp`, set this parameter to `{"ts": "timestamp"}` to map this key to a column named `ts`.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 1024.
Key Pattern: `^\S+$`
Value Length Constraints: Minimum length of 1. Maximum length of 1024.
Value Pattern: `^(?!\s*$).+`
Required: No

 ** ConvertDotsInJsonKeysToUnderscores **   <a name="Firehose-Type-OpenXJsonSerDe-ConvertDotsInJsonKeysToUnderscores"></a>
When set to `true`, specifies that the names of the keys include dots and that you want Firehose to replace them with underscores. This is useful because Apache Hive does not allow dots in column names. For example, if the JSON contains a key whose name is "a.b", you can define the column name to be "a\_b" when using this option.
The default is `false`.
Type: Boolean
Required: No

## See Also
<a name="API_OpenXJsonSerDe_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/OpenXJsonSerDe)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/OpenXJsonSerDe)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/OpenXJsonSerDe)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
