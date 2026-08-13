---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-dlpsetting-microsoftpurviewproviderconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::DLPSetting MicrosoftPurviewProviderConfig
<a name="aws-properties-quicksight-dlpsetting-microsoftpurviewproviderconfig"></a>

<a name="aws-properties-quicksight-dlpsetting-microsoftpurviewproviderconfig-description"></a>The `MicrosoftPurviewProviderConfig` property type specifies Property description not available. for an [AWS::QuickSight::DLPSetting](aws-resource-quicksight-dlpsetting.md).

## Syntax
<a name="aws-properties-quicksight-dlpsetting-microsoftpurviewproviderconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-dlpsetting-microsoftpurviewproviderconfig-syntax.json"></a>

```
{
  "[Credentials](#cfn-quicksight-dlpsetting-microsoftpurviewproviderconfig-credentials)" : {{MicrosoftPurviewCredentials}},
  "[LabelActionMappings](#cfn-quicksight-dlpsetting-microsoftpurviewproviderconfig-labelactionmappings)" : {{[ LabelActionMapping, ... ]}},
  "[UnmappedAction](#cfn-quicksight-dlpsetting-microsoftpurviewproviderconfig-unmappedaction)" : {{String}}
}
```

### YAML
<a name="aws-properties-quicksight-dlpsetting-microsoftpurviewproviderconfig-syntax.yaml"></a>

```
  [Credentials](#cfn-quicksight-dlpsetting-microsoftpurviewproviderconfig-credentials): {{
    MicrosoftPurviewCredentials}}
  [LabelActionMappings](#cfn-quicksight-dlpsetting-microsoftpurviewproviderconfig-labelactionmappings): {{
    - LabelActionMapping}}
  [UnmappedAction](#cfn-quicksight-dlpsetting-microsoftpurviewproviderconfig-unmappedaction): {{String}}
```

## Properties
<a name="aws-properties-quicksight-dlpsetting-microsoftpurviewproviderconfig-properties"></a>

`Credentials`  <a name="cfn-quicksight-dlpsetting-microsoftpurviewproviderconfig-credentials"></a>
Property description not available.
*Required*: Yes
*Type*: [MicrosoftPurviewCredentials](aws-properties-quicksight-dlpsetting-microsoftpurviewcredentials.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LabelActionMappings`  <a name="cfn-quicksight-dlpsetting-microsoftpurviewproviderconfig-labelactionmappings"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [LabelActionMapping](aws-properties-quicksight-dlpsetting-labelactionmapping.md)
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UnmappedAction`  <a name="cfn-quicksight-dlpsetting-microsoftpurviewproviderconfig-unmappedaction"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `ALLOW | WARN | BLOCK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
