---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-smsvoice-senderid.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SMSVOICE::SenderId
<a name="aws-resource-smsvoice-senderid"></a>

Request a new sender ID that doesn't require registration.

## Syntax
<a name="aws-resource-smsvoice-senderid-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-smsvoice-senderid-syntax.json"></a>

```
{
  "Type" : "AWS::SMSVOICE::SenderId",
  "Properties" : {
      "[DeletionProtectionEnabled](#cfn-smsvoice-senderid-deletionprotectionenabled)" : {{Boolean}},
      "[IsoCountryCode](#cfn-smsvoice-senderid-isocountrycode)" : {{String}},
      "[SenderId](#cfn-smsvoice-senderid-senderid)" : {{String}},
      "[Tags](#cfn-smsvoice-senderid-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-smsvoice-senderid-syntax.yaml"></a>

```
Type: AWS::SMSVOICE::SenderId
Properties:
  [DeletionProtectionEnabled](#cfn-smsvoice-senderid-deletionprotectionenabled): {{Boolean}}
  [IsoCountryCode](#cfn-smsvoice-senderid-isocountrycode): {{String}}
  [SenderId](#cfn-smsvoice-senderid-senderid): {{String}}
  [Tags](#cfn-smsvoice-senderid-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-smsvoice-senderid-properties"></a>

`DeletionProtectionEnabled`  <a name="cfn-smsvoice-senderid-deletionprotectionenabled"></a>
By default this is set to false. When set to true the sender ID can't be deleted.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IsoCountryCode`  <a name="cfn-smsvoice-senderid-isocountrycode"></a>
The two-character code, in ISO 3166-1 alpha-2 format, for the country or region.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Z]{2}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SenderId`  <a name="cfn-smsvoice-senderid-senderid"></a>
The sender ID string to request. The sender ID can be 1-11 alphanumeric characters including letters (A-Z, a-z), numbers (0-9), or hyphens (-). The sender ID must contain at least one letter and cannot start or end with a hyphen.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Z0-9_-]+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-smsvoice-senderid-tags"></a>
An array of tags (key and value pairs) to associate with the sender ID.
*Required*: No
*Type*: Array of [Tag](aws-properties-smsvoice-senderid-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-smsvoice-senderid-return-values"></a>

### Ref
<a name="aws-resource-smsvoice-senderid-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns`IsoCountryCode|SenderId`.

### Fn::GetAtt
<a name="aws-resource-smsvoice-senderid-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-smsvoice-senderid-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name of the `SenderId`.
