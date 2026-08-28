---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_CdcSpecification.html
---

# CdcSpecification
<a name="API_CdcSpecification"></a>

The settings for the CDC stream of a table. For more information about CDC streams, see [Working with change data capture (CDC) streams in Amazon Keyspaces](https://docs.aws.amazon.com/keyspaces/latest/devguide/cdc.html) in the *Amazon Keyspaces Developer Guide*.

## Contents
<a name="API_CdcSpecification_Contents"></a>

 ** status **   <a name="keyspaces-Type-CdcSpecification-status"></a>
The status of the CDC stream. You can enable or disable a stream for a table.
Type: String
Valid Values: `ENABLED | ENABLING | DISABLED | DISABLING`
Required: Yes

 ** propagateTags **   <a name="keyspaces-Type-CdcSpecification-propagateTags"></a>
Specifies that the stream inherits the tags from the table.
Type: String
Valid Values: `TABLE | NONE`
Required: No

 ** tags **   <a name="keyspaces-Type-CdcSpecification-tags"></a>
The tags (key-value pairs) that you want to apply to the stream.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 60 items.
Required: No

 ** viewType **   <a name="keyspaces-Type-CdcSpecification-viewType"></a>
The view type specifies the changes Amazon Keyspaces records for each changed row in the stream. After you create the stream, you can't make changes to this selection.
The options are:
+  `NEW_AND_OLD_IMAGES` - both versions of the row, before and after the change. This is the default.
+  `NEW_IMAGE` - the version of the row after the change.
+  `OLD_IMAGE` - the version of the row before the change.
+  `KEYS_ONLY` - the partition and clustering keys of the row that was changed.
Type: String
Valid Values: `NEW_IMAGE | OLD_IMAGE | KEYS_ONLY | NEW_AND_OLD_IMAGES`
Required: No

## See Also
<a name="API_CdcSpecification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/CdcSpecification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/CdcSpecification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/CdcSpecification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces (for Apache Cassandra). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
