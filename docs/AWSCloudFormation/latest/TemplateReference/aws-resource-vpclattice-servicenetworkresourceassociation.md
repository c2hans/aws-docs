---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-vpclattice-servicenetworkresourceassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::ServiceNetworkResourceAssociation
<a name="aws-resource-vpclattice-servicenetworkresourceassociation"></a>

Associates the specified service network with the specified resource configuration. This allows the resource configuration to receive connections through the service network, including through a service network VPC endpoint.

## Syntax
<a name="aws-resource-vpclattice-servicenetworkresourceassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-vpclattice-servicenetworkresourceassociation-syntax.json"></a>

```
{
  "Type" : "AWS::VpcLattice::ServiceNetworkResourceAssociation",
  "Properties" : {
      "[PrivateDnsEnabled](#cfn-vpclattice-servicenetworkresourceassociation-privatednsenabled)" : {{Boolean}},
      "[ResourceConfigurationId](#cfn-vpclattice-servicenetworkresourceassociation-resourceconfigurationid)" : {{String}},
      "[ServiceNetworkId](#cfn-vpclattice-servicenetworkresourceassociation-servicenetworkid)" : {{String}},
      "[Tags](#cfn-vpclattice-servicenetworkresourceassociation-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-vpclattice-servicenetworkresourceassociation-syntax.yaml"></a>

```
Type: AWS::VpcLattice::ServiceNetworkResourceAssociation
Properties:
  [PrivateDnsEnabled](#cfn-vpclattice-servicenetworkresourceassociation-privatednsenabled): {{Boolean}}
  [ResourceConfigurationId](#cfn-vpclattice-servicenetworkresourceassociation-resourceconfigurationid): {{String}}
  [ServiceNetworkId](#cfn-vpclattice-servicenetworkresourceassociation-servicenetworkid): {{String}}
  [Tags](#cfn-vpclattice-servicenetworkresourceassociation-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-vpclattice-servicenetworkresourceassociation-properties"></a>

`PrivateDnsEnabled`  <a name="cfn-vpclattice-servicenetworkresourceassociation-privatednsenabled"></a>
 Indicates if private DNS is enabled for the service network resource association.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceConfigurationId`  <a name="cfn-vpclattice-servicenetworkresourceassociation-resourceconfigurationid"></a>
The ID of the resource configuration associated with the service network.
*Required*: No
*Type*: String
*Pattern*: `^rcfg-[0-9a-z]{17}$`
*Minimum*: `17`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ServiceNetworkId`  <a name="cfn-vpclattice-servicenetworkresourceassociation-servicenetworkid"></a>
The ID of the service network associated with the resource configuration.
*Required*: No
*Type*: String
*Pattern*: `^((sn-[0-9a-z]{17})|(arn:[a-z0-9\-]+:vpc-lattice:[a-zA-Z0-9\-]+:\d{12}:servicenetwork/sn-[0-9a-z]{17}))$`
*Minimum*: `3`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-vpclattice-servicenetworkresourceassociation-tags"></a>
A key-value pair to associate with a resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-vpclattice-servicenetworkresourceassociation-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-vpclattice-servicenetworkresourceassociation-return-values"></a>

### Ref
<a name="aws-resource-vpclattice-servicenetworkresourceassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the association.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-vpclattice-servicenetworkresourceassociation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-vpclattice-servicenetworkresourceassociation-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the association.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the association between the service network and resource configuration.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
