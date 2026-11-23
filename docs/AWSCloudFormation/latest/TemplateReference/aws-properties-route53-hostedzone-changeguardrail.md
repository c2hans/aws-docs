---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53-hostedzone-changeguardrail.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53::HostedZone ChangeGuardrail

A Change Guardrail setting for a hosted zone. When a guardrail is enabled, Route 53 blocks the corresponding change.

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
The name of the Change Guardrail. Valid values are `NS_OCCLUSION_CHECK`, `ALIAS_TARGET_CHECK`, `ACTIVE_RECORD_CHECK`, and `ACTIVE_DELEGATION_CHECK`. `NS_OCCLUSION_CHECK` is available on both the standard and advanced tiers; the other values are available only on the advanced tier.
*Required*: Yes
*Type*: String
*Allowed values*: `NS_OCCLUSION_CHECK | ALIAS_TARGET_CHECK | ACTIVE_RECORD_CHECK | ACTIVE_DELEGATION_CHECK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-route53-hostedzone-changeguardrail-status"></a>
The status of the Change Guardrail. `ENABLED` makes Route 53 block the corresponding change; `DISABLED` turns the guardrail off.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
