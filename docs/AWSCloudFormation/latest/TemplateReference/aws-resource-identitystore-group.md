---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-identitystore-group.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IdentityStore::Group
<a name="aws-resource-identitystore-group"></a>

A group object, which contains a specified group’s metadata and attributes.

## Syntax
<a name="aws-resource-identitystore-group-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-identitystore-group-syntax.json"></a>

```
{
  "Type" : "AWS::IdentityStore::Group",
  "Properties" : {
      "[Description](#cfn-identitystore-group-description)" : {{String}},
      "[DisplayName](#cfn-identitystore-group-displayname)" : {{String}},
      "[IdentityStoreId](#cfn-identitystore-group-identitystoreid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-identitystore-group-syntax.yaml"></a>

```
Type: AWS::IdentityStore::Group
Properties:
  [Description](#cfn-identitystore-group-description): {{String}}
  [DisplayName](#cfn-identitystore-group-displayname): {{String}}
  [IdentityStoreId](#cfn-identitystore-group-identitystoreid): {{String}}
```

## Properties
<a name="aws-resource-identitystore-group-properties"></a>

`Description`  <a name="cfn-identitystore-group-description"></a>
A string containing the description of the group.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r 　]+$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-identitystore-group-displayname"></a>
The display name value for the group. The length limit is 1,024 characters. This value can consist of letters, accented characters, symbols, numbers, punctuation, tab, new line, carriage return, space, and nonbreaking space in this attribute. This value is specified at the time the group is created and stored as an attribute of the group object in the identity store.
Prefix search supports a maximum of 1,000 characters for the string.
*Required*: Yes
*Type*: String
*Pattern*: `^[\p{L}\p{M}\p{S}\p{N}\p{P}\t\n\r ]+$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdentityStoreId`  <a name="cfn-identitystore-group-identitystoreid"></a>
The globally unique identifier for the identity store.
*Required*: Yes
*Type*: String
*Pattern*: `^d-[0-9a-f]{10}$|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Minimum*: `1`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-identitystore-group-return-values"></a>

### Ref
<a name="aws-resource-identitystore-group-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `Physical ID` of the resource created which is the format `GroupID|IdentityStoreId`.

### Fn::GetAtt
<a name="aws-resource-identitystore-group-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-identitystore-group-return-values-fn--getatt-fn--getatt"></a>

`GroupId`  <a name="GroupId-fn::getatt"></a>
The identifier of the newly created group in the identity store.

## Examples
<a name="aws-resource-identitystore-group--examples"></a>

### Declare a Identity Store Resource
<a name="aws-resource-identitystore-group--examples--Declare_a_Identity_Store_Resource"></a>

The following example shows how to create a Identity Store `Group` resource:

#### JSON
<a name="aws-resource-identitystore-group--examples--Declare_a_Identity_Store_Resource--json"></a>

```
{
  "Type": "AWS::IdentityStore::Group",
  "Properties": {
    "Description": {
      "description": "Group for developers",
    },
    "DisplayName": {
      "description": "Developers",
    },
    "IdentityStoreId": {
      "description": "d-1111111111",

    }
}
```

#### YAML
<a name="aws-resource-identitystore-group--examples--Declare_a_Identity_Store_Resource--yaml"></a>

```
Type: AWS::IdentityStore::Group
    Properties:
       Description: "Group for Developers"
       DisplayName: "Developers"
       IdentityStoreId: "d-1111111111a"
```
