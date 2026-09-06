---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-identitystore-user-name.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IdentityStore::User Name
<a name="aws-properties-identitystore-user-name"></a>

The full name of the user.

## Syntax
<a name="aws-properties-identitystore-user-name-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-identitystore-user-name-syntax.json"></a>

```
{
  "[FamilyName](#cfn-identitystore-user-name-familyname)" : {{String}},
  "[Formatted](#cfn-identitystore-user-name-formatted)" : {{String}},
  "[GivenName](#cfn-identitystore-user-name-givenname)" : {{String}},
  "[HonorificPrefix](#cfn-identitystore-user-name-honorificprefix)" : {{String}},
  "[HonorificSuffix](#cfn-identitystore-user-name-honorificsuffix)" : {{String}},
  "[MiddleName](#cfn-identitystore-user-name-middlename)" : {{String}}
}
```

### YAML
<a name="aws-properties-identitystore-user-name-syntax.yaml"></a>

```
  [FamilyName](#cfn-identitystore-user-name-familyname): {{String}}
  [Formatted](#cfn-identitystore-user-name-formatted): {{String}}
  [GivenName](#cfn-identitystore-user-name-givenname): {{String}}
  [HonorificPrefix](#cfn-identitystore-user-name-honorificprefix): {{String}}
  [HonorificSuffix](#cfn-identitystore-user-name-honorificsuffix): {{String}}
  [MiddleName](#cfn-identitystore-user-name-middlename): {{String}}
```

## Properties
<a name="aws-properties-identitystore-user-name-properties"></a>

`FamilyName`  <a name="cfn-identitystore-user-name-familyname"></a>
The family name of the user.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Formatted`  <a name="cfn-identitystore-user-name-formatted"></a>
A string containing a formatted version of the name for display.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`GivenName`  <a name="cfn-identitystore-user-name-givenname"></a>
The given name of the user.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HonorificPrefix`  <a name="cfn-identitystore-user-name-honorificprefix"></a>
The honorific prefix of the user. For example, "Dr."
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`HonorificSuffix`  <a name="cfn-identitystore-user-name-honorificsuffix"></a>
The honorific suffix of the user. For example, "M.D."
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MiddleName`  <a name="cfn-identitystore-user-name-middlename"></a>
The middle name of the user.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
