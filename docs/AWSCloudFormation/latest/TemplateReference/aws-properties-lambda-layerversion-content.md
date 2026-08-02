---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-layerversion-content.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::LayerVersion Content
<a name="aws-properties-lambda-layerversion-content"></a>

A ZIP archive that contains the contents of an [Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html).

## Syntax
<a name="aws-properties-lambda-layerversion-content-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-layerversion-content-syntax.json"></a>

```
{
  "[S3Bucket](#cfn-lambda-layerversion-content-s3bucket)" : {{String}},
  "[S3Key](#cfn-lambda-layerversion-content-s3key)" : {{String}},
  "[S3ObjectStorageMode](#cfn-lambda-layerversion-content-s3objectstoragemode)" : {{String}},
  "[S3ObjectVersion](#cfn-lambda-layerversion-content-s3objectversion)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-layerversion-content-syntax.yaml"></a>

```
  [S3Bucket](#cfn-lambda-layerversion-content-s3bucket): {{String}}
  [S3Key](#cfn-lambda-layerversion-content-s3key): {{String}}
  [S3ObjectStorageMode](#cfn-lambda-layerversion-content-s3objectstoragemode): {{String}}
  [S3ObjectVersion](#cfn-lambda-layerversion-content-s3objectversion): {{String}}
```

## Properties
<a name="aws-properties-lambda-layerversion-content-properties"></a>

`S3Bucket`  <a name="cfn-lambda-layerversion-content-s3bucket"></a>
The Amazon S3 bucket of the layer archive.
*Required*: Yes
*Type*: String
*Pattern*: `[0-9A-Za-z\.\-_]*(?<!\.)`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3Key`  <a name="cfn-lambda-layerversion-content-s3key"></a>
The Amazon S3 key of the layer archive.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3ObjectStorageMode`  <a name="cfn-lambda-layerversion-content-s3objectstoragemode"></a>
Specifies the storage mode for the layer archive. Use `COPY` to store the archive in AWS Lambda-managed storage. Use `REFERENCE` to read the archive directly from the Amazon S3 bucket. If omitted, the default is `COPY`.
*Required*: No
*Type*: String
*Allowed values*: `COPY | REFERENCE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`S3ObjectVersion`  <a name="cfn-lambda-layerversion-content-s3objectversion"></a>
For versioned objects, the version of the layer archive object to use.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Examples
<a name="aws-properties-lambda-layerversion-content--examples"></a>

### Layer Content
<a name="aws-properties-lambda-layerversion-content--examples--Layer_Content"></a>

The location of a layer archive in Amazon S3.

#### JSON
<a name="aws-properties-lambda-layerversion-content--examples--Layer_Content--json"></a>

```
        "Content": {
            "S3Bucket": "amzn-s3-demo-bucket",
            "S3Key": "layer.zip"
        }
```

#### YAML
<a name="aws-properties-lambda-layerversion-content--examples--Layer_Content--yaml"></a>

```
    Content:
      S3Bucket: amzn-s3-demo-bucket
      S3Key: layer.zip
```
