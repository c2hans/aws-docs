---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-securityprofile-primaryattributeaccesscontrolconfigurationitem.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::SecurityProfile PrimaryAttributeAccessControlConfigurationItem
<a name="aws-properties-connect-securityprofile-primaryattributeaccesscontrolconfigurationitem"></a>

A primary attribute access control configuration item.

## Syntax
<a name="aws-properties-connect-securityprofile-primaryattributeaccesscontrolconfigurationitem-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-securityprofile-primaryattributeaccesscontrolconfigurationitem-syntax.json"></a>

```
{
  "[PrimaryAttributeValues](#cfn-connect-securityprofile-primaryattributeaccesscontrolconfigurationitem-primaryattributevalues)" : {{[ PrimaryAttributeValue, ... ]}}
}
```

### YAML
<a name="aws-properties-connect-securityprofile-primaryattributeaccesscontrolconfigurationitem-syntax.yaml"></a>

```
  [PrimaryAttributeValues](#cfn-connect-securityprofile-primaryattributeaccesscontrolconfigurationitem-primaryattributevalues): {{
    - PrimaryAttributeValue}}
```

## Properties
<a name="aws-properties-connect-securityprofile-primaryattributeaccesscontrolconfigurationitem-properties"></a>

`PrimaryAttributeValues`  <a name="cfn-connect-securityprofile-primaryattributeaccesscontrolconfigurationitem-primaryattributevalues"></a>
The item's primary attribute values.
*Required*: No
*Type*: Array of [PrimaryAttributeValue](aws-properties-connect-securityprofile-primaryattributevalue.md)
*Minimum*: `1`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
