---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-location-job-joboutputoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Location::Job JobOutputOptions
<a name="aws-properties-location-job-joboutputoptions"></a>

<a name="aws-properties-location-job-joboutputoptions-description"></a>The `JobOutputOptions` property type specifies Property description not available. for an [AWS::Location::Job](aws-resource-location-job.md).

## Syntax
<a name="aws-properties-location-job-joboutputoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-location-job-joboutputoptions-syntax.json"></a>

```
{
  "[Format](#cfn-location-job-joboutputoptions-format)" : {{String}},
  "[Location](#cfn-location-job-joboutputoptions-location)" : {{String}}
}
```

### YAML
<a name="aws-properties-location-job-joboutputoptions-syntax.yaml"></a>

```
  [Format](#cfn-location-job-joboutputoptions-format): {{String}}
  [Location](#cfn-location-job-joboutputoptions-location): {{String}}
```

## Properties
<a name="aws-properties-location-job-joboutputoptions-properties"></a>

`Format`  <a name="cfn-location-job-joboutputoptions-format"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `Parquet`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Location`  <a name="cfn-location-job-joboutputoptions-location"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:aws(-[a-z]+)*:[a-z0-9-]+:[a-z0-9-]*(:\d{12})?:[\w/+=,.-]+|s3://[a-z0-9][a-z0-9._-]{2,254}(/[^/]+)*/)$`
*Maximum*: `300`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
