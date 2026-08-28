---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-synthetics-group.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Synthetics::Group
<a name="aws-resource-synthetics-group"></a>

Creates or updates a group which you can use to associate canaries with each other, including cross-Region canaries. Using groups can help you with managing and automating your canaries, and you can also view aggregated run results and statistics for all canaries in a group.

Groups are global resources. When you create a group, it is replicated across all AWS Regions, and you can add canaries from any Region to it, and view it in any Region. Although the group ARN format reflects the Region name where it was created, a group is not constrained to any Region. This means that you can put canaries from multiple Regions into the same group, and then use that group to view and manage all of those canaries in a single view.

Each group can contain as many as 10 canaries. You can have as many as 20 groups in your account. Any single canary can be a member of up to 10 groups.

## Syntax
<a name="aws-resource-synthetics-group-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-synthetics-group-syntax.json"></a>

```
{
  "Type" : "AWS::Synthetics::Group",
  "Properties" : {
      "[Name](#cfn-synthetics-group-name)" : {{String}},
      "[ResourceArns](#cfn-synthetics-group-resourcearns)" : {{[ String, ... ]}},
      "[Tags](#cfn-synthetics-group-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-synthetics-group-syntax.yaml"></a>

```
Type: AWS::Synthetics::Group
Properties:
  [Name](#cfn-synthetics-group-name): {{String}}
  [ResourceArns](#cfn-synthetics-group-resourcearns): {{
    - String}}
  [Tags](#cfn-synthetics-group-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-synthetics-group-properties"></a>

`Name`  <a name="cfn-synthetics-group-name"></a>
A name for the group. It can include any Unicode characters.
The names for all groups in your account, across all Regions, must be unique.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-z_\-]{1,64}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceArns`  <a name="cfn-synthetics-group-resourcearns"></a>
The ARNs of the canaries that you want to associate with this group.
*Required*: No
*Type*: Array of String
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-synthetics-group-tags"></a>
The list of key-value pairs that are associated with the group.
*Required*: No
*Type*: Array of [Tag](aws-properties-synthetics-group-tag.md)
*Minimum*: `0`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-synthetics-group-return-values"></a>

### Ref
<a name="aws-resource-synthetics-group-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the group.

### Fn::GetAtt
<a name="aws-resource-synthetics-group-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-synthetics-group-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
The Id of the group.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
