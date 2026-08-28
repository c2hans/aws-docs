---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_CdcSpecificationSummary.html
---

# CdcSpecificationSummary
<a name="API_CdcSpecificationSummary"></a>

The settings of the CDC stream of the table. For more information about CDC streams, see [Working with change data capture (CDC) streams in Amazon Keyspaces](https://docs.aws.amazon.com/keyspaces/latest/devguide/cdc.html) in the *Amazon Keyspaces Developer Guide*.

## Contents
<a name="API_CdcSpecificationSummary_Contents"></a>

 ** status **   <a name="keyspaces-Type-CdcSpecificationSummary-status"></a>
The status of the CDC stream. Specifies if the table has a CDC stream.
Type: String
Valid Values: `ENABLED | ENABLING | DISABLED | DISABLING`
Required: Yes

 ** viewType **   <a name="keyspaces-Type-CdcSpecificationSummary-viewType"></a>
The view type specifies the changes Amazon Keyspaces records for each changed row in the stream. This setting can't be changed, after the stream has been created.
The options are:
+  `NEW_AND_OLD_IMAGES` - both versions of the row, before and after the change. This is the default.
+  `NEW_IMAGE` - the version of the row after the change.
+  `OLD_IMAGE` - the version of the row before the change.
+  `KEYS_ONLY` - the partition and clustering keys of the row that was changed.
Type: String
Valid Values: `NEW_IMAGE | OLD_IMAGE | KEYS_ONLY | NEW_AND_OLD_IMAGES`
Required: No

## See Also
<a name="API_CdcSpecificationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/CdcSpecificationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/CdcSpecificationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/CdcSpecificationSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces (for Apache Cassandra). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
