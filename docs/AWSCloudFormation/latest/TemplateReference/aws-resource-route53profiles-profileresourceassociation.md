---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53profiles-profileresourceassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53Profiles::ProfileResourceAssociation
<a name="aws-resource-route53profiles-profileresourceassociation"></a>

 The association between a Route 53 Profile and resources.

## Syntax
<a name="aws-resource-route53profiles-profileresourceassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-route53profiles-profileresourceassociation-syntax.json"></a>

```
{
  "Type" : "AWS::Route53Profiles::ProfileResourceAssociation",
  "Properties" : {
      "[Name](#cfn-route53profiles-profileresourceassociation-name)" : {{String}},
      "[ProfileId](#cfn-route53profiles-profileresourceassociation-profileid)" : {{String}},
      "[ResourceArn](#cfn-route53profiles-profileresourceassociation-resourcearn)" : {{String}},
      "[ResourceProperties](#cfn-route53profiles-profileresourceassociation-resourceproperties)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-route53profiles-profileresourceassociation-syntax.yaml"></a>

```
Type: AWS::Route53Profiles::ProfileResourceAssociation
Properties:
  [Name](#cfn-route53profiles-profileresourceassociation-name): {{String}}
  [ProfileId](#cfn-route53profiles-profileresourceassociation-profileid): {{String}}
  [ResourceArn](#cfn-route53profiles-profileresourceassociation-resourcearn): {{String}}
  [ResourceProperties](#cfn-route53profiles-profileresourceassociation-resourceproperties): {{String}}
```

## Properties
<a name="aws-resource-route53profiles-profileresourceassociation-properties"></a>

`Name`  <a name="cfn-route53profiles-profileresourceassociation-name"></a>
 Name of the Profile resource association.
*Required*: Yes
*Type*: String
*Pattern*: `(?!^[0-9]+$)([a-zA-Z0-9\-_' ']+)`
*Minimum*: `0`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProfileId`  <a name="cfn-route53profiles-profileresourceassociation-profileid"></a>
 Profile ID of the Profile that the resources are associated with.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceArn`  <a name="cfn-route53profiles-profileresourceassociation-resourcearn"></a>
 The Amazon Resource Name (ARN) of the resource association.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceProperties`  <a name="cfn-route53profiles-profileresourceassociation-resourceproperties"></a>
 If the DNS resource is a DNS Firewall rule group, this indicates the priority.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-route53profiles-profileresourceassociation-return-values"></a>

### Ref
<a name="aws-resource-route53profiles-profileresourceassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns`ProfileResourceAssociation` ID for the profile resource association, such as `rpr-001ba2563f9example6`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-route53profiles-profileresourceassociation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-route53profiles-profileresourceassociation-return-values-fn--getatt-fn--getatt"></a>

`Id`  <a name="Id-fn::getatt"></a>
 ID of the Profile resource association.

`ResourceType`  <a name="ResourceType-fn::getatt"></a>
 Resource type, such as a private hosted zone, interface VPC endpoint, Resolver query log configuration, or DNS Firewall rule group.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
