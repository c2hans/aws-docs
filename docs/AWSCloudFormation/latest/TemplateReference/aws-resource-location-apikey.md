---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-location-apikey.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Location::APIKey
<a name="aws-resource-location-apikey"></a>

The API key resource in your AWS account, which lets you grant actions for Amazon Location resources to the API key bearer.

## Syntax
<a name="aws-resource-location-apikey-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-location-apikey-syntax.json"></a>

```
{
  "Type" : "AWS::Location::APIKey",
  "Properties" : {
      "[Description](#cfn-location-apikey-description)" : {{String}},
      "[ExpireTime](#cfn-location-apikey-expiretime)" : {{String}},
      "[ForceDelete](#cfn-location-apikey-forcedelete)" : {{Boolean}},
      "[ForceUpdate](#cfn-location-apikey-forceupdate)" : {{Boolean}},
      "[KeyName](#cfn-location-apikey-keyname)" : {{String}},
      "[NoExpiry](#cfn-location-apikey-noexpiry)" : {{Boolean}},
      "[Restrictions](#cfn-location-apikey-restrictions)" : {{ApiKeyRestrictions}},
      "[Tags](#cfn-location-apikey-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-location-apikey-syntax.yaml"></a>

```
Type: AWS::Location::APIKey
Properties:
  [Description](#cfn-location-apikey-description): {{String}}
  [ExpireTime](#cfn-location-apikey-expiretime): {{String}}
  [ForceDelete](#cfn-location-apikey-forcedelete): {{Boolean}}
  [ForceUpdate](#cfn-location-apikey-forceupdate): {{Boolean}}
  [KeyName](#cfn-location-apikey-keyname): {{String}}
  [NoExpiry](#cfn-location-apikey-noexpiry): {{Boolean}}
  [Restrictions](#cfn-location-apikey-restrictions): {{
    ApiKeyRestrictions}}
  [Tags](#cfn-location-apikey-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-location-apikey-properties"></a>

`Description`  <a name="cfn-location-apikey-description"></a>
Updates the description for the API key resource.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExpireTime`  <a name="cfn-location-apikey-expiretime"></a>
The optional timestamp for when the API key resource will expire in [ISO 8601 format](https://www.iso.org/iso-8601-date-and-time-format.html).
*Required*: No
*Type*: String
*Pattern*: `^([0-2]\d{3})-(0[0-9]|1[0-2])-([0-2]\d|3[01])T([01]\d|2[0-4]):([0-5]\d):([0-6]\d)((\.\d{3})?)Z$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ForceDelete`  <a name="cfn-location-apikey-forcedelete"></a>
ForceDelete bypasses an API key's expiry conditions and deletes the key. Set the parameter `true` to delete the key or to `false` to not preemptively delete the API key.
Valid values: `true`, or `false`.
This action is irreversible. Only use ForceDelete if you are certain the key is no longer in use.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ForceUpdate`  <a name="cfn-location-apikey-forceupdate"></a>
The boolean flag to be included for updating `ExpireTime` or Restrictions details. Must be set to `true` to update an API key resource that has been used in the past 7 days. `False` if force update is not preferred.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KeyName`  <a name="cfn-location-apikey-keyname"></a>
A custom name for the API key resource.
Requirements:
+ Contain only alphanumeric characters (A–Z, a–z, 0–9), hyphens (-), periods (.), and underscores (\_).
+ Must be a unique API key name.
+ No spaces allowed. For example, `ExampleAPIKey`.
*Required*: Yes
*Type*: String
*Pattern*: `^[-._\w]+$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`NoExpiry`  <a name="cfn-location-apikey-noexpiry"></a>
Whether the API key should expire. Set to `true` to set the API key to have no expiration time.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Restrictions`  <a name="cfn-location-apikey-restrictions"></a>
The API key restrictions for the API key resource.
*Required*: Yes
*Type*: [ApiKeyRestrictions](aws-properties-location-apikey-apikeyrestrictions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-location-apikey-tags"></a>
Applies one or more tags to the map resource. A tag is a key-value pair that helps manage, identify, search, and filter your resources by labelling them.
*Required*: No
*Type*: Array of [Tag](aws-properties-location-apikey-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-location-apikey-return-values"></a>

### Ref
<a name="aws-resource-location-apikey-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the `APIKey`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-location-apikey-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-location-apikey-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the resource. Used when you need to specify a resource across all AWS.

`CreateTime`  <a name="CreateTime-fn::getatt"></a>
The timestamp for when the API key resource was created in ISO 8601 format: YYYY-MM-DDThh:mm:ss.sssZ.

`KeyArn`  <a name="KeyArn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the API key resource. Used when you need to specify a resource across all AWS.

`UpdateTime`  <a name="UpdateTime-fn::getatt"></a>
The timestamp for when the API key resource was last updated in ISO 8601 format: `YYYY-MM-DDThh:mm:ss.sssZ`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
