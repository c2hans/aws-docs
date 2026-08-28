---
source_url: https://docs.aws.amazon.com/timestream/latest/APIReference/API_Database.html
---

# Database
<a name="API_Database"></a>

A top-level container for a table. Databases and tables are the fundamental management concepts in Amazon Timestream. All tables in a database are encrypted with the same AWS KMS key.

## Contents
<a name="API_Database_Contents"></a>

 ** Arn **   <a name="timestream-Type-Database-Arn"></a>
The Amazon Resource Name that uniquely identifies this database.
Type: String
Required: No

 ** CreationTime **   <a name="timestream-Type-Database-CreationTime"></a>
The time when the database was created, calculated from the Unix epoch time.
Type: Timestamp
Required: No

 ** DatabaseName **   <a name="timestream-Type-Database-DatabaseName"></a>
The name of the Timestream database.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 256.
Required: No

 ** KmsKeyId **   <a name="timestream-Type-Database-KmsKeyId"></a>
The identifier of the AWS KMS key used to encrypt the data stored in the database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** LastUpdatedTime **   <a name="timestream-Type-Database-LastUpdatedTime"></a>
 The last time that this database was updated.
Type: Timestamp
Required: No

 ** TableCount **   <a name="timestream-Type-Database-TableCount"></a>
The total number of tables found within a Timestream database.
Type: Long
Required: No

## See Also
<a name="API_Database_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/timestream-write-2018-11-01/Database)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/timestream-write-2018-11-01/Database)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/timestream-write-2018-11-01/Database)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream for LiveAnalytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
