---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-rds-optiongroup-optionsetting.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RDS::OptionGroup OptionSetting
<a name="aws-properties-rds-optiongroup-optionsetting"></a>

The `OptionSetting` property type specifies the value for an option within an `OptionSetting` property.

## Syntax
<a name="aws-properties-rds-optiongroup-optionsetting-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-rds-optiongroup-optionsetting-syntax.json"></a>

```
{
  "[Name](#cfn-rds-optiongroup-optionsetting-name)" : {{String}},
  "[Value](#cfn-rds-optiongroup-optionsetting-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-rds-optiongroup-optionsetting-syntax.yaml"></a>

```
  [Name](#cfn-rds-optiongroup-optionsetting-name): {{String}}
  [Value](#cfn-rds-optiongroup-optionsetting-value): {{String}}
```

## Properties
<a name="aws-properties-rds-optiongroup-optionsetting-properties"></a>

`Name`  <a name="cfn-rds-optiongroup-optionsetting-name"></a>
The name of the option that has settings that you can set.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-rds-optiongroup-optionsetting-value"></a>
The current value of the option setting.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Examples
<a name="aws-properties-rds-optiongroup-optionsetting--examples"></a>

### Enable ingress to a DB security group
<a name="aws-properties-rds-optiongroup-optionsetting--examples--Enable_ingress_to_a_DB_security_group"></a>

The following example creates an option group for the Oracle Enterprise Edition engine, version 19, and configures it with the Oracle Enterprise Manager option, specifying necessary option settings and a port.

#### JSON
<a name="aws-properties-rds-optiongroup-optionsetting--examples--Enable_ingress_to_a_DB_security_group--json"></a>

```
{
  "Resources": {
    "MyOptionGroup": {
      "Type": "AWS::RDS::OptionGroup",
      "Properties": {
        "EngineName": "oracle-ee",
        "MajorEngineVersion": "19",
        "OptionGroupDescription": "My Oracle OEM Option Group",
        "Options": [
          {
            "OptionName": "OEM",
            "Port": 5500,
            "OptionSettings": [
              {
                "Name": "OEM_HOST",
                "Value": "oem.example.com"
              },
              {
                "Name": "OEM_PORT",
                "Value": "5500"
              },
              {
                "Name": "SECURITY_GROUP_IDS",
                "Value": "sg-0123456789abcdef0"
              }
            ]
          }
        ],
        "Tags": [
          {
            "Key": "Name",
            "Value": "MyOptionGroup"
          }
        ]
      }
    }
  }
}
```

#### YAML
<a name="aws-properties-rds-optiongroup-optionsetting--examples--Enable_ingress_to_a_DB_security_group--yaml"></a>

```
Resources:
  MyOptionGroup:
    Type: AWS::RDS::OptionGroup
    Properties:
      EngineName: oracle-ee
      MajorEngineVersion: 19
      OptionGroupDescription: My Oracle OEM Option Group
      Options:
        - OptionName: OEM
          Port: 5500
          OptionSettings:
            - Name: OEM_HOST
              Value: oem.example.com
            - Name: OEM_PORT
              Value: 5500
            - Name: SECURITY_GROUP_IDS
              Value: sg-0123456789abcdef0
      Tags:
        - Key: Name
          Value: MyOptionGroup
```
