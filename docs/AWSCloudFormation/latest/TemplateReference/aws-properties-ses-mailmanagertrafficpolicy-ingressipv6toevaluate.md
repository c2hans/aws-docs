---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagertrafficpolicy-ingressipv6toevaluate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerTrafficPolicy IngressIpv6ToEvaluate
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressipv6toevaluate"></a>

The structure for an IPv6 based condition matching on the incoming mail.

## Syntax
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressipv6toevaluate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressipv6toevaluate-syntax.json"></a>

```
{
  "[Attribute](#cfn-ses-mailmanagertrafficpolicy-ingressipv6toevaluate-attribute)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressipv6toevaluate-syntax.yaml"></a>

```
  [Attribute](#cfn-ses-mailmanagertrafficpolicy-ingressipv6toevaluate-attribute): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressipv6toevaluate-properties"></a>

`Attribute`  <a name="cfn-ses-mailmanagertrafficpolicy-ingressipv6toevaluate-attribute"></a>
An enum type representing the allowed attribute types for an IPv6 condition.
*Required*: Yes
*Type*: String
*Allowed values*: `SENDER_IPV6`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
