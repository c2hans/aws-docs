---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iottwinmaker-metadatatransferjob.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTTwinMaker::MetadataTransferJob
<a name="aws-resource-iottwinmaker-metadatatransferjob"></a>

<a name="aws-resource-iottwinmaker-metadatatransferjob-description"></a>The `AWS::IoTTwinMaker::MetadataTransferJob` resource Property description not available. for IoTTwinMaker.

## Syntax
<a name="aws-resource-iottwinmaker-metadatatransferjob-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iottwinmaker-metadatatransferjob-syntax.json"></a>

```
{
  "Type" : "AWS::IoTTwinMaker::MetadataTransferJob",
  "Properties" : {
      "[Description](#cfn-iottwinmaker-metadatatransferjob-description)" : {{String}},
      "[Destination](#cfn-iottwinmaker-metadatatransferjob-destination)" : {{DestinationConfiguration}},
      "[MetadataTransferJobId](#cfn-iottwinmaker-metadatatransferjob-metadatatransferjobid)" : {{String}},
      "[Sources](#cfn-iottwinmaker-metadatatransferjob-sources)" : {{[ SourceConfiguration, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-iottwinmaker-metadatatransferjob-syntax.yaml"></a>

```
Type: AWS::IoTTwinMaker::MetadataTransferJob
Properties:
  [Description](#cfn-iottwinmaker-metadatatransferjob-description): {{String}}
  [Destination](#cfn-iottwinmaker-metadatatransferjob-destination): {{
    DestinationConfiguration}}
  [MetadataTransferJobId](#cfn-iottwinmaker-metadatatransferjob-metadatatransferjobid): {{String}}
  [Sources](#cfn-iottwinmaker-metadatatransferjob-sources): {{
    - SourceConfiguration}}
```

## Properties
<a name="aws-resource-iottwinmaker-metadatatransferjob-properties"></a>

`Description`  <a name="cfn-iottwinmaker-metadatatransferjob-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Destination`  <a name="cfn-iottwinmaker-metadatatransferjob-destination"></a>
Property description not available.
*Required*: Yes
*Type*: [DestinationConfiguration](aws-properties-iottwinmaker-metadatatransferjob-destinationconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MetadataTransferJobId`  <a name="cfn-iottwinmaker-metadatatransferjob-metadatatransferjobid"></a>
The metadata transfer job summary Id.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z_0-9][a-zA-Z_\-0-9]*[a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Sources`  <a name="cfn-iottwinmaker-metadatatransferjob-sources"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [SourceConfiguration](aws-properties-iottwinmaker-metadatatransferjob-sourceconfiguration.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-iottwinmaker-metadatatransferjob-return-values"></a>

### Ref
<a name="aws-resource-iottwinmaker-metadatatransferjob-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-iottwinmaker-metadatatransferjob-return-values-fn--getatt"></a>

####
<a name="aws-resource-iottwinmaker-metadatatransferjob-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The metadata transfer job summary ARN.

`CreationDateTime`  <a name="CreationDateTime-fn::getatt"></a>
The metadata transfer job summary creation DateTime object.

`UpdateDateTime`  <a name="UpdateDateTime-fn::getatt"></a>
The metadata transfer job summary update DateTime object
