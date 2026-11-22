---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53-hostedzone-changeguardrail.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53::HostedZone ChangeGuardrail

<a name="aws-properties-route53-hostedzone-changeguardrail-description"></a>The `ChangeGuardrail` property type specifies Property description not available. for an [AWS::Route53::HostedZone](aws-resource-route53-hostedzone.md).

## Syntax
<a name="aws-properties-route53-hostedzone-changeguardrail-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-route53-hostedzone-changeguardrail-syntax.json"></a>

```json
{
  "[Name](#cfn-route53-hostedzone-changeguardrail-name)" : {{String}},
  "[Status](#cfn-route53-hostedzone-changeguardrail-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-route53-hostedzone-changeguardrail-syntax.yaml"></a>

```yaml
  [Name](#cfn-route53-hostedzone-changeguardrail-name): {{String}}
  [Status](#cfn-route53-hostedzone-changeguardrail-status): {{String}}
```

## Properties
<a name="aws-properties-route53-hostedzone-changeguardrail-properties"></a>

`Name`  <a name="cfn-route53-hostedzone-changeguardrail-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `NS_OCCLUSION_CHECK | ALIAS_TARGET_CHECK | ACTIVE_RECORD_CHECK | ACTIVE_DELEGATION_CHECK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-route53-hostedzone-changeguardrail-status"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
