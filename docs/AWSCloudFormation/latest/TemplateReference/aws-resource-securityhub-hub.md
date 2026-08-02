---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-securityhub-hub.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::Hub
<a name="aws-resource-securityhub-hub"></a>

The `AWS::SecurityHub::Hub` resource specifies the enablement of the AWS Security Hub CSPM service in your AWS account. The service is enabled in the current AWS Region or the specified Region. You create a separate `Hub` resource in each Region in which you want to enable Security Hub CSPM.

When you use this resource to enable Security Hub CSPM, default security standards are enabled. To disable default standards, set the `EnableDefaultStandards` property to `false`. You can use the [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-standard.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-securityhub-standard.html) resource to enable additional standards.

When you use this resource to enable Security Hub CSPM, new controls are automatically enabled for your enabled standards. To disable automatic enablement of new controls, set the `AutoEnableControls` property to `false`.

You must create an `AWS::SecurityHub::Hub` resource for an account before you can create other types of Security Hub CSPM resources for the account through CloudFormation. Use a [DependsOn attribute](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-attribute-dependson.html), such as `"DependsOn": "Hub"`, to ensure that you've created an `AWS::SecurityHub::Hub` resource before creating other Security Hub CSPM resources for an account.

## Syntax
<a name="aws-resource-securityhub-hub-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-securityhub-hub-syntax.json"></a>

