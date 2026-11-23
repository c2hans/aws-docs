---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-route53-hostedzone-changehistory.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53::HostedZone ChangeHistory

The change history feature of a hosted zone. This complex type is read-only and reports whether change history is enabled and, when enabled, the earliest time the hosted zone's change history can be read from.

## Syntax
<a name="aws-properties-route53-hostedzone-changehistory-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-route53-hostedzone-changehistory-syntax.json"></a>

```json
{
  "[RetentionStartsAt](#cfn-route53-hostedzone-changehistory-retentionstartsat)" : {{String}},
  "[Status](#cfn-route53-hostedzone-changehistory-status)" : {{String}}
}
```

### YAML
<a name="aws-properties-route53-hostedzone-changehistory-syntax.yaml"></a>

```yaml
  [RetentionStartsAt](#cfn-route53-hostedzone-changehistory-retentionstartsat): {{String}}
  [Status](#cfn-route53-hostedzone-changehistory-status): {{String}}
```

## Properties
<a name="aws-properties-route53-hostedzone-changehistory-properties"></a>

`RetentionStartsAt`  <a name="cfn-route53-hostedzone-changehistory-retentionstartsat"></a>
The earliest time the hosted zone's change history can be read from, as an ISO 8601 timestamp. Present only when `Status` is `ENABLED`.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-route53-hostedzone-changehistory-status"></a>
Whether change history is enabled for the hosted zone. Valid values are `ENABLED` and `DISABLED`.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
