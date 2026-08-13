---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datazone-userprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::UserProfile
<a name="aws-resource-datazone-userprofile"></a>

The user type of the user for which the user profile is created.

## Syntax
<a name="aws-resource-datazone-userprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-datazone-userprofile-syntax.json"></a>

```
{
  "Type" : "AWS::DataZone::UserProfile",
  "Properties" : {
      "[DomainIdentifier](#cfn-datazone-userprofile-domainidentifier)" : {{String}},
      "[SessionName](#cfn-datazone-userprofile-sessionname)" : {{String}},
      "[Status](#cfn-datazone-userprofile-status)" : {{String}},
      "[UserIdentifier](#cfn-datazone-userprofile-useridentifier)" : {{String}},
      "[UserType](#cfn-datazone-userprofile-usertype)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-datazone-userprofile-syntax.yaml"></a>

```
Type: AWS::DataZone::UserProfile
Properties:
  [DomainIdentifier](#cfn-datazone-userprofile-domainidentifier): {{String}}
  [SessionName](#cfn-datazone-userprofile-sessionname): {{String}}
  [Status](#cfn-datazone-userprofile-status): {{String}}
  [UserIdentifier](#cfn-datazone-userprofile-useridentifier): {{String}}
  [UserType](#cfn-datazone-userprofile-usertype): {{String}}
```

## Properties
<a name="aws-resource-datazone-userprofile-properties"></a>

`DomainIdentifier`  <a name="cfn-datazone-userprofile-domainidentifier"></a>
The identifier of a Amazon DataZone domain in which a user profile exists.
*Required*: Yes
*Type*: String
*Pattern*: `^dzd[-_][a-zA-Z0-9_-]{1,36}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SessionName`  <a name="cfn-datazone-userprofile-sessionname"></a>
The session name for IAM role sessions.
*Required*: No
*Type*: String
*Minimum*: `2`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-datazone-userprofile-status"></a>
The status of the user profile.
*Required*: No
*Type*: String
*Allowed values*: `ASSIGNED | NOT_ASSIGNED | ACTIVATED | DEACTIVATED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserIdentifier`  <a name="cfn-datazone-userprofile-useridentifier"></a>
The identifier of the user for which the user profile is created.
*Required*: Yes
*Type*: String
*Pattern*: `(^([0-9a-f]{10}-|)[A-Fa-f0-9]{8}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{4}-[A-Fa-f0-9]{12}$|^[a-zA-Z_0-9+=,.@-]+$|^arn:aws:iam::\d{12}:.+$)`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UserType`  <a name="cfn-datazone-userprofile-usertype"></a>
The user type of the user for which the user profile is created.
*Required*: No
*Type*: String
*Allowed values*: `IAM_USER | IAM_ROLE | SSO_USER | IAM_ROLE_SESSION`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-datazone-userprofile-return-values"></a>

### Ref
<a name="aws-resource-datazone-userprofile-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a string containing pipe-separated `DomainId` and `UserProfileId` that uniquely identify the user profile. For example: `{ "Ref": "MyUserProfile" }` for the resource with the logical ID `MyUserProfile`, `Ref` returns `DomainId|UserProfileId`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-datazone-userprofile-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-datazone-userprofile-return-values-fn--getatt-fn--getatt"></a>

`DomainId`  <a name="DomainId-fn::getatt"></a>
The identifier of a Amazon DataZone domain in which a user profile exists.

`Id`  <a name="Id-fn::getatt"></a>
The ID of the user profile.

`Type`  <a name="Type-fn::getatt"></a>
The type of the user profile.
