---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-elasticbeanstalk-applicationversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ElasticBeanstalk::ApplicationVersion
<a name="aws-resource-elasticbeanstalk-applicationversion"></a>

The AWS::ElasticBeanstalk::ApplicationVersion resource is an AWS Elastic Beanstalk resource type that specifies an application version, an iteration of deployable code, for an Elastic Beanstalk application.

Use `SourceBundle` to provide a source archive in Amazon S3. You can also use `BuildConfiguration` with a source bundle to have Elastic Beanstalk package the application version with AWS CodeBuild, or use `ImageConfiguration` to deploy an existing container image or build one from the source bundle.

**Note**
After you create an application version with a specified Amazon S3 bucket and key location, you can't change that Amazon S3 location. If you change the Amazon S3 location, an attempt to launch an environment from the application version will fail.

## Syntax
<a name="aws-resource-elasticbeanstalk-applicationversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-elasticbeanstalk-applicationversion-syntax.json"></a>

```
{
  "Type" : "AWS::ElasticBeanstalk::ApplicationVersion",
  "Properties" : {
      "[ApplicationName](#cfn-elasticbeanstalk-applicationversion-applicationname)" : {{String}},
      "[BuildConfiguration](#cfn-elasticbeanstalk-applicationversion-buildconfiguration)" : {{BuildConfiguration}},
      "[Description](#cfn-elasticbeanstalk-applicationversion-description)" : {{String}},
      "[ImageConfiguration](#cfn-elasticbeanstalk-applicationversion-imageconfiguration)" : {{ImageConfiguration}},
      "[Process](#cfn-elasticbeanstalk-applicationversion-process)" : {{Boolean}},
      "[SourceBundle](#cfn-elasticbeanstalk-applicationversion-sourcebundle)" : {{SourceBundle}}
    }
}
```

### YAML
<a name="aws-resource-elasticbeanstalk-applicationversion-syntax.yaml"></a>

```
Type: AWS::ElasticBeanstalk::ApplicationVersion
Properties:
  [ApplicationName](#cfn-elasticbeanstalk-applicationversion-applicationname): {{String}}
  [BuildConfiguration](#cfn-elasticbeanstalk-applicationversion-buildconfiguration): {{
    BuildConfiguration}}
  [Description](#cfn-elasticbeanstalk-applicationversion-description): {{String}}
  [ImageConfiguration](#cfn-elasticbeanstalk-applicationversion-imageconfiguration): {{
    ImageConfiguration}}
  [Process](#cfn-elasticbeanstalk-applicationversion-process): {{Boolean}}
  [SourceBundle](#cfn-elasticbeanstalk-applicationversion-sourcebundle): {{
    SourceBundle}}
```

## Properties
<a name="aws-resource-elasticbeanstalk-applicationversion-properties"></a>

