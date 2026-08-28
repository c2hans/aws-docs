---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_LookupTable.html
---

# LookupTable
<a name="API_LookupTable"></a>

Contains metadata about a lookup table returned by `DescribeLookupTables`.

## Contents
<a name="API_LookupTable_Contents"></a>

 ** description **   <a name="CWL-Type-LookupTable-description"></a>
The description of the lookup table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** kmsKeyId **   <a name="CWL-Type-LookupTable-kmsKeyId"></a>
The ARN of the AWS KMS key used to encrypt the lookup table data, if applicable.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** lastUpdatedTime **   <a name="CWL-Type-LookupTable-lastUpdatedTime"></a>
The time when the lookup table was last updated, expressed as the number of milliseconds after `Jan 1, 1970 00:00:00 UTC`.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** lookupTableArn **   <a name="CWL-Type-LookupTable-lookupTableArn"></a>
The ARN of the lookup table.
Type: String
Required: No

 ** lookupTableName **   <a name="CWL-Type-LookupTable-lookupTableName"></a>
The name of the lookup table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9_]+$`
Required: No

 ** recordsCount **   <a name="CWL-Type-LookupTable-recordsCount"></a>
The number of data rows in the lookup table, excluding the header row.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** sizeBytes **   <a name="CWL-Type-LookupTable-sizeBytes"></a>
The size of the lookup table in bytes.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** tableFields **   <a name="CWL-Type-LookupTable-tableFields"></a>
The column headers from the first row of the CSV file.
Type: Array of strings
Required: No

## See Also
<a name="API_LookupTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/LookupTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/LookupTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/LookupTable)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
