---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-resourceversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::ResourceVersion
<a name="aws-resource-cloudformation-resourceversion"></a>

The `AWS::CloudFormation::ResourceVersion` resource registers a resource version with the CloudFormation registry. Registering a resource version makes it available for use in CloudFormation templates in your AWS account, and includes:
+ Validating the resource schema.
+ Determining which handlers, if any, have been specified for the resource.
+ Making the resource available for use in your account.

For information about the CloudFormation registry, see [Managing extensions with the CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) in the *CloudFormation User Guide*.

You can have a maximum of 50 resource versions registered at a time. This maximum is per account and per Region.

## Syntax
<a name="aws-resource-cloudformation-resourceversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudformation-resourceversion-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFormation::ResourceVersion",
  "Properties" : {
      "[ExecutionRoleArn](#cfn-cloudformation-resourceversion-executionrolearn)" : {{String}},
      "[LoggingConfig](#cfn-cloudformation-resourceversion-loggingconfig)" : {{LoggingConfig}},
      "[SchemaHandlerPackage](#cfn-cloudformation-resourceversion-schemahandlerpackage)" : {{String}},
      "[TypeName](#cfn-cloudformation-resourceversion-typename)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cloudformation-resourceversion-syntax.yaml"></a>

```
Type: AWS::CloudFormation::ResourceVersion
Properties:
  [ExecutionRoleArn](#cfn-cloudformation-resourceversion-executionrolearn): {{String}}
  [LoggingConfig](#cfn-cloudformation-resourceversion-loggingconfig): {{
    LoggingConfig}}
  [SchemaHandlerPackage](#cfn-cloudformation-resourceversion-schemahandlerpackage): {{String}}
  [TypeName](#cfn-cloudformation-resourceversion-typename): {{String}}
```

## Properties
<a name="aws-resource-cloudformation-resourceversion-properties"></a>

`ExecutionRoleArn`  <a name="cfn-cloudformation-resourceversion-executionrolearn"></a>
The Amazon Resource Name (ARN) of the IAM role for CloudFormation to assume when invoking the resource. If your resource calls AWS APIs in any of its handlers, you must create an IAM execution role that includes the necessary permissions to call those AWS APIs, and provision that execution role in your account. When CloudFormation needs to invoke the resource type handler, CloudFormation assumes this execution role to create a temporary session token, which it then passes to the resource type handler, thereby supplying your resource type with the appropriate credentials.
*Required*: No
*Type*: String
*Pattern*: `arn:.+:iam::[0-9]{12}:role/.+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LoggingConfig`  <a name="cfn-cloudformation-resourceversion-loggingconfig"></a>
Logging configuration information for a resource.
*Required*: No
*Type*: [LoggingConfig](aws-properties-cloudformation-resourceversion-loggingconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SchemaHandlerPackage`  <a name="cfn-cloudformation-resourceversion-schemahandlerpackage"></a>
A URL to the S3 bucket for the resource project package that contains the necessary files for the resource you want to register.
For information on generating a schema handler package, see [Modeling resource types to use with CloudFormation](https://docs.aws.amazon.com/cloudformation-cli/latest/userguide/resource-type-model.html) in the *CloudFormation Command Line Interface (CLI) User Guide*.
To register the resource version, you must have `s3:GetObject` permissions to access the S3 objects.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `4096`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TypeName`  <a name="cfn-cloudformation-resourceversion-typename"></a>
The name of the resource being registered.
We recommend that resource names adhere to the following pattern: *company\_or\_organization*::*service*::*type*.
The following organization namespaces are reserved and can't be used in your resource names:
+  `Alexa`
+  `AMZN`
+  `Amazon`
+  `AWS`
+  `Custom`
+  `Dev`
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-cloudformation-resourceversion-return-values"></a>

### Ref
<a name="aws-resource-cloudformation-resourceversion-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the resource version. For example:

 `arn:aws:cloudformation:us-west-2:123456789012:type/resource/Sample-CloudFormation-Resource/00000001`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudformation-resourceversion-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudformation-resourceversion-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the resource.

`IsDefaultVersion`  <a name="IsDefaultVersion-fn::getatt"></a>
Whether the specified resource version is set as the default version.
This applies only to private extensions you have registered in your account, and extensions published by AWS. For public third-party extensions, whether they are activated in your account, CloudFormation returns `null`.

`ProvisioningType`  <a name="ProvisioningType-fn::getatt"></a>
For resource type extensions, the provisioning behavior of the resource type. CloudFormation determines the provisioning type during registration, based on the types of handlers in the schema handler package submitted.
Possible values:
+ `FULLY_MUTABLE`: The resource type includes an update handler to process updates to the type during stack update operations.
+ `IMMUTABLE`: The resource type doesn't include an update handler, so the type can't be updated and must instead be replaced during stack update operations.
+ `NON_PROVISIONABLE`: The resource type doesn't include all the following handlers, and therefore can't actually be provisioned.
  + create
  + read
  + delete

`TypeArn`  <a name="TypeArn-fn::getatt"></a>
The Amazon Resource Name (ARN) for the extension.

`VersionId`  <a name="VersionId-fn::getatt"></a>
The ID of a specific version of the resource. The version ID is the value at the end of the Amazon Resource Name (ARN) assigned to the resource version when it is registered.

`Visibility`  <a name="Visibility-fn::getatt"></a>
The visibility level that determines who can see and use this resource in CloudFormation operations:
+ `PRIVATE`: The resource is only visible and usable within the account where it was registered. CloudFormation automatically marks any resources you register as `PRIVATE`.
+ `PUBLIC`: The resource is publicly visible and usable within any AWS account.

## Examples
<a name="aws-resource-cloudformation-resourceversion--examples"></a>

**Topics**
+ [Specifying a resource version](#aws-resource-cloudformation-resourceversion--examples--Specifying_a_resource_version)
+ [Specifying a resource version and setting it as the default version](#aws-resource-cloudformation-resourceversion--examples--Specifying_a_resource_version_and_setting_it_as_the_default_version)

### Specifying a resource version
<a name="aws-resource-cloudformation-resourceversion--examples--Specifying_a_resource_version"></a>

The following example demonstrates how to specify a new resource version.

#### JSON
<a name="aws-resource-cloudformation-resourceversion--examples--Specifying_a_resource_version--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "ResourceVersion": {
            "Type": "AWS::CloudFormation::ResourceVersion",
            "Properties": {
                "TypeName": "My::Sample::Resource",
                "SchemaHandlerPackage": "s3://amzn-s3-demo-bucket/my-sample-resource.zip"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-cloudformation-resourceversion--examples--Specifying_a_resource_version--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  ResourceVersion:
    Type: AWS::CloudFormation::ResourceVersion
    Properties:
      TypeName: My::Sample::Resource
      SchemaHandlerPackage: s3://amzn-s3-demo-bucket/my-sample-resource.zip
```

### Specifying a resource version and setting it as the default version
<a name="aws-resource-cloudformation-resourceversion--examples--Specifying_a_resource_version_and_setting_it_as_the_default_version"></a>

The following example demonstrates how to specify and new resource version, and use the `Ref` return value to set that version as the default version.

#### JSON
<a name="aws-resource-cloudformation-resourceversion--examples--Specifying_a_resource_version_and_setting_it_as_the_default_version--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Resources": {
        "ResourceVersion": {
            "Type": "AWS::CloudFormation::ResourceVersion",
            "Properties": {
                "TypeName": "My::Sample::Resource",
                "SchemaHandlerPackage": "s3://amzn-s3-demo-bucket/my-sample-resource.zip"
            }
        },
        "ResourceDefaultVersion": {
            "Type": "AWS::CloudFormation::ResourceDefaultVersion",
            "Properties": {
                "TypeVersionArn": {
                    "Ref": "ResourceVersion"
                }
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-cloudformation-resourceversion--examples--Specifying_a_resource_version_and_setting_it_as_the_default_version--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Resources:
  ResourceVersion:
    Type: AWS::CloudFormation::ResourceVersion
    Properties:
      TypeName: My::Sample::Resource
      SchemaHandlerPackage: s3://amzn-s3-demo-bucket/my-sample-resource.zip
  ResourceDefaultVersion:
    Type: AWS::CloudFormation::ResourceDefaultVersion
    Properties:
      TypeVersionArn: !Ref ResourceVersion
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
