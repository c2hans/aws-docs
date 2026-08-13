---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-smsvoice-protectconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SMSVOICE::ProtectConfiguration
<a name="aws-resource-smsvoice-protectconfiguration"></a>

Create a new protect configuration. By default all country rule sets for each capability are set to `ALLOW`. A protect configurations name is stored as a Tag with the key set to `Name` and value as the name of the protect configuration.

## Syntax
<a name="aws-resource-smsvoice-protectconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-smsvoice-protectconfiguration-syntax.json"></a>

```
{
  "Type" : "AWS::SMSVOICE::ProtectConfiguration",
  "Properties" : {
      "[CountryRuleSet](#cfn-smsvoice-protectconfiguration-countryruleset)" : {{CountryRuleSet}},
      "[DeletionProtectionEnabled](#cfn-smsvoice-protectconfiguration-deletionprotectionenabled)" : {{Boolean}},
      "[Tags](#cfn-smsvoice-protectconfiguration-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-smsvoice-protectconfiguration-syntax.yaml"></a>

```
Type: AWS::SMSVOICE::ProtectConfiguration
Properties:
  [CountryRuleSet](#cfn-smsvoice-protectconfiguration-countryruleset): {{
    CountryRuleSet}}
  [DeletionProtectionEnabled](#cfn-smsvoice-protectconfiguration-deletionprotectionenabled): {{Boolean}}
  [Tags](#cfn-smsvoice-protectconfiguration-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-smsvoice-protectconfiguration-properties"></a>

`CountryRuleSet`  <a name="cfn-smsvoice-protectconfiguration-countryruleset"></a>
The set of `CountryRules` you specify to control which countries AWS End User Messaging SMS can send your messages to.
*Required*: No
*Type*: [CountryRuleSet](aws-properties-smsvoice-protectconfiguration-countryruleset.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeletionProtectionEnabled`  <a name="cfn-smsvoice-protectconfiguration-deletionprotectionenabled"></a>
The status of deletion protection for the protect configuration. When set to true deletion protection is enabled. By default this is set to false.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-smsvoice-protectconfiguration-tags"></a>
An array of key and value pair tags that are associated with the resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-smsvoice-protectconfiguration-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-smsvoice-protectconfiguration-return-values"></a>

### Ref
<a name="aws-resource-smsvoice-protectconfiguration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns`ProtectConfigurationId`.

### Fn::GetAtt
<a name="aws-resource-smsvoice-protectconfiguration-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-smsvoice-protectconfiguration-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the protect configuration.

`ProtectConfigurationId`  <a name="ProtectConfigurationId-fn::getatt"></a>
The unique identifier for the protect configuration.
