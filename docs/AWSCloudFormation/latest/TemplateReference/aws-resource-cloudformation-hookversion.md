---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-hookversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::HookVersion
<a name="aws-resource-cloudformation-hookversion"></a>

The `AWS::CloudFormation::HookVersion` resource publishes new or first version of a Hook to the CloudFormation registry.

For information about the CloudFormation registry, see [Managing extensions with the CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) in the *CloudFormation User Guide*.

This resource type is not compatible with Guard and Lambda Hooks.

## Syntax
<a name="aws-resource-cloudformation-hookversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudformation-hookversion-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFormation::HookVersion",
  "Properties" : {
      "[ExecutionRoleArn](#cfn-cloudformation-hookversion-executionrolearn)" : {{String}},
      "[LoggingConfig](#cfn-cloudformation-hookversion-loggingconfig)" : {{LoggingConfig}},
      "[SchemaHandlerPackage](#cfn-cloudformation-hookversion-schemahandlerpackage)" : {{String}},
      "[TypeName](#cfn-cloudformation-hookversion-typename)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cloudformation-hookversion-syntax.yaml"></a>

```
Type: AWS::CloudFormation::HookVersion
Properties:
  [ExecutionRoleArn](#cfn-cloudformation-hookversion-executionrolearn): {{String}}
  [LoggingConfig](#cfn-cloudformation-hookversion-loggingconfig): {{
    LoggingConfig}}
  [SchemaHandlerPackage](#cfn-cloudformation-hookversion-schemahandlerpackage): {{String}}
  [TypeName](#cfn-cloudformation-hookversion-typename): {{String}}
```

## Properties
<a name="aws-resource-cloudformation-hookversion-properties"></a>

`ExecutionRoleArn`  <a name="cfn-cloudformation-hookversion-executionrolearn"></a>
The Amazon Resource Name (ARN) of the task execution role that grants the Hook permission.
*Required*: No
*Type*: String
*Pattern*: `arn:.+:iam::[0-9]{12}:role/.+`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LoggingConfig`  <a name="cfn-cloudformation-hookversion-loggingconfig"></a>
Contains logging configuration information for an extension.
*Required*: No
*Type*: [LoggingConfig](aws-properties-cloudformation-hookversion-loggingconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SchemaHandlerPackage`  <a name="cfn-cloudformation-hookversion-schemahandlerpackage"></a>
A URL to the Amazon S3 bucket for the Hook project package that contains the necessary files for the Hook you want to register.
For information on generating a schema handler package, see [Modeling custom CloudFormation Hooks](https://docs.aws.amazon.com/cloudformation-cli/latest/hooks-userguide/hooks-model.html) in the *CloudFormation Hooks User Guide*.
To register the Hook, you must have `s3:GetObject` permissions to access the S3 objects.
*Required*: Yes
*Type*: String
*Maximum*: `4096`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TypeName`  <a name="cfn-cloudformation-hookversion-typename"></a>
The unique name for your Hook. Specifies a three-part namespace for your Hook, with a recommended pattern of `Organization::Service::Hook`.
The following organization namespaces are reserved and can't be used in your Hook type names:
+  `Alexa`
+  `AMZN`
+  `Amazon`
+  `ASK`
+  `AWS`
+  `Custom`
+  `Dev`
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-cloudformation-hookversion-return-values"></a>

### Ref
<a name="aws-resource-cloudformation-hookversion-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the Hook version. For example:

 `arn:aws:cloudformation:us-west-2:123456789012:type/hook/Sample-CloudFormation-Hook/00000001`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudformation-hookversion-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudformation-hookversion-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the Hook.

`IsDefaultVersion`  <a name="IsDefaultVersion-fn::getatt"></a>
Whether the specified Hook version is set as the default version.

`TypeArn`  <a name="TypeArn-fn::getatt"></a>
The Amazon Resource Number (ARN) assigned to this version of the Hook.

`VersionId`  <a name="VersionId-fn::getatt"></a>
The ID of this version of the Hook.

`Visibility`  <a name="Visibility-fn::getatt"></a>
The visibility level that determines who can see and use this Hook in CloudFormation operations:
+ `PRIVATE`: The Hook is only visible and usable within the account where it was registered. CloudFormation automatically marks any Hooks you register as `PRIVATE`.
+ `PUBLIC`: The Hook is publicly visible and usable within any AWS account.

## Examples
<a name="aws-resource-cloudformation-hookversion--examples"></a>

**Topics**
+ [Specifying a Hook version](#aws-resource-cloudformation-hookversion--examples--Specifying_a_Hook_version)
+ [Specifying the default Hook version](#aws-resource-cloudformation-hookversion--examples--Specifying_the_default_Hook_version)

### Specifying a Hook version
<a name="aws-resource-cloudformation-hookversion--examples--Specifying_a_Hook_version"></a>

The following example demonstrates how to specify a new Hook version.

#### JSON
<a name="aws-resource-cloudformation-hookversion--examples--Specifying_a_Hook_version--json"></a>

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
        }
    }
}
```

#### YAML
<a name="aws-resource-cloudformation-hookversion--examples--Specifying_a_Hook_version--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  HookVersion:
    Type: AWS::CloudFormation::HookVersion
    Properties:
      TypeName: 'My::Sample::Hook'
      SchemaHandlerPackage: 's3://amzn-s3-demo-bucket/my-sample-hook.zip'
```

### Specifying the default Hook version
<a name="aws-resource-cloudformation-hookversion--examples--Specifying_the_default_Hook_version"></a>

The following example demonstrates how to specify a new Hook version and use the `Ref` return value to set that version as the default version.

#### JSON
<a name="aws-resource-cloudformation-hookversion--examples--Specifying_the_default_Hook_version--json"></a>

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
<a name="aws-resource-cloudformation-hookversion--examples--Specifying_the_default_Hook_version--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  HookVersion:
    Type: AWS::CloudFormation::HookVersion
    Properties:
      TypeName: My::Sample::Hook
      SchemaHandlerPackage: s3://amzn-s3-demo-bucket/my-sample-hook.zip
  HookDefaultVersion:
    Type: AWS::CloudFormation::HookDefaultVersion
    Properties:
      TypeVersionArn: !Ref HookVersion
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
