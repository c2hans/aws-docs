---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_LookupTableConfiguration.html
---

# LookupTableConfiguration
<a name="API_LookupTableConfiguration"></a>

Configuration for a lookup table destination. Use it to automatically refresh a lookup table with query results on a schedule.

## Contents
<a name="API_LookupTableConfiguration_Contents"></a>

 ** roleArn **   <a name="CWL-Type-LookupTableConfiguration-roleArn"></a>
The ARN of the IAM role that grants permissions to create or update the lookup table with query results.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** tableName **   <a name="CWL-Type-LookupTableConfiguration-tableName"></a>
The name of the lookup table to create or update with query results. The name can contain only alphanumeric characters and underscores.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9_]+$`
Required: Yes

 ** description **   <a name="CWL-Type-LookupTableConfiguration-description"></a>
A description of the lookup table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** kmsKeyId **   <a name="CWL-Type-LookupTableConfiguration-kmsKeyId"></a>
The ARN of the AWS KMS key to use to encrypt the lookup table data. If you don't specify a key, the data is encrypted with an AWS-owned key.
Type: String
Length Constraints: Maximum length of 256.
Required: No

 ** tags **   <a name="CWL-Type-LookupTableConfiguration-tags"></a>
Key-value pairs to associate with the lookup table for resource management and cost allocation. The service applies tags only during initial table creation.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]+)$`
Value Length Constraints: Maximum length of 256.
Value Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_LookupTableConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/LookupTableConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/LookupTableConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/LookupTableConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
