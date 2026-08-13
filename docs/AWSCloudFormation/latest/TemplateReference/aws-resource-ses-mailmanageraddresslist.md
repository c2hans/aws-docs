---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ses-mailmanageraddresslist.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerAddressList
<a name="aws-resource-ses-mailmanageraddresslist"></a>

The structure representing the address lists and address list attribute that will be used in evaluation of boolean expression.

## Syntax
<a name="aws-resource-ses-mailmanageraddresslist-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ses-mailmanageraddresslist-syntax.json"></a>

```
{
  "Type" : "AWS::SES::MailManagerAddressList",
  "Properties" : {
      "[AddressListName](#cfn-ses-mailmanageraddresslist-addresslistname)" : {{String}},
      "[Tags](#cfn-ses-mailmanageraddresslist-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ses-mailmanageraddresslist-syntax.yaml"></a>

```
Type: AWS::SES::MailManagerAddressList
Properties:
  [AddressListName](#cfn-ses-mailmanageraddresslist-addresslistname): {{String}}
  [Tags](#cfn-ses-mailmanageraddresslist-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ses-mailmanageraddresslist-properties"></a>

`AddressListName`  <a name="cfn-ses-mailmanageraddresslist-addresslistname"></a>
A user-friendly name for the address list.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_.-]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ses-mailmanageraddresslist-tags"></a>
The tags used to organize, track, or control access for the resource. For example, { "tags": {"key1":"value1", "key2":"value2"} }.
*Required*: No
*Type*: Array of [Tag](aws-properties-ses-mailmanageraddresslist-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ses-mailmanageraddresslist-return-values"></a>

### Ref
<a name="aws-resource-ses-mailmanageraddresslist-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource ID, such as *al-3qlenopx5xw66ewlx3phx7jz*.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ses-mailmanageraddresslist-return-values-fn--getatt"></a>

####
<a name="aws-resource-ses-mailmanageraddresslist-return-values-fn--getatt-fn--getatt"></a>

`AddressListArn`  <a name="AddressListArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the address list.

`AddressListId`  <a name="AddressListId-fn::getatt"></a>
The identifier of the address list.
