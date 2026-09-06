---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-contactlist.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::ContactList
<a name="aws-resource-ses-contactlist"></a>

A list that contains contacts that have subscribed to a particular topic or topics.

## Syntax
<a name="aws-resource-ses-contactlist-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ses-contactlist-syntax.json"></a>

```
{
  "Type" : "AWS::SES::ContactList",
  "Properties" : {
      "[ContactListName](#cfn-ses-contactlist-contactlistname)" : {{String}},
      "[Description](#cfn-ses-contactlist-description)" : {{String}},
      "[Tags](#cfn-ses-contactlist-tags)" : {{[ Tag, ... ]}},
      "[Topics](#cfn-ses-contactlist-topics)" : {{[ Topic, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ses-contactlist-syntax.yaml"></a>

```
Type: AWS::SES::ContactList
Properties:
  [ContactListName](#cfn-ses-contactlist-contactlistname): {{String}}
  [Description](#cfn-ses-contactlist-description): {{String}}
  [Tags](#cfn-ses-contactlist-tags): {{
    - Tag}}
  [Topics](#cfn-ses-contactlist-topics): {{
    - Topic}}
```

## Properties
<a name="aws-resource-ses-contactlist-properties"></a>

`ContactListName`  <a name="cfn-ses-contactlist-contactlistname"></a>
The name of the contact list.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]{1,64}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-ses-contactlist-description"></a>
A description of what the contact list is about.
*Required*: No
*Type*: String
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ses-contactlist-tags"></a>
The tags associated with a contact list.
*Required*: No
*Type*: Array of [Tag](aws-properties-ses-contactlist-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Topics`  <a name="cfn-ses-contactlist-topics"></a>
An interest group, theme, or label within a list. A contact list can have multiple topics.
*Required*: No
*Type*: Array of [Topic](aws-properties-ses-contactlist-topic.md)
*Minimum*: `0`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ses-contactlist-return-values"></a>

### Ref
<a name="aws-resource-ses-contactlist-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic Ref function, Ref returns the resource name. For example:

 `{ "Ref" : "ContactListName" }`

For the Amazon SES ContactList, `Ref` returns the name of the contact list.
