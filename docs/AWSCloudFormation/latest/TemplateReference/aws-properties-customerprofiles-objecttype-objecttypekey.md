---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-objecttype-objecttypekey.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::ObjectType ObjectTypeKey
<a name="aws-properties-customerprofiles-objecttype-objecttypekey"></a>

An object that defines the Key element of a ProfileObject. A Key is a special element that can be used to search for a customer profile.

## Syntax
<a name="aws-properties-customerprofiles-objecttype-objecttypekey-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-objecttype-objecttypekey-syntax.json"></a>

```
{
  "[FieldNames](#cfn-customerprofiles-objecttype-objecttypekey-fieldnames)" : {{[ String, ... ]}},
  "[StandardIdentifiers](#cfn-customerprofiles-objecttype-objecttypekey-standardidentifiers)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-customerprofiles-objecttype-objecttypekey-syntax.yaml"></a>

```
  [FieldNames](#cfn-customerprofiles-objecttype-objecttypekey-fieldnames): {{
    - String}}
  [StandardIdentifiers](#cfn-customerprofiles-objecttype-objecttypekey-standardidentifiers): {{
    - String}}
```

## Properties
<a name="aws-properties-customerprofiles-objecttype-objecttypekey-properties"></a>

`FieldNames`  <a name="cfn-customerprofiles-objecttype-objecttypekey-fieldnames"></a>
The reference for the key name of the fields map.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StandardIdentifiers`  <a name="cfn-customerprofiles-objecttype-objecttypekey-standardidentifiers"></a>
The types of keys that a ProfileObject can have. Each ProfileObject can have only 1 UNIQUE key but multiple PROFILE keys. PROFILE means that this key can be used to tie an object to a PROFILE. UNIQUE means that it can be used to uniquely identify an object. If a key a is marked as SECONDARY, it will be used to search for profiles after all other PROFILE keys have been searched. A LOOKUP\_ONLY key is only used to match a profile but is not persisted to be used for searching of the profile. A NEW\_ONLY key is only used if the profile does not already exist before the object is ingested, otherwise it is only used for matching objects to profiles.
*Required*: No
*Type*: Array of String
*Allowed values*: `PROFILE | UNIQUE | SECONDARY | LOOKUP_ONLY | NEW_ONLY | ASSET | CASE | ORDER | AIR_PREFERENCE | AIR_BOOKING | AIR_SEGMENT | HOTEL_PREFERENCE | HOTEL_STAY_REVENUE | HOTEL_RESERVATION | LOYALTY | LOYALTY_TRANSACTION | LOYALTY_PROMOTION | WEB_ANALYTICS | DEVICE | COMMUNICATION_RECORD`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
