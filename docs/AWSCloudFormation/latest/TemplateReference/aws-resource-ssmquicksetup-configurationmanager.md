---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssmquicksetup-configurationmanager.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSMQuickSetup::ConfigurationManager
<a name="aws-resource-ssmquicksetup-configurationmanager"></a>

Creates a Quick Setup configuration manager resource. This object is a collection of desired state configurations for multiple configuration definitions and summaries describing the deployments of those definitions.

## Syntax
<a name="aws-resource-ssmquicksetup-configurationmanager-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ssmquicksetup-configurationmanager-syntax.json"></a>

```
{
  "Type" : "AWS::SSMQuickSetup::ConfigurationManager",
  "Properties" : {
      "[ConfigurationDefinitions](#cfn-ssmquicksetup-configurationmanager-configurationdefinitions)" : {{[ ConfigurationDefinition, ... ]}},
      "[Description](#cfn-ssmquicksetup-configurationmanager-description)" : {{String}},
      "[Name](#cfn-ssmquicksetup-configurationmanager-name)" : {{String}},
      "[Tags](#cfn-ssmquicksetup-configurationmanager-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-ssmquicksetup-configurationmanager-syntax.yaml"></a>

```
Type: AWS::SSMQuickSetup::ConfigurationManager
Properties:
  [ConfigurationDefinitions](#cfn-ssmquicksetup-configurationmanager-configurationdefinitions): {{
    - ConfigurationDefinition}}
  [Description](#cfn-ssmquicksetup-configurationmanager-description): {{String}}
  [Name](#cfn-ssmquicksetup-configurationmanager-name): {{String}}
  [Tags](#cfn-ssmquicksetup-configurationmanager-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-ssmquicksetup-configurationmanager-properties"></a>

`ConfigurationDefinitions`  <a name="cfn-ssmquicksetup-configurationmanager-configurationdefinitions"></a>
The definition of the Quick Setup configuration that the configuration manager deploys.
*Required*: Yes
*Type*: Array of [ConfigurationDefinition](aws-properties-ssmquicksetup-configurationmanager-configurationdefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-ssmquicksetup-configurationmanager-description"></a>
The description of the configuration.
*Required*: No
*Type*: String
*Pattern*: `^.{0,512}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-ssmquicksetup-configurationmanager-name"></a>
The name of the configuration
*Required*: No
*Type*: String
*Pattern*: `^[ A-Za-z0-9_-]{1,50}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ssmquicksetup-configurationmanager-tags"></a>
Key-value pairs of metadata to assign to the configuration manager.
*Required*: No
*Type*: Object of String
*Pattern*: `^[A-Za-z0-9 +=@_\/:.-]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ssmquicksetup-configurationmanager-return-values"></a>

### Ref
<a name="aws-resource-ssmquicksetup-configurationmanager-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the configuration manager.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ssmquicksetup-configurationmanager-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ssmquicksetup-configurationmanager-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The datetime stamp when the configuration manager was created.

`LastModifiedAt`  <a name="LastModifiedAt-fn::getatt"></a>
The datetime stamp when the configuration manager was last updated.

`ManagerArn`  <a name="ManagerArn-fn::getatt"></a>
The ARN of the Quick Setup configuration.

`StatusSummaries`  <a name="StatusSummaries-fn::getatt"></a>
Summaries of the state of the configuration manager. These summaries include an aggregate of the statuses from the configuration definition associated with the configuration manager. This includes deployment statuses, association statuses, drift statuses, health checks, and more.

## Examples
<a name="aws-resource-ssmquicksetup-configurationmanager--examples"></a>

### AWS Config Recording - local
<a name="aws-resource-ssmquicksetup-configurationmanager--examples--Recording_-_local"></a>

Set up AWS Config Recording for the local account.

#### YAML
<a name="aws-resource-ssmquicksetup-configurationmanager--examples--Recording_-_local--yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
   SSMQuickSetupTestConfigurationManager:
      Type: "AWS::SSMQuickSetup::ConfigurationManager"
      Properties:
      Name: "Example"
      Description: "Example template"
      ConfigurationDefinitions:
         - Type: "AWSQuickSetupType-PatchPolicy"
            Parameters:
            TargetAccounts:
               Ref: AWS::AccountId
            TargetRegions:
               Ref: AWS::Region
            LocalDeploymentAdministrationRoleArn: !Sub "arn:aws:iam::${AWS::AccountId}:role/{{AWS-QuickSetup-StackSet-Example-AdministrationRole}}"
            LocalDeploymentExecutionRoleName: "{{AWS-QuickSetup-StackSet-Example-ExecutionRole}}"
      Tags:
         exampleTag: "exampleTagValue"
Outputs:
  Sample:
    Description: This is an example
    Value: !GetAtt SSMQuickSetupTestConfigurationManager.ManagerArn
```
