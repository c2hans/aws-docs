---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_DocDbSettings.html
---

# DocDbSettings
<a name="API_DocDbSettings"></a>

Provides information that defines a DocumentDB endpoint.

## Contents
<a name="API_DocDbSettings_Contents"></a>

 ** DatabaseName **   <a name="DMS-Type-DocDbSettings-DatabaseName"></a>
 The database name on the DocumentDB source endpoint.
Type: String
Required: No

 ** DocsToInvestigate **   <a name="DMS-Type-DocDbSettings-DocsToInvestigate"></a>
 Indicates the number of documents to preview to determine the document organization. Use this setting when `NestingLevel` is set to `"one"`.
Must be a positive value greater than `0`. Default value is `1000`.
Type: Integer
Required: No

 ** ExtractDocId **   <a name="DMS-Type-DocDbSettings-ExtractDocId"></a>
Specifies whether the document ID is added to the target table. Use this setting when `NestingLevel` is set to `"none"`.
Set `ExtractDocId` to `true` when using [multi-document transactions](https://www.mongodb.com/docs/manual/reference/method/Session.startTransaction/#mongodb-method-Session.startTransaction) with CDC.
Default value is `false`.
Type: Boolean
Required: No

 ** KmsKeyId **   <a name="DMS-Type-DocDbSettings-KmsKeyId"></a>
The AWS KMS key identifier that is used to encrypt the content on the replication instance. If you don't specify a value for the `KmsKeyId` parameter, then AWS DMS uses your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.
Type: String
Required: No

 ** NestingLevel **   <a name="DMS-Type-DocDbSettings-NestingLevel"></a>
 Specifies either document or table mode.
Default value is `"none"`. Specify `"none"` to use document mode. Specify `"one"` to use table mode.
Type: String
Valid Values: `none | one`
Required: No

 ** Password **   <a name="DMS-Type-DocDbSettings-Password"></a>
 The password for the user account you use to access the DocumentDB source endpoint.
Type: String
Required: No

 ** Port **   <a name="DMS-Type-DocDbSettings-Port"></a>
 The port value for the DocumentDB source endpoint.
Type: Integer
Required: No

 ** ReplicateShardCollections **   <a name="DMS-Type-DocDbSettings-ReplicateShardCollections"></a>
If `true`, AWS DMS replicates data to shard collections. AWS DMS only uses this setting if the target endpoint is a DocumentDB elastic cluster.
When this setting is `true`, note the following:
+ You must set `TargetTablePrepMode` to `nothing`.
+  AWS DMS automatically sets `useUpdateLookup` to `false`.
Type: Boolean
Required: No

 ** SecretsManagerAccessRoleArn **   <a name="DMS-Type-DocDbSettings-SecretsManagerAccessRoleArn"></a>
The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret`. The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the AWS Secrets Manager secret that allows access to the DocumentDB endpoint.
You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId`. Or you can specify clear-text values for `UserName`, `Password`, `ServerName`, and `Port`. You can't specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access AWS Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the * AWS Database Migration Service User Guide*.
Type: String
Required: No

 ** SecretsManagerSecretId **   <a name="DMS-Type-DocDbSettings-SecretsManagerSecretId"></a>
The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the DocumentDB endpoint connection details.
Type: String
Required: No

 ** ServerName **   <a name="DMS-Type-DocDbSettings-ServerName"></a>
 The name of the server on the DocumentDB source endpoint.
Type: String
Required: No

 ** Username **   <a name="DMS-Type-DocDbSettings-Username"></a>
The user name you use to access the DocumentDB source endpoint.
Type: String
Required: No

 ** UseUpdateLookUp **   <a name="DMS-Type-DocDbSettings-UseUpdateLookUp"></a>
If `true`, AWS DMS retrieves the entire document from the DocumentDB source during migration. This may cause a migration failure if the server response exceeds bandwidth limits. To fetch only updates and deletes during migration, set this parameter to `false`.
Type: Boolean
Required: No

## See Also
<a name="API_DocDbSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/DocDbSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/DocDbSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/DocDbSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
