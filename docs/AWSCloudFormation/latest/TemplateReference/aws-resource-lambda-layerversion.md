---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-layerversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::LayerVersion
<a name="aws-resource-lambda-layerversion"></a>

The `AWS::Lambda::LayerVersion` resource creates a [Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html) from a ZIP archive.

## Syntax
<a name="aws-resource-lambda-layerversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lambda-layerversion-syntax.json"></a>

```
{
  "Type" : "AWS::Lambda::LayerVersion",
  "Properties" : {
      "[CompatibleArchitectures](#cfn-lambda-layerversion-compatiblearchitectures)" : {{[ String, ... ]}},
      "[CompatibleRuntimes](#cfn-lambda-layerversion-compatibleruntimes)" : {{[ String, ... ]}},
      "[Content](#cfn-lambda-layerversion-content)" : {{Content}},
      "[Description](#cfn-lambda-layerversion-description)" : {{String}},
      "[LayerName](#cfn-lambda-layerversion-layername)" : {{String}},
      "[LicenseInfo](#cfn-lambda-layerversion-licenseinfo)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-lambda-layerversion-syntax.yaml"></a>

```
Type: AWS::Lambda::LayerVersion
Properties:
  [CompatibleArchitectures](#cfn-lambda-layerversion-compatiblearchitectures): {{
    - String}}
  [CompatibleRuntimes](#cfn-lambda-layerversion-compatibleruntimes): {{
    - String}}
  [Content](#cfn-lambda-layerversion-content): {{
    Content}}
  [Description](#cfn-lambda-layerversion-description): {{String}}
  [LayerName](#cfn-lambda-layerversion-layername): {{String}}
  [LicenseInfo](#cfn-lambda-layerversion-licenseinfo): {{String}}
```

## Properties
<a name="aws-resource-lambda-layerversion-properties"></a>

`CompatibleArchitectures`  <a name="cfn-lambda-layerversion-compatiblearchitectures"></a>
A list of compatible [instruction set architectures](https://docs.aws.amazon.com/lambda/latest/dg/foundation-arch.html).
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CompatibleRuntimes`  <a name="cfn-lambda-layerversion-compatibleruntimes"></a>
A list of compatible [function runtimes](https://docs.aws.amazon.com/lambda/latest/dg/lambda-runtimes.html). Used for filtering with [ListLayers](https://docs.aws.amazon.com/lambda/latest/dg/API_ListLayers.html) and [ListLayerVersions](https://docs.aws.amazon.com/lambda/latest/dg/API_ListLayerVersions.html).
*Required*: No
*Type*: Array of String
*Minimum*: `0`
*Maximum*: `15`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Content`  <a name="cfn-lambda-layerversion-content"></a>
The function layer archive.
*Required*: Yes
*Type*: [Content](aws-properties-lambda-layerversion-content.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-lambda-layerversion-description"></a>
The description of the version.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LayerName`  <a name="cfn-lambda-layerversion-layername"></a>
The name or Amazon Resource Name (ARN) of the layer.
*Required*: No
*Type*: String
*Pattern*: `(arn:[a-zA-Z0-9-]+:lambda:[a-zA-Z0-9-]+:\d{12}:layer:[a-zA-Z0-9-_]+)|[a-zA-Z0-9-_]+`
*Minimum*: `1`
*Maximum*: `140`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LicenseInfo`  <a name="cfn-lambda-layerversion-licenseinfo"></a>
The layer's software license. It can be any of the following:
+ An [SPDX license identifier](https://spdx.org/licenses/). For example, `MIT`.
+ The URL of a license hosted on the internet. For example, `https://opensource.org/licenses/MIT`.
+ The full text of the license.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-lambda-layerversion-return-values"></a>

### Ref
<a name="aws-resource-lambda-layerversion-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the layer version, such as `arn:aws:lambda:us-east-2:123456789012:layer:my-layer:1`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-lambda-layerversion-return-values-fn--getatt"></a>

####
<a name="aws-resource-lambda-layerversion-return-values-fn--getatt-fn--getatt"></a>

`LayerVersionArn`  <a name="LayerVersionArn-fn::getatt"></a>
The ARN of the layer version.

## Examples
<a name="aws-resource-lambda-layerversion--examples"></a>

### Layer Version
<a name="aws-resource-lambda-layerversion--examples--Layer_Version"></a>

Create a layer named `my-layer`.

#### JSON
<a name="aws-resource-lambda-layerversion--examples--Layer_Version--json"></a>

```
"MyLayer": {
    "Type": "AWS::Lambda::LayerVersion",
    "Properties": {
        "CompatibleRuntimes": [
            "python3.12",
            "python3.11"
        ],
        "Content": {
            "S3Bucket": "amzn-s3-demo-bucket",
            "S3Key": "layer.zip"
        },
        "Description": "My layer",
        "LayerName": "my-layer",
        "LicenseInfo": "MIT"
    }
}
```

#### YAML
<a name="aws-resource-lambda-layerversion--examples--Layer_Version--yaml"></a>

```
MyLayer:
  Type: AWS::Lambda::LayerVersion
  Properties:
    CompatibleRuntimes:
      - python3.12
      - python3.11
    Content:
      S3Bucket: amzn-s3-demo-bucket
      S3Key: layer.zip
    Description: My layer
    LayerName: my-layer
    LicenseInfo: MIT
```
