---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-identitystore-user.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IdentityStore::User
<a name="aws-resource-identitystore-user"></a>

A user object that contains the metadata and attributes for a specified user.

## Syntax
<a name="aws-resource-identitystore-user-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-identitystore-user-syntax.json"></a>

```
{
  "Type" : "AWS::IdentityStore::User",
  "Properties" : {
      "[Addresses](#cfn-identitystore-user-addresses)" : {{[ AddressesItems, ... ]}},
      "[Birthdate](#cfn-identitystore-user-birthdate)" : {{String}},
      "[DisplayName](#cfn-identitystore-user-displayname)" : {{String}},
      "[Emails](#cfn-identitystore-user-emails)" : {{[ EmailsItems, ... ]}},
      "[IdentityStoreId](#cfn-identitystore-user-identitystoreid)" : {{String}},
      "[Locale](#cfn-identitystore-user-locale)" : {{String}},
      "[Name](#cfn-identitystore-user-name)" : {{Name}},
      "[NickName](#cfn-identitystore-user-nickname)" : {{String}},
      "[PhoneNumbers](#cfn-identitystore-user-phonenumbers)" : {{[ PhoneNumbersItems, ... ]}},
      "[Photos](#cfn-identitystore-user-photos)" : {{[ PhotosItems, ... ]}},
      "[PreferredLanguage](#cfn-identitystore-user-preferredlanguage)" : {{String}},
      "[ProfileUrl](#cfn-identitystore-user-profileurl)" : {{String}},
      "[Roles](#cfn-identitystore-user-roles)" : {{[ RolesItems, ... ]}},
      "[Timezone](#cfn-identitystore-user-timezone)" : {{String}},
      "[Title](#cfn-identitystore-user-title)" : {{String}},
      "[UserName](#cfn-identitystore-user-username)" : {{String}},
      "[UserType](#cfn-identitystore-user-usertype)" : {{String}},
      "[Website](#cfn-identitystore-user-website)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-identitystore-user-syntax.yaml"></a>

```
Type: AWS::IdentityStore::User
Properties:
  [Addresses](#cfn-identitystore-user-addresses): {{
    - AddressesItems}}
  [Birthdate](#cfn-identitystore-user-birthdate): {{String}}
  [DisplayName](#cfn-identitystore-user-displayname): {{String}}
  [Emails](#cfn-identitystore-user-emails): {{
    - EmailsItems}}
  [IdentityStoreId](#cfn-identitystore-user-identitystoreid): {{String}}
  [Locale](#cfn-identitystore-user-locale): {{String}}
  [Name](#cfn-identitystore-user-name): {{
    Name}}
  [NickName](#cfn-identitystore-user-nickname): {{String}}
  [PhoneNumbers](#cfn-identitystore-user-phonenumbers): {{
    - PhoneNumbersItems}}
  [Photos](#cfn-identitystore-user-photos): {{
    - PhotosItems}}
  [PreferredLanguage](#cfn-identitystore-user-preferredlanguage): {{String}}
  [ProfileUrl](#cfn-identitystore-user-profileurl): {{String}}
  [Roles](#cfn-identitystore-user-roles): {{
    - RolesItems}}
  [Timezone](#cfn-identitystore-user-timezone): {{String}}
  [Title](#cfn-identitystore-user-title): {{String}}
  [UserName](#cfn-identitystore-user-username): {{String}}
  [UserType](#cfn-identitystore-user-usertype): {{String}}
  [Website](#cfn-identitystore-user-website): {{String}}
```

## Properties
<a name="aws-resource-identitystore-user-properties"></a>

`Addresses`  <a name="cfn-identitystore-user-addresses"></a>
A list of `Address` objects containing addresses associated with the user.
*Required*: No
*Type*: Array of [AddressesItems](aws-properties-identitystore-user-addressesitems.md)
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Birthdate`  <a name="cfn-identitystore-user-birthdate"></a>
The user's birthdate in YYYY-MM-DD format. This field stores personal birthdate information for the user.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-identitystore-user-displayname"></a>
A string containing the name of the user that is formatted for display when the user is referenced. For example, "John Doe."
Prefix search supports a maximum of 1,000 characters for the string.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Emails`  <a name="cfn-identitystore-user-emails"></a>
A list of `Email` objects containing email addresses associated with the user.
*Required*: No
*Type*: Array of [EmailsItems](aws-properties-identitystore-user-emailsitems.md)
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IdentityStoreId`  <a name="cfn-identitystore-user-identitystoreid"></a>
The globally unique identifier for the identity store.
*Required*: Yes
*Type*: String
*Pattern*: `^d-[0-9a-f]{10}$|^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Minimum*: `1`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Locale`  <a name="cfn-identitystore-user-locale"></a>
A string containing the geographical region or location of the user.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-identitystore-user-name"></a>
An object containing the name of the user.
*Required*: No
*Type*: [Name](aws-properties-identitystore-user-name.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NickName`  <a name="cfn-identitystore-user-nickname"></a>
A string containing an alternate name for the user.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PhoneNumbers`  <a name="cfn-identitystore-user-phonenumbers"></a>
A list of `PhoneNumber` objects containing phone numbers associated with the user.
*Required*: No
*Type*: Array of [PhoneNumbersItems](aws-properties-identitystore-user-phonenumbersitems.md)
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Photos`  <a name="cfn-identitystore-user-photos"></a>
A list of photos associated with the user. Users can have up to 3 photos with metadata including type, display name, and primary designation.
*Required*: No
*Type*: Array of [PhotosItems](aws-properties-identitystore-user-photositems.md)
*Maximum*: `3`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PreferredLanguage`  <a name="cfn-identitystore-user-preferredlanguage"></a>
A string containing the preferred language of the user. For example, "American English" or "en-us."
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProfileUrl`  <a name="cfn-identitystore-user-profileurl"></a>
A string containing a URL that might be associated with the user.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Roles`  <a name="cfn-identitystore-user-roles"></a>
A list of `Role` objects containing roles associated with the user.
*Required*: No
*Type*: Array of [RolesItems](aws-properties-identitystore-user-rolesitems.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Timezone`  <a name="cfn-identitystore-user-timezone"></a>
A string containing the time zone of the user.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Title`  <a name="cfn-identitystore-user-title"></a>
A string containing the title of the user. Possible values are left unspecified. The value can vary based on your specific use case.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserName`  <a name="cfn-identitystore-user-username"></a>
A unique string used to identify the user. The length limit is 128 characters. This value can consist of letters, accented characters, symbols, numbers, and punctuation. This value is specified at the time the user is created and stored as an attribute of the user object in the identity store.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}\p{M}\p{S}\p{N}\p{P}]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UserType`  <a name="cfn-identitystore-user-usertype"></a>
A string indicating the type of user. Possible values are left unspecified. The value can vary based on your specific use case.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Website`  <a name="cfn-identitystore-user-website"></a>
The user's personal website or blog URL. This field stores website information for personal or professional use.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-identitystore-user-return-values"></a>

### Ref
<a name="aws-resource-identitystore-user-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-identitystore-user-return-values-fn--getatt"></a>

####
<a name="aws-resource-identitystore-user-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time the user was created.

`CreatedBy`  <a name="CreatedBy-fn::getatt"></a>
The identifier of the user or system that created the user.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time the user was last updated.

`UpdatedBy`  <a name="UpdatedBy-fn::getatt"></a>
The identifier of the user or system that last updated the user.

`UserId`  <a name="UserId-fn::getatt"></a>
The identifier for a user in the identity store.

`UserStatus`  <a name="UserStatus-fn::getatt"></a>
The current status of the user account.
