---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sagemaker-app.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SageMaker::App
<a name="aws-resource-sagemaker-app"></a>

Creates a running app for the specified UserProfile. This operation is automatically invoked by Amazon SageMaker AI upon access to the associated Domain, and when new kernel configurations are selected by the user. A user may have multiple Apps active simultaneously.

## Syntax
<a name="aws-resource-sagemaker-app-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sagemaker-app-syntax.json"></a>

```
{
  "Type" : "AWS::SageMaker::App",
  "Properties" : {
      "[AppName](#cfn-sagemaker-app-appname)" : {{String}},
      "[AppType](#cfn-sagemaker-app-apptype)" : {{String}},
      "[DomainId](#cfn-sagemaker-app-domainid)" : {{String}},
      "[RecoveryMode](#cfn-sagemaker-app-recoverymode)" : {{Boolean}},
      "[ResourceSpec](#cfn-sagemaker-app-resourcespec)" : {{ResourceSpec}},
      "[Tags](#cfn-sagemaker-app-tags)" : {{[ Tag, ... ]}},
      "[UserProfileName](#cfn-sagemaker-app-userprofilename)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-sagemaker-app-syntax.yaml"></a>

```
Type: AWS::SageMaker::App
Properties:
  [AppName](#cfn-sagemaker-app-appname): {{String}}
  [AppType](#cfn-sagemaker-app-apptype): {{String}}
  [DomainId](#cfn-sagemaker-app-domainid): {{String}}
  [RecoveryMode](#cfn-sagemaker-app-recoverymode): {{Boolean}}
  [ResourceSpec](#cfn-sagemaker-app-resourcespec): {{
    ResourceSpec}}
  [Tags](#cfn-sagemaker-app-tags): {{
    - Tag}}
  [UserProfileName](#cfn-sagemaker-app-userprofilename): {{String}}
```

## Properties
<a name="aws-resource-sagemaker-app-properties"></a>

`AppName`  <a name="cfn-sagemaker-app-appname"></a>
The name of the app.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AppType`  <a name="cfn-sagemaker-app-apptype"></a>
The type of app.
*Required*: Yes
*Type*: String
*Allowed values*: `JupyterServer | KernelGateway | RStudioServerPro | RSessionGateway | Canvas`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DomainId`  <a name="cfn-sagemaker-app-domainid"></a>
The domain ID.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RecoveryMode`  <a name="cfn-sagemaker-app-recoverymode"></a>
Enables recovery mode for the SageMaker Studio application. When enabled, recovery mode allows you to access your Studio application when a configuration issue prevents normal startup. For more information, see [Recovery mode](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-troubleshooting.html).
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceSpec`  <a name="cfn-sagemaker-app-resourcespec"></a>
Specifies the ARNs of a SageMaker image and SageMaker image version, and the instance type that the version runs on.
*Required*: No
*Type*: [ResourceSpec](aws-properties-sagemaker-app-resourcespec.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-sagemaker-app-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-sagemaker-app-tag.md)
*Minimum*: `0`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserProfileName`  <a name="cfn-sagemaker-app-userprofilename"></a>
The user profile name.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9](-*[a-zA-Z0-9]){0,62}`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-sagemaker-app-return-values"></a>

### Ref
<a name="aws-resource-sagemaker-app-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the app type, app name, Domain ID, and user profile name.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-sagemaker-app-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-sagemaker-app-return-values-fn--getatt-fn--getatt"></a>

`AppArn`  <a name="AppArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the app, such as `arn:aws:sagemaker:us-west-2:account-id:app/my-app-name`.

`BuiltInLifecycleConfigArn`  <a name="BuiltInLifecycleConfigArn-fn::getatt"></a>
The lifecycle configuration that runs before the default lifecycle configuration. It can override changes made in the default lifecycle configuration.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