`ApplicationName`  <a name="cfn-elasticbeanstalk-applicationversion-applicationname"></a>
The name of the Elastic Beanstalk application that is associated with this application version.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`BuildConfiguration`  <a name="cfn-elasticbeanstalk-applicationversion-buildconfiguration"></a>
Settings for an AWS CodeBuild build.
Don't specify `BuildConfiguration` together with `ImageConfiguration`, which configures a container image build instead.
*Required*: No
*Type*: [BuildConfiguration](aws-properties-elasticbeanstalk-applicationversion-buildconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-elasticbeanstalk-applicationversion-description"></a>
A description of this application version.
*Required*: No
*Type*: String
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageConfiguration`  <a name="cfn-elasticbeanstalk-applicationversion-imageconfiguration"></a>
The source of the container image for this application version. You can specify an image that you built and pushed to a container registry yourself, or settings for Elastic Beanstalk to build one from your source bundle. Specify exactly one of the `Source` and `Build` members.
Don't specify `ImageConfiguration` together with `BuildConfiguration`, which configures an AWS CodeBuild build instead.
*Required*: No
*Type*: [ImageConfiguration](aws-properties-elasticbeanstalk-applicationversion-imageconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Process`  <a name="cfn-elasticbeanstalk-applicationversion-process"></a>
Pre-processes and validates the environment manifest (`env.yaml`) and configuration files (`*.config` files in the `.ebextensions` folder) in the source bundle. Validating configuration files can identify issues prior to deploying the application version to an environment.
You must turn processing on for application versions that you create using AWS CodeBuild or AWS CodeCommit. For application versions built from a source bundle in Amazon S3, processing is optional.
The `Process` option validates Elastic Beanstalk configuration files. It doesn't validate your application's configuration files, like proxy server or Docker configuration.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceBundle`  <a name="cfn-elasticbeanstalk-applicationversion-sourcebundle"></a>
The Amazon S3 bucket and key that identify the location of the source bundle for this version.
If you specify `BuildConfiguration`, Elastic Beanstalk uses this source bundle as the build input. If you specify `ImageConfiguration.Build`, also specify `SourceBundle`. If you specify `ImageConfiguration.Source`, don't specify `SourceBundle`.
The Amazon S3 bucket must be in the same region as the environment.
*Required*: No
*Type*: [SourceBundle](aws-properties-elasticbeanstalk-applicationversion-sourcebundle.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-elasticbeanstalk-applicationversion-return-values"></a>

### Ref
<a name="aws-resource-elasticbeanstalk-applicationversion-return-values-ref"></a>

When the logical ID of this resource is provided to the `Ref` intrinsic function, `Ref` returns the resource name.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-elasticbeanstalk-applicationversion-return-values-fn--getatt"></a>

## Examples
<a name="aws-resource-elasticbeanstalk-applicationversion--examples"></a>

**Topics**
+ [](#aws-resource-elasticbeanstalk-applicationversion--examples--)
+ [Application Version from a Container Image](#aws-resource-elasticbeanstalk-applicationversion--examples--Application_Version_from_a_Container_Image)

###
<a name="aws-resource-elasticbeanstalk-applicationversion--examples--"></a>

#### JSON
<a name="aws-resource-elasticbeanstalk-applicationversion--examples----json"></a>

```
"myAppVersion": {
  "Type" : "AWS::ElasticBeanstalk::ApplicationVersion",
  "Properties" : {
    "ApplicationName" : {"Ref" : "myApp"},
    "Description" : "my sample version",
    "SourceBundle" : {
      "S3Bucket" : { "Fn::Join" :
        ["-", [ "elasticbeanstalk-samples", { "Ref" : "AWS::Region" } ] ] },
      "S3Key" : "php-newsample-app.zip"
    }
  }
}
```

#### YAML
<a name="aws-resource-elasticbeanstalk-applicationversion--examples----yaml"></a>

```
myAppVersion:
  Type: AWS::ElasticBeanstalk::ApplicationVersion
  Properties:
    ApplicationName:
      Ref: "myApp"
    Description: "my sample version"
    SourceBundle:
      S3Bucket:
        Fn::Join:
          - "-"
          -
            - "elasticbeanstalk-samples"
            - Ref: "AWS::Region"
      S3Key: "php-newsample-app.zip"
```

### Application Version from a Container Image
<a name="aws-resource-elasticbeanstalk-applicationversion--examples--Application_Version_from_a_Container_Image"></a>

#### JSON
<a name="aws-resource-elasticbeanstalk-applicationversion--examples--Application_Version_from_a_Container_Image--json"></a>

```
"myImageAppVersion": {
  "Type" : "AWS::ElasticBeanstalk::ApplicationVersion",
  "Properties" : {
    "ApplicationName" : { "Ref" : "myApp" },
    "Description" : "Application version from a container image",
    "ImageConfiguration" : {
      "Source" : {
        "Uri" : "111122223333.dkr.ecr.us-east-1.amazonaws.com/my-repository:latest"
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-elasticbeanstalk-applicationversion--examples--Application_Version_from_a_Container_Image--yaml"></a>

```
myImageAppVersion:
  Type: AWS::ElasticBeanstalk::ApplicationVersion
  Properties:
    ApplicationName:
      Ref: "myApp"
    Description: "Application version from a container image"
    ImageConfiguration:
      Source:
        Uri: "111122223333.dkr.ecr.us-east-1.amazonaws.com/my-repository:latest"
```

## See also
<a name="aws-resource-elasticbeanstalk-applicationversion--seealso"></a>
+ For a complete Elastic Beanstalk sample template, see [Elastic Beanstalk Template Snippets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/quickref-elasticbeanstalk.html).
