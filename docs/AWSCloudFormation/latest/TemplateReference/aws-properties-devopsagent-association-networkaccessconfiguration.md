---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-devopsagent-association-networkaccessconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DevOpsAgent::Association NetworkAccessConfiguration

Specifies how AWS DevOps Agent reaches your application through a release management environment. Specify exactly one access type.

## Syntax
<a name="aws-properties-devopsagent-association-networkaccessconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-devopsagent-association-networkaccessconfiguration-syntax.json"></a>

```json
{
  "[PrivateAccess](#cfn-devopsagent-association-networkaccessconfiguration-privateaccess)" : {{PrivateNetworkAccess}}
}
```

### YAML
<a name="aws-properties-devopsagent-association-networkaccessconfiguration-syntax.yaml"></a>

```yaml
  [PrivateAccess](#cfn-devopsagent-association-networkaccessconfiguration-privateaccess): {{
    PrivateNetworkAccess}}
```

## Properties
<a name="aws-properties-devopsagent-association-networkaccessconfiguration-properties"></a>

`PrivateAccess`  <a name="cfn-devopsagent-association-networkaccessconfiguration-privateaccess"></a>
Private network access to your application inside a VPC. AWS DevOps Agent reaches the application through a private connection.
*Required*: Yes
*Type*: [PrivateNetworkAccess](aws-properties-devopsagent-association-privatenetworkaccess.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
