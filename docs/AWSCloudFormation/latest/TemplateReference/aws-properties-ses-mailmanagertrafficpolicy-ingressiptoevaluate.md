---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagertrafficpolicy-ingressiptoevaluate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerTrafficPolicy IngressIpToEvaluate
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressiptoevaluate"></a>

The structure for an IP based condition matching on the incoming mail.

## Syntax
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressiptoevaluate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressiptoevaluate-syntax.json"></a>

```
{
  "[Attribute](#cfn-ses-mailmanagertrafficpolicy-ingressiptoevaluate-attribute)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressiptoevaluate-syntax.yaml"></a>

```
  [Attribute](#cfn-ses-mailmanagertrafficpolicy-ingressiptoevaluate-attribute): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressiptoevaluate-properties"></a>

`Attribute`  <a name="cfn-ses-mailmanagertrafficpolicy-ingressiptoevaluate-attribute"></a>
An enum type representing the allowed attribute types for an IP condition.
*Required*: Yes
*Type*: String
*Allowed values*: `SENDER_IP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
