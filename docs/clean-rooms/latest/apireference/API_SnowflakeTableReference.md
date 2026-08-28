---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_SnowflakeTableReference.html
---

# SnowflakeTableReference
<a name="API_SnowflakeTableReference"></a>

 A reference to a table within Snowflake.

## Contents
<a name="API_SnowflakeTableReference_Contents"></a>

 ** accountIdentifier **   <a name="API-Type-SnowflakeTableReference-accountIdentifier"></a>
 The account identifier for the Snowflake table reference.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 256.
Pattern: `[\p{L}\p{M}\p{N}\p{Pc}\p{Pd}\p{Zs}.]+`
Required: Yes

 ** databaseName **   <a name="API-Type-SnowflakeTableReference-databaseName"></a>
 The name of the database the Snowflake table belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}\p{M}\p{N}\p{Pc}\p{Pd}\p{Zs}]+`
Required: Yes

 ** schemaName **   <a name="API-Type-SnowflakeTableReference-schemaName"></a>
 The schema name of the Snowflake table reference.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}\p{M}\p{N}\p{Pc}\p{Pd}\p{Zs}]+`
Required: Yes

 ** secretArn **   <a name="API-Type-SnowflakeTableReference-secretArn"></a>
 The secret ARN of the Snowflake table reference.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws:secretsmanager:[a-z]{2}-[a-z]+-[0-9]:\d{12}:secret:.*`
Required: Yes

 ** tableName **   <a name="API-Type-SnowflakeTableReference-tableName"></a>
 The name of the Snowflake table.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[\p{L}\p{M}\p{N}\p{Pc}\p{Pd}\p{Zs}]+`
Required: Yes

 ** tableSchema **   <a name="API-Type-SnowflakeTableReference-tableSchema"></a>
 The schema of the Snowflake table.
Type: [SnowflakeTableSchema](API_SnowflakeTableSchema.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## See Also
<a name="API_SnowflakeTableReference_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/SnowflakeTableReference)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/SnowflakeTableReference)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/SnowflakeTableReference)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
