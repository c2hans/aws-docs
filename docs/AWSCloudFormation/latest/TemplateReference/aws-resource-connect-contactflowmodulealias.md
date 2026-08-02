---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-contactflowmodulealias.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::ContactFlowModuleAlias
<a name="aws-resource-connect-contactflowmodulealias"></a>

Creates a named alias that points to a specific version of a contact flow module.

## Syntax
<a name="aws-resource-connect-contactflowmodulealias-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-contactflowmodulealias-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::ContactFlowModuleAlias",
  "Properties" : {
      "[ContactFlowModuleId](#cfn-connect-contactflowmodulealias-contactflowmoduleid)" : {{String}},
      "[ContactFlowModuleVersion](#cfn-connect-contactflowmodulealias-contactflowmoduleversion)" : {{Integer}},
      "[Description](#cfn-connect-contactflowmodulealias-description)" : {{String}},
      "[Name](#cfn-connect-contactflowmodulealias-name)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-connect-contactflowmodulealias-syntax.yaml"></a>

```
Type: AWS::Connect::ContactFlowModuleAlias
Properties:
  [ContactFlowModuleId](#cfn-connect-contactflowmodulealias-contactflowmoduleid): {{String}}
  [ContactFlowModuleVersion](#cfn-connect-contactflowmodulealias-contactflowmoduleversion): {{Integer}}
  [Description](#cfn-connect-contactflowmodulealias-description): {{String}}
  [Name](#cfn-connect-contactflowmodulealias-name): {{String}}
```

## Properties
<a name="aws-resource-connect-contactflowmodulealias-properties"></a>

`ContactFlowModuleId`  <a name="cfn-connect-contactflowmodulealias-contactflowmoduleid"></a>
The identifier of the flow module.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]+:[0-9]{12}:instance/[-a-zA-Z0-9]+/flow-module/[-a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ContactFlowModuleVersion`  <a name="cfn-connect-contactflowmodulealias-contactflowmoduleversion"></a>
The version of the flow module.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-connect-contactflowmodulealias-description"></a>
The description of the alias.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-connect-contactflowmodulealias-name"></a>
The name of the alias.
*Required*: Yes
*Type*: String
*Pattern*: `^([$0-9a-zA-Z][_-]?)+$`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-connect-contactflowmodulealias-return-values"></a>

### Ref
<a name="aws-resource-connect-contactflowmodulealias-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-connect-contactflowmodulealias-return-values-fn--getatt"></a>

####
<a name="aws-resource-connect-contactflowmodulealias-return-values-fn--getatt-fn--getatt"></a>

`AliasId`  <a name="AliasId-fn::getatt"></a>
The identifier of the alias.

`ContactFlowModuleAliasARN`  <a name="ContactFlowModuleAliasARN-fn::getatt"></a>
Property description not available.
