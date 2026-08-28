---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudformation-typeactivation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudFormation::TypeActivation
<a name="aws-resource-cloudformation-typeactivation"></a>

The `AWS::CloudFormation::TypeActivation` resource activates a public third-party extension, making it available for use in stack templates.

For information about the CloudFormation registry, see [Managing extensions with the CloudFormation registry](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/registry.html) in the *CloudFormation User Guide*.

## Syntax
<a name="aws-resource-cloudformation-typeactivation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudformation-typeactivation-syntax.json"></a>

```
{
  "Type" : "AWS::CloudFormation::TypeActivation",
  "Properties" : {
      "[AutoUpdate](#cfn-cloudformation-typeactivation-autoupdate)" : {{Boolean}},
      "[ExecutionRoleArn](#cfn-cloudformation-typeactivation-executionrolearn)" : {{String}},
      "[LoggingConfig](#cfn-cloudformation-typeactivation-loggingconfig)" : {{LoggingConfig}},
      "[MajorVersion](#cfn-cloudformation-typeactivation-majorversion)" : {{String}},
      "[PublicTypeArn](#cfn-cloudformation-typeactivation-publictypearn)" : {{String}},
      "[PublisherId](#cfn-cloudformation-typeactivation-publisherid)" : {{String}},
      "[Type](#cfn-cloudformation-typeactivation-type)" : {{String}},
      "[TypeName](#cfn-cloudformation-typeactivation-typename)" : {{String}},
      "[TypeNameAlias](#cfn-cloudformation-typeactivation-typenamealias)" : {{String}},
      "[VersionBump](#cfn-cloudformation-typeactivation-versionbump)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-cloudformation-typeactivation-syntax.yaml"></a>

```
Type: AWS::CloudFormation::TypeActivation
Properties:
  [AutoUpdate](#cfn-cloudformation-typeactivation-autoupdate): {{Boolean}}
  [ExecutionRoleArn](#cfn-cloudformation-typeactivation-executionrolearn): {{String}}
  [LoggingConfig](#cfn-cloudformation-typeactivation-loggingconfig): {{
    LoggingConfig}}
  [MajorVersion](#cfn-cloudformation-typeactivation-majorversion): {{String}}
  [PublicTypeArn](#cfn-cloudformation-typeactivation-publictypearn): {{String}}
  [PublisherId](#cfn-cloudformation-typeactivation-publisherid): {{String}}
  [Type](#cfn-cloudformation-typeactivation-type): {{String}}
  [TypeName](#cfn-cloudformation-typeactivation-typename): {{String}}
  [TypeNameAlias](#cfn-cloudformation-typeactivation-typenamealias): {{String}}
  [VersionBump](#cfn-cloudformation-typeactivation-versionbump): {{String}}
```

## Properties
<a name="aws-resource-cloudformation-typeactivation-properties"></a>

`AutoUpdate`  <a name="cfn-cloudformation-typeactivation-autoupdate"></a>
Whether to automatically update the extension in this account and Region when a new *minor* version is published by the extension publisher. Major versions released by the publisher must be manually updated.
The default is `true`.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionRoleArn`  <a name="cfn-cloudformation-typeactivation-executionrolearn"></a>
The name of the IAM execution role to use to activate the extension.
*Required*: No
*Type*: String
*Pattern*: `arn:.+:iam::[0-9]{12}:role/.+`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LoggingConfig`  <a name="cfn-cloudformation-typeactivation-loggingconfig"></a>
Specifies logging configuration information for an extension.
*Required*: No
*Type*: [LoggingConfig](aws-properties-cloudformation-typeactivation-loggingconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MajorVersion`  <a name="cfn-cloudformation-typeactivation-majorversion"></a>
The major version of this extension you want to activate, if multiple major versions are available. The default is the latest major version. CloudFormation uses the latest available *minor* version of the major version selected.
You can specify `MajorVersion` or `VersionBump`, but not both.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `100000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PublicTypeArn`  <a name="cfn-cloudformation-typeactivation-publictypearn"></a>
The Amazon Resource Number (ARN) of the public extension.
Conditional: You must specify `PublicTypeArn`, or `TypeName`, `Type`, and `PublisherId`.
*Required*: Conditional
*Type*: String
*Pattern*: `arn:aws[A-Za-z0-9-]{0,64}:cloudformation:[A-Za-z0-9-]{1,64}:([0-9]{12})?:type/.+`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PublisherId`  <a name="cfn-cloudformation-typeactivation-publisherid"></a>
The ID of the extension publisher.
Conditional: You must specify `PublicTypeArn`, or `TypeName`, `Type`, and `PublisherId`.
*Required*: Conditional
*Type*: String
*Pattern*: `[0-9a-zA-Z-]{1,40}`
*Minimum*: `1`
*Maximum*: `40`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-cloudformation-typeactivation-type"></a>
The extension type.
Conditional: You must specify `PublicTypeArn`, or `TypeName`, `Type`, and `PublisherId`.
*Required*: Conditional
*Type*: String
*Allowed values*: `RESOURCE | MODULE | HOOK`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TypeName`  <a name="cfn-cloudformation-typeactivation-typename"></a>
The name of the extension.
Conditional: You must specify `PublicTypeArn`, or `TypeName`, `Type`, and `PublisherId`.
*Required*: Conditional
*Type*: String
*Pattern*: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}(::MODULE){0,1}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`TypeNameAlias`  <a name="cfn-cloudformation-typeactivation-typenamealias"></a>
An alias to assign to the public extension in this account and Region. If you specify an alias for the extension, CloudFormation treats the alias as the extension type name within this account and Region. You must use the alias to refer to the extension in your templates, API calls, and CloudFormation console.
An extension alias must be unique within a given account and Region. You can activate the same public resource multiple times in the same account and Region, using different type name aliases.
*Required*: No
*Type*: String
*Pattern*: `[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}::[A-Za-z0-9]{2,64}(::MODULE){0,1}`
*Minimum*: `10`
*Maximum*: `204`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VersionBump`  <a name="cfn-cloudformation-typeactivation-versionbump"></a>
Manually updates a previously-activated type to a new major or minor version, if available. You can also use this parameter to update the value of `AutoUpdate`.
+ `MAJOR`: CloudFormation updates the extension to the newest major version, if one is available.
+ `MINOR`: CloudFormation updates the extension to the newest minor version, if one is available.
*Required*: No
*Type*: String
*Allowed values*: `MAJOR | MINOR`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudformation-typeactivation-return-values"></a>

### Ref
<a name="aws-resource-cloudformation-typeactivation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Number (ARN) of the activated extension, in this account and Region.

 `{ "Ref": "arn:aws:cloudformation:us-west-2:123456789012:type/resource/My-Example" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudformation-typeactivation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudformation-typeactivation-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the activated extension in this account and Region.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
