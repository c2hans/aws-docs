---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-interconnect-connection-remoteaccount.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Interconnect::Connection RemoteAccount
<a name="aws-properties-interconnect-connection-remoteaccount"></a>

The remote account identifier for the connection.

## Syntax
<a name="aws-properties-interconnect-connection-remoteaccount-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-interconnect-connection-remoteaccount-syntax.json"></a>

```
{
  "[Identifier](#cfn-interconnect-connection-remoteaccount-identifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-interconnect-connection-remoteaccount-syntax.yaml"></a>

```
  [Identifier](#cfn-interconnect-connection-remoteaccount-identifier): {{String}}
```

## Properties
<a name="aws-properties-interconnect-connection-remoteaccount-properties"></a>

`Identifier`  <a name="cfn-interconnect-connection-remoteaccount-identifier"></a>
The identifier of the remote account.
*Required*: Yes
*Type*: String
*Pattern*: `^[-a-zA-Z0-9_@\.]+$`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
