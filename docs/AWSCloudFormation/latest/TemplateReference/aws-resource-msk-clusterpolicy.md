---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-msk-clusterpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::ClusterPolicy
<a name="aws-resource-msk-clusterpolicy"></a>

Create or update cluster policy.

## Syntax
<a name="aws-resource-msk-clusterpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-msk-clusterpolicy-syntax.json"></a>

```
{
  "Type" : "AWS::MSK::ClusterPolicy",
  "Properties" : {
      "[ClusterArn](#cfn-msk-clusterpolicy-clusterarn)" : {{String}},
      "[Policy](#cfn-msk-clusterpolicy-policy)" : {{Json}}
    }
}
```

### YAML
<a name="aws-resource-msk-clusterpolicy-syntax.yaml"></a>

```
Type: AWS::MSK::ClusterPolicy
Properties:
  [ClusterArn](#cfn-msk-clusterpolicy-clusterarn): {{String}}
  [Policy](#cfn-msk-clusterpolicy-policy): {{Json}}
```

## Properties
<a name="aws-resource-msk-clusterpolicy-properties"></a>

`ClusterArn`  <a name="cfn-msk-clusterpolicy-clusterarn"></a>
The Amazon Resource Name (ARN) that uniquely identifies the cluster.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[\w-]+:kafka:[\w-]+:\d+:cluster.*\Z`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Policy`  <a name="cfn-msk-clusterpolicy-policy"></a>
Resource policy for the cluster. The maximum size supported for a resource-based policy document is 20 KB.
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-msk-clusterpolicy-return-values"></a>

### Ref
<a name="aws-resource-msk-clusterpolicy-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the cluster for the resource policy.

For Amazon MSK cluster policy `MyClusterPolicy`, `Ref` returns the cluster ARN for the resource policy whose logical ID is `MyClusterPolicy`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-msk-clusterpolicy-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-msk-clusterpolicy-return-values-fn--getatt-fn--getatt"></a>

`CurrentVersion`  <a name="CurrentVersion-fn::getatt"></a>
The current version of the policy attached to the specified cluster.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
