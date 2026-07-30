---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-aps-rulegroupsnamespace.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::APS::RuleGroupsNamespace
<a name="aws-resource-aps-rulegroupsnamespace"></a>

The definition of a rule groups namespace in an Amazon Managed Service for Prometheus workspace. A rule groups namespace is associated with exactly one rules file. A workspace can have multiple rule groups namespaces. For more information about rules files, see [Creating a rules file](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-ruler-rulesfile.html), in the *Amazon Managed Service for Prometheus User Guide*.

## Syntax
<a name="aws-resource-aps-rulegroupsnamespace-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-aps-rulegroupsnamespace-syntax.json"></a>

```
{
  "Type" : "AWS::APS::RuleGroupsNamespace",
  "Properties" : {
      "[Data](#cfn-aps-rulegroupsnamespace-data)" : {{String}},
      "[Name](#cfn-aps-rulegroupsnamespace-name)" : {{String}},
      "[Tags](#cfn-aps-rulegroupsnamespace-tags)" : {{[ Tag, ... ]}},
      "[Workspace](#cfn-aps-rulegroupsnamespace-workspace)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-aps-rulegroupsnamespace-syntax.yaml"></a>

```
Type: AWS::APS::RuleGroupsNamespace
Properties:
  [Data](#cfn-aps-rulegroupsnamespace-data): {{String}}
  [Name](#cfn-aps-rulegroupsnamespace-name): {{String}}
  [Tags](#cfn-aps-rulegroupsnamespace-tags): {{
    - Tag}}
  [Workspace](#cfn-aps-rulegroupsnamespace-workspace): {{String}}
```

## Properties
<a name="aws-resource-aps-rulegroupsnamespace-properties"></a>

`Data`  <a name="cfn-aps-rulegroupsnamespace-data"></a>
The rules file used in the namespace.
For more details about the rules file, see [Creating a rules file](https://docs.aws.amazon.com/prometheus/latest/userguide/AMP-ruler-rulesfile.html) in the *Amazon Managed Service for Prometheus User Guide*.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-aps-rulegroupsnamespace-name"></a>
The name of the rule groups namespace.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-aps-rulegroupsnamespace-tags"></a>
The list of tag keys and values that are associated with the rule groups namespace.
*Required*: No
*Type*: Array of [Tag](aws-properties-aps-rulegroupsnamespace-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Workspace`  <a name="cfn-aps-rulegroupsnamespace-workspace"></a>
The ID of the workspace to add the rule groups namespace.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov|aws-cn):aps:[a-z0-9-]+:[0-9]+:workspace/[a-zA-Z0-9-]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-aps-rulegroupsnamespace-return-values"></a>

### Ref
<a name="aws-resource-aps-rulegroupsnamespace-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource name. For example:

 `{ "Ref": "Arn" }`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-aps-rulegroupsnamespace-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-aps-rulegroupsnamespace-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the rule groups namespace. For example, `arn:aws:aps:<region>:123456789012:rulegroupsnamespace/ws-example1-1234-abcd-5678-ef90abcd1234/rulesfile1`.
