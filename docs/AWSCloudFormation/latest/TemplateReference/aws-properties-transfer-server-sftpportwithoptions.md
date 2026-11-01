---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-transfer-server-sftpportwithoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::Server SftpPortWithOptions
<a name="aws-properties-transfer-server-sftpportwithoptions"></a>

Specifies the configuration for a single SFTP port on a Transfer Family server that uses the SFTP protocol and has a `PUBLIC` endpoint. Each entry in the `SftpPorts` list is an `SftpPortWithOptions` object that pairs a port number with a communication mode.

## Syntax
<a name="aws-properties-transfer-server-sftpportwithoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-transfer-server-sftpportwithoptions-syntax.json"></a>

```
{
  "[CommunicationMode](#cfn-transfer-server-sftpportwithoptions-communicationmode)" : {{String}},
  "[SftpPort](#cfn-transfer-server-sftpportwithoptions-sftpport)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-transfer-server-sftpportwithoptions-syntax.yaml"></a>

```
  [CommunicationMode](#cfn-transfer-server-sftpportwithoptions-communicationmode): {{String}}
  [SftpPort](#cfn-transfer-server-sftpportwithoptions-sftpport): {{Integer}}
```

## Properties
<a name="aws-properties-transfer-server-sftpportwithoptions-properties"></a>

`CommunicationMode`  <a name="cfn-transfer-server-sftpportwithoptions-communicationmode"></a>
Determines whether the server or the client sends data first when a client establishes an SFTP connection on this port. Valid values are `SERVER_TALK_FIRST` and `CLIENT_TALK_FIRST`. For a description of each mode, see the `SftpPorts` property. This value is optional.
*Required*: No
*Type*: String
*Allowed values*: `CLIENT_TALK_FIRST | SERVER_TALK_FIRST`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`SftpPort`  <a name="cfn-transfer-server-sftpportwithoptions-sftpport"></a>
The port on which the Transfer Family server listens for SFTP connections. Specify any integer from 2000 to 65535, or 22. This value is required for each entry in the `SftpPorts` list.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)
