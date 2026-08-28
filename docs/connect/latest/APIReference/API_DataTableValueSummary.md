---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DataTableValueSummary.html
---

# DataTableValueSummary
<a name="API_DataTableValueSummary"></a>

A data table value summary.

## Contents
<a name="API_DataTableValueSummary_Contents"></a>

 ** AttributeName **   <a name="connect-Type-DataTableValueSummary-AttributeName"></a>
The summary's attribute name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `^[\p{L}\p{Z}\p{N}\-_.:=@'|]+$`
Required: Yes

 ** PrimaryValues **   <a name="connect-Type-DataTableValueSummary-PrimaryValues"></a>
The summary's primary values.
Type: Array of [PrimaryValueResponse](API_PrimaryValueResponse.md) objects
Required: Yes

 ** Value **   <a name="connect-Type-DataTableValueSummary-Value"></a>
The summary's value.
Type: String
Required: Yes

 ** ValueType **   <a name="connect-Type-DataTableValueSummary-ValueType"></a>
The summary's value type.
Type: String
Valid Values: `TEXT | NUMBER | BOOLEAN | TEXT_LIST | NUMBER_LIST`
Required: Yes

 ** AttributeId **   <a name="connect-Type-DataTableValueSummary-AttributeId"></a>
The summary's attribute ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-DataTableValueSummary-LastModifiedRegion"></a>
The summary's last modified region.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-DataTableValueSummary-LastModifiedTime"></a>
The summary's last modified time.
Type: Timestamp
Required: No

 ** LockVersion **   <a name="connect-Type-DataTableValueSummary-LockVersion"></a>
The summary's lock version.
Type: [DataTableLockVersion](API_DataTableLockVersion.md) object
Required: No

 ** RecordId **   <a name="connect-Type-DataTableValueSummary-RecordId"></a>
The summary's record ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## See Also
<a name="API_DataTableValueSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DataTableValueSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DataTableValueSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DataTableValueSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
