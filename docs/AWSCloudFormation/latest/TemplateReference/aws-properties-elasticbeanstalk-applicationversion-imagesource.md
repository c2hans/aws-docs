---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticbeanstalk-applicationversion-imagesource.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticBeanstalk::ApplicationVersion ImageSource
<a name="aws-properties-elasticbeanstalk-applicationversion-imagesource"></a>

The `ImageSource` property type specifies the location of a container image.

## Syntax
<a name="aws-properties-elasticbeanstalk-applicationversion-imagesource-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticbeanstalk-applicationversion-imagesource-syntax.json"></a>

```
{
  "[Uri](#cfn-elasticbeanstalk-applicationversion-imagesource-uri)" : {{String}}
}
```

### YAML
<a name="aws-properties-elasticbeanstalk-applicationversion-imagesource-syntax.yaml"></a>

```
  [Uri](#cfn-elasticbeanstalk-applicationversion-imagesource-uri): {{String}}
```

## Properties
<a name="aws-properties-elasticbeanstalk-applicationversion-imagesource-properties"></a>

`Uri`  <a name="cfn-elasticbeanstalk-applicationversion-imagesource-uri"></a>
The URI of the container image, including the registry, the repository, and the image tag or digest. For example, `111122223333.dkr.ecr.us-east-1.amazonaws.com/my-repository:latest`.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
