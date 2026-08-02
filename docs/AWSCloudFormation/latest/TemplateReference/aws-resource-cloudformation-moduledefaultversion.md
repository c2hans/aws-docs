---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-moduledefaultversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::ModuleDefaultVersion
<a name="aws-resource-cloudformation-moduledefaultversion"></a>

Specifies the default version of a module. The default version of the module will be used in CloudFormation operations for this account and Region.

For more information, see [Create reusable resource configurations that can be included across templates with CloudFormation modules](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/modules.html) in the *CloudFormation User Guide*.

For information about the CloudFormation registry, see [Managing extensions with the CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) in the *CloudFormation User Guide*.

## Syntax
<a name="aws-resource-cloudformation-moduledefaultversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudformation-moduledefaultversion-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFormation::ModuleDefaultVersion",
  "Properties" : {
      "[Arn](#cfn-cloudformation-moduledefaultversion-arn)" : {{String}},
      "[ModuleName](#cfn-cloudformation-moduledefaultversion-modulename)" : {{String}},
      "[VersionId](#cfn-cloudformation-moduledefaultversion-versionid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cloudformation-moduledefaultversion-syntax.yaml"></a>

```
Type: AWS::CloudFormation::ModuleDefaultVersion
Properties:
  [Arn](#cfn-cloudformation-moduledefaultversion-arn): {{String}}
  [ModuleName](#cfn-cloudformation-moduledefaultversion-modulename): {{String}}
  [VersionId](#cfn-cloudformation-moduledefaultversion-versionid): {{String}}
```

## Properties
<a name="aws-resource-cloudformation-moduledefaultversion-properties"></a>

`Arn`  <a name="cfn-cloudformation-moduledefaultversion-arn"></a>
The Amazon Resource Name (ARN) of the module version to set as the default version.
Conditional: You must specify either `Arn`, or `ModuleName` and `VersionId`.
*Required*: Conditional
*Type*: String
*Pattern*: `^arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type/module/.+/[0-9]{8}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModuleName`  <a name="cfn-cloudformation-moduledefaultversion-modulename"></a>
The name of the module.
Conditional: You must specify either `Arn`, or `ModuleName` and `VersionId`.
*Required*: Conditional
*Type*: String
*Pattern*: `^[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::MODULE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VersionId`  <a name="cfn-cloudformation-moduledefaultversion-versionid"></a>
The ID for the specific version of the module.
Conditional: You must specify either `Arn`, or `ModuleName` and `VersionId`.
*Required*: Conditional
*Type*: String
*Pattern*: `^[0-9]{8}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-cloudformation-moduledefaultversion-return-values"></a>

### Ref
<a name="aws-resource-cloudformation-moduledefaultversion-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the module version.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## Remarks
<a name="aws-resource-cloudformation-moduledefaultversion--remarks"></a>

Considerations when managing the default module version:
+ The first module version to be registered in an account and Region remains the default version CloudFormation uses, unless and until you explicitly sets another version as the default.
+ For ease of determining which module version is the default version, we recommend that you only include a single `AWS::CloudFormation::ModuleDefaultVersion` resource for a given module in a template.
+ If you delete an `AWS::CloudFormation::ModuleVersion` resource, either by deleting it from a stack or deleting the entire stack, CloudFormation marks the corresponding module version as `DEPRECATED`. For more information on deprecating module versions, see [DeregisterType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeregisterType.html) in the *CloudFormation API Reference*.
+ If you attempt to delete an `AWS::CloudFormation::ModuleVersion` resource that represents the default version, the operation will fail if there are other active versions.

## Examples
<a name="aws-resource-cloudformation-moduledefaultversion--examples"></a>

### Specifying the default module version
<a name="aws-resource-cloudformation-moduledefaultversion--examples--Specifying_the_default_module_version"></a>

The following example registers two versions of a module, and then sets the second version as the default version for CloudFormation to use. Note that the example uses the `DependsOn` attribute to ensure that CloudFormation provisions version one before version two.

#### JSON
<a name="aws-resource-cloudformation-moduledefaultversion--examples--Specifying_the_default_module_version--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "ModuleVersion1": {
            "Type": "AWS::CloudFormation::ModuleVersion",
            "Properties": {
                "ModuleName": "My::Sample::Test::MODULE",
                "ModulePackage": "s3://amzn-s3-demo-bucket/sample-module-package-v1.zip"
            }
        },
        "ModuleVersion2": {
            "Type": "AWS::CloudFormation::ModuleVersion",
            "Properties": {
                "ModuleName": "My::Sample::Test::MODULE",
                "ModulePackage": "s3://amzn-s3-demo-bucket/sample-module-package-v2.zip"
            },
            "DependsOn": "ModuleVersion1"
        },
        "ModuleDefaultVersion": {
            "Type": "AWS::CloudFormation::ModuleDefaultVersion",
            "Properties": {
                "Arn": {
                    "Ref": "ModuleVersion2"
                }
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-cloudformation-moduledefaultversion--examples--Specifying_the_default_module_version--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  ModuleVersion1:
    Type: AWS::CloudFormation::ModuleVersion
    Properties:
      ModuleName: 'My::Sample::Test::MODULE'
      ModulePackage: 's3://amzn-s3-demo-bucket/sample-module-package-v1.zip'
  ModuleVersion2:
    Type: AWS::CloudFormation::ModuleVersion
    Properties:
      ModuleName: 'My::Sample::Test::MODULE'
      ModulePackage: 's3://amzn-s3-demo-bucket/sample-module-package-v2.zip'
    DependsOn: ModuleVersion1
  ModuleDefaultVersion:
    Type: AWS::CloudFormation::ModuleDefaultVersion
    Properties:
      Arn: !Ref ModuleVersion2
```
