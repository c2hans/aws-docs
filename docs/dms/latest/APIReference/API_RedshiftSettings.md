---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_RedshiftSettings.html
---

# RedshiftSettings
<a name="API_RedshiftSettings"></a>

Provides information that defines an Amazon Redshift endpoint.

## Contents
<a name="API_RedshiftSettings_Contents"></a>

 ** AcceptAnyDate **   <a name="DMS-Type-RedshiftSettings-AcceptAnyDate"></a>
A value that indicates to allow any date format, including invalid formats such as 00/00/00 00:00:00, to be loaded without generating an error. You can choose `true` or `false` (the default).
This parameter applies only to TIMESTAMP and DATE columns. Always use ACCEPTANYDATE with the DATEFORMAT parameter. If the date format for the data doesn't match the DATEFORMAT specification, Amazon Redshift inserts a NULL value into that field.
Type: Boolean
Required: No

 ** AfterConnectScript **   <a name="DMS-Type-RedshiftSettings-AfterConnectScript"></a>
Code to run after connecting. This parameter should contain the code itself, not the name of a file containing the code.
Type: String
Required: No

 ** BucketFolder **   <a name="DMS-Type-RedshiftSettings-BucketFolder"></a>
An S3 folder where the comma-separated-value (.csv) files are stored before being uploaded to the target Redshift cluster.
For full load mode, AWS DMS converts source records into .csv files and loads them to the *BucketFolder/TableID* path. AWS DMS uses the Redshift `COPY` command to upload the .csv files to the target table. The files are deleted once the `COPY` operation has finished. For more information, see [COPY](https://docs.aws.amazon.com/redshift/latest/dg/r_COPY.html) in the *Amazon Redshift Database Developer Guide*.
For change-data-capture (CDC) mode, AWS DMS creates a *NetChanges* table, and loads the .csv files to this *BucketFolder/NetChangesTableID* path.
Type: String
Required: No

 ** BucketName **   <a name="DMS-Type-RedshiftSettings-BucketName"></a>
The name of the intermediate S3 bucket used to store .csv files before uploading data to Redshift.
Type: String
Required: No

 ** CaseSensitiveNames **   <a name="DMS-Type-RedshiftSettings-CaseSensitiveNames"></a>
If Amazon Redshift is configured to support case sensitive schema names, set `CaseSensitiveNames` to `true`. The default is `false`.
Type: Boolean
Required: No

 ** CompUpdate **   <a name="DMS-Type-RedshiftSettings-CompUpdate"></a>
If you set `CompUpdate` to `true` Amazon Redshift applies automatic compression if the table is empty. This applies even if the table columns already have encodings other than `RAW`. If you set `CompUpdate` to `false`, automatic compression is disabled and existing column encodings aren't changed. The default is `true`.
Type: Boolean
Required: No

 ** ConnectionTimeout **   <a name="DMS-Type-RedshiftSettings-ConnectionTimeout"></a>
A value that sets the amount of time to wait (in milliseconds) before timing out, beginning from when you initially establish a connection.
Type: Integer
Required: No

 ** DatabaseName **   <a name="DMS-Type-RedshiftSettings-DatabaseName"></a>
The name of the Amazon Redshift data warehouse (service) that you are working with.
Type: String
Required: No

 ** DateFormat **   <a name="DMS-Type-RedshiftSettings-DateFormat"></a>
The date format that you are using. Valid values are `auto` (case-sensitive), your date format string enclosed in quotes, or NULL. If this parameter is left unset (NULL), it defaults to a format of 'YYYY-MM-DD'. Using `auto` recognizes most strings, even some that aren't supported when you use a date format string.
If your date and time values use formats different from each other, set this to `auto`.
Type: String
Required: No

 ** EmptyAsNull **   <a name="DMS-Type-RedshiftSettings-EmptyAsNull"></a>
A value that specifies whether AWS DMS should migrate empty CHAR and VARCHAR fields as NULL. A value of `true` sets empty CHAR and VARCHAR fields to null. The default is `false`.
Type: Boolean
Required: No

 ** EncryptionMode **   <a name="DMS-Type-RedshiftSettings-EncryptionMode"></a>
The type of server-side encryption that you want to use for your data. This encryption type is part of the endpoint settings or the extra connections attributes for Amazon S3. You can choose either `SSE_S3` (the default) or `SSE_KMS`.
For the `ModifyEndpoint` operation, you can change the existing value of the `EncryptionMode` parameter from `SSE_KMS` to `SSE_S3`. But you can’t change the existing value from `SSE_S3` to `SSE_KMS`.
To use `SSE_S3`, create an AWS Identity and Access Management (IAM) role with a policy that allows `"arn:aws:s3:::*"` to use the following actions: `"s3:PutObject", "s3:ListBucket"`
Type: String
Valid Values: `sse-s3 | sse-kms`
Required: No

 ** ExplicitIds **   <a name="DMS-Type-RedshiftSettings-ExplicitIds"></a>
This setting is only valid for a full-load migration task. Set `ExplicitIds` to `true` to have tables with `IDENTITY` columns override their auto-generated values with explicit values loaded from the source data files used to populate the tables. The default is `false`.
Type: Boolean
Required: No

 ** FileTransferUploadStreams **   <a name="DMS-Type-RedshiftSettings-FileTransferUploadStreams"></a>
The number of threads used to upload a single file. This parameter accepts a value from 1 through 64. It defaults to 10.
The number of parallel streams used to upload a single .csv file to an S3 bucket using S3 Multipart Upload. For more information, see [Multipart upload overview](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html).
 `FileTransferUploadStreams` accepts a value from 1 through 64. It defaults to 10.
Type: Integer
Required: No

 ** LoadTimeout **   <a name="DMS-Type-RedshiftSettings-LoadTimeout"></a>
The amount of time to wait (in seconds) before timing out of operations performed by AWS DMS on a Redshift cluster, such as Redshift COPY, INSERT, DELETE, and UPDATE.
Type: Integer
Required: No

 ** MapBooleanAsBoolean **   <a name="DMS-Type-RedshiftSettings-MapBooleanAsBoolean"></a>
When true, lets Redshift migrate the boolean type as boolean. By default, Redshift migrates booleans as `varchar(1)`. You must set this setting on both the source and target endpoints for it to take effect.
Type: Boolean
Required: No

 ** MaxFileSize **   <a name="DMS-Type-RedshiftSettings-MaxFileSize"></a>
The maximum size (in KB) of any .csv file used to load data on an S3 bucket and transfer data to Amazon Redshift. It defaults to 1048576KB (1 GB).
Type: Integer
Required: No

 ** Password **   <a name="DMS-Type-RedshiftSettings-Password"></a>
The password for the user named in the `username` property.
Type: String
Required: No

 ** Port **   <a name="DMS-Type-RedshiftSettings-Port"></a>
The port number for Amazon Redshift. The default value is 5439.
Type: Integer
Required: No

 ** RemoveQuotes **   <a name="DMS-Type-RedshiftSettings-RemoveQuotes"></a>
A value that specifies to remove surrounding quotation marks from strings in the incoming data. All characters within the quotation marks, including delimiters, are retained. Choose `true` to remove quotation marks. The default is `false`.
Type: Boolean
Required: No

 ** ReplaceChars **   <a name="DMS-Type-RedshiftSettings-ReplaceChars"></a>
A value that specifies to replaces the invalid characters specified in `ReplaceInvalidChars`, substituting the specified characters instead. The default is `"?"`.
Type: String
Required: No

 ** ReplaceInvalidChars **   <a name="DMS-Type-RedshiftSettings-ReplaceInvalidChars"></a>
A list of characters that you want to replace. Use with `ReplaceChars`.
Type: String
Required: No

 ** SecretsManagerAccessRoleArn **   <a name="DMS-Type-RedshiftSettings-SecretsManagerAccessRoleArn"></a>
The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret`. The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the AWS Secrets Manager secret that allows access to the Amazon Redshift endpoint.
You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId`. Or you can specify clear-text values for `UserName`, `Password`, `ServerName`, and `Port`. You can't specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access AWS Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the * AWS Database Migration Service User Guide*.
Type: String
Required: No

 ** SecretsManagerSecretId **   <a name="DMS-Type-RedshiftSettings-SecretsManagerSecretId"></a>
The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the Amazon Redshift endpoint connection details.
Type: String
Required: No

 ** ServerName **   <a name="DMS-Type-RedshiftSettings-ServerName"></a>
The name of the Amazon Redshift cluster you are using.
Type: String
Required: No

 ** ServerSideEncryptionKmsKeyId **   <a name="DMS-Type-RedshiftSettings-ServerSideEncryptionKmsKeyId"></a>
The AWS KMS key ID. If you are using `SSE_KMS` for the `EncryptionMode`, provide this key ID. The key that you use needs an attached policy that enables IAM user permissions and allows use of the key.
Type: String
Required: No

 ** ServiceAccessRoleArn **   <a name="DMS-Type-RedshiftSettings-ServiceAccessRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role that has access to the Amazon Redshift service. The role must allow the `iam:PassRole` action.
Type: String
Required: No

 ** TimeFormat **   <a name="DMS-Type-RedshiftSettings-TimeFormat"></a>
The time format that you want to use. Valid values are `auto` (case-sensitive), `'timeformat_string'`, `'epochsecs'`, or `'epochmillisecs'`. It defaults to 10. Using `auto` recognizes most strings, even some that aren't supported when you use a time format string.
If your date and time values use formats different from each other, set this parameter to `auto`.
Type: String
Required: No

 ** TrimBlanks **   <a name="DMS-Type-RedshiftSettings-TrimBlanks"></a>
A value that specifies to remove the trailing white space characters from a VARCHAR string. This parameter applies only to columns with a VARCHAR data type. Choose `true` to remove unneeded white space. The default is `false`.
Type: Boolean
Required: No

 ** TruncateColumns **   <a name="DMS-Type-RedshiftSettings-TruncateColumns"></a>
A value that specifies to truncate data in columns to the appropriate number of characters, so that the data fits in the column. This parameter applies only to columns with a VARCHAR or CHAR data type, and rows with a size of 4 MB or less. Choose `true` to truncate data. The default is `false`.
Type: Boolean
Required: No

 ** Username **   <a name="DMS-Type-RedshiftSettings-Username"></a>
An Amazon Redshift user name for a registered user.
Type: String
Required: No

 ** WriteBufferSize **   <a name="DMS-Type-RedshiftSettings-WriteBufferSize"></a>
The size (in KB) of the in-memory file write buffer used when generating .csv files on the local disk at the DMS replication instance. The default value is 1000 (buffer size is 1000KB).
Type: Integer
Required: No

## See Also
<a name="API_RedshiftSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/RedshiftSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/RedshiftSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/RedshiftSettings)
