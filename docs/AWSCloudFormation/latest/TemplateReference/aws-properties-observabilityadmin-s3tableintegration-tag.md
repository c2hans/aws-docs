---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-s3tableintegration-tag.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::S3TableIntegration Tag
<a name="aws-properties-observabilityadmin-s3tableintegration-tag"></a>

The key-value pairs to associate with the S3 Table integration resource for categorization and management purposes.

## Syntax
<a name="aws-properties-observabilityadmin-s3tableintegration-tag-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-s3tableintegration-tag-syntax.json"></a>

```
{
  "[Key](#cfn-observabilityadmin-s3tableintegration-tag-key)" : {{String}},
  "[Value](#cfn-observabilityadmin-s3tableintegration-tag-value)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-s3tableintegration-tag-syntax.yaml"></a>

```
  [Key](#cfn-observabilityadmin-s3tableintegration-tag-key): {{String}}
  [Value](#cfn-observabilityadmin-s3tableintegration-tag-value): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-s3tableintegration-tag-properties"></a>

`Key`  <a name="cfn-observabilityadmin-s3tableintegration-tag-key"></a>
One part of a key-value pair that makes up a tag associated with the S3 Table integration. A key is a general label that acts like a category for more specific tag values.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-observabilityadmin-s3tableintegration-tag-value"></a>
One part of a key-value pair that makes up a tag associated with an S3 Table integration. A value acts as a descriptor within a tag category (key). The value can be empty or null.
*Required*: Yes
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
