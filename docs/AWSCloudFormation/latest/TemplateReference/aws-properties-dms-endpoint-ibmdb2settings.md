---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dms-endpoint-ibmdb2settings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DMS::Endpoint IbmDb2Settings
<a name="aws-properties-dms-endpoint-ibmdb2settings"></a>

Provides information that defines an IBMDB2 endpoint. This information includes the output format of records applied to the endpoint and details of transaction and control table data information. For more information about other available settings, see [ Extra connection attributes when using Db2 LUW as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.DB2.html#CHAP_Source.DB2.ConnectionAttrib) in the *AWS Database Migration Service User Guide*.

## Syntax
<a name="aws-properties-dms-endpoint-ibmdb2settings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dms-endpoint-ibmdb2settings-syntax.json"></a>

```
{
  "[CurrentLsn](#cfn-dms-endpoint-ibmdb2settings-currentlsn)" : {{String}},
  "[KeepCsvFiles](#cfn-dms-endpoint-ibmdb2settings-keepcsvfiles)" : {{Boolean}},
  "[LoadTimeout](#cfn-dms-endpoint-ibmdb2settings-loadtimeout)" : {{Integer}},
  "[MaxFileSize](#cfn-dms-endpoint-ibmdb2settings-maxfilesize)" : {{Integer}},
  "[MaxKBytesPerRead](#cfn-dms-endpoint-ibmdb2settings-maxkbytesperread)" : {{Integer}},
  "[SecretsManagerAccessRoleArn](#cfn-dms-endpoint-ibmdb2settings-secretsmanageraccessrolearn)" : {{String}},
  "[SecretsManagerSecretId](#cfn-dms-endpoint-ibmdb2settings-secretsmanagersecretid)" : {{String}},
  "[SetDataCaptureChanges](#cfn-dms-endpoint-ibmdb2settings-setdatacapturechanges)" : {{Boolean}},
  "[WriteBufferSize](#cfn-dms-endpoint-ibmdb2settings-writebuffersize)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-dms-endpoint-ibmdb2settings-syntax.yaml"></a>

```
  [CurrentLsn](#cfn-dms-endpoint-ibmdb2settings-currentlsn): {{String}}
  [KeepCsvFiles](#cfn-dms-endpoint-ibmdb2settings-keepcsvfiles): {{Boolean}}
  [LoadTimeout](#cfn-dms-endpoint-ibmdb2settings-loadtimeout): {{Integer}}
  [MaxFileSize](#cfn-dms-endpoint-ibmdb2settings-maxfilesize): {{Integer}}
  [MaxKBytesPerRead](#cfn-dms-endpoint-ibmdb2settings-maxkbytesperread): {{Integer}}
  [SecretsManagerAccessRoleArn](#cfn-dms-endpoint-ibmdb2settings-secretsmanageraccessrolearn): {{String}}
  [SecretsManagerSecretId](#cfn-dms-endpoint-ibmdb2settings-secretsmanagersecretid): {{String}}
  [SetDataCaptureChanges](#cfn-dms-endpoint-ibmdb2settings-setdatacapturechanges): {{Boolean}}
  [WriteBufferSize](#cfn-dms-endpoint-ibmdb2settings-writebuffersize): {{Integer}}
```

## Properties
<a name="aws-properties-dms-endpoint-ibmdb2settings-properties"></a>

`CurrentLsn`  <a name="cfn-dms-endpoint-ibmdb2settings-currentlsn"></a>
For ongoing replication (CDC), use CurrentLSN to specify a log sequence number (LSN) where you want the replication to start.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeepCsvFiles`  <a name="cfn-dms-endpoint-ibmdb2settings-keepcsvfiles"></a>
If true, AWS DMS saves any .csv files to the Db2 LUW target that were used to replicate data. DMS uses these files for analysis and troubleshooting.
The default value is false.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LoadTimeout`  <a name="cfn-dms-endpoint-ibmdb2settings-loadtimeout"></a>
The amount of time (in milliseconds) before AWS DMS times out operations performed by DMS on the Db2 target. The default value is 1200 (20 minutes).
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxFileSize`  <a name="cfn-dms-endpoint-ibmdb2settings-maxfilesize"></a>
Specifies the maximum size (in KB) of .csv files used to transfer data to Db2 LUW.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxKBytesPerRead`  <a name="cfn-dms-endpoint-ibmdb2settings-maxkbytesperread"></a>
Maximum number of bytes per read, as a NUMBER value. The default is 64 KB.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretsManagerAccessRoleArn`  <a name="cfn-dms-endpoint-ibmdb2settings-secretsmanageraccessrolearn"></a>
The full Amazon Resource Name (ARN) of the IAM role that specifies AWS DMS as the trusted entity and grants the required permissions to access the value in `SecretsManagerSecret`. The role must allow the `iam:PassRole` action. `SecretsManagerSecret` has the value ofthe AWS Secrets Manager secret that allows access to the Db2 LUW endpoint.
You can specify one of two sets of values for these permissions. You can specify the values for this setting and `SecretsManagerSecretId`. Or you can specify clear-text values for `UserName`, `Password`, `ServerName`, and `Port`. You can't specify both.
For more information on creating this `SecretsManagerSecret`, the corresponding `SecretsManagerAccessRoleArn`, and the `SecretsManagerSecretId` that is required to access it, see [ Using secrets to access AWS Database Migration Service resources](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Security.html#security-iam-secretsmanager) in the *AWS Database Migration Service User Guide*.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecretsManagerSecretId`  <a name="cfn-dms-endpoint-ibmdb2settings-secretsmanagersecretid"></a>
The full ARN, partial ARN, or display name of the `SecretsManagerSecret` that contains the IBMDB2 endpoint connection details.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SetDataCaptureChanges`  <a name="cfn-dms-endpoint-ibmdb2settings-setdatacapturechanges"></a>
Enables ongoing replication (CDC) as a BOOLEAN value. The default is true.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WriteBufferSize`  <a name="cfn-dms-endpoint-ibmdb2settings-writebuffersize"></a>
The size (in KB) of the in-memory file write buffer used when generating .csv files on the local disk on the DMS replication instance. The default value is 1024 (1 MB).
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
