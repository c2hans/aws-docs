---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_IBMDb2Settings.html
---

# IBMDb2Settings
<a name="API_IBMDb2Settings"></a>

Provides information that defines an IBM Db2 LUW endpoint.

## Contents
<a name="API_IBMDb2Settings_Contents"></a>

 ** CurrentLsn **   <a name="DMS-Type-IBMDb2Settings-CurrentLsn"></a>
For ongoing replication (CDC), use CurrentLSN to specify a log sequence number (LSN) where you want the replication to start.
Type: String
Required: No

 ** DatabaseName **   <a name="DMS-Type-IBMDb2Settings-DatabaseName"></a>
Database name for the endpoint.
Type: String
Required: No

 ** KeepCsvFiles **   <a name="DMS-Type-IBMDb2Settings-KeepCsvFiles"></a>
If true, AWS DMS saves any .csv files to the Db2 LUW target that were used to replicate data. DMS uses these files for analysis and troubleshooting.
The default value is false.
Type: Boolean
Required: No

 ** LoadTimeout **   <a name="DMS-Type-IBMDb2Settings-LoadTimeout"></a>
The amount of time (in milliseconds) before AWS DMS times out operations performed by DMS on the Db2 target. The default value is 1200 (20 minutes).
Type: Integer
Required: No

 ** MaxFileSize **   <a name="DMS-Type-IBMDb2Settings-MaxFileSize"></a>
Specifies the maximum size (in KB) of .csv files used to transfer data to Db2 LUW.
Type: Integer
Required: No

 ** MaxKBytesPerRead **   <a name="DMS-Type-IBMDb2Settings-MaxKBytesPerRead"></a>
Maximum number of bytes per read, as a NUMBER value. The default is 64 KB.
Type: Integer
Required: No

 ** Password **   <a name="DMS-Type-IBMDb2Settings-Password"></a>
Endpoint connection password.
Type: String
Required: No

 ** Port **   <a name="DMS-Type-IBMDb2Settings-Port"></a>
Endpoint TCP port. The default value is 50000.
Type: Integer
Required: No

 ** SecretsManagerAccessRoleArn **   <a name="DMS-Type-IBMDb2Settings-SecretsManagerAccessRoleArn"></a>
The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret`. The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value of the AWS Secrets Manager secret that allows access to the Db2 LUW endpoint.
You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId`. Or you can specify clear-text values for `UserName`, `Password`, `ServerName`, and `Port`. You can't specify both. For more information on creating this `SecretsManagerSecret` and the `SecretsManagerAccessRoleArn` and `SecretsManagerSecretId` required to access it, see [Using secrets to access AWS Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the * AWS Database Migration Service User Guide*.
Type: String
Required: No

 ** SecretsManagerSecretId **   <a name="DMS-Type-IBMDb2Settings-SecretsManagerSecretId"></a>
The full ARN, partial ARN, or friendly name of the `SecretsManagerSecret` that contains the Db2 LUW endpoint connection details.
Type: String
Required: No

 ** ServerName **   <a name="DMS-Type-IBMDb2Settings-ServerName"></a>
Fully qualified domain name of the endpoint.
Type: String
Required: No

 ** SetDataCaptureChanges **   <a name="DMS-Type-IBMDb2Settings-SetDataCaptureChanges"></a>
Enables ongoing replication (CDC) as a BOOLEAN value. The default is true.
Type: Boolean
Required: No

 ** Username **   <a name="DMS-Type-IBMDb2Settings-Username"></a>
Endpoint connection user name.
Type: String
Required: No

 ** WriteBufferSize **   <a name="DMS-Type-IBMDb2Settings-WriteBufferSize"></a>
The size (in KB) of the in-memory file write buffer used when generating .csv files on the local disk on the DMS replication instance. The default value is 1024 (1 MB).
Type: Integer
Required: No

## See Also
<a name="API_IBMDb2Settings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/IBMDb2Settings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/IBMDb2Settings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/IBMDb2Settings)
