---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrock-flowversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::FlowVersion
<a name="aws-resource-bedrock-flowversion"></a>

Creates a version of the flow that you can deploy. For more information, see [Deploy a flow in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-deploy.html) in the Amazon Bedrock User Guide.

## Syntax
<a name="aws-resource-bedrock-flowversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrock-flowversion-syntax.json"></a>

```
{
  "Type" : "AWS::Bedrock::FlowVersion",
  "Properties" : {
      "[Description](#cfn-bedrock-flowversion-description)" : {{String}},
      "[FlowArn](#cfn-bedrock-flowversion-flowarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-bedrock-flowversion-syntax.yaml"></a>

```
Type: AWS::Bedrock::FlowVersion
Properties:
  [Description](#cfn-bedrock-flowversion-description): {{String}}
  [FlowArn](#cfn-bedrock-flowversion-flowarn): {{String}}
```

## Properties
<a name="aws-resource-bedrock-flowversion-properties"></a>

`Description`  <a name="cfn-bedrock-flowversion-description"></a>
The description of the flow version.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FlowArn`  <a name="cfn-bedrock-flowversion-flowarn"></a>
The Amazon Resource Name (ARN) of the flow that the version belongs to.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:bedrock:[a-z0-9-]{1,20}:[0-9]{12}:flow/[0-9a-zA-Z]{10}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-bedrock-flowversion-return-values"></a>

### Ref
<a name="aws-resource-bedrock-flowversion-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Number (ARN) of the flow the version of the flow, separated by a pipe (`|`).

For example, `{ "Ref": "myFlowVersion" }` could return the value `"arn:aws:bedrock:us-east-1:123456789012:flow/FLOW12345|1"`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-bedrock-flowversion-return-values-fn--getatt"></a>

####
<a name="aws-resource-bedrock-flowversion-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The time at the version was created.

`CustomerEncryptionKeyArn`  <a name="CustomerEncryptionKeyArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the KMS key that the flow version is encrypted with.

`ExecutionRoleArn`  <a name="ExecutionRoleArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the service role with permissions to create a flow. For more information, see [Create a service row for flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows-permissions.html) in the Amazon Bedrock User Guide.

`FlowId`  <a name="FlowId-fn::getatt"></a>
The unique identifier of the flow.

`Name`  <a name="Name-fn::getatt"></a>
The name of the flow.

`Status`  <a name="Status-fn::getatt"></a>
The status of the flow.

`Version`  <a name="Version-fn::getatt"></a>
The version of the flow.
