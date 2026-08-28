---
source_url: https://docs.aws.amazon.com/appsync/latest/APIReference/API_DynamodbDataSourceConfig.html
---

# DynamodbDataSourceConfig
<a name="API_DynamodbDataSourceConfig"></a>

Describes an Amazon DynamoDB data source configuration.

## Contents
<a name="API_DynamodbDataSourceConfig_Contents"></a>

 ** awsRegion **   <a name="appsync-Type-DynamodbDataSourceConfig-awsRegion"></a>
The AWS Region.
Type: String
Required: Yes

 ** tableName **   <a name="appsync-Type-DynamodbDataSourceConfig-tableName"></a>
The table name.
Type: String
Required: Yes

 ** deltaSyncConfig **   <a name="appsync-Type-DynamodbDataSourceConfig-deltaSyncConfig"></a>
The `DeltaSyncConfig` for a versioned data source.
Type: [DeltaSyncConfig](API_DeltaSyncConfig.md) object
Required: No

 ** useCallerCredentials **   <a name="appsync-Type-DynamodbDataSourceConfig-useCallerCredentials"></a>
Set to TRUE to use Amazon Cognito credentials with this data source.
Type: Boolean
Required: No

 ** versioned **   <a name="appsync-Type-DynamodbDataSourceConfig-versioned"></a>
Set to TRUE to use Conflict Detection and Resolution with this data source.
Type: Boolean
Required: No

## See Also
<a name="API_DynamodbDataSourceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/DynamodbDataSourceConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/DynamodbDataSourceConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/DynamodbDataSourceConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
