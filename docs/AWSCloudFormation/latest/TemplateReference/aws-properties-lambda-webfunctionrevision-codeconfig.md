---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-webfunctionrevision-codeconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::WebFunctionRevision CodeConfig
<a name="aws-properties-lambda-webfunctionrevision-codeconfig"></a>

The code configuration specifying the location of the deployment artifact.

## Syntax
<a name="aws-properties-lambda-webfunctionrevision-codeconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-webfunctionrevision-codeconfig-syntax.json"></a>

```
{
  "[S3Object](#cfn-lambda-webfunctionrevision-codeconfig-s3object)" : {{S3Object}}
}
```

### YAML
<a name="aws-properties-lambda-webfunctionrevision-codeconfig-syntax.yaml"></a>

```
  [S3Object](#cfn-lambda-webfunctionrevision-codeconfig-s3object): {{
    S3Object}}
```

## Properties
<a name="aws-properties-lambda-webfunctionrevision-codeconfig-properties"></a>

`S3Object`  <a name="cfn-lambda-webfunctionrevision-codeconfig-s3object"></a>
The Amazon S3 location of the deployment artifact.
*Required*: Yes
*Type*: [S3Object](aws-properties-lambda-webfunctionrevision-s3object.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
