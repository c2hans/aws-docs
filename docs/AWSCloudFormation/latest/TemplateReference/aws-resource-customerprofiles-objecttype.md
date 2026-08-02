---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-customerprofiles-objecttype.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::ObjectType
<a name="aws-resource-customerprofiles-objecttype"></a>

Specifies an Amazon Connect Customer Profiles Object Type Mapping.

## Syntax
<a name="aws-resource-customerprofiles-objecttype-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-customerprofiles-objecttype-syntax.json"></a>

```
{
  "Type" : "AWS::CustomerProfiles::ObjectType",
  "Properties" : {
      "[AllowProfileCreation](#cfn-customerprofiles-objecttype-allowprofilecreation)" : {{Boolean}},
      "[Description](#cfn-customerprofiles-objecttype-description)" : {{String}},
      "[DomainName](#cfn-customerprofiles-objecttype-domainname)" : {{String}},
      "[EncryptionKey](#cfn-customerprofiles-objecttype-encryptionkey)" : {{String}},
      "[ExpirationDays](#cfn-customerprofiles-objecttype-expirationdays)" : {{Integer}},
      "[Fields](#cfn-customerprofiles-objecttype-fields)" : {{[ FieldMap, ... ]}},
      "[Keys](#cfn-customerprofiles-objecttype-keys)" : {{[ KeyMap, ... ]}},
      "[MaxProfileObjectCount](#cfn-customerprofiles-objecttype-maxprofileobjectcount)" : {{Integer}},
      "[ObjectTypeName](#cfn-customerprofiles-objecttype-objecttypename)" : {{String}},
      "[SourceLastUpdatedTimestampFormat](#cfn-customerprofiles-objecttype-sourcelastupdatedtimestampformat)" : {{String}},
      "[SourcePriority](#cfn-customerprofiles-objecttype-sourcepriority)" : {{Integer}},
      "[Tags](#cfn-customerprofiles-objecttype-tags)" : {{[ Tag, ... ]}},
      "[TemplateId](#cfn-customerprofiles-objecttype-templateid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-customerprofiles-objecttype-syntax.yaml"></a>

```
Type: AWS::CustomerProfiles::ObjectType
Properties:
  [AllowProfileCreation](#cfn-customerprofiles-objecttype-allowprofilecreation): {{Boolean}}
  [Description](#cfn-customerprofiles-objecttype-description): {{String}}
  [DomainName](#cfn-customerprofiles-objecttype-domainname): {{String}}
  [EncryptionKey](#cfn-customerprofiles-objecttype-encryptionkey): {{String}}
  [ExpirationDays](#cfn-customerprofiles-objecttype-expirationdays): {{Integer}}
  [Fields](#cfn-customerprofiles-objecttype-fields): {{
    - FieldMap}}
  [Keys](#cfn-customerprofiles-objecttype-keys): {{
    - KeyMap}}
  [MaxProfileObjectCount](#cfn-customerprofiles-objecttype-maxprofileobjectcount): {{Integer}}
  [ObjectTypeName](#cfn-customerprofiles-objecttype-objecttypename): {{String}}
  [SourceLastUpdatedTimestampFormat](#cfn-customerprofiles-objecttype-sourcelastupdatedtimestampformat): {{String}}
  [SourcePriority](#cfn-customerprofiles-objecttype-sourcepriority): {{Integer}}
  [Tags](#cfn-customerprofiles-objecttype-tags): {{
    - Tag}}
  [TemplateId](#cfn-customerprofiles-objecttype-templateid): {{String}}
```

## Properties
<a name="aws-resource-customerprofiles-objecttype-properties"></a>

`AllowProfileCreation`  <a name="cfn-customerprofiles-objecttype-allowprofilecreation"></a>
Indicates whether a profile should be created when data is received if one doesn’t exist for an object of this type. The default is `FALSE`. If the AllowProfileCreation flag is set to `FALSE`, then the service tries to fetch a standard profile and associate this object with the profile. If it is set to `TRUE`, and if no match is found, then the service creates a new standard profile.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-customerprofiles-objecttype-description"></a>
The description of the profile object type mapping.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `10000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainName`  <a name="cfn-customerprofiles-objecttype-domainname"></a>
The unique name of the domain.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EncryptionKey`  <a name="cfn-customerprofiles-objecttype-encryptionkey"></a>
The customer-provided key to encrypt the profile object that will be created in this profile object type mapping. If not specified the system will use the encryption key of the domain.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExpirationDays`  <a name="cfn-customerprofiles-objecttype-expirationdays"></a>
The number of days until the data of this type expires.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `1098`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Fields`  <a name="cfn-customerprofiles-objecttype-fields"></a>
A list of field definitions for the object type mapping.
*Required*: No
*Type*: Array of [FieldMap](aws-properties-customerprofiles-objecttype-fieldmap.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Keys`  <a name="cfn-customerprofiles-objecttype-keys"></a>
A list of keys that can be used to map data to the profile or search for the profile.
*Required*: No
*Type*: Array of [KeyMap](aws-properties-customerprofiles-objecttype-keymap.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxProfileObjectCount`  <a name="cfn-customerprofiles-objecttype-maxprofileobjectcount"></a>
The amount of profile object max count assigned to the object type.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ObjectTypeName`  <a name="cfn-customerprofiles-objecttype-objecttypename"></a>
The name of the profile object type.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceLastUpdatedTimestampFormat`  <a name="cfn-customerprofiles-objecttype-sourcelastupdatedtimestampformat"></a>
The format of your sourceLastUpdatedTimestamp that was previously set up.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SourcePriority`  <a name="cfn-customerprofiles-objecttype-sourcepriority"></a>
An integer that determines the priority of this object type when data from multiple sources is ingested. Lower values take priority. Object types without a specified source priority default to the lowest priority.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-customerprofiles-objecttype-tags"></a>
The tags used to organize, track, or control access for this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-customerprofiles-objecttype-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TemplateId`  <a name="cfn-customerprofiles-objecttype-templateid"></a>
A unique identifier for the template mapping. This can be used instead of specifying the Keys and Fields properties directly.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-customerprofiles-objecttype-return-values"></a>

### Ref
<a name="aws-resource-customerprofiles-objecttype-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the DomainName and the ObjectTypeName of the object type.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-customerprofiles-objecttype-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-customerprofiles-objecttype-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp of when the object type was created.

`LastUpdatedAt`  <a name="LastUpdatedAt-fn::getatt"></a>
The timestamp of when the object type was most recently edited.

`MaxAvailableProfileObjectCount`  <a name="MaxAvailableProfileObjectCount-fn::getatt"></a>
The amount of provisioned profile object max count available.

## Examples
<a name="aws-resource-customerprofiles-objecttype--examples"></a>

The following example creates a object type if Domain existed.

###
<a name="aws-resource-customerprofiles-objecttype--examples--"></a>

#### YAML
<a name="aws-resource-customerprofiles-objecttype--examples----yaml"></a>

```
Type: "AWS::CustomerProfiles::ObjectType"
Properties:
    DomainName: "ExampleDomain"
    ObjectTypeName: "ExampleObjectType"
    AllowProfileCreation: false
    Description: "Description Example"
    ExpirationDays: 1
    Fields:
      - Name: "email"
        ObjectTypeField:
          Source: "_source.email"
          Target: "_profile.BusinessEmail"
          ContentType: "EMAIL_ADDRESS"
    Keys:
      - Name: "_email"
        ObjectTypeKeyList:
          - FieldNames:
            - "email"
            StandardIdentifiers:
              - "PROFILE"
              - "UNIQUE"
```

#### JSON
<a name="aws-resource-customerprofiles-objecttype--examples----json"></a>

```
"Type": "AWS::CustomerProfiles::ObjectType",
"Properties": {
    "DomainName": "ExampleDomain",
    "ObjectTypeName": "ExampleObjectType",
    "AllowProfileCreation": false,
    "Description": "Description Example",
    "ExpirationDays": 1,
    "Fields": [{
        "Name": "email",
        "ObjectTypeField": {
            "Source": "_source.email",
            "Target": "_profile.BusinessEmail",
            "ContentType": "EMAIL_ADDRESS"
        }
    }],
    "Keys": [{
        "Name": "_email",
        "ObjectTypeKeyList": [{
            "FieldNames": [ "email" ],
            "StandardIdentifiers": [ "PROFILE", "UNIQUE" ]
        }]
    }]
}
```
