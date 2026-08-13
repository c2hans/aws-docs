---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-microvmimage.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::MicrovmImage
<a name="aws-resource-lambda-microvmimage"></a>

Creates a MicroVM image from the specified code artifact and base image. The build is asynchronous — the image transitions from CREATING to CREATED on success, or CREATE\_FAILED on failure. Use GetMicrovmImage to poll for completion.

## Syntax
<a name="aws-resource-lambda-microvmimage-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lambda-microvmimage-syntax.json"></a>

```
{
  "Type" : "AWS::Lambda::MicrovmImage",
  "Properties" : {
      "[AdditionalOsCapabilities](#cfn-lambda-microvmimage-additionaloscapabilities)" : {{[ String, ... ]}},
      "[BaseImageArn](#cfn-lambda-microvmimage-baseimagearn)" : {{String}},
      "[BaseImageVersion](#cfn-lambda-microvmimage-baseimageversion)" : {{String}},
      "[BuildRoleArn](#cfn-lambda-microvmimage-buildrolearn)" : {{String}},
      "[CodeArtifact](#cfn-lambda-microvmimage-codeartifact)" : {{CodeArtifact}},
      "[CpuConfigurations](#cfn-lambda-microvmimage-cpuconfigurations)" : {{[ CpuConfiguration, ... ]}},
      "[Description](#cfn-lambda-microvmimage-description)" : {{String}},
      "[EgressNetworkConnectors](#cfn-lambda-microvmimage-egressnetworkconnectors)" : {{[ String, ... ]}},
      "[EnvironmentVariables](#cfn-lambda-microvmimage-environmentvariables)" : {{[ EnvironmentVariable, ... ]}},
      "[Hooks](#cfn-lambda-microvmimage-hooks)" : {{Hooks}},
      "[Logging](#cfn-lambda-microvmimage-logging)" : {{Logging}},
      "[Name](#cfn-lambda-microvmimage-name)" : {{String}},
      "[Resources](#cfn-lambda-microvmimage-resources)" : {{[ Resources, ... ]}},
      "[Tags](#cfn-lambda-microvmimage-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-lambda-microvmimage-syntax.yaml"></a>

```
Type: AWS::Lambda::MicrovmImage
Properties:
  [AdditionalOsCapabilities](#cfn-lambda-microvmimage-additionaloscapabilities): {{
    - String}}
  [BaseImageArn](#cfn-lambda-microvmimage-baseimagearn): {{String}}
  [BaseImageVersion](#cfn-lambda-microvmimage-baseimageversion): {{String}}
  [BuildRoleArn](#cfn-lambda-microvmimage-buildrolearn): {{String}}
  [CodeArtifact](#cfn-lambda-microvmimage-codeartifact): {{
    CodeArtifact}}
  [CpuConfigurations](#cfn-lambda-microvmimage-cpuconfigurations): {{
    - CpuConfiguration}}
  [Description](#cfn-lambda-microvmimage-description): {{String}}
  [EgressNetworkConnectors](#cfn-lambda-microvmimage-egressnetworkconnectors): {{
    - String}}
  [EnvironmentVariables](#cfn-lambda-microvmimage-environmentvariables): {{
    - EnvironmentVariable}}
  [Hooks](#cfn-lambda-microvmimage-hooks): {{
    Hooks}}
  [Logging](#cfn-lambda-microvmimage-logging): {{
    Logging}}
  [Name](#cfn-lambda-microvmimage-name): {{String}}
  [Resources](#cfn-lambda-microvmimage-resources): {{
    - Resources}}
  [Tags](#cfn-lambda-microvmimage-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-lambda-microvmimage-properties"></a>

`AdditionalOsCapabilities`  <a name="cfn-lambda-microvmimage-additionaloscapabilities"></a>
Additional OS capabilities granted to the MicroVM runtime environment.
*Required*: Yes
*Type*: Array of String
*Allowed values*: `ALL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BaseImageArn`  <a name="cfn-lambda-microvmimage-baseimagearn"></a>
The ARN of the base MicroVM image used.
*Required*: Yes
*Type*: String
*Pattern*: `^[^\s]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BaseImageVersion`  <a name="cfn-lambda-microvmimage-baseimageversion"></a>
The specific version of the base MicroVM image.
*Required*: Yes
*Type*: String
*Pattern*: `^[^\s]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`BuildRoleArn`  <a name="cfn-lambda-microvmimage-buildrolearn"></a>
The ARN of the IAM build role.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-zA-Z-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CodeArtifact`  <a name="cfn-lambda-microvmimage-codeartifact"></a>
The code artifact for this version.
*Required*: Yes
*Type*: [CodeArtifact](aws-properties-lambda-microvmimage-codeartifact.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CpuConfigurations`  <a name="cfn-lambda-microvmimage-cpuconfigurations"></a>
The list of supported CPU configurations for the MicroVM.
*Required*: Yes
*Type*: Array of [CpuConfiguration](aws-properties-lambda-microvmimage-cpuconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-lambda-microvmimage-description"></a>
The description of the version.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EgressNetworkConnectors`  <a name="cfn-lambda-microvmimage-egressnetworkconnectors"></a>
The list of egress network connectors available to the MicroVM at runtime.
*Required*: Yes
*Type*: Array of String
*Maximum*: `10`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnvironmentVariables`  <a name="cfn-lambda-microvmimage-environmentvariables"></a>
Environment variables set in the MicroVM runtime environment.
*Required*: Yes
*Type*: Array of [EnvironmentVariable](aws-properties-lambda-microvmimage-environmentvariable.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Hooks`  <a name="cfn-lambda-microvmimage-hooks"></a>
Lifecycle hook configuration for MicroVMs and MicroVM images.
*Required*: Yes
*Type*: [Hooks](aws-properties-lambda-microvmimage-hooks.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Logging`  <a name="cfn-lambda-microvmimage-logging"></a>
Configuration for MicroVM logging output. Specify exactly one: cloudWatch to enable CloudWatch logging, or disabled to turn off logging.
*Required*: Yes
*Type*: [Logging](aws-properties-lambda-microvmimage-logging.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-lambda-microvmimage-name"></a>
The name of the MicroVM image.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Resources`  <a name="cfn-lambda-microvmimage-resources"></a>
The resource requirements for the MicroVM.
*Required*: Yes
*Type*: [Array](aws-properties-lambda-microvmimage-resources.md) of [Resources](aws-properties-lambda-microvmimage-resources.md)
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-lambda-microvmimage-tags"></a>
Key-value pairs associated with the version.
*Required*: No
*Type*: Array of [Tag](aws-properties-lambda-microvmimage-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-lambda-microvmimage-return-values"></a>

### Ref
<a name="aws-resource-lambda-microvmimage-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the image ARN.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-lambda-microvmimage-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-lambda-microvmimage-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the version was created.

`ImageArn`  <a name="ImageArn-fn::getatt"></a>
The ARN of the MicroVM image.

`LatestActiveImageVersion`  <a name="LatestActiveImageVersion-fn::getatt"></a>
The latest active version of the MicroVM image.

`LatestFailedImageVersion`  <a name="LatestFailedImageVersion-fn::getatt"></a>
The latest failed version of the MicroVM image, if any.

`State`  <a name="State-fn::getatt"></a>
The current state of the version.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the version was last updated.
