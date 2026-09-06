---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagertrafficpolicy-ingresstlsprotocoltoevaluate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerTrafficPolicy IngressTlsProtocolToEvaluate
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingresstlsprotocoltoevaluate"></a>

The union type representing the allowed types for the left hand side of a TLS condition.

## Syntax
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingresstlsprotocoltoevaluate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingresstlsprotocoltoevaluate-syntax.json"></a>

```
{
  "[Attribute](#cfn-ses-mailmanagertrafficpolicy-ingresstlsprotocoltoevaluate-attribute)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingresstlsprotocoltoevaluate-syntax.yaml"></a>

```
  [Attribute](#cfn-ses-mailmanagertrafficpolicy-ingresstlsprotocoltoevaluate-attribute): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingresstlsprotocoltoevaluate-properties"></a>

`Attribute`  <a name="cfn-ses-mailmanagertrafficpolicy-ingresstlsprotocoltoevaluate-attribute"></a>
The enum type representing the allowed attribute types for the TLS condition.
*Required*: Yes
*Type*: String
*Allowed values*: `TLS_PROTOCOL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