```
{
  "Type" : "AWS::SecurityHub::Hub",
  "Properties" : {
      "[AutoEnableControls](#cfn-securityhub-hub-autoenablecontrols)" : {{Boolean}},
      "[ControlFindingGenerator](#cfn-securityhub-hub-controlfindinggenerator)" : {{String}},
      "[EnableDefaultStandards](#cfn-securityhub-hub-enabledefaultstandards)" : {{Boolean}},
      "[Tags](#cfn-securityhub-hub-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-securityhub-hub-syntax.yaml"></a>

```
Type: AWS::SecurityHub::Hub
Properties:
  [AutoEnableControls](#cfn-securityhub-hub-autoenablecontrols): {{Boolean}}
  [ControlFindingGenerator](#cfn-securityhub-hub-controlfindinggenerator): {{String}}
  [EnableDefaultStandards](#cfn-securityhub-hub-enabledefaultstandards): {{Boolean}}
  [Tags](#cfn-securityhub-hub-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-securityhub-hub-properties"></a>

`AutoEnableControls`  <a name="cfn-securityhub-hub-autoenablecontrols"></a>
Whether to automatically enable new controls when they are added to standards that are enabled.
By default, this is set to `true`, and new controls are enabled automatically. To not automatically enable new controls, set this to `false`.
When you automatically enable new controls, you can interact with the controls in the console and programmatically immediately after release. However, automatically enabled controls have a temporary default status of `DISABLED`. It can take up to several days for Security Hub CSPM to process the control release and designate the control as `ENABLED` in your account. During the processing period, you can manually enable or disable a control, and Security Hub CSPM will maintain that designation regardless of whether you have `AutoEnableControls` set to `true`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ControlFindingGenerator`  <a name="cfn-securityhub-hub-controlfindinggenerator"></a>
Specifies whether an account has consolidated control findings turned on or off. If the value for this field is set to `SECURITY_CONTROL`, Security Hub CSPM generates a single finding for a control check even when the check applies to multiple enabled standards.
If the value for this field is set to `STANDARD_CONTROL`, Security Hub CSPM generates separate findings for a control check when the check applies to multiple enabled standards.
The value for this field in a member account matches the value in the administrator account. For accounts that aren't part of an organization, the default value of this field is `SECURITY_CONTROL` if you enabled Security Hub CSPM on or after February 23, 2023.
*Required*: No
*Type*: String
*Pattern*: `^(SECURITY_CONTROL|STANDARD_CONTROL)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableDefaultStandards`  <a name="cfn-securityhub-hub-enabledefaultstandards"></a>
Whether to enable the security standards that Security Hub CSPM has designated as automatically enabled. If you don't provide a value for `EnableDefaultStandards`, it is set to `true`, and the designated standards are automatically enabled in each AWS Region where you enable Security Hub CSPM. If you don't want to enable the designated standards, set `EnableDefaultStandards` to `false`.
Currently, the automatically enabled standards are the Center for Internet Security (CIS) AWS Foundations Benchmark v1.2.0 and AWS Foundational Security Best Practices (FSBP).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-securityhub-hub-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Object of String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]+$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-securityhub-hub-return-values"></a>

### Ref
<a name="aws-resource-securityhub-hub-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `HubArn` for the hub resource created, such as `arn:aws:securityhub:us-east-1:123456789012:hub/default`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-securityhub-hub-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-securityhub-hub-return-values-fn--getatt-fn--getatt"></a>

`ARN`  <a name="ARN-fn::getatt"></a>
The Amazon Resource Name (ARN) of the `Hub` resource that was retrieved.

`SubscribedAt`  <a name="SubscribedAt-fn::getatt"></a>
The date and time when Security Hub CSPM was enabled in your account.

## Examples
<a name="aws-resource-securityhub-hub--examples"></a>

The following examples show how to declare an `AWS::SecurityHub::Hub` resource.

**Topics**
+ [Creating a `Hub` resource that enables default standards and turns on consolidated control findings](#aws-resource-securityhub-hub--examples--Creating_a_Hub_resource_that_enables_default_standards_and_turns_on_consolidated_control_findings)
+ [Creating a `Hub` resource that disables default standards and turns off consolidated control findings](#aws-resource-securityhub-hub--examples--Creating_a_Hub_resource_that_disables_default_standards_and_turns_off_consolidated_control_findings)

### Creating a `Hub` resource that enables default standards and turns on consolidated control findings
<a name="aws-resource-securityhub-hub--examples--Creating_a_Hub_resource_that_enables_default_standards_and_turns_on_consolidated_control_findings"></a>

In this example, the default standards are automatically enabled, and consolidated control findings is turned on.

#### JSON
<a name="aws-resource-securityhub-hub--examples--Creating_a_Hub_resource_that_enables_default_standards_and_turns_on_consolidated_control_findings--json"></a>

```
{
    "Description": "Example template to create a Hub resource",
    "Resources": {
        "ExampleHubWithTags": {
            "Type": "AWS::SecurityHub::Hub",
            "Properties": {
                "Tags": {
                    "key1": "value1",
                    "key2": "value2"
                },
                "EnableDefaultStandards": true,
                "ControlFindingGenerator": "SECURITY_CONTROL"
            }
        }
    },
    "Outputs": {
        "HubArn": {
            "Value": {
                "Ref": "ExampleHubWithTags"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-securityhub-hub--examples--Creating_a_Hub_resource_that_enables_default_standards_and_turns_on_consolidated_control_findings--yaml"></a>

```
Description: Example template to create a Hub resource
Resources:
  ExampleHubWithTags:
    Type: 'AWS::SecurityHub::Hub'
    Properties:
      Tags:
        key1: value1
        key2: value2
      EnableDefaultStandards: true
      ControlFindingGenerator: 'SECURITY_CONTROL'

Outputs:
  HubArn:
    Value: !Ref ExampleHubWithTags
```

### Creating a `Hub` resource that disables default standards and turns off consolidated control findings
<a name="aws-resource-securityhub-hub--examples--Creating_a_Hub_resource_that_disables_default_standards_and_turns_off_consolidated_control_findings"></a>

In this example, the default standards are disabled, and consolidated control findings is turned off.

#### JSON
<a name="aws-resource-securityhub-hub--examples--Creating_a_Hub_resource_that_disables_default_standards_and_turns_off_consolidated_control_findings--json"></a>

```
{
    "Description": "Example template to create a Hub resource",
    "Resources": {
        "ExampleHubWithTags": {
            "Type": "AWS::SecurityHub::Hub",
            "Properties": {
                "Tags": {
                    "key1": "value1",
                    "key2": "value2"
                },
                "EnableDefaultStandards": false,
                "ControlFindingGenerator": "STANDARD_CONTROL"
            }
        }
    },
    "Outputs": {
        "HubArn": {
            "Value": {
                "Ref": "ExampleHubWithTags"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-securityhub-hub--examples--Creating_a_Hub_resource_that_disables_default_standards_and_turns_off_consolidated_control_findings--yaml"></a>

```
Description: Example template to create a Hub resource
Resources:
  ExampleHubWithTags:
    Type: 'AWS::SecurityHub::Hub'
    Properties:
      Tags:
        key1: value1
        key2: value2
      EnableDefaultStandards: false
      ControlFindingGenerator: 'STANDARD_CONTROL'

Outputs:
  HubArn:
    Value: !Ref ExampleHubWithTags
```
