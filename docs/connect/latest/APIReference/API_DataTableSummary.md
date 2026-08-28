---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DataTableSummary.html
---

# DataTableSummary
<a name="API_DataTableSummary"></a>

A data table summary.

## Contents
<a name="API_DataTableSummary_Contents"></a>

 ** Arn **   <a name="connect-Type-DataTableSummary-Arn"></a>
The summary's ARN.
Type: String
Required: No

 ** Id **   <a name="connect-Type-DataTableSummary-Id"></a>
The summary's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-DataTableSummary-LastModifiedRegion"></a>
The summary's last modified region.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-DataTableSummary-LastModifiedTime"></a>
The summary's last modified time.
Type: Timestamp
Required: No

 ** Name **   <a name="connect-Type-DataTableSummary-Name"></a>
The summary's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `^[\p{L}\p{Z}\p{N}\-_.:=@'|]+$`
Required: No

## See Also
<a name="API_DataTableSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DataTableSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DataTableSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DataTableSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
