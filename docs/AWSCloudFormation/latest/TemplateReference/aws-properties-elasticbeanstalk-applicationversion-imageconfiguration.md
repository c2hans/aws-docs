---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-elasticbeanstalk-applicationversion-imageconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticBeanstalk::ApplicationVersion ImageConfiguration
<a name="aws-properties-elasticbeanstalk-applicationversion-imageconfiguration"></a>

The source of the container image for an application version: an image that you built and pushed to a container registry yourself, or settings for Elastic Beanstalk to build one from your source bundle.

## Syntax
<a name="aws-properties-elasticbeanstalk-applicationversion-imageconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-elasticbeanstalk-applicationversion-imageconfiguration-syntax.json"></a>

```
{
  "[Build](#cfn-elasticbeanstalk-applicationversion-imageconfiguration-build)" : {{ImageBuildConfiguration}},
  "[Source](#cfn-elasticbeanstalk-applicationversion-imageconfiguration-source)" : {{ImageSource}}
}
```

### YAML
<a name="aws-properties-elasticbeanstalk-applicationversion-imageconfiguration-syntax.yaml"></a>

```
  [Build](#cfn-elasticbeanstalk-applicationversion-imageconfiguration-build): {{
    ImageBuildConfiguration}}
  [Source](#cfn-elasticbeanstalk-applicationversion-imageconfiguration-source): {{
    ImageSource}}
```

## Properties
<a name="aws-properties-elasticbeanstalk-applicationversion-imageconfiguration-properties"></a>

`Build`  <a name="cfn-elasticbeanstalk-applicationversion-imageconfiguration-build"></a>
Settings that Elastic Beanstalk uses to build a container image from the source bundle of the application version.
If you specify `Build`, also specify the request's `SourceBundle` parameter, and don't specify `Source`.
*Required*: No
*Type*: [ImageBuildConfiguration](aws-properties-elasticbeanstalk-applicationversion-imagebuildconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Source`  <a name="cfn-elasticbeanstalk-applicationversion-imageconfiguration-source"></a>
The location of a container image that you built and pushed to a container registry yourself. Elastic Beanstalk deploys the image without a build step.
If you specify `Source`, don't specify `Build` or the request's `SourceBundle` parameter.
*Required*: No
*Type*: [ImageSource](aws-properties-elasticbeanstalk-applicationversion-imagesource.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
