---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-hookdefaultversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::HookDefaultVersion
<a name="aws-resource-cloudformation-hookdefaultversion"></a>

The `AWS::CloudFormation::HookDefaultVersion` resource specifies the default version of a Hook. The default version of the Hook is used in CloudFormation operations for this AWS account and AWS Region.

For information about the CloudFormation registry, see [Managing extensions with the CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) in the *CloudFormation User Guide*.

This resource type is not compatible with Guard and Lambda Hooks.

## Syntax
<a name="aws-resource-cloudformation-hookdefaultversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudformation-hookdefaultversion-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFormation::HookDefaultVersion",
  "Properties" : {
      "[TypeName](#cfn-cloudformation-hookdefaultversion-typename)" : {{String}},
      "[TypeVersionArn](#cfn-cloudformation-hookdefaultversion-typeversionarn)" : {{String}},
      "[VersionId](#cfn-cloudformation-hookdefaultversion-versionid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cloudformation-hookdefaultversion-syntax.yaml"></a>

```
Type: AWS::CloudFormation::HookDefaultVersion
Properties:
  [TypeName](#cfn-cloudformation-hookdefaultversion-typename): {{String}}
  [TypeVersionArn](#cfn-cloudformation-hookdefaultversion-typeversionarn): {{String}}
  [VersionId](#cfn-cloudformation-hookdefaultversion-versionid): {{String}}
```

## Properties
<a name="aws-resource-cloudformation-hookdefaultversion-properties"></a>

`TypeName`  <a name="cfn-cloudformation-hookdefaultversion-typename"></a>
The name of the Hook.
You must specify either `TypeVersionArn`, or `TypeName` and `VersionId`.
*Required*: Conditional
*Type*: String
*Pattern*: `^[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TypeVersionArn`  <a name="cfn-cloudformation-hookdefaultversion-typeversionarn"></a>
The version ID of the type configuration.
You must specify either `TypeVersionArn`, or `TypeName` and `VersionId`.
*Required*: Conditional
*Type*: String
*Pattern*: `^arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type/hook/.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VersionId`  <a name="cfn-cloudformation-hookdefaultversion-versionid"></a>
The version ID of the type specified.
You must specify either `TypeVersionArn`, or `TypeName` and `VersionId`.
*Required*: Conditional
*Type*: String
*Pattern*: `^[A-Za-z0-9-]{1,128}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudformation-hookdefaultversion-return-values"></a>

### Ref
<a name="aws-resource-cloudformation-hookdefaultversion-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the Hook version. For example:

 `arn:aws:cloudformation:us-west-2:123456789012:type/hook/Sample-CloudFormation-Hook/00000001`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudformation-hookdefaultversion-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudformation-hookdefaultversion-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Number (ARN) of the activated Hook in this account and Region.

## Examples
<a name="aws-resource-cloudformation-hookdefaultversion--examples"></a>

**Topics**
+ [Specifying a Hook default version](#aws-resource-cloudformation-hookdefaultversion--examples--Specifying_a_Hook_default_version)
+ [Specifying a Hook default version using TypeVersionArn](#aws-resource-cloudformation-hookdefaultversion--examples--Specifying_a_Hook_default_version_using_TypeVersionArn)
+ [Specifying a Hook default version using TypeName and VersionId](#aws-resource-cloudformation-hookdefaultversion--examples--Specifying_a_Hook_default_version_using_TypeName_and_VersionId)

### Specifying a Hook default version
<a name="aws-resource-cloudformation-hookdefaultversion--examples--Specifying_a_Hook_default_version"></a>

The following example demonstrates how to specify a new Hook version and use the `Ref` return value to set that version as the default version.

#### JSON
<a name="aws-resource-cloudformation-hookdefaultversion--examples--Specifying_a_Hook_default_version--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "HookVersion": {
            "Type": "AWS::CloudFormation::HookVersion",
            "Properties": {
                "TypeName": "My::Sample::Hook",
                "SchemaHandlerPackage": "s3://amzn-s3-demo-bucket/my-sample-hook.zip"
            }
        },
        "HookDefaultVersion": {
            "Type": "AWS::CloudFormation::HookDefaultVersion",
            "Properties": {
                "TypeVersionArn": {
                    "Ref": "HookVersion"
                }
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-cloudformation-hookdefaultversion--examples--Specifying_a_Hook_default_version--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  HookVersion:
    Type: AWS::CloudFormation::HookVersion
    Properties:
      TypeName: 'My::Sample::Hook'
      SchemaHandlerPackage: 's3://amzn-s3-demo-bucket/my-sample-hook.zip'
  HookDefaultVersion:
    Type: AWS::CloudFormation::HookDefaultVersion
    Properties:
      TypeVersionArn: !Ref HookVersion
```

### Specifying a Hook default version using TypeVersionArn
<a name="aws-resource-cloudformation-hookdefaultversion--examples--Specifying_a_Hook_default_version_using_TypeVersionArn"></a>

The following example demonstrates how to set a Hook version as the default version through the `TypeVersionArn` property type.

#### JSON
<a name="aws-resource-cloudformation-hookdefaultversion--examples--Specifying_a_Hook_default_version_using_TypeVersionArn--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "HookDefaultVersion": {
            "Type": "AWS::CloudFormation::HookDefaultVersion",
            "Properties": {
                "TypeVersionArn": "arn:aws:cloudformation:us-west-2:123456789012:type/hook/My-Sample-Hook/00000001"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-cloudformation-hookdefaultversion--examples--Specifying_a_Hook_default_version_using_TypeVersionArn--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  HookDefaultVersion:
    Type: AWS::CloudFormation::HookDefaultVersion
    Properties:
      TypeVersionArn: >-
        arn:aws:cloudformation:us-west-2:123456789012:type/hook/My-Sample-Hook/00000001
```

### Specifying a Hook default version using TypeName and VersionId
<a name="aws-resource-cloudformation-hookdefaultversion--examples--Specifying_a_Hook_default_version_using_TypeName_and_VersionId"></a>

The following example demonstrates how to set a Hook version as the default version through the `VersionId` property type.

#### JSON
<a name="aws-resource-cloudformation-hookdefaultversion--examples--Specifying_a_Hook_default_version_using_TypeName_and_VersionId--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "HookDefaultVersion": {
            "Type": "AWS::CloudFormation::HookDefaultVersion",
            "Properties": {
                "TypeName": "My::Sample::Hook",
                "VersionId": 1
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-cloudformation-hookdefaultversion--examples--Specifying_a_Hook_default_version_using_TypeName_and_VersionId--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  HookDefaultVersion:
    Type: AWS::CloudFormation::HookDefaultVersion
    Properties:
      TypeName: 'My::Sample::Hook'
      VersionId: 1
```
