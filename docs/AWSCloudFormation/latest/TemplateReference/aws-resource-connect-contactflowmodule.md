---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-contactflowmodule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::ContactFlowModule
<a name="aws-resource-connect-contactflowmodule"></a>

Specifies a flow module for an Connect Customer instance.

## Syntax
<a name="aws-resource-connect-contactflowmodule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-contactflowmodule-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::ContactFlowModule",
  "Properties" : {
      "[Content](#cfn-connect-contactflowmodule-content)" : {{String}},
      "[Description](#cfn-connect-contactflowmodule-description)" : {{String}},
      "[ExternalInvocationConfiguration](#cfn-connect-contactflowmodule-externalinvocationconfiguration)" : {{ExternalInvocationConfiguration}},
      "[InstanceArn](#cfn-connect-contactflowmodule-instancearn)" : {{String}},
      "[Name](#cfn-connect-contactflowmodule-name)" : {{String}},
      "[Settings](#cfn-connect-contactflowmodule-settings)" : {{String}},
      "[State](#cfn-connect-contactflowmodule-state)" : {{String}},
      "[Tags](#cfn-connect-contactflowmodule-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-connect-contactflowmodule-syntax.yaml"></a>

```
Type: AWS::Connect::ContactFlowModule
Properties:
  [Content](#cfn-connect-contactflowmodule-content): {{String}}
  [Description](#cfn-connect-contactflowmodule-description): {{String}}
  [ExternalInvocationConfiguration](#cfn-connect-contactflowmodule-externalinvocationconfiguration): {{
    ExternalInvocationConfiguration}}
  [InstanceArn](#cfn-connect-contactflowmodule-instancearn): {{String}}
  [Name](#cfn-connect-contactflowmodule-name): {{String}}
  [Settings](#cfn-connect-contactflowmodule-settings): {{String}}
  [State](#cfn-connect-contactflowmodule-state): {{String}}
  [Tags](#cfn-connect-contactflowmodule-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-connect-contactflowmodule-properties"></a>

`Content`  <a name="cfn-connect-contactflowmodule-content"></a>
The content of the flow module.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-connect-contactflowmodule-description"></a>
The description of the flow module.
*Required*: No
*Type*: String
*Pattern*: `.*\S.*`
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExternalInvocationConfiguration`  <a name="cfn-connect-contactflowmodule-externalinvocationconfiguration"></a>
The external invocation configuration for the flow module
*Required*: No
*Type*: [ExternalInvocationConfiguration](aws-properties-connect-contactflowmodule-externalinvocationconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceArn`  <a name="cfn-connect-contactflowmodule-instancearn"></a>
The Amazon Resource Name (ARN) of the Connect Customer instance.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]*:[0-9]{12}:instance/[-a-zA-Z0-9]*$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-connect-contactflowmodule-name"></a>
The name of the flow module.
*Required*: Yes
*Type*: String
*Pattern*: `.*\S.*`
*Minimum*: `1`
*Maximum*: `127`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Settings`  <a name="cfn-connect-contactflowmodule-settings"></a>
The configuration settings for the flow module.
*Required*: No
*Type*: String
*Maximum*: `256000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`State`  <a name="cfn-connect-contactflowmodule-state"></a>
The state of the flow module.
*Required*: No
*Type*: String
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-connect-contactflowmodule-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-connect-contactflowmodule-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-connect-contactflowmodule-return-values"></a>

### Ref
<a name="aws-resource-connect-contactflowmodule-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the flow module. For example:

 `{ "Ref": "myFlowModuleArn" }`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-connect-contactflowmodule-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-connect-contactflowmodule-return-values-fn--getatt-fn--getatt"></a>

`ContactFlowModuleArn`  <a name="ContactFlowModuleArn-fn::getatt"></a>
When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the flow module.
For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

`Status`  <a name="Status-fn::getatt"></a>
Property description not available.

## Examples
<a name="aws-resource-connect-contactflowmodule--examples"></a>

### Specify a flow module resource
<a name="aws-resource-connect-contactflowmodule--examples--Specify_a_flow_module_resource"></a>

The following example specifies a flow module resource for an Connect Customer instance.

#### YAML
<a name="aws-resource-connect-contactflowmodule--examples--Specify_a_flow_module_resource--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: Specifies a flow module for an Connect Customer instance
Resources:
  cf11:
    Type: 'AWS::Connect::ContactFlowModule'
    Properties:
      Name: ExampleFlowModule
      Description: flow module created using cfn
      InstanceArn: arn:aws:connect:region-name:aws-account-id:instance/instance-arn
      Content: ExampleFlowModule content(JSON) using Connect Customer Flow Language.
      Tags:
        - Key: testkey
          Value: testValue
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
