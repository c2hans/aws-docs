---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datazone-groupprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::GroupProfile
<a name="aws-resource-datazone-groupprofile"></a>

The details of a group profile in Amazon DataZone.

## Syntax
<a name="aws-resource-datazone-groupprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-datazone-groupprofile-syntax.json"></a>

```
{
  "Type" : "AWS::DataZone::GroupProfile",
  "Properties" : {
      "[DomainIdentifier](#cfn-datazone-groupprofile-domainidentifier)" : {{String}},
      "[GroupIdentifier](#cfn-datazone-groupprofile-groupidentifier)" : {{String}},
      "[GroupType](#cfn-datazone-groupprofile-grouptype)" : {{String}},
      "[RolePrincipalArn](#cfn-datazone-groupprofile-roleprincipalarn)" : {{String}},
      "[Status](#cfn-datazone-groupprofile-status)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-datazone-groupprofile-syntax.yaml"></a>

```
Type: AWS::DataZone::GroupProfile
Properties:
  [DomainIdentifier](#cfn-datazone-groupprofile-domainidentifier): {{String}}
  [GroupIdentifier](#cfn-datazone-groupprofile-groupidentifier): {{String}}
  [GroupType](#cfn-datazone-groupprofile-grouptype): {{String}}
  [RolePrincipalArn](#cfn-datazone-groupprofile-roleprincipalarn): {{String}}
  [Status](#cfn-datazone-groupprofile-status): {{String}}
```

## Properties
<a name="aws-resource-datazone-groupprofile-properties"></a>

`DomainIdentifier`  <a name="cfn-datazone-groupprofile-domainidentifier"></a>
The identifier of the Amazon DataZone domain in which a group profile exists.
*Required*: Yes
*Type*: String
*Pattern*: `^dzd[-_][a-zA-Z0-9_-]{1,36}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GroupIdentifier`  <a name="cfn-datazone-groupprofile-groupidentifier"></a>
The ID of the group of a project member.
*Required*: No
*Type*: String
*Pattern*: `(^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$|[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r ]+)`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`GroupType`  <a name="cfn-datazone-groupprofile-grouptype"></a>
The group type for which to search.
*Required*: No
*Type*: String
*Allowed values*: `DATAZONE_SSO_GROUP | IAM_ROLE_SESSION_GROUP`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RolePrincipalArn`  <a name="cfn-datazone-groupprofile-roleprincipalarn"></a>
The ARN of the IAM role principal. This role is associated with the group profile.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Status`  <a name="cfn-datazone-groupprofile-status"></a>
The status of a group profile.
*Required*: No
*Type*: String
*Allowed values*: `ASSIGNED | NOT_ASSIGNED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-datazone-groupprofile-return-values"></a>

### Ref
<a name="aws-resource-datazone-groupprofile-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a string containing pipe-separated `DomainId` and `GroupProfileId` that uniquely identify the group profile. For example: `{ "Ref": "MyGroupProfile" }` for the resource with the logical ID `MyGroupProfile`, `Ref` returns `DomainId|GroupProfileId`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-datazone-groupprofile-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-datazone-groupprofile-return-values-fn--getatt-fn--getatt"></a>

`DomainId`  <a name="DomainId-fn::getatt"></a>
The identifier of the Amazon DataZone domain in which a group profile exists.

`GroupName`  <a name="GroupName-fn::getatt"></a>
The name of a group profile.

`Id`  <a name="Id-fn::getatt"></a>
The ID of a group profile.

`RolePrincipalId`  <a name="RolePrincipalId-fn::getatt"></a>
The unique identifier of the IAM role principal. This principal is associated with the group profile.
