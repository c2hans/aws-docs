---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-vpclattice-domainverification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::DomainVerification
<a name="aws-resource-vpclattice-domainverification"></a>

A domain name verification is an entity that allows you to prove your ownership of a given domain. When you create a domain verification using CloudFormation, use a waiter to make sure the domain verification is complete before you create a service network resource association, a VPC endpoint, or a service network VPC association with this domain.

## Syntax
<a name="aws-resource-vpclattice-domainverification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-vpclattice-domainverification-syntax.json"></a>

```
{
  "Type" : "AWS::VpcLattice::DomainVerification",
  "Properties" : {
      "[DomainName](#cfn-vpclattice-domainverification-domainname)" : {{String}},
      "[Tags](#cfn-vpclattice-domainverification-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-vpclattice-domainverification-syntax.yaml"></a>

```
Type: AWS::VpcLattice::DomainVerification
Properties:
  [DomainName](#cfn-vpclattice-domainverification-domainname): {{String}}
  [Tags](#cfn-vpclattice-domainverification-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-vpclattice-domainverification-properties"></a>

`DomainName`  <a name="cfn-vpclattice-domainverification-domainname"></a>
 The domain name being verified.
*Required*: Yes
*Type*: String
*Minimum*: `3`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-vpclattice-domainverification-tags"></a>
 The tags associated with the domain verification.
*Required*: No
*Type*: Array of [Tag](aws-properties-vpclattice-domainverification-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-vpclattice-domainverification-return-values"></a>

### Ref
<a name="aws-resource-vpclattice-domainverification-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-vpclattice-domainverification-return-values-fn--getatt"></a>

####
<a name="aws-resource-vpclattice-domainverification-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
 The Amazon Resource Name (ARN) of the domain verification.

`Id`  <a name="Id-fn::getatt"></a>
 The ID of the domain verification.

`Status`  <a name="Status-fn::getatt"></a>
 The current status of the domain verification process.
