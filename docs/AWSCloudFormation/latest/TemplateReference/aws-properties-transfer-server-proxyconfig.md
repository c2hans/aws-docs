---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-transfer-server-proxyconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::Server ProxyConfig
<a name="aws-properties-transfer-server-proxyconfig"></a>

Contains configuration for PROXY protocol version 2 (PPv2) support on an AWS Transfer Family server. When enabled, Transfer Family reads the added PPv2 header from incoming connections to extract the client's source IP address. This address is then available in Amazon CloudWatch Logs entries and is passed to custom identity providers during authentication, enabling IP-based access policies. For more information, see [Working with Network Load Balancers](https://docs.aws.amazon.com/transfer/latest/userguide/working-with-nlb.html).

## Syntax
<a name="aws-properties-transfer-server-proxyconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-transfer-server-proxyconfig-syntax.json"></a>

```
{
  "[SftpMode](#cfn-transfer-server-proxyconfig-sftpmode)" : {{String}}
}
```

### YAML
<a name="aws-properties-transfer-server-proxyconfig-syntax.yaml"></a>

```
  [SftpMode](#cfn-transfer-server-proxyconfig-sftpmode): {{String}}
```

## Properties
<a name="aws-properties-transfer-server-proxyconfig-properties"></a>

`SftpMode`  <a name="cfn-transfer-server-proxyconfig-sftpmode"></a>
Specifies whether the Transfer Family server requires or ignores a PPv2 header containing the client's source IP address on incoming SFTP connections. If you don't specify a value, the default is `NONE`
+ `NONE`: the server reads and ignores any PPv2 header on incoming SFTP connections. This is the default value. Use this value when your SFTP server is not behind an NLB, or when you do not need to preserve the client's source IP address through an NLB.
+ `PROXY_PROTOCOL_V2_ENFORCED`: the server requires a valid PPv2 header on every incoming SFTP connection. When a valid header is present, the server applies it and uses the source IP address from the header. If a connection arrives without a PPv2 header, the server refuses the connection and logs an error to Amazon CloudWatch Logs indicating that the expected PPv2 header was missing. Use this value when your SFTP server is behind an NLB with PPv2 enabled on the target group.
**Important**
With `PROXY_PROTOCOL_V2_ENFORCED` you must restrict the server's VPC endpoint security group to allow inbound traffic only via the trusted NLB. For more information, see [Working with Network Load Balancers](https://docs.aws.amazon.com/transfer/latest/userguide/working-with-nlb.html).
*Required*: No
*Type*: String
*Allowed values*: `PROXY_PROTOCOL_V2_ENFORCED | NONE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
