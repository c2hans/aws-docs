---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-comprehend-entityrecognizer-entityrecognizerentitylist.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Comprehend::EntityRecognizer EntityRecognizerEntityList
<a name="aws-properties-comprehend-entityrecognizer-entityrecognizerentitylist"></a>

Describes the entity list submitted with an entity recognizer.

## Syntax
<a name="aws-properties-comprehend-entityrecognizer-entityrecognizerentitylist-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-comprehend-entityrecognizer-entityrecognizerentitylist-syntax.json"></a>

```
{
  "[S3Uri](#cfn-comprehend-entityrecognizer-entityrecognizerentitylist-s3uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-comprehend-entityrecognizer-entityrecognizerentitylist-syntax.yaml"></a>

```
  [S3Uri](#cfn-comprehend-entityrecognizer-entityrecognizerentitylist-s3uri): {{String}}
```

## Properties
<a name="aws-properties-comprehend-entityrecognizer-entityrecognizerentitylist-properties"></a>

`S3Uri`  <a name="cfn-comprehend-entityrecognizer-entityrecognizerentitylist-s3uri"></a>
Specifies the Amazon S3 location where the entity list is located. The URI must be in the same Region as the API endpoint that you are calling.
*Required*: Yes
*Type*: String
*Pattern*: `^s3://[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9](/.*)?$`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
