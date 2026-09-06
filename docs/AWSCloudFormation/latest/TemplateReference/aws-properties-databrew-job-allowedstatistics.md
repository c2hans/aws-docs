---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-databrew-job-allowedstatistics.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataBrew::Job AllowedStatistics
<a name="aws-properties-databrew-job-allowedstatistics"></a>

Configuration of statistics that are allowed to be run on columns that contain detected entities. When undefined, no statistics will be computed on columns that contain detected entities.

## Syntax
<a name="aws-properties-databrew-job-allowedstatistics-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-databrew-job-allowedstatistics-syntax.json"></a>

```
{
  "[Statistics](#cfn-databrew-job-allowedstatistics-statistics)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-databrew-job-allowedstatistics-syntax.yaml"></a>

```
  [Statistics](#cfn-databrew-job-allowedstatistics-statistics): {{
    - String}}
```

## Properties
<a name="aws-properties-databrew-job-allowedstatistics-properties"></a>

`Statistics`  <a name="cfn-databrew-job-allowedstatistics-statistics"></a>
One or more column statistics to allow for columns that contain detected entities.
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
