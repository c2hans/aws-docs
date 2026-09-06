---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bcmdataexports-export-destinationconfigurations.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BCMDataExports::Export DestinationConfigurations
<a name="aws-properties-bcmdataexports-export-destinationconfigurations"></a>

The destinations used for data exports.

## Syntax
<a name="aws-properties-bcmdataexports-export-destinationconfigurations-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bcmdataexports-export-destinationconfigurations-syntax.json"></a>

```
{
  "[S3Destination](#cfn-bcmdataexports-export-destinationconfigurations-s3destination)" : {{S3Destination}}
}
```

### YAML
<a name="aws-properties-bcmdataexports-export-destinationconfigurations-syntax.yaml"></a>

```
  [S3Destination](#cfn-bcmdataexports-export-destinationconfigurations-s3destination): {{
    S3Destination}}
```

## Properties
<a name="aws-properties-bcmdataexports-export-destinationconfigurations-properties"></a>

`S3Destination`  <a name="cfn-bcmdataexports-export-destinationconfigurations-s3destination"></a>
An object that describes the destination of the data exports file.
*Required*: Yes
*Type*: [S3Destination](aws-properties-bcmdataexports-export-s3destination.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
