---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-s3outposts-bucket-filterandoperator.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::S3Outposts::Bucket FilterAndOperator
<a name="aws-properties-s3outposts-bucket-filterandoperator"></a>

<a name="aws-properties-s3outposts-bucket-filterandoperator-description"></a>The `FilterAndOperator` property type specifies Property description not available. for an [AWS::S3Outposts::Bucket](aws-resource-s3outposts-bucket.md).

## Syntax
<a name="aws-properties-s3outposts-bucket-filterandoperator-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-s3outposts-bucket-filterandoperator-syntax.json"></a>

```
{
  "[Prefix](#cfn-s3outposts-bucket-filterandoperator-prefix)" : {{String}},
  "[Tags](#cfn-s3outposts-bucket-filterandoperator-tags)" : {{[ FilterTag, ... ]}}
}
```

### YAML
<a name="aws-properties-s3outposts-bucket-filterandoperator-syntax.yaml"></a>

```
  [Prefix](#cfn-s3outposts-bucket-filterandoperator-prefix): {{String}}
  [Tags](#cfn-s3outposts-bucket-filterandoperator-tags): {{
    - FilterTag}}
```

## Properties
<a name="aws-properties-s3outposts-bucket-filterandoperator-properties"></a>

`Prefix`  <a name="cfn-s3outposts-bucket-filterandoperator-prefix"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-s3outposts-bucket-filterandoperator-tags"></a>
Property description not available.
*Required*: Yes
*Type*: Array of [FilterTag](aws-properties-s3outposts-bucket-filtertag.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
