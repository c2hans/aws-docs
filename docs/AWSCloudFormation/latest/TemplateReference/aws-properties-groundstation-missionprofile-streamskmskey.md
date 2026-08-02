---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-groundstation-missionprofile-streamskmskey.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::GroundStation::MissionProfile StreamsKmsKey
<a name="aws-properties-groundstation-missionprofile-streamskmskey"></a>

KMS key info.

## Syntax
<a name="aws-properties-groundstation-missionprofile-streamskmskey-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-groundstation-missionprofile-streamskmskey-syntax.json"></a>

```
{
  "[KmsAliasArn](#cfn-groundstation-missionprofile-streamskmskey-kmsaliasarn)" : {{String}},
  "[KmsAliasName](#cfn-groundstation-missionprofile-streamskmskey-kmsaliasname)" : {{String}},
  "[KmsKeyArn](#cfn-groundstation-missionprofile-streamskmskey-kmskeyarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-groundstation-missionprofile-streamskmskey-syntax.yaml"></a>

```
  [KmsAliasArn](#cfn-groundstation-missionprofile-streamskmskey-kmsaliasarn): {{String}}
  [KmsAliasName](#cfn-groundstation-missionprofile-streamskmskey-kmsaliasname): {{String}}
  [KmsKeyArn](#cfn-groundstation-missionprofile-streamskmskey-kmskeyarn): {{String}}
```

## Properties
<a name="aws-properties-groundstation-missionprofile-streamskmskey-properties"></a>

`KmsAliasArn`  <a name="cfn-groundstation-missionprofile-streamskmskey-kmsaliasarn"></a>
KMS Alias Arn.
*Required*: No
*Type*: String
*Pattern*: `^(arn:(aws[a-zA-Z-]*)?:[a-z0-9-.]+:.*)|()$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsAliasName`  <a name="cfn-groundstation-missionprofile-streamskmskey-kmsaliasname"></a>
KMS Alias Name.
*Required*: No
*Type*: String
*Pattern*: `^alias/[a-zA-Z0-9:/_-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-groundstation-missionprofile-streamskmskey-kmskeyarn"></a>
KMS Key Arn.
*Required*: No
*Type*: String
*Pattern*: `^(arn:(aws[a-zA-Z-]*)?:[a-z0-9-.]+:.*)|()$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
