---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-medialive-inputsecuritygroup-inputwhitelistrule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MediaLive::InputSecurityGroup InputWhitelistRule

Whitelist rule

## Syntax
<a name="aws-properties-medialive-inputsecuritygroup-inputwhitelistrule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-medialive-inputsecuritygroup-inputwhitelistrule-syntax.json"></a>

```json
{
  "[Cidr](#cfn-medialive-inputsecuritygroup-inputwhitelistrule-cidr)" : {{String}}
}
```

### YAML
<a name="aws-properties-medialive-inputsecuritygroup-inputwhitelistrule-syntax.yaml"></a>

```yaml
  [Cidr](#cfn-medialive-inputsecuritygroup-inputwhitelistrule-cidr): {{String}}
```

## Properties
<a name="aws-properties-medialive-inputsecuritygroup-inputwhitelistrule-properties"></a>

`Cidr`  <a name="cfn-medialive-inputsecuritygroup-inputwhitelistrule-cidr"></a>
The IPv4 CIDR that's whitelisted.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
