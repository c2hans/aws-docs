---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cloudwatch-alert-nodata.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::Alert NoData
<a name="aws-properties-cloudwatch-alert-nodata"></a>

How the alert behaves when an evaluation returns no data. If omitted, the alert reports NODATA.

## Syntax
<a name="aws-properties-cloudwatch-alert-nodata-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cloudwatch-alert-nodata-syntax.json"></a>

```
{
  "[TreatAs](#cfn-cloudwatch-alert-nodata-treatas)" : {{String}}
}
```

### YAML
<a name="aws-properties-cloudwatch-alert-nodata-syntax.yaml"></a>

```
  [TreatAs](#cfn-cloudwatch-alert-nodata-treatas): {{String}}
```

## Properties
<a name="aws-properties-cloudwatch-alert-nodata-properties"></a>

`TreatAs`  <a name="cfn-cloudwatch-alert-nodata-treatas"></a>
The state to report when an evaluation returns no data. Valid values: OK, WARNING, CRITICAL, NODATA.
*Required*: Yes
*Type*: String
*Allowed values*: `OK | WARNING | CRITICAL | NODATA`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
