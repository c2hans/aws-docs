---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-lambda-runtimeversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::RuntimeVersion

The `AWS::Lambda::RuntimeVersion` resource creates a runtime version for a customer-managed runtime. A runtime version defines the function execution environment by referencing a container image in Amazon Elastic Container Registry (Amazon ECR). The image of a runtime version can't change: to release a new image, create a new runtime version and point a runtime alias at it.

When you delete this resource, Lambda schedules it for deletion after a 30-day recovery window, and CloudFormation treats it as deleted. Until the window ends, the name stays reserved: you can't create a runtime version with the same name, so use a new name if you re-create it.

## Syntax
<a name="aws-resource-lambda-runtimeversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-lambda-runtimeversion-syntax.json"></a>

```json
{
  "Type" : "AWS::Lambda::RuntimeVersion",
  "Properties" : {
      "[ImageUri](#cfn-lambda-runtimeversion-imageuri)" : {{String}},
      "[Name](#cfn-lambda-runtimeversion-name)" : {{String}},
      "[ReleaseNotes](#cfn-lambda-runtimeversion-releasenotes)" : {{String}},
      "[RuntimeName](#cfn-lambda-runtimeversion-runtimename)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-lambda-runtimeversion-syntax.yaml"></a>

```yaml
Type: AWS::Lambda::RuntimeVersion
Properties:
  [ImageUri](#cfn-lambda-runtimeversion-imageuri): {{String}}
  [Name](#cfn-lambda-runtimeversion-name): {{String}}
  [ReleaseNotes](#cfn-lambda-runtimeversion-releasenotes): {{String}}
  [RuntimeName](#cfn-lambda-runtimeversion-runtimename): {{String}}
```

## Properties
<a name="aws-resource-lambda-runtimeversion-properties"></a>

`ImageUri`  <a name="cfn-lambda-runtimeversion-imageuri"></a>
The URI of the container image in Amazon ECR that defines the execution environment for this runtime version. The caller must have permission to read the image. CloudFormation doesn't return this value. To get the image that was published, use `ResolvedUri`.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-lambda-runtimeversion-name"></a>
The name to assign to the new runtime version.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9_]([A-Za-z0-9_.-]{0,126}[A-Za-z0-9_])?$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ReleaseNotes`  <a name="cfn-lambda-runtimeversion-releasenotes"></a>
The release notes for the runtime version. If you remove this property from the template, the release notes are cleared.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RuntimeName`  <a name="cfn-lambda-runtimeversion-runtimename"></a>
The name of the runtime that the version belongs to.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9]([a-z0-9_.-]{0,126})?[a-z0-9]$`
*Minimum*: `2`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-lambda-runtimeversion-return-values"></a>

### Ref
<a name="aws-resource-lambda-runtimeversion-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the runtime version.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-lambda-runtimeversion-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

 `Compatibility`
The compatibility of the runtime version: the integration models and architectures it supports, and whether it supports Lambda Managed Instances. The value is a [Compatibility](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-runtimeversion-compatibility.html) object.

####
<a name="aws-resource-lambda-runtimeversion-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the runtime version.

`Created`  <a name="Created-fn::getatt"></a>
The date and time when the runtime version was created.

`LastModified`  <a name="LastModified-fn::getatt"></a>
The date and time when the runtime version was last modified.

`Platforms`  <a name="Platforms-fn::getatt"></a>
The platforms (architecture and OS combinations) available for the runtime version.

`ResolvedUri`  <a name="ResolvedUri-fn::getatt"></a>
The resolved image URI of the runtime version.

`State`  <a name="State-fn::getatt"></a>
The current state of the runtime version.

## Examples
<a name="aws-resource-lambda-runtimeversion--examples"></a>

### Runtime version
<a name="aws-resource-lambda-runtimeversion--examples--Runtime_version"></a>

Publish a container image as version `v1` of the runtime `my-runtime`.

#### JSON
<a name="aws-resource-lambda-runtimeversion--examples--Runtime_version--json"></a>

```json
"MyRuntimeVersion": {
    "Type": "AWS::Lambda::RuntimeVersion",
    "Properties": {
        "RuntimeName": {
            "Ref": "MyRuntimeName"
        },
        "Name": "v1",
        "ImageUri": "111122223333.dkr.ecr.us-east-1.amazonaws.com/my-runtime-image:v1",
        "ReleaseNotes": "Initial release"
    }
}
```

#### YAML
<a name="aws-resource-lambda-runtimeversion--examples--Runtime_version--yaml"></a>

```yaml
MyRuntimeVersion:
  Type: AWS::Lambda::RuntimeVersion
  Properties:
    RuntimeName:
      Ref: MyRuntimeName
    Name: v1
    ImageUri: 111122223333.dkr.ecr.us-east-1.amazonaws.com/my-runtime-image:v1
    ReleaseNotes: Initial release
```
