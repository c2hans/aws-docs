---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-securityagent-application.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityAgent::Application
<a name="aws-resource-securityagent-application"></a>

The `AWS::SecurityAgent::Application` resource specifies a Security Agent application. An application provides the top-level configuration for Security Agent, including identity and access management settings and encryption options.

## Syntax
<a name="aws-resource-securityagent-application-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-securityagent-application-syntax.json"></a>

```
{
  "Type" : "AWS::SecurityAgent::Application",
  "Properties" : {
      "[DefaultKmsKeyId](#cfn-securityagent-application-defaultkmskeyid)" : {{String}},
      "[IdCConfiguration](#cfn-securityagent-application-idcconfiguration)" : {{IdCConfiguration}},
      "[RoleArn](#cfn-securityagent-application-rolearn)" : {{String}},
      "[Tags](#cfn-securityagent-application-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-securityagent-application-syntax.yaml"></a>

```
Type: AWS::SecurityAgent::Application
Properties:
  [DefaultKmsKeyId](#cfn-securityagent-application-defaultkmskeyid): {{String}}
  [IdCConfiguration](#cfn-securityagent-application-idcconfiguration): {{
    IdCConfiguration}}
  [RoleArn](#cfn-securityagent-application-rolearn): {{String}}
  [Tags](#cfn-securityagent-application-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-securityagent-application-properties"></a>

`DefaultKmsKeyId`  <a name="cfn-securityagent-application-defaultkmskeyid"></a>
The identifier of the default Amazon Web Services KMS key to use for encrypting data in the application.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdCConfiguration`  <a name="cfn-securityagent-application-idcconfiguration"></a>
The IAM Identity Center configuration for the application.
*Required*: No
*Type*: [IdCConfiguration](aws-properties-securityagent-application-idcconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-securityagent-application-rolearn"></a>
The Amazon Resource Name (ARN) of the IAM role to associate with the application.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-securityagent-application-tags"></a>
The tags to associate with the application.
*Required*: No
*Type*: Array of [Tag](aws-properties-securityagent-application-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-securityagent-application-return-values"></a>

### Ref
<a name="aws-resource-securityagent-application-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the application ID. For example:

 `{ "Ref": "MyApplication" }`

For the application `MyApplication`, `Ref` returns the unique identifier of the Security Agent application.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-securityagent-application-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-securityagent-application-return-values-fn--getatt-fn--getatt"></a>

`ApplicationId`  <a name="ApplicationId-fn::getatt"></a>
The unique identifier of the Security Agent application. For example: `app-0123456789abcdef0`.

`ApplicationName`  <a name="ApplicationName-fn::getatt"></a>
The name of the Security Agent application.

`Domain`  <a name="Domain-fn::getatt"></a>
The domain associated with the Security Agent application.

`IdCConfiguration.IdCApplicationArn`  <a name="IdCConfiguration.IdCApplicationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the IAM Identity Center application associated with the Security Agent application.
