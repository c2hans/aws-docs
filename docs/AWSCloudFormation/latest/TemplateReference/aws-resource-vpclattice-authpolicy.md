---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-vpclattice-authpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::AuthPolicy
<a name="aws-resource-vpclattice-authpolicy"></a>

Creates or updates the auth policy. The policy string in JSON must not contain newlines or blank lines.

For more information, see [Auth policies](https://docs.aws.amazon.com/vpc-lattice/latest/ug/auth-policies.html) in the *Amazon VPC Lattice User Guide*.

## Syntax
<a name="aws-resource-vpclattice-authpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-vpclattice-authpolicy-syntax.json"></a>

```
{
  "Type" : "AWS::VpcLattice::AuthPolicy",
  "Properties" : {
      "[Policy](#cfn-vpclattice-authpolicy-policy)" : {{Json}},
      "[ResourceIdentifier](#cfn-vpclattice-authpolicy-resourceidentifier)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-vpclattice-authpolicy-syntax.yaml"></a>

```
Type: AWS::VpcLattice::AuthPolicy
Properties:
  [Policy](#cfn-vpclattice-authpolicy-policy): {{Json}}
  [ResourceIdentifier](#cfn-vpclattice-authpolicy-resourceidentifier): {{String}}
```

## Properties
<a name="aws-resource-vpclattice-authpolicy-properties"></a>

`Policy`  <a name="cfn-vpclattice-authpolicy-policy"></a>
The auth policy.
*Required*: Yes
*Type*: Json
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceIdentifier`  <a name="cfn-vpclattice-authpolicy-resourceidentifier"></a>
The ID or ARN of the service network or service for which the policy is created.
*Required*: Yes
*Type*: String
*Pattern*: `^((((sn)|(svc))-[0-9a-z]{17})|(arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:((servicenetwork/sn)|(service/svc))-[0-9a-z]{17}))$`
*Minimum*: `17`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-vpclattice-authpolicy-return-values"></a>

### Ref
<a name="aws-resource-vpclattice-authpolicy-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the auth policy.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-vpclattice-authpolicy-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-vpclattice-authpolicy-return-values-fn--getatt-fn--getatt"></a>

`State`  <a name="State-fn::getatt"></a>
The state of the auth policy. The auth policy is only active when the auth type is set to `AWS_IAM`. If you provide a policy, then authentication and authorization decisions are made based on this policy and the client's IAM policy. If the auth type is `NONE`, then any auth policy you provide will remain inactive.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
