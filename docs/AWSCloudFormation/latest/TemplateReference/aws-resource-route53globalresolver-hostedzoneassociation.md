---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53globalresolver-hostedzoneassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53GlobalResolver::HostedZoneAssociation
<a name="aws-resource-route53globalresolver-hostedzoneassociation"></a>

Associates a Route 53 private hosted zone with a Route 53 Global Resolver resource. This allows the resolver to resolve DNS queries for the private hosted zone from anywhere globally.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Syntax
<a name="aws-resource-route53globalresolver-hostedzoneassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-route53globalresolver-hostedzoneassociation-syntax.json"></a>

```
{
  "Type" : "AWS::Route53GlobalResolver::HostedZoneAssociation",
  "Properties" : {
      "[HostedZoneId](#cfn-route53globalresolver-hostedzoneassociation-hostedzoneid)" : {{String}},
      "[Name](#cfn-route53globalresolver-hostedzoneassociation-name)" : {{String}},
      "[ResourceArn](#cfn-route53globalresolver-hostedzoneassociation-resourcearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-route53globalresolver-hostedzoneassociation-syntax.yaml"></a>

```
Type: AWS::Route53GlobalResolver::HostedZoneAssociation
Properties:
  [HostedZoneId](#cfn-route53globalresolver-hostedzoneassociation-hostedzoneid): {{String}}
  [Name](#cfn-route53globalresolver-hostedzoneassociation-name): {{String}}
  [ResourceArn](#cfn-route53globalresolver-hostedzoneassociation-resourcearn): {{String}}
```

## Properties
<a name="aws-resource-route53globalresolver-hostedzoneassociation-properties"></a>

`HostedZoneId`  <a name="cfn-route53globalresolver-hostedzoneassociation-hostedzoneid"></a>
The ID of the hosted zone.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `32`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-route53globalresolver-hostedzoneassociation-name"></a>
The name of the hosted zone association.
*Required*: Yes
*Type*: String
*Pattern*: `(?!^[0-9]+$)([a-zA-Z0-9-_' ']+)`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceArn`  <a name="cfn-route53globalresolver-hostedzoneassociation-resourcearn"></a>
The Amazon Resource Name (ARN) of the resource associated with the hosted zone.
*Required*: Yes
*Type*: String
*Pattern*: `arn:[-.a-z0-9]{1,63}:[-.a-z0-9]{1,63}:[-.a-z0-9]{0,63}:[-.a-z0-9]{0,63}:[^/].{0,1023}`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-route53globalresolver-hostedzoneassociation-return-values"></a>

### Ref
<a name="aws-resource-route53globalresolver-hostedzoneassociation-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-route53globalresolver-hostedzoneassociation-return-values-fn--getatt"></a>

####
<a name="aws-resource-route53globalresolver-hostedzoneassociation-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time when the hosted zone association was created.

`HostedZoneAssociationId`  <a name="HostedZoneAssociationId-fn::getatt"></a>
ID of the private hosted zone association.

`HostedZoneName`  <a name="HostedZoneName-fn::getatt"></a>
The name of the hosted zone.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the hosted zone association.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time when the hosted zone association was last updated.
