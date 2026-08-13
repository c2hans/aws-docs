---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-applicationsignals-groupingconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ApplicationSignals::GroupingConfiguration
<a name="aws-resource-applicationsignals-groupingconfiguration"></a>

A structure that contains the complete grouping configuration for an account, including all defined grouping attributes and metadata about when it was last updated.

## Syntax
<a name="aws-resource-applicationsignals-groupingconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-applicationsignals-groupingconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::ApplicationSignals::GroupingConfiguration",
  "Properties" : {
      "[GroupingAttributeDefinitions](#cfn-applicationsignals-groupingconfiguration-groupingattributedefinitions)" : {{[ GroupingAttributeDefinition, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-applicationsignals-groupingconfiguration-syntax.yaml"></a>

```
Type: AWS::ApplicationSignals::GroupingConfiguration
Properties:
  [GroupingAttributeDefinitions](#cfn-applicationsignals-groupingconfiguration-groupingattributedefinitions): {{
    - GroupingAttributeDefinition}}
```

## Properties
<a name="aws-resource-applicationsignals-groupingconfiguration-properties"></a>

`GroupingAttributeDefinitions`  <a name="cfn-applicationsignals-groupingconfiguration-groupingattributedefinitions"></a>
An array of grouping attribute definitions that specify how services should be grouped based on various attributes and source keys.
*Required*: Yes
*Type*: Array of [GroupingAttributeDefinition](aws-properties-applicationsignals-groupingconfiguration-groupingattributedefinition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-applicationsignals-groupingconfiguration-return-values"></a>

### Ref
<a name="aws-resource-applicationsignals-groupingconfiguration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the 12 digit AWS Account ID for the account.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-applicationsignals-groupingconfiguration-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-applicationsignals-groupingconfiguration-return-values-fn--getatt-fn--getatt"></a>

`AccountId`  <a name="AccountId-fn::getatt"></a>
The 12 digit AWS Account ID for the account.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when this grouping configuration was last updated. When used in a raw HTTP Query API, it is formatted as epoch time in seconds.
