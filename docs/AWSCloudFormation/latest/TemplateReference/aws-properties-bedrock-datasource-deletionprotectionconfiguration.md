---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-deletionprotectionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource DeletionProtectionConfiguration
<a name="aws-properties-bedrock-datasource-deletionprotectionconfiguration"></a>

Configuration for deletion protection.

## Syntax
<a name="aws-properties-bedrock-datasource-deletionprotectionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-deletionprotectionconfiguration-syntax.json"></a>

```
{
  "[DeletionProtectionStatus](#cfn-bedrock-datasource-deletionprotectionconfiguration-deletionprotectionstatus)" : {{String}},
  "[DeletionProtectionThreshold](#cfn-bedrock-datasource-deletionprotectionconfiguration-deletionprotectionthreshold)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-deletionprotectionconfiguration-syntax.yaml"></a>

```
  [DeletionProtectionStatus](#cfn-bedrock-datasource-deletionprotectionconfiguration-deletionprotectionstatus): {{String}}
  [DeletionProtectionThreshold](#cfn-bedrock-datasource-deletionprotectionconfiguration-deletionprotectionthreshold): {{Integer}}
```

## Properties
<a name="aws-properties-bedrock-datasource-deletionprotectionconfiguration-properties"></a>

`DeletionProtectionStatus`  <a name="cfn-bedrock-datasource-deletionprotectionconfiguration-deletionprotectionstatus"></a>
Enable or disable deletion protection for the connector.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeletionProtectionThreshold`  <a name="cfn-bedrock-datasource-deletionprotectionconfiguration-deletionprotectionthreshold"></a>
The threshold is the maximum percentage of documents that a sync job can delete from your index. If a sync would delete more than this percentage, the sync skips its delete phase, leaving your indexed documents in place. Not supported for the Custom connector.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
