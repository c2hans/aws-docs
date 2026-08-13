---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-transfer-connector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::Connector
<a name="aws-resource-transfer-connector"></a>

Creates the connector, which captures the parameters for a connection for the AS2 or SFTP protocol. For AS2, the connector is required for sending files to an externally hosted AS2 server. For SFTP, the connector is required when sending files to an SFTP server or receiving files from an SFTP server. For more details about connectors, see [Configure AS2 connectors](https://docs.aws.amazon.com/transfer/latest/userguide/configure-as2-connector.html) and [Create SFTP connectors](https://docs.aws.amazon.com/transfer/latest/userguide/configure-sftp-connector.html).

**Note**
You must specify exactly one configuration object: either for AS2 (`As2Config`) or SFTP (`SftpConfig`).

## Syntax
<a name="aws-resource-transfer-connector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-transfer-connector-syntax.json"></a>

```
{
  "Type" : "AWS::Transfer::Connector",
  "Properties" : {
      "[AccessRole](#cfn-transfer-connector-accessrole)" : {{String}},
      "[As2Config](#cfn-transfer-connector-as2config)" : {{As2Config}},
      "[EgressConfig](#cfn-transfer-connector-egressconfig)" : {{ConnectorEgressConfig}},
      "[EgressType](#cfn-transfer-connector-egresstype)" : {{String}},
      "[IpAddressType](#cfn-transfer-connector-ipaddresstype)" : {{String}},
      "[LoggingRole](#cfn-transfer-connector-loggingrole)" : {{String}},
      "[SecurityPolicyName](#cfn-transfer-connector-securitypolicyname)" : {{String}},
      "[SftpConfig](#cfn-transfer-connector-sftpconfig)" : {{SftpConfig}},
      "[Tags](#cfn-transfer-connector-tags)" : {{[ Tag, ... ]}},
      "[Url](#cfn-transfer-connector-url)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-transfer-connector-syntax.yaml"></a>

```
Type: AWS::Transfer::Connector
Properties:
  [AccessRole](#cfn-transfer-connector-accessrole): {{String}}
  [As2Config](#cfn-transfer-connector-as2config): {{
    As2Config}}
  [EgressConfig](#cfn-transfer-connector-egressconfig): {{
    ConnectorEgressConfig}}
  [EgressType](#cfn-transfer-connector-egresstype): {{String}}
  [IpAddressType](#cfn-transfer-connector-ipaddresstype): {{String}}
  [LoggingRole](#cfn-transfer-connector-loggingrole): {{String}}
  [SecurityPolicyName](#cfn-transfer-connector-securitypolicyname): {{String}}
  [SftpConfig](#cfn-transfer-connector-sftpconfig): {{
    SftpConfig}}
  [Tags](#cfn-transfer-connector-tags): {{
    - Tag}}
  [Url](#cfn-transfer-connector-url): {{String}}
```

## Properties
<a name="aws-resource-transfer-connector-properties"></a>

`AccessRole`  <a name="cfn-transfer-connector-accessrole"></a>
Connectors are used to send files using either the AS2 or SFTP protocol. For the access role, provide the Amazon Resource Name (ARN) of the AWS Identity and Access Management role to use.
 **For AS2 connectors**
With AS2, you can send files by calling `StartFileTransfer` and specifying the file paths in the request parameter, `SendFilePaths`. We use the file’s parent directory (for example, for `--send-file-paths /bucket/dir/file.txt`, parent directory is `/bucket/dir/`) to temporarily store a processed AS2 message file, store the MDN when we receive them from the partner, and write a final JSON file containing relevant metadata of the transmission. So, the `AccessRole` needs to provide read and write access to the parent directory of the file location used in the `StartFileTransfer` request. Additionally, you need to provide read and write access to the parent directory of the files that you intend to send with `StartFileTransfer`.
If you are using Basic authentication for your AS2 connector, the access role requires the `secretsmanager:GetSecretValue` permission for the secret. If the secret is encrypted using a customer-managed key instead of the AWS managed key in Secrets Manager, then the role also needs the `kms:Decrypt` permission for that key.
 **For SFTP connectors**
Make sure that the access role provides read and write access to the parent directory of the file location that's used in the `StartFileTransfer` request. Additionally, make sure that the role provides `secretsmanager:GetSecretValue` permission to AWS Secrets Manager.
*Required*: Yes
*Type*: String
*Pattern*: `arn:.*role/.*`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`As2Config`  <a name="cfn-transfer-connector-as2config"></a>
A structure that contains the parameters for an AS2 connector object.
*Required*: No
*Type*: [As2Config](aws-properties-transfer-connector-as2config.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EgressConfig`  <a name="cfn-transfer-connector-egressconfig"></a>
Current egress configuration of the connector, showing how traffic is routed to the SFTP server. Contains VPC Lattice settings when using VPC\_LATTICE egress type.
When using the VPC\_LATTICE egress type, AWS Transfer Family uses a managed Service Network to simplify the resource sharing process.
*Required*: No
*Type*: [ConnectorEgressConfig](aws-properties-transfer-connector-connectoregressconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EgressType`  <a name="cfn-transfer-connector-egresstype"></a>
Type of egress configuration for the connector. SERVICE\_MANAGED uses Transfer Family managed NAT gateways, while VPC\_LATTICE routes traffic through customer VPCs using VPC Lattice.
*Required*: No
*Type*: String
*Allowed values*: `SERVICE_MANAGED | VPC_LATTICE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpAddressType`  <a name="cfn-transfer-connector-ipaddresstype"></a>
IP address type for the connector's network connections. When set to `IPV4`, the connector uses IPv4 addresses only. When set to `DUALSTACK`, the connector supports both IPv4 and IPv6 addresses, with IPv6 preferred when available.
*Required*: No
*Type*: String
*Allowed values*: `IPV4 | DUALSTACK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LoggingRole`  <a name="cfn-transfer-connector-loggingrole"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows a connector to turn on CloudWatch logging for Amazon S3 events. When set, you can view connector activity in your CloudWatch logs.
*Required*: No
*Type*: String
*Pattern*: `arn:.*role/.*`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityPolicyName`  <a name="cfn-transfer-connector-securitypolicyname"></a>
The text name of the security policy for the specified connector.
*Required*: No
*Type*: String
*Pattern*: `TransferSFTPConnectorSecurityPolicy-[A-Za-z0-9-]+`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SftpConfig`  <a name="cfn-transfer-connector-sftpconfig"></a>
A structure that contains the parameters for an SFTP connector object.
*Required*: No
*Type*: [SftpConfig](aws-properties-transfer-connector-sftpconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-transfer-connector-tags"></a>
Key-value pairs that can be used to group and search for connectors.
*Required*: No
*Type*: Array of [Tag](aws-properties-transfer-connector-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Url`  <a name="cfn-transfer-connector-url"></a>
The URL of the partner's AS2 or SFTP endpoint.
When creating AS2 connectors or service-managed SFTP connectors (connectors without egress configuration), you must provide a URL to specify the remote server endpoint. For VPC Lattice type connectors, the URL must be null.
*Required*: No
*Type*: String
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-transfer-connector-return-values"></a>

### Fn::GetAtt
<a name="aws-resource-transfer-connector-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-transfer-connector-return-values-fn--getatt-fn--getatt"></a>

`ConnectorId`  <a name="ConnectorId-fn::getatt"></a>
The service-assigned ID of the connector that is created.

`ErrorMessage`  <a name="ErrorMessage-fn::getatt"></a>
Error message providing details when the connector is in ERRORED status. Contains information to help troubleshoot connector creation or operation failures.

`ServiceManagedEgressIpAddresses`  <a name="ServiceManagedEgressIpAddresses-fn::getatt"></a>
The list of egress IP addresses of this connector. These IP addresses are assigned automatically when you create the connector.

`Status`  <a name="Status-fn::getatt"></a>
Current status of the connector. PENDING indicates creation/update in progress, ACTIVE means ready for operations, and ERRORED indicates a failure requiring attention.
