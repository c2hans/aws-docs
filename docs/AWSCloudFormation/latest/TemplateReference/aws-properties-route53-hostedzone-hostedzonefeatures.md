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
The Change Guardrail settings for the hosted zone. When a guardrail is enabled, Route 53 blocks the corresponding change. `NS_OCCLUSION_CHECK` is available on both the standard and advanced tiers; the other guardrails are available only on the advanced tier.
*Required*: No
*Type*: Array of [ChangeGuardrail](aws-properties-route53-hostedzone-changeguardrail.md)
*Minimum*: `1`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`ChangeHistory`  <a name="cfn-route53-hostedzone-hostedzonefeatures-changehistory"></a>
The change history setting for the hosted zone. This property is read-only and reports whether change history is enabled for the hosted zone.
*Required*: No
*Type*: [ChangeHistory](aws-properties-route53-hostedzone-changehistory.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableAcceleratedRecovery`  <a name="cfn-route53-hostedzone-hostedzonefeatures-enableacceleratedrecovery"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`EnablePublicDNSFallback`  <a name="cfn-route53-hostedzone-hostedzonefeatures-enablepublicdnsfallback"></a>
Enables public DNS fallback for a private hosted zone. When a query for a name in the private hosted zone matches no existing name, Route 53 falls back to public DNS instead of returning a negative response. Fallback does not occur when the name exists but has no record of the requested type.
Supported on private hosted zones only, and only when the hosted zone is on the advanced tier.
*Required*: No
*Type*: Boolean
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)
