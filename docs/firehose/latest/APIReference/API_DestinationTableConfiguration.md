---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_DestinationTableConfiguration.html
---

# DestinationTableConfiguration
<a name="API_DestinationTableConfiguration"></a>

 Describes the configuration of a destination in Apache Iceberg Tables. This section is only needed for tables where you want to update or delete data.

## Contents
<a name="API_DestinationTableConfiguration_Contents"></a>

 ** DestinationDatabaseName **   <a name="Firehose-Type-DestinationTableConfiguration-DestinationDatabaseName"></a>
 The name of the Apache Iceberg database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\.\_]+`
Required: Yes

 ** DestinationTableName **   <a name="Firehose-Type-DestinationTableConfiguration-DestinationTableName"></a>
 Specifies the name of the Apache Iceberg Table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\.\_]+`
Required: Yes

 ** PartitionSpec **   <a name="Firehose-Type-DestinationTableConfiguration-PartitionSpec"></a>
The partition spec configuration for a table that is used by automatic table creation.
Amazon Data Firehose is in preview release and is subject to change.
Type: [PartitionSpec](API_PartitionSpec.md) object
Required: No

 ** S3ErrorOutputPrefix **   <a name="Firehose-Type-DestinationTableConfiguration-S3ErrorOutputPrefix"></a>
 The table specific S3 error output prefix. All the errors that occurred while delivering to this table will be prefixed with this value in S3 destination.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** UniqueKeys **   <a name="Firehose-Type-DestinationTableConfiguration-UniqueKeys"></a>
 A list of unique keys for a given Apache Iceberg table. Firehose will use these for running Create, Update, or Delete operations on the given Iceberg table.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^\S+$`
Required: No

## See Also
<a name="API_DestinationTableConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/DestinationTableConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/DestinationTableConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/DestinationTableConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Data Firehose. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query firehose` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
