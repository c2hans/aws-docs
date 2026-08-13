---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53resolver-resolverconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53Resolver::ResolverConfig
<a name="aws-resource-route53resolver-resolverconfig"></a>

A complex type that contains information about a Resolver configuration for a VPC.

## Syntax
<a name="aws-resource-route53resolver-resolverconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-route53resolver-resolverconfig-syntax.json"></a>

```
{
  "Type" : "AWS::Route53Resolver::ResolverConfig",
  "Properties" : {
      "[AutodefinedReverseFlag](#cfn-route53resolver-resolverconfig-autodefinedreverseflag)" : {{String}},
      "[ResourceId](#cfn-route53resolver-resolverconfig-resourceid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-route53resolver-resolverconfig-syntax.yaml"></a>

```
Type: AWS::Route53Resolver::ResolverConfig
Properties:
  [AutodefinedReverseFlag](#cfn-route53resolver-resolverconfig-autodefinedreverseflag): {{String}}
  [ResourceId](#cfn-route53resolver-resolverconfig-resourceid): {{String}}
```

## Properties
<a name="aws-resource-route53resolver-resolverconfig-properties"></a>

`AutodefinedReverseFlag`  <a name="cfn-route53resolver-resolverconfig-autodefinedreverseflag"></a>
Represents the desired status of `AutodefinedReverse`. The only supported value on creation is `DISABLE`. Deletion of this resource will return `AutodefinedReverse` to its default value of `ENABLED`.
*Required*: Yes
*Type*: String
*Allowed values*: `DISABLE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceId`  <a name="cfn-route53resolver-resolverconfig-resourceid"></a>
The ID of the Amazon Virtual Private Cloud VPC or a Route 53 Profile that you're configuring Resolver for.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-route53resolver-resolverconfig-return-values"></a>

### Ref
<a name="aws-resource-route53resolver-resolverconfig-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `ResolverConfiguration` ID.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-route53resolver-resolverconfig-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-route53resolver-resolverconfig-return-values-fn--getatt-fn--getatt"></a>

`AutodefinedReverse`  <a name="AutodefinedReverse-fn::getatt"></a>
The status of whether or not the Route 53 Resolver will create autodefined rules for reverse DNS lookups. This is enabled by default.

`Id`  <a name="Id-fn::getatt"></a>
ID for the Route 53 Resolver configuration.

`OwnerId`  <a name="OwnerId-fn::getatt"></a>
The owner account ID of the Amazon Virtual Private Cloud VPC.
