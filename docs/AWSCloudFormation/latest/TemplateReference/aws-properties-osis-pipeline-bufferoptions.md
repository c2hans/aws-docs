---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-osis-pipeline-bufferoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OSIS::Pipeline BufferOptions
<a name="aws-properties-osis-pipeline-bufferoptions"></a>

Options that specify the configuration of a persistent buffer. To configure how OpenSearch Ingestion encrypts this data, set the `EncryptionAtRestOptions`. For more information, see [Persistent buffering](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/osis-features-overview.html#persistent-buffering).

## Syntax
<a name="aws-properties-osis-pipeline-bufferoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-osis-pipeline-bufferoptions-syntax.json"></a>

```
{
  "[PersistentBufferEnabled](#cfn-osis-pipeline-bufferoptions-persistentbufferenabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-osis-pipeline-bufferoptions-syntax.yaml"></a>

```
  [PersistentBufferEnabled](#cfn-osis-pipeline-bufferoptions-persistentbufferenabled): {{Boolean}}
```

## Properties
<a name="aws-properties-osis-pipeline-bufferoptions-properties"></a>

`PersistentBufferEnabled`  <a name="cfn-osis-pipeline-bufferoptions-persistentbufferenabled"></a>
Whether persistent buffering should be enabled.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
