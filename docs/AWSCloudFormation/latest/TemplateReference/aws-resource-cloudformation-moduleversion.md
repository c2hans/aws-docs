---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-moduleversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::ModuleVersion
<a name="aws-resource-cloudformation-moduleversion"></a>

The `AWS::CloudFormation::ModuleVersion` resource registers the specified version of the module with the CloudFormation registry. Registering a module makes it available for use in CloudFormation templates in your AWS account and Region.

For more information, see [Create reusable resource configurations that can be included across templates with CloudFormation modules](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/modules.html) in the *CloudFormation User Guide*.

For information about the CloudFormation registry, see [Managing extensions with the CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) in the *CloudFormation User Guide*.

## Syntax
<a name="aws-resource-cloudformation-moduleversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudformation-moduleversion-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFormation::ModuleVersion",
  "Properties" : {
      "[ModuleName](#cfn-cloudformation-moduleversion-modulename)" : {{String}},
      "[ModulePackage](#cfn-cloudformation-moduleversion-modulepackage)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cloudformation-moduleversion-syntax.yaml"></a>

```
Type: AWS::CloudFormation::ModuleVersion
Properties:
  [ModuleName](#cfn-cloudformation-moduleversion-modulename): {{String}}
  [ModulePackage](#cfn-cloudformation-moduleversion-modulepackage): {{String}}
```

## Properties
<a name="aws-resource-cloudformation-moduleversion-properties"></a>

`ModuleName`  <a name="cfn-cloudformation-moduleversion-modulename"></a>
The name of the module being registered.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::MODULE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ModulePackage`  <a name="cfn-cloudformation-moduleversion-modulepackage"></a>
A URL to the S3 bucket for the package that contains the template fragment and schema files for the module version to register.
For more information, see [Module structure and requirements](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/modules-structure.html) in the *CloudFormation Command Line Interface (CLI) User Guide*.
To register the module version, you must have `s3:GetObject` permissions to access the S3 objects.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-cloudformation-moduleversion-return-values"></a>

### Ref
<a name="aws-resource-cloudformation-moduleversion-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the module version.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudformation-moduleversion-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudformation-moduleversion-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the module.

`Description`  <a name="Description-fn::getatt"></a>
The description of the module.

`DocumentationUrl`  <a name="DocumentationUrl-fn::getatt"></a>
The URL of a page providing detailed documentation for this module.

`IsDefaultVersion`  <a name="IsDefaultVersion-fn::getatt"></a>
Whether the specified module version is set as the default version.
This applies only to private extensions you have registered in your account, and extensions published by AWS. For public third-party extensions, whether they are activated in your account, CloudFormation returns `null`.

`Schema`  <a name="Schema-fn::getatt"></a>
The schema that defines the module.

`TimeCreated`  <a name="TimeCreated-fn::getatt"></a>
When the specified private module version was registered or activated in your account.

`VersionId`  <a name="VersionId-fn::getatt"></a>
The ID of this version of the module.

`Visibility`  <a name="Visibility-fn::getatt"></a>
The visibility level that determines who can see and use this module in CloudFormation operations:
+ `PRIVATE`: The module is only visible and usable within the account where it was registered. CloudFormation automatically marks any modules you register as `PRIVATE`.
+ `PUBLIC`: The module is publicly visible and usable within any AWS account.

## Remarks
<a name="aws-resource-cloudformation-moduleversion--remarks"></a>

Considerations when managing module versions:
+ The account in which you register the module version must have permission to access the S3 bucket in which the module package resides.
+ The first module version to be registered in an account and region remains the default version CloudFormation uses, unless and until you explicitly sets another version as the default. To specify a module version as the default version, use the [AWS::CloudFormation::ModuleDefaultVersion](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-moduledefaultversion.html) resource.
+ If your template contains multiple versions of the same module, we strongly recommend using the `DependsOn` attribute to explicitly set the order in which the versions are registered.
+ If you delete an `AWS::CloudFormation::ModuleVersion` resource, either by deleting it from a stack or deleting the entire stack, CloudFormation marks the corresponding module version as `DEPRECATED`.

  If you attempt to delete an `AWS::CloudFormation::ModuleVersion` resource that represent the default version, the operation will fail if there are other active versions.

  For more information on deprecating module versions, see [DeregisterType](https://docs.aws.amazon.com/AWSCloudFormation/latest/APIReference/API_DeregisterType.html) in the *CloudFormation API Reference*.
+ You can't edit a module version. Updating an `AWS::CloudFormation::ModuleVersion` resource results in a new module version being registered in the CloudFormation registry.

## Examples
<a name="aws-resource-cloudformation-moduleversion--examples"></a>

**Topics**
+ [Registering a module version](#aws-resource-cloudformation-moduleversion--examples--Registering_a_module_version)
+ [Registering multiple module versions](#aws-resource-cloudformation-moduleversion--examples--Registering_multiple_module_versions)

### Registering a module version
<a name="aws-resource-cloudformation-moduleversion--examples--Registering_a_module_version"></a>

The following example registers a module version. If this is the only version of the module registered in this account and Region, CloudFormation sets this version as the default version.

#### JSON
<a name="aws-resource-cloudformation-moduleversion--examples--Registering_a_module_version--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "ModuleVersion": {
            "Type": "AWS::CloudFormation::ModuleVersion",
            "Properties": {
                "ModuleName": "My::Sample::Test::MODULE",
                "ModulePackage": "s3://my-sample-moduleversion-bucket/sample-module-package-v1.zip"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-cloudformation-moduleversion--examples--Registering_a_module_version--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  ModuleVersion:
    Type: 'AWS::CloudFormation::ModuleVersion'
    Properties:
      ModuleName: 'My::Sample::Test::MODULE'
      ModulePackage: 's3://my-sample-moduleversion-bucket/sample-module-package-v1.zip'
```

### Registering multiple module versions
<a name="aws-resource-cloudformation-moduleversion--examples--Registering_multiple_module_versions"></a>

The following example registers two versions of a module. Note the following:
+ The example uses the `DependsOn` attribute to ensure that CloudFormation provisions version one before version two.
+ CloudFormation sets version one of the module as the default version, as it's registered first. (This assumes no other versions of the module are currently registered in this account and Region.)

#### JSON
<a name="aws-resource-cloudformation-moduleversion--examples--Registering_multiple_module_versions--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "ModuleVersion1": {
            "Type": "AWS::CloudFormation::ModuleVersion",
            "Properties": {
                "ModuleName": "My::Sample::Test::MODULE",
                "ModulePackage": "s3://my-sample-moduleversion-bucket/sample-module-package-v1.zip"
            }
        },
        "ModuleVersion2": {
            "Type": "AWS::CloudFormation::ModuleVersion",
            "Properties": {
                "ModuleName": "My::Sample::Test::MODULE",
                "ModulePackage": "s3://my-sample-moduleversion-bucket/sample-module-package-v2.zip"
            },
            "DependsOn": "ModuleVersion1"
        }
    }
}
```

#### YAML
<a name="aws-resource-cloudformation-moduleversion--examples--Registering_multiple_module_versions--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  ModuleVersion1:
    Type: 'AWS::CloudFormation::ModuleVersion'
    Properties:
      ModuleName: 'My::Sample::Test::MODULE'
      ModulePackage: 's3://my-sample-moduleversion-bucket/sample-module-package-v1.zip'
  ModuleVersion2:
    Type: 'AWS::CloudFormation::ModuleVersion'
    Properties:
      ModuleName: 'My::Sample::Test::MODULE'
      ModulePackage: 's3://my-sample-moduleversion-bucket/sample-module-package-v2.zip'
    DependsOn: ModuleVersion1
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
