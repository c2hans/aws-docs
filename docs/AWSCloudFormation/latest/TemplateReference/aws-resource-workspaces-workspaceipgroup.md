---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-workspaces-workspaceipgroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpaces::WorkspaceIpGroup
<a name="aws-resource-workspaces-workspaceipgroup"></a>

<a name="aws-resource-workspaces-workspaceipgroup-description"></a>The `AWS::WorkSpaces::WorkspaceIpGroup` resource Property description not available. for WorkSpaces.

## Syntax
<a name="aws-resource-workspaces-workspaceipgroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-workspaces-workspaceipgroup-syntax.json"></a>

```
{
  "Type" : "AWS::WorkSpaces::WorkspaceIpGroup",
  "Properties" : {
      "[GroupDesc](#cfn-workspaces-workspaceipgroup-groupdesc)" : {{String}},
      "[GroupName](#cfn-workspaces-workspaceipgroup-groupname)" : {{String}},
      "[Tags](#cfn-workspaces-workspaceipgroup-tags)" : {{[ Tag, ... ]}},
      "[UserRules](#cfn-workspaces-workspaceipgroup-userrules)" : {{[ IpRuleItem, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-workspaces-workspaceipgroup-syntax.yaml"></a>

```
Type: AWS::WorkSpaces::WorkspaceIpGroup
Properties:
  [GroupDesc](#cfn-workspaces-workspaceipgroup-groupdesc): {{String}}
  [GroupName](#cfn-workspaces-workspaceipgroup-groupname): {{String}}
  [Tags](#cfn-workspaces-workspaceipgroup-tags): {{
    - Tag}}
  [UserRules](#cfn-workspaces-workspaceipgroup-userrules): {{
    - IpRuleItem}}
```

## Properties
<a name="aws-resource-workspaces-workspaceipgroup-properties"></a>

`GroupDesc`  <a name="cfn-workspaces-workspaceipgroup-groupdesc"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GroupName`  <a name="cfn-workspaces-workspaceipgroup-groupname"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-workspaces-workspaceipgroup-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-workspaces-workspaceipgroup-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserRules`  <a name="cfn-workspaces-workspaceipgroup-userrules"></a>
Property description not available.
*Required*: No
*Type*: Array of [IpRuleItem](aws-properties-workspaces-workspaceipgroup-ipruleitem.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-workspaces-workspaceipgroup-return-values"></a>

### Ref
<a name="aws-resource-workspaces-workspaceipgroup-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-workspaces-workspaceipgroup-return-values-fn--getatt"></a>

####
<a name="aws-resource-workspaces-workspaceipgroup-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`GroupId`  <a name="GroupId-fn::getatt"></a>
Property description not available.
