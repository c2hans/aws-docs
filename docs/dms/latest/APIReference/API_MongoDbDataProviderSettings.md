---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_MongoDbDataProviderSettings.html
---

# MongoDbDataProviderSettings
<a name="API_MongoDbDataProviderSettings"></a>

Provides information that defines a MongoDB data provider.

## Contents
<a name="API_MongoDbDataProviderSettings_Contents"></a>

 ** AuthMechanism **   <a name="DMS-Type-MongoDbDataProviderSettings-AuthMechanism"></a>
The authentication method for connecting to the data provider. Valid values are DEFAULT, MONGODB\_CR, or SCRAM\_SHA\_1.
Type: String
Valid Values: `default | mongodb_cr | scram_sha_1`
Required: No

 ** AuthSource **   <a name="DMS-Type-MongoDbDataProviderSettings-AuthSource"></a>
 The MongoDB database name. This setting isn't used when `AuthType` is set to `"no"`.
The default is `"admin"`.
Type: String
Required: No

 ** AuthType **   <a name="DMS-Type-MongoDbDataProviderSettings-AuthType"></a>
The authentication type for the database connection. Valid values are PASSWORD or NO.
Type: String
Valid Values: `no | password`
Required: No

 ** CertificateArn **   <a name="DMS-Type-MongoDbDataProviderSettings-CertificateArn"></a>
The Amazon Resource Name (ARN) of the certificate used for SSL connection.
Type: String
Required: No

 ** DatabaseName **   <a name="DMS-Type-MongoDbDataProviderSettings-DatabaseName"></a>
The database name on the MongoDB data provider.
Type: String
Required: No

 ** Port **   <a name="DMS-Type-MongoDbDataProviderSettings-Port"></a>
The port value for the MongoDB data provider.
Type: Integer
Required: No

 ** ServerName **   <a name="DMS-Type-MongoDbDataProviderSettings-ServerName"></a>
The name of the MongoDB server.
Type: String
Required: No

 ** SslMode **   <a name="DMS-Type-MongoDbDataProviderSettings-SslMode"></a>
The SSL mode used to connect to the MongoDB data provider. The default value is `none`.
Type: String
Valid Values: `none | require | verify-ca | verify-full`
Required: No

## See Also
<a name="API_MongoDbDataProviderSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/MongoDbDataProviderSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/MongoDbDataProviderSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/MongoDbDataProviderSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
