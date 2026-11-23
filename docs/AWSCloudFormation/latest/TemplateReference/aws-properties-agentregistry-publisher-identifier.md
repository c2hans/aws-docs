---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-agentregistry-publisher-identifier.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::Publisher Identifier

The `Identifier` structure contains the value that identifies a publisher. The only supported identifier type is a domain.

## Syntax
<a name="aws-properties-agentregistry-publisher-identifier-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-agentregistry-publisher-identifier-syntax.json"></a>

```json
{
  "[Domain](#cfn-agentregistry-publisher-identifier-domain)" : {{String}}
}
```

### YAML
<a name="aws-properties-agentregistry-publisher-identifier-syntax.yaml"></a>

```yaml
  [Domain](#cfn-agentregistry-publisher-identifier-domain): {{String}}
```

## Properties
<a name="aws-properties-agentregistry-publisher-identifier-properties"></a>

`Domain`  <a name="cfn-agentregistry-publisher-identifier-domain"></a>
The `Domain` property specifies the fully qualified domain name that the publisher proves ownership of. Specify at least two labels in lowercase, such as `example.com`. Agent Registry stores domain names in lowercase.
*Required*: Yes
*Type*: String
*Pattern*: `^([a-z0-9]([a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z]{2,63}$`
*Minimum*: `1`
*Maximum*: `253`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
