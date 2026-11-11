---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53profiles-profileassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53Profiles::ProfileAssociation
<a name="aws-resource-route53profiles-profileassociation"></a>

 An association between a Route 53 Profile and a VPC.

## Syntax
<a name="aws-resource-route53profiles-profileassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-route53profiles-profileassociation-syntax.json"></a>

```
{
  "Type" : "AWS::Route53Profiles::ProfileAssociation",
  "Properties" : {
      "[Arn](#cfn-route53profiles-profileassociation-arn)" : {{String}},
      "[Name](#cfn-route53profiles-profileassociation-name)" : {{String}},
      "[Priority](#cfn-route53profiles-profileassociation-priority)" : {{Integer}},
      "[ProfileId](#cfn-route53profiles-profileassociation-profileid)" : {{String}},
      "[ResourceId](#cfn-route53profiles-profileassociation-resourceid)" : {{String}},
      "[Tags](#cfn-route53profiles-profileassociation-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-route53profiles-profileassociation-syntax.yaml"></a>

```
Type: AWS::Route53Profiles::ProfileAssociation
Properties:
  [Arn](#cfn-route53profiles-profileassociation-arn): {{String}}
  [Name](#cfn-route53profiles-profileassociation-name): {{String}}
  [Priority](#cfn-route53profiles-profileassociation-priority): {{Integer}}
  [ProfileId](#cfn-route53profiles-profileassociation-profileid): {{String}}
  [ResourceId](#cfn-route53profiles-profileassociation-resourceid): {{String}}
  [Tags](#cfn-route53profiles-profileassociation-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-route53profiles-profileassociation-properties"></a>

`Arn`  <a name="cfn-route53profiles-profileassociation-arn"></a>
The Amazon Resource Name (ARN) of the profile association to a VPC.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-route53profiles-profileassociation-name"></a>
 Name of the Profile association.
*Required*: Yes
*Type*: String
*Pattern*: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
*Minimum*: `0`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Priority`  <a name="cfn-route53profiles-profileassociation-priority"></a>
The priority of the Profile association, from 100 to 9900. Route 53 VPC Resolver evaluates the Profile associations for a VPC in priority order, starting with the lowest value. A lower value means a higher priority.
Priority is optional when the VPC has no other Profile associations and defaults to 100. When the VPC already has a Profile association, you must specify a `Priority` that no other Profile association for that VPC uses.
Changing `Priority` updates the association in place without replacement. Only the account that created the Profile association can change its priority.
This value sets the evaluation order of the Profiles associated with a VPC. It's different from the DNS Firewall rule group priority in the `ResourceProperties` of a `ProfileResourceAssociation`.
*Required*: No
*Type*: Integer
*Minimum*: `100`
*Maximum*: `9900`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProfileId`  <a name="cfn-route53profiles-profileassociation-profileid"></a>
 ID of the Profile.
A VPC can have up to two Profile associations. For more information, see [Route 53 Profiles](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/profiles.html).
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceId`  <a name="cfn-route53profiles-profileassociation-resourceid"></a>
 The ID of the VPC.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-route53profiles-profileassociation-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-route53profiles-profileassociation-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-route53profiles-profileassociation-return-values"></a>

### Ref
<a name="aws-resource-route53profiles-profileassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns`ProfileAssociation` ID for the profile association to a VPC, such as `rpassoc-a6d96d8cexample4`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-route53profiles-profileassociation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-route53profiles-profileassociation-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
 ID of the Profile association.
