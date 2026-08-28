---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-devopsagent-privateconnection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::PrivateConnection
<a name="aws-resource-devopsagent-privateconnection"></a>

The `AWS::DevOpsAgent::PrivateConnection` resource specifies a private connection that provides a secure network path between the AWS DevOps Agent service and a target resource in your VPC.

Private connections are account-level resources that you can reuse across multiple integrations and Agent Spaces that reach the same host.

## Syntax
<a name="aws-resource-devopsagent-privateconnection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-devopsagent-privateconnection-syntax.json"></a>

```
{
  "Type" : "AWS::DevOpsAgent::PrivateConnection",
  "Properties" : {
      "[Certificate](#cfn-devopsagent-privateconnection-certificate)" : {{String}},
      "[ConnectionConfiguration](#cfn-devopsagent-privateconnection-connectionconfiguration)" : {{ConnectionConfiguration}},
      "[Name](#cfn-devopsagent-privateconnection-name)" : {{String}},
      "[Tags](#cfn-devopsagent-privateconnection-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-devopsagent-privateconnection-syntax.yaml"></a>

```
Type: AWS::DevOpsAgent::PrivateConnection
Properties:
  [Certificate](#cfn-devopsagent-privateconnection-certificate): {{String}}
  [ConnectionConfiguration](#cfn-devopsagent-privateconnection-connectionconfiguration): {{
    ConnectionConfiguration}}
  [Name](#cfn-devopsagent-privateconnection-name): {{String}}
  [Tags](#cfn-devopsagent-privateconnection-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-devopsagent-privateconnection-properties"></a>

`Certificate`  <a name="cfn-devopsagent-privateconnection-certificate"></a>
The PEM-encoded certificate chain of the target service. Required when a private certificate authority issues the TLS certificate of the target service.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `32768`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ConnectionConfiguration`  <a name="cfn-devopsagent-privateconnection-connectionconfiguration"></a>
The connection configuration, which determines whether AWS DevOps Agent manages the underlying Amazon VPC Lattice resources or you provide your own.
*Required*: Yes
*Type*: [ConnectionConfiguration](aws-properties-devopsagent-privateconnection-connectionconfiguration.md)
*Update requires*: Updates are not supported.

`Name`  <a name="cfn-devopsagent-privateconnection-name"></a>
The unique name of the private connection within your account.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9]([a-z0-9-]*[a-z0-9])?$`
*Minimum*: `3`
*Maximum*: `30`
*Update requires*: Updates are not supported.

`Tags`  <a name="cfn-devopsagent-privateconnection-tags"></a>
An array of key-value pairs to apply to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-devopsagent-privateconnection-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-devopsagent-privateconnection-return-values"></a>

### Ref
<a name="aws-resource-devopsagent-privateconnection-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the private connection.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-devopsagent-privateconnection-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-devopsagent-privateconnection-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the private connection.

`CertificateExpiryTime`  <a name="CertificateExpiryTime-fn::getatt"></a>
The timestamp when the certificate associated with the private connection expires.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the private connection.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
