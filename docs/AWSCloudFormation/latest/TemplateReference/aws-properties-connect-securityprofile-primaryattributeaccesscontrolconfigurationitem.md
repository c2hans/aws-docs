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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
