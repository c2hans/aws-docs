---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-securityprofile-primaryattributevalue.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::SecurityProfile PrimaryAttributeValue
<a name="aws-properties-connect-securityprofile-primaryattributevalue"></a>

A primary attribute value.

## Syntax
<a name="aws-properties-connect-securityprofile-primaryattributevalue-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-securityprofile-primaryattributevalue-syntax.json"></a>

```
{
  "[AccessType](#cfn-connect-securityprofile-primaryattributevalue-accesstype)" : {{String}},
  "[AttributeName](#cfn-connect-securityprofile-primaryattributevalue-attributename)" : {{String}},
  "[Values](#cfn-connect-securityprofile-primaryattributevalue-values)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-connect-securityprofile-primaryattributevalue-syntax.yaml"></a>

```
  [AccessType](#cfn-connect-securityprofile-primaryattributevalue-accesstype): {{String}}
  [AttributeName](#cfn-connect-securityprofile-primaryattributevalue-attributename): {{String}}
  [Values](#cfn-connect-securityprofile-primaryattributevalue-values): {{
    - String}}
```

## Properties
<a name="aws-properties-connect-securityprofile-primaryattributevalue-properties"></a>

`AccessType`  <a name="cfn-connect-securityprofile-primaryattributevalue-accesstype"></a>
The value's access type.
*Required*: No
*Type*: String
*Allowed values*: `ALLOW`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AttributeName`  <a name="cfn-connect-securityprofile-primaryattributevalue-attributename"></a>
The value's attribute name.
*Required*: No
*Type*: String
*Pattern*: `^(?!aws:|connect:)[\p{L}\p{Z}\p{N}\-_.:=@'|]+$`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Values`  <a name="cfn-connect-securityprofile-primaryattributevalue-values"></a>
The value's values.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 1`
*Maximum*: `1000 | 2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
