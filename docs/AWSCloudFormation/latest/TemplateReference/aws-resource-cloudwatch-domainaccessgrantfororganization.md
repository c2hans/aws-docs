---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-domainaccessgrantfororganization.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::DomainAccessGrantForOrganization
<a name="aws-resource-cloudwatch-domainaccessgrantfororganization"></a>

<a name="aws-resource-cloudwatch-domainaccessgrantfororganization-description"></a>The `AWS::CloudWatch::DomainAccessGrantForOrganization` resource Property description not available. for CloudWatch.

## Syntax
<a name="aws-resource-cloudwatch-domainaccessgrantfororganization-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudwatch-domainaccessgrantfororganization-syntax.json"></a>

```
{
  "Type" : "AWS::CloudWatch::DomainAccessGrantForOrganization",
  "Properties" : {
      "[DomainId](#cfn-cloudwatch-domainaccessgrantfororganization-domainid)" : {{String}},
      "[Name](#cfn-cloudwatch-domainaccessgrantfororganization-name)" : {{String}},
      "[Permission](#cfn-cloudwatch-domainaccessgrantfororganization-permission)" : {{String}},
      "[Principal](#cfn-cloudwatch-domainaccessgrantfororganization-principal)" : {{OrganizationAccessGrantPrincipal}},
      "[Tags](#cfn-cloudwatch-domainaccessgrantfororganization-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cloudwatch-domainaccessgrantfororganization-syntax.yaml"></a>

```
Type: AWS::CloudWatch::DomainAccessGrantForOrganization
Properties:
  [DomainId](#cfn-cloudwatch-domainaccessgrantfororganization-domainid): {{String}}
  [Name](#cfn-cloudwatch-domainaccessgrantfororganization-name): {{String}}
  [Permission](#cfn-cloudwatch-domainaccessgrantfororganization-permission): {{String}}
  [Principal](#cfn-cloudwatch-domainaccessgrantfororganization-principal): {{
    OrganizationAccessGrantPrincipal}}
  [Tags](#cfn-cloudwatch-domainaccessgrantfororganization-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cloudwatch-domainaccessgrantfororganization-properties"></a>

`DomainId`  <a name="cfn-cloudwatch-domainaccessgrantfororganization-domainid"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^d-[0-9a-z]{1,25}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-cloudwatch-domainaccessgrantfororganization-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Permission`  <a name="cfn-cloudwatch-domainaccessgrantfororganization-permission"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `ADMIN`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Principal`  <a name="cfn-cloudwatch-domainaccessgrantfororganization-principal"></a>
Property description not available.
*Required*: Yes
*Type*: [OrganizationAccessGrantPrincipal](aws-properties-cloudwatch-domainaccessgrantfororganization-organizationaccessgrantprincipal.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cloudwatch-domainaccessgrantfororganization-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudwatch-domainaccessgrantfororganization-tag.md)
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-cloudwatch-domainaccessgrantfororganization-return-values"></a>

### Ref
<a name="aws-resource-cloudwatch-domainaccessgrantfororganization-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-cloudwatch-domainaccessgrantfororganization-return-values-fn--getatt"></a>

####
<a name="aws-resource-cloudwatch-domainaccessgrantfororganization-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Property description not available.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
Property description not available.

`GrantId`  <a name="GrantId-fn::getatt"></a>
Property description not available.

`GrantType`  <a name="GrantType-fn::getatt"></a>
Property description not available.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
Property description not available.
