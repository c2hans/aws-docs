---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_MongoDbSettings.html
---

# MongoDbSettings
<a name="API_MongoDbSettings"></a>

Provides information that defines a MongoDB endpoint.

## Contents
<a name="API_MongoDbSettings_Contents"></a>

 ** AuthMechanism **   <a name="DMS-Type-MongoDbSettings-AuthMechanism"></a>
 The authentication mechanism you use to access the MongoDB source endpoint.
For the default value, in MongoDB version 2.x, `"default"` is `"mongodb_cr"`. For MongoDB version 3.x or later, `"default"` is `"scram_sha_1"`. This setting isn't used when `AuthType` is set to `"no"`.
Type: String
Valid Values: `default | mongodb_cr | scram_sha_1`
Required: No

 ** AuthSource **   <a name="DMS-Type-MongoDbSettings-AuthSource"></a>
 The MongoDB database name. This setting isn't used when `AuthType` is set to `"no"`.
The default is `"admin"`.
Type: String
Required: No

 ** AuthType **   <a name="DMS-Type-MongoDbSettings-AuthType"></a>
 The authentication type you use to access the MongoDB source endpoint.
When when set to `"no"`, user name and password parameters are not used and can be empty.
Type: String
Valid Values: `no | password`
Required: No

 ** DatabaseName **   <a name="DMS-Type-MongoDbSettings-DatabaseName"></a>
 The database name on the MongoDB source endpoint.
Type: String
Required: No

 ** DocsToInvestigate **   <a name="DMS-Type-MongoDbSettings-DocsToInvestigate"></a>
 Indicates the number of documents to preview to determine the document organization. Use this setting when `NestingLevel` is set to `"one"`.
Must be a positive value greater than `0`. Default value is `1000`.
Type: String
Required: No

 ** ExtractDocId **   <a name="DMS-Type-MongoDbSettings-ExtractDocId"></a>
Specifies whether the document ID is added to the target table. Use this setting when `NestingLevel` is set to `"none"`.
Set `ExtractDocId` to `"true"` when using [multi-document transactions](https://www.mongodb.com/docs/manual/reference/method/Session.startTransaction/#mongodb-method-Session.startTransaction) with CDC.
Default value is `"false"`.
Type: String
Required: No

 ** KmsKeyId **   <a name="DMS-Type-MongoDbSettings-KmsKeyId"></a>
The AWS KMS key identifier that is used to encrypt the content on the replication instance. If you don't specify a value for the `KmsKeyId` parameter, then AWS DMS uses your default encryption key. AWS KMS creates the default encryption key for your AWS account. Your AWS account has a different default encryption key for each AWS Region.
Type: String
Required: No

 ** NestingLevel **   <a name="DMS-Type-MongoDbSettings-NestingLevel"></a>
 Specifies either document or table mode.
Default value is `"none"`. Specify `"none"` to use document mode. Specify `"one"` to use table mode.
Type: String
Valid Values: `none | one`
Required: No

 ** Password **   <a name="DMS-Type-MongoDbSettings-Password"></a>
 The password for the user account you use to access the MongoDB source endpoint.
Type: String
Required: No

 ** Port **   <a name="DMS-Type-MongoDbSettings-Port"></a>
 The port value for the MongoDB source endpoint.
Type: Integer
Required: No

 ** ReplicateShardCollections **   <a name="DMS-Type-MongoDbSettings-ReplicateShardCollections"></a>
If `true`, AWS DMS replicates data to shard collections. AWS DMS only uses this setting if the target endpoint is a DocumentDB elastic cluster.
When this setting is `true`, note the following:
+ You must set `TargetTablePrepMode` to `nothing`.
+  AWS DMS automatically sets `useUpdateLookup` to `false`.
Type: Boolean
Required: No

 ** SecretsManagerAccessRoleArn **   <a name="DMS-Type-MongoDbSettings-SecretsManagerAccessRoleArn"></a>
The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret`. The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the AWS Secrets Manager secret that allows access to the MongoDB endpoint.
You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId`. Or you can specify clear-text values for `UserName`, `Password`, `ServerName`, and `Port`. You can't specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access AWS Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the * AWS Database Migration Service User Guide*.
Type: String
Required: No

 ** SecretsManagerSecretId **   <a name="DMS-Type-MongoDbSettings-SecretsManagerSecretId"></a>
The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the MongoDB endpoint connection details.
Type: String
Required: No

 ** ServerName **   <a name="DMS-Type-MongoDbSettings-ServerName"></a>
 The name of the server on the MongoDB source endpoint. For MongoDB Atlas, provide the server name for any of the servers in the replication set.
Type: String
Required: No

 ** Username **   <a name="DMS-Type-MongoDbSettings-Username"></a>
The user name you use to access the MongoDB source endpoint.
Type: String
Required: No

 ** UseUpdateLookUp **   <a name="DMS-Type-MongoDbSettings-UseUpdateLookUp"></a>
If `true`, AWS DMS retrieves the entire document from the MongoDB source during migration. This may cause a migration failure if the server response exceeds bandwidth limits. To fetch only updates and deletes during migration, set this parameter to `false`.
Type: Boolean
Required: No

## See Also
<a name="API_MongoDbSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/MongoDbSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/MongoDbSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/MongoDbSettings)
