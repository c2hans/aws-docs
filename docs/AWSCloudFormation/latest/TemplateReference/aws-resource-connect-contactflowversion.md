---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-contactflowversion.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::ContactFlowVersion
<a name="aws-resource-connect-contactflowversion"></a>

Creates a version for the specified customer-managed flow within the specified instance.

## Syntax
<a name="aws-resource-connect-contactflowversion-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-contactflowversion-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::ContactFlowVersion",
  "Properties" : {
      "[ContactFlowId](#cfn-connect-contactflowversion-contactflowid)" : {{String}},
      "[Description](#cfn-connect-contactflowversion-description)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-connect-contactflowversion-syntax.yaml"></a>

```
Type: AWS::Connect::ContactFlowVersion
Properties:
  [ContactFlowId](#cfn-connect-contactflowversion-contactflowid): {{String}}
  [Description](#cfn-connect-contactflowversion-description): {{String}}
```

## Properties
<a name="aws-resource-connect-contactflowversion-properties"></a>

`ContactFlowId`  <a name="cfn-connect-contactflowversion-contactflowid"></a>
The identifier of the flow.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z0-9]*:connect:[-a-z0-9]+:[0-9]{12}:instance/[-a-zA-Z0-9]+/contact-flow/[-a-zA-Z0-9]+$`
*Minimum*: `1`
*Maximum*: `500`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-connect-contactflowversion-description"></a>
The description of the flow version.
*Required*: No
*Type*: String
*Maximum*: `500`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-connect-contactflowversion-return-values"></a>

### Ref
<a name="aws-resource-connect-contactflowversion-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-connect-contactflowversion-return-values-fn--getatt"></a>

####
<a name="aws-resource-connect-contactflowversion-return-values-fn--getatt-fn--getatt"></a>

`ContactFlowVersionARN`  <a name="ContactFlowVersionARN-fn::getatt"></a>
The Amazon Resource Name (ARN) of the flow version.

`FlowContentSha256`  <a name="FlowContentSha256-fn::getatt"></a>
Indicates the checksum value of the flow content.

`Version`  <a name="Version-fn::getatt"></a>
The identifier of the flow version.
