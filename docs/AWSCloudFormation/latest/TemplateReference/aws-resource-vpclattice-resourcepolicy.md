---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-vpclattice-resourcepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::ResourcePolicy
<a name="aws-resource-vpclattice-resourcepolicy"></a>

Retrieves information about the specified resource policy. The resource policy is an IAM policy created on behalf of the resource owner when they share a resource.

## Syntax
<a name="aws-resource-vpclattice-resourcepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-vpclattice-resourcepolicy-syntax.json"></a>

```
{
  "Type" : "AWS::VpcLattice::ResourcePolicy",
  "Properties" : {
      "[Policy](#cfn-vpclattice-resourcepolicy-policy)" : {{Json}},
      "[ResourceArn](#cfn-vpclattice-resourcepolicy-resourcearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-vpclattice-resourcepolicy-syntax.yaml"></a>

```
Type: AWS::VpcLattice::ResourcePolicy
Properties:
  [Policy](#cfn-vpclattice-resourcepolicy-policy): {{Json}}
  [ResourceArn](#cfn-vpclattice-resourcepolicy-resourcearn): {{String}}
```

## Properties
<a name="aws-resource-vpclattice-resourcepolicy-properties"></a>

`Policy`  <a name="cfn-vpclattice-resourcepolicy-policy"></a>
The Amazon Resource Name (ARN) of the service network or service.
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceArn`  <a name="cfn-vpclattice-resourcepolicy-resourcearn"></a>
An IAM policy.
*Required*: Yes
*Type*: String
*Pattern*: `^arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:((servicenetwork/sn)|(service/svc)|(resourceconfiguration/rcfg))-[0-9a-z]{17}$`
*Minimum*: `20`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-vpclattice-resourcepolicy-return-values"></a>

### Ref
<a name="aws-resource-vpclattice-resourcepolicy-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the resource policy.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).
