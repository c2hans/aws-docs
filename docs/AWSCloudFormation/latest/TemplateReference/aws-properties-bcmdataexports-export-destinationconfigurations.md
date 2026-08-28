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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
