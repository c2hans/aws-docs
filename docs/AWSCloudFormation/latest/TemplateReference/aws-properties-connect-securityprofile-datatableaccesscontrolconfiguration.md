---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-securityprofile-datatableaccesscontrolconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::SecurityProfile DataTableAccessControlConfiguration
<a name="aws-properties-connect-securityprofile-datatableaccesscontrolconfiguration"></a>

A data table access control configuration.

## Syntax
<a name="aws-properties-connect-securityprofile-datatableaccesscontrolconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-securityprofile-datatableaccesscontrolconfiguration-syntax.json"></a>

```
{
  "[PrimaryAttributeAccessControlConfiguration](#cfn-connect-securityprofile-datatableaccesscontrolconfiguration-primaryattributeaccesscontrolconfiguration)" : {{PrimaryAttributeAccessControlConfigurationItem}}
}
```

### YAML
<a name="aws-properties-connect-securityprofile-datatableaccesscontrolconfiguration-syntax.yaml"></a>

```
  [PrimaryAttributeAccessControlConfiguration](#cfn-connect-securityprofile-datatableaccesscontrolconfiguration-primaryattributeaccesscontrolconfiguration): {{
    PrimaryAttributeAccessControlConfigurationItem}}
```

## Properties
<a name="aws-properties-connect-securityprofile-datatableaccesscontrolconfiguration-properties"></a>

`PrimaryAttributeAccessControlConfiguration`  <a name="cfn-connect-securityprofile-datatableaccesscontrolconfiguration-primaryattributeaccesscontrolconfiguration"></a>
The configuration's primary attribute access control configuration.
*Required*: No
*Type*: [PrimaryAttributeAccessControlConfigurationItem](aws-properties-connect-securityprofile-primaryattributeaccesscontrolconfigurationitem.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
