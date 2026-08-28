---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-fms-resourceset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::FMS::ResourceSet
<a name="aws-resource-fms-resourceset"></a>

A set of resources to include in a policy.

## Syntax
<a name="aws-resource-fms-resourceset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-fms-resourceset-syntax.json"></a>

```
{
  "Type" : "AWS::FMS::ResourceSet",
  "Properties" : {
      "[Description](#cfn-fms-resourceset-description)" : {{String}},
      "[Name](#cfn-fms-resourceset-name)" : {{String}},
      "[Resources](#cfn-fms-resourceset-resources)" : {{[ String, ... ]}},
      "[ResourceTypeList](#cfn-fms-resourceset-resourcetypelist)" : {{[ String, ... ]}},
      "[Tags](#cfn-fms-resourceset-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-fms-resourceset-syntax.yaml"></a>

```
Type: AWS::FMS::ResourceSet
Properties:
  [Description](#cfn-fms-resourceset-description): {{String}}
  [Name](#cfn-fms-resourceset-name): {{String}}
  [Resources](#cfn-fms-resourceset-resources): {{
    - String}}
  [ResourceTypeList](#cfn-fms-resourceset-resourcetypelist): {{
    - String}}
  [Tags](#cfn-fms-resourceset-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-fms-resourceset-properties"></a>

`Description`  <a name="cfn-fms-resourceset-description"></a>
A description of the resource set.
*Required*: No
*Type*: String
*Pattern*: `^([a-zA-Z0-9_.:/=+\-@\s]*)$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-fms-resourceset-name"></a>
The descriptive name of the resource set. You can't change the name of a resource set after you create it.
*Required*: Yes
*Type*: String
*Pattern*: `^([a-zA-Z0-9_.:/=+\-@\s]+)$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Resources`  <a name="cfn-fms-resourceset-resources"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceTypeList`  <a name="cfn-fms-resourceset-resourcetypelist"></a>
Determines the resources that can be associated to the resource set. Depending on your setting for max results and the number of resource sets, a single call might not return the full list.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-fms-resourceset-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-fms-resourceset-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-fms-resourceset-return-values"></a>

### Ref
<a name="aws-resource-fms-resourceset-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-fms-resourceset-return-values-fn--getatt"></a>

####
<a name="aws-resource-fms-resourceset-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
A unique identifier for the resource set. This ID is returned in the responses to create and list commands. You provide it to operations like update and delete.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
