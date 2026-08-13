---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iottwinmaker-metadatatransferjob-destinationconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTTwinMaker::MetadataTransferJob DestinationConfiguration
<a name="aws-properties-iottwinmaker-metadatatransferjob-destinationconfiguration"></a>

<a name="aws-properties-iottwinmaker-metadatatransferjob-destinationconfiguration-description"></a>The `DestinationConfiguration` property type specifies Property description not available. for an [AWS::IoTTwinMaker::MetadataTransferJob](aws-resource-iottwinmaker-metadatatransferjob.md).

## Syntax
<a name="aws-properties-iottwinmaker-metadatatransferjob-destinationconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iottwinmaker-metadatatransferjob-destinationconfiguration-syntax.json"></a>

```
{
  "[S3Configuration](#cfn-iottwinmaker-metadatatransferjob-destinationconfiguration-s3configuration)" : {{S3DestinationConfiguration}},
  "[Type](#cfn-iottwinmaker-metadatatransferjob-destinationconfiguration-type)" : {{String}}
}
```

### YAML
<a name="aws-properties-iottwinmaker-metadatatransferjob-destinationconfiguration-syntax.yaml"></a>

```
  [S3Configuration](#cfn-iottwinmaker-metadatatransferjob-destinationconfiguration-s3configuration): {{
    S3DestinationConfiguration}}
  [Type](#cfn-iottwinmaker-metadatatransferjob-destinationconfiguration-type): {{String}}
```

## Properties
<a name="aws-properties-iottwinmaker-metadatatransferjob-destinationconfiguration-properties"></a>

`S3Configuration`  <a name="cfn-iottwinmaker-metadatatransferjob-destinationconfiguration-s3configuration"></a>
Property description not available.
*Required*: No
*Type*: [S3DestinationConfiguration](aws-properties-iottwinmaker-metadatatransferjob-s3destinationconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-iottwinmaker-metadatatransferjob-destinationconfiguration-type"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `s3 | iotsitewise | iottwinmaker | S3 | IOTSITEWISE | IOTTWINMAKER`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
