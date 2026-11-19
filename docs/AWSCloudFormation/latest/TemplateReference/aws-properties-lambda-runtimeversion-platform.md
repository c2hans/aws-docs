---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-runtimeversion-platform.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::RuntimeVersion Platform

Describes a single OCI platform (CPU architecture and operating system) available for a runtime version.

## Syntax
<a name="aws-properties-lambda-runtimeversion-platform-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-runtimeversion-platform-syntax.json"></a>

```
{
  "[Architecture](#cfn-lambda-runtimeversion-platform-architecture)" : {{String}},
  "[Digest](#cfn-lambda-runtimeversion-platform-digest)" : {{String}},
  "[Os](#cfn-lambda-runtimeversion-platform-os)" : {{String}}
}
```

### YAML
<a name="aws-properties-lambda-runtimeversion-platform-syntax.yaml"></a>

```
  [Architecture](#cfn-lambda-runtimeversion-platform-architecture): {{String}}
  [Digest](#cfn-lambda-runtimeversion-platform-digest): {{String}}
  [Os](#cfn-lambda-runtimeversion-platform-os): {{String}}
```

## Properties
<a name="aws-properties-lambda-runtimeversion-platform-properties"></a>

`Architecture`  <a name="cfn-lambda-runtimeversion-platform-architecture"></a>
The CPU architecture of the platform, for example x86\_64 or arm64.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Digest`  <a name="cfn-lambda-runtimeversion-platform-digest"></a>
The content digest of the platform-specific image.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Os`  <a name="cfn-lambda-runtimeversion-platform-os"></a>
The operating system of the platform.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
