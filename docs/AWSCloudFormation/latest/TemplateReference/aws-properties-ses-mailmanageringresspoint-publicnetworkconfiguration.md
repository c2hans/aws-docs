---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanageringresspoint-publicnetworkconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerIngressPoint PublicNetworkConfiguration
<a name="aws-properties-ses-mailmanageringresspoint-publicnetworkconfiguration"></a>

Specifies the network configuration for the public ingress point.

## Syntax
<a name="aws-properties-ses-mailmanageringresspoint-publicnetworkconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanageringresspoint-publicnetworkconfiguration-syntax.json"></a>

```
{
  "[IpType](#cfn-ses-mailmanageringresspoint-publicnetworkconfiguration-iptype)" : {{}}
}
```

### YAML
<a name="aws-properties-ses-mailmanageringresspoint-publicnetworkconfiguration-syntax.yaml"></a>

```
  [IpType](#cfn-ses-mailmanageringresspoint-publicnetworkconfiguration-iptype): {{
    }}
```

## Properties
<a name="aws-properties-ses-mailmanageringresspoint-publicnetworkconfiguration-properties"></a>

`IpType`  <a name="cfn-ses-mailmanageringresspoint-publicnetworkconfiguration-iptype"></a>
The IP address type for the public ingress point. Valid values are IPV4 and DUAL\_STACK.
*Required*: Yes
*Type*:
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
