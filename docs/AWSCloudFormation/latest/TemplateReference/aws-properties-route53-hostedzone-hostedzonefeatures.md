---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53-hostedzone-hostedzonefeatures.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53::HostedZone HostedZoneFeatures

Represents the features configuration for a hosted zone, including the status of various features and any associated failure reasons.

## Syntax
<a name="aws-properties-route53-hostedzone-hostedzonefeatures-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-route53-hostedzone-hostedzonefeatures-syntax.json"></a>

```json
{
  "[ChangeGuardrails](#cfn-route53-hostedzone-hostedzonefeatures-changeguardrails)" : {{[ ChangeGuardrail, ... ]}},
  "[ChangeHistory](#cfn-route53-hostedzone-hostedzonefeatures-changehistory)" : {{ChangeHistory}},
  "[EnableAcceleratedRecovery](#cfn-route53-hostedzone-hostedzonefeatures-enableacceleratedrecovery)" : {{Boolean}},
  "[EnablePublicDNSFallback](#cfn-route53-hostedzone-hostedzonefeatures-enablepublicdnsfallback)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-route53-hostedzone-hostedzonefeatures-syntax.yaml"></a>

```yaml
  [ChangeGuardrails](#cfn-route53-hostedzone-hostedzonefeatures-changeguardrails): {{
    - ChangeGuardrail}}
  [ChangeHistory](#cfn-route53-hostedzone-hostedzonefeatures-changehistory): {{
    ChangeHistory}}
  [EnableAcceleratedRecovery](#cfn-route53-hostedzone-hostedzonefeatures-enableacceleratedrecovery): {{Boolean}}
  [EnablePublicDNSFallback](#cfn-route53-hostedzone-hostedzonefeatures-enablepublicdnsfallback): {{Boolean}}
```

## Properties
<a name="aws-properties-route53-hostedzone-hostedzonefeatures-properties"></a>

`ChangeGuardrails`  <a name="cfn-route53-hostedzone-hostedzonefeatures-changeguardrails"></a>
Property description not available.
*Required*: No
*Type*: Array of [ChangeGuardrail](aws-properties-route53-hostedzone-changeguardrail.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ChangeHistory`  <a name="cfn-route53-hostedzone-hostedzonefeatures-changehistory"></a>
Property description not available.
*Required*: No
*Type*: [ChangeHistory](aws-properties-route53-hostedzone-changehistory.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableAcceleratedRecovery`  <a name="cfn-route53-hostedzone-hostedzonefeatures-enableacceleratedrecovery"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`EnablePublicDNSFallback`  <a name="cfn-route53-hostedzone-hostedzonefeatures-enablepublicdnsfallback"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
