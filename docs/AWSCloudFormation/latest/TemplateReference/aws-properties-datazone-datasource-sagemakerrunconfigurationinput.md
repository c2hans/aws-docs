---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-datasource-sagemakerrunconfigurationinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::DataSource SageMakerRunConfigurationInput
<a name="aws-properties-datazone-datasource-sagemakerrunconfigurationinput"></a>

The Amazon SageMaker run configuration.

## Syntax
<a name="aws-properties-datazone-datasource-sagemakerrunconfigurationinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-datasource-sagemakerrunconfigurationinput-syntax.json"></a>

```
{
  "[TrackingAssets](#cfn-datazone-datasource-sagemakerrunconfigurationinput-trackingassets)" : {{{{{Key}}: {{Value}}, ...}}}
}
```

### YAML
<a name="aws-properties-datazone-datasource-sagemakerrunconfigurationinput-syntax.yaml"></a>

```
  [TrackingAssets](#cfn-datazone-datasource-sagemakerrunconfigurationinput-trackingassets): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-properties-datazone-datasource-sagemakerrunconfigurationinput-properties"></a>

`TrackingAssets`  <a name="cfn-datazone-datasource-sagemakerrunconfigurationinput-trackingassets"></a>
The tracking assets of the Amazon SageMaker run.
*Required*: Yes
*Type*: Object of Array
*Pattern*: `^.{1,64}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
