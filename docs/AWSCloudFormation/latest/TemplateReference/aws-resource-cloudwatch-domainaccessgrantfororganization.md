---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-domainaccessgrantfororganization.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::DomainAccessGrantForOrganization
<a name="aws-resource-cloudwatch-domainaccessgrantfororganization"></a>

Resource Type definition for `AWS::CloudWatch::DomainAccessGrantForOrganization`. An organization access grant authorizes a principal to administer an organization-scoped CloudWatch Omni domain.

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
The unique identifier of the organization domain the grant applies to.
*Required*: Yes
*Type*: String
*Pattern*: `^d-[0-9a-z]{1,25}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-cloudwatch-domainaccessgrantfororganization-name"></a>
The name of the grant.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Permission`  <a name="cfn-cloudwatch-domainaccessgrantfororganization-permission"></a>
The permission level the grant confers. Organization grants are administrative only.
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
An array of key-value pairs to apply to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-cloudwatch-domainaccessgrantfororganization-tag.md)
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-cloudwatch-domainaccessgrantfororganization-return-values"></a>

### Ref
<a name="aws-resource-cloudwatch-domainaccessgrantfororganization-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the value of the `Arn` property.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudwatch-domainaccessgrantfororganization-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudwatch-domainaccessgrantfororganization-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the organization access grant.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The time the grant was created.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
The principal that created the grant.

`GrantId`  <a name="GrantId-fn::getatt"></a>
The unique identifier of the grant.

`GrantType`  <a name="GrantType-fn::getatt"></a>
Whether the grant is managed by the service or by the customer.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The time the grant was last updated.
