---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-m2-application.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::M2::Application
<a name="aws-resource-m2-application"></a>

Specifies a new application with given parameters. Requires an existing runtime environment and application definition file.

For information about application definitions, see the [AWS Mainframe Modernization User Guide](https://docs.aws.amazon.com/m2/latest/userguide/applications-m2-definition.html).

## Syntax
<a name="aws-resource-m2-application-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-m2-application-syntax.json"></a>

```
{
  "Type" : "AWS::M2::Application",
  "Properties" : {
      "[Definition](#cfn-m2-application-definition)" : {{Definition}},
      "[Description](#cfn-m2-application-description)" : {{String}},
      "[EngineType](#cfn-m2-application-enginetype)" : {{String}},
      "[KmsKeyId](#cfn-m2-application-kmskeyid)" : {{String}},
      "[Name](#cfn-m2-application-name)" : {{String}},
      "[RoleArn](#cfn-m2-application-rolearn)" : {{String}},
      "[Tags](#cfn-m2-application-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-m2-application-syntax.yaml"></a>

```
Type: AWS::M2::Application
Properties:
  [Definition](#cfn-m2-application-definition): {{
    Definition}}
  [Description](#cfn-m2-application-description): {{String}}
  [EngineType](#cfn-m2-application-enginetype): {{String}}
  [KmsKeyId](#cfn-m2-application-kmskeyid): {{String}}
  [Name](#cfn-m2-application-name): {{String}}
  [RoleArn](#cfn-m2-application-rolearn): {{String}}
  [Tags](#cfn-m2-application-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-m2-application-properties"></a>

`Definition`  <a name="cfn-m2-application-definition"></a>
The application definition for a particular application. You can specify either inline JSON or an Amazon S3 bucket location.
For information about application definitions, see the [AWS Mainframe Modernization User Guide](https://docs.aws.amazon.com/m2/latest/userguide/applications-m2-definition.html).
*Required*: No
*Type*: [Definition](aws-properties-m2-application-definition.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-m2-application-description"></a>
The description of the application.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EngineType`  <a name="cfn-m2-application-enginetype"></a>
The type of the target platform for this application.
*Required*: Yes
*Type*: String
*Allowed values*: `microfocus | bluage`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`KmsKeyId`  <a name="cfn-m2-application-kmskeyid"></a>
The identifier of a customer managed key.
*Required*: No
*Type*: String
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-m2-application-name"></a>
The name of the application.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9][A-Za-z0-9_\-]{1,59}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-m2-application-rolearn"></a>
The Amazon Resource Name (ARN) of the role associated with the application.
*Required*: No
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]|):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+=,@.-]{0,1023}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-m2-application-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Object of String
*Pattern*: `^(?!aws:).+$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-m2-application-return-values"></a>

### Ref
<a name="aws-resource-m2-application-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the application Amazon Resource Name (ARN), such as the following:

 `{ "Ref": “SampleApp” }`

Returns a value similar to the following:

 `arn:aws:m2:us-west-2:1234567890:app/y3ca6bhaife2bcvxar3lpivfou`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-m2-application-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-m2-application-return-values-fn--getatt-fn--getatt"></a>

`ApplicationArn`  <a name="ApplicationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the application.

`ApplicationId`  <a name="ApplicationId-fn::getatt"></a>
The identifier of the application.
