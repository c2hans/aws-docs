---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datasync-locationhdfs.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationHDFS
<a name="aws-resource-datasync-locationhdfs"></a>

The `AWS::DataSync::LocationHDFS` resource specifies an endpoint for a Hadoop Distributed File System (HDFS).

## Syntax
<a name="aws-resource-datasync-locationhdfs-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-datasync-locationhdfs-syntax.json"></a>

```
{
  "Type" : "AWS::DataSync::LocationHDFS",
  "Properties" : {
      "[AgentArns](#cfn-datasync-locationhdfs-agentarns)" : {{[ String, ... ]}},
      "[AuthenticationType](#cfn-datasync-locationhdfs-authenticationtype)" : {{String}},
      "[BlockSize](#cfn-datasync-locationhdfs-blocksize)" : {{Integer}},
      "[CmkSecretConfig](#cfn-datasync-locationhdfs-cmksecretconfig)" : {{CmkSecretConfig}},
      "[CustomSecretConfig](#cfn-datasync-locationhdfs-customsecretconfig)" : {{CustomSecretConfig}},
      "[KerberosKeytab](#cfn-datasync-locationhdfs-kerberoskeytab)" : {{String}},
      "[KerberosKrb5Conf](#cfn-datasync-locationhdfs-kerberoskrb5conf)" : {{String}},
      "[KerberosPrincipal](#cfn-datasync-locationhdfs-kerberosprincipal)" : {{String}},
      "[KmsKeyProviderUri](#cfn-datasync-locationhdfs-kmskeyprovideruri)" : {{String}},
      "[NameNodes](#cfn-datasync-locationhdfs-namenodes)" : {{[ NameNode, ... ]}},
      "[QopConfiguration](#cfn-datasync-locationhdfs-qopconfiguration)" : {{QopConfiguration}},
      "[ReplicationFactor](#cfn-datasync-locationhdfs-replicationfactor)" : {{Integer}},
      "[SimpleUser](#cfn-datasync-locationhdfs-simpleuser)" : {{String}},
      "[Subdirectory](#cfn-datasync-locationhdfs-subdirectory)" : {{String}},
      "[Tags](#cfn-datasync-locationhdfs-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-datasync-locationhdfs-syntax.yaml"></a>

```
Type: AWS::DataSync::LocationHDFS
Properties:
  [AgentArns](#cfn-datasync-locationhdfs-agentarns): {{
    - String}}
  [AuthenticationType](#cfn-datasync-locationhdfs-authenticationtype): {{String}}
  [BlockSize](#cfn-datasync-locationhdfs-blocksize): {{Integer}}
  [CmkSecretConfig](#cfn-datasync-locationhdfs-cmksecretconfig): {{
    CmkSecretConfig}}
  [CustomSecretConfig](#cfn-datasync-locationhdfs-customsecretconfig): {{
    CustomSecretConfig}}
  [KerberosKeytab](#cfn-datasync-locationhdfs-kerberoskeytab): {{String}}
  [KerberosKrb5Conf](#cfn-datasync-locationhdfs-kerberoskrb5conf): {{String}}
  [KerberosPrincipal](#cfn-datasync-locationhdfs-kerberosprincipal): {{String}}
  [KmsKeyProviderUri](#cfn-datasync-locationhdfs-kmskeyprovideruri): {{String}}
  [NameNodes](#cfn-datasync-locationhdfs-namenodes): {{
    - NameNode}}
  [QopConfiguration](#cfn-datasync-locationhdfs-qopconfiguration): {{
    QopConfiguration}}
  [ReplicationFactor](#cfn-datasync-locationhdfs-replicationfactor): {{Integer}}
  [SimpleUser](#cfn-datasync-locationhdfs-simpleuser): {{String}}
  [Subdirectory](#cfn-datasync-locationhdfs-subdirectory): {{String}}
  [Tags](#cfn-datasync-locationhdfs-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-datasync-locationhdfs-properties"></a>

`AgentArns`  <a name="cfn-datasync-locationhdfs-agentarns"></a>
The Amazon Resource Names (ARNs) of the DataSync agents that can connect to your HDFS cluster.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `128 | 8`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthenticationType`  <a name="cfn-datasync-locationhdfs-authenticationtype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `SIMPLE | KERBEROS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BlockSize`  <a name="cfn-datasync-locationhdfs-blocksize"></a>
The size of data blocks to write into the HDFS cluster. The block size must be a multiple of 512 bytes. The default block size is 128 mebibytes (MiB).
*Required*: No
*Type*: Integer
*Minimum*: `1048576`
*Maximum*: `1073741824`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CmkSecretConfig`  <a name="cfn-datasync-locationhdfs-cmksecretconfig"></a>
Specifies configuration information for a DataSync-managed secret, such as an authentication token, secret key, password, or Kerberos keytab that DataSync uses to access a specific storage location, with a customer-managed AWS KMS key.
You can use either `CmkSecretConfig` or `CustomSecretConfig` to provide credentials for a `CreateLocation` request. Do not provide both parameters for the same request.
*Required*: No
*Type*: [CmkSecretConfig](aws-properties-datasync-locationhdfs-cmksecretconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomSecretConfig`  <a name="cfn-datasync-locationhdfs-customsecretconfig"></a>
Specifies configuration information for a customer-managed Secrets Manager secret where a storage location credentials is stored in Secrets Manager as plain text (for authentication token, secret key, or password) or as binary (for Kerberos keytab). This configuration includes the secret ARN, and the ARN for an IAM role that provides access to the secret.
You can use either `CmkSecretConfig` or `CustomSecretConfig` to provide credentials for a `CreateLocation` request. Do not provide both parameters for the same request.
*Required*: No
*Type*: [CustomSecretConfig](aws-properties-datasync-locationhdfs-customsecretconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KerberosKeytab`  <a name="cfn-datasync-locationhdfs-kerberoskeytab"></a>
The Kerberos key table (keytab) that contains mappings between the defined Kerberos principal and the encrypted keys. Provide the base64-encoded file text. If `KERBEROS` is specified for `AuthType`, this value is required.
*Required*: No
*Type*: String
*Maximum*: `87384`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KerberosKrb5Conf`  <a name="cfn-datasync-locationhdfs-kerberoskrb5conf"></a>
The `krb5.conf` file that contains the Kerberos configuration information. You can load the `krb5.conf` by providing a string of the file's contents or an Amazon S3 presigned URL of the file. If`KERBEROS` is specified for `AuthType`, this value is required.
*Required*: No
*Type*: String
*Maximum*: `174764`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KerberosPrincipal`  <a name="cfn-datasync-locationhdfs-kerberosprincipal"></a>
The Kerberos principal with access to the files and folders on the HDFS cluster.
If `KERBEROS` is specified for `AuthenticationType`, this parameter is required.
*Required*: No
*Type*: String
*Pattern*: `^.+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyProviderUri`  <a name="cfn-datasync-locationhdfs-kmskeyprovideruri"></a>
The URI of the HDFS cluster's Key Management Server (KMS).
*Required*: No
*Type*: String
*Pattern*: `^kms:\/\/http[s]?@(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-]*[A-Za-z0-9])(;(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-]*[A-Za-z0-9]))*:[0-9]{1,5}\/kms$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NameNodes`  <a name="cfn-datasync-locationhdfs-namenodes"></a>
The NameNode that manages the HDFS namespace. The NameNode performs operations such as opening, closing, and renaming files and directories. The NameNode contains the information to map blocks of data to the DataNodes.
The number of NameNodes you can specify depends on the task mode:
+ **Enhanced mode** – You can specify multiple NameNodes for HDFS High Availability (HA) configurations.
+ **Basic mode** – You can specify only one NameNode.
*Required*: Yes
*Type*: Array of [NameNode](aws-properties-datasync-locationhdfs-namenode.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`QopConfiguration`  <a name="cfn-datasync-locationhdfs-qopconfiguration"></a>
The Quality of Protection (QOP) configuration specifies the Remote Procedure Call (RPC) and data transfer protection settings configured on the Hadoop Distributed File System (HDFS) cluster. If `QopConfiguration` isn't specified, `RpcProtection` and `DataTransferProtection` default to `PRIVACY`. If you set `RpcProtection` or `DataTransferProtection`, the other parameter assumes the same value.
*Required*: No
*Type*: [QopConfiguration](aws-properties-datasync-locationhdfs-qopconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReplicationFactor`  <a name="cfn-datasync-locationhdfs-replicationfactor"></a>
The number of DataNodes to replicate the data to when writing to the HDFS cluster. By default, data is replicated to three DataNodes.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SimpleUser`  <a name="cfn-datasync-locationhdfs-simpleuser"></a>
The user name used to identify the client on the host operating system.
If `SIMPLE` is specified for `AuthenticationType`, this parameter is required.
*Required*: No
*Type*: String
*Pattern*: `^[_.A-Za-z0-9][-_.A-Za-z0-9]*$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subdirectory`  <a name="cfn-datasync-locationhdfs-subdirectory"></a>
A subdirectory in the HDFS cluster. This subdirectory is used to read data from or write data to the HDFS cluster. If the subdirectory isn't specified, it will default to `/`.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-\+\./\(\)\$\p{Zs}]+$`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-datasync-locationhdfs-tags"></a>
The key-value pair that represents the tag that you want to add to the location. The value can be an empty string. We recommend using tags to name your resources.
*Required*: No
*Type*: Array of [Tag](aws-properties-datasync-locationhdfs-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-datasync-locationhdfs-return-values"></a>

### Ref
<a name="aws-resource-datasync-locationhdfs-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the location resource ARN. For example:

 `arn:aws:datasync:us-east-2:111222333444:location/loc-07db7abfc326c50s3`

For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-datasync-locationhdfs-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-datasync-locationhdfs-return-values-fn--getatt-fn--getatt"></a>

`CmkSecretConfig.SecretArn`  <a name="CmkSecretConfig.SecretArn-fn::getatt"></a>
Property description not available.

`LocationArn`  <a name="LocationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the HDFS cluster location to describe.

`LocationUri`  <a name="LocationUri-fn::getatt"></a>
The URI of the HDFS cluster location.
