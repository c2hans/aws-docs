---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ssm-cloudconnector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SSM::CloudConnector
<a name="aws-resource-ssm-cloudconnector"></a>

Creates a cloud connector that establishes a connection between Systems Manager and a third-party cloud environment.

## Syntax
<a name="aws-resource-ssm-cloudconnector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ssm-cloudconnector-syntax.json"></a>

```
{
  "Type" : "AWS::SSM::CloudConnector",
  "Properties" : {
      "[ConfigConnectorArn](#cfn-ssm-cloudconnector-configconnectorarn)" : {{String}},
      "[Configuration](#cfn-ssm-cloudconnector-configuration)" : {{CloudConnectorConfiguration}},
      "[Description](#cfn-ssm-cloudconnector-description)" : {{String}},
      "[DisplayName](#cfn-ssm-cloudconnector-displayname)" : {{String}},
      "[RoleArn](#cfn-ssm-cloudconnector-rolearn)" : {{String}},
      "[Tags](#cfn-ssm-cloudconnector-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ssm-cloudconnector-syntax.yaml"></a>

```
Type: AWS::SSM::CloudConnector
Properties:
  [ConfigConnectorArn](#cfn-ssm-cloudconnector-configconnectorarn): {{String}}
  [Configuration](#cfn-ssm-cloudconnector-configuration): {{
    CloudConnectorConfiguration}}
  [Description](#cfn-ssm-cloudconnector-description): {{String}}
  [DisplayName](#cfn-ssm-cloudconnector-displayname): {{String}}
  [RoleArn](#cfn-ssm-cloudconnector-rolearn): {{String}}
  [Tags](#cfn-ssm-cloudconnector-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ssm-cloudconnector-properties"></a>

`ConfigConnectorArn`  <a name="cfn-ssm-cloudconnector-configconnectorarn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-cn|-us-gov)?:config:[a-z0-9-]+:\d{12}:connector/.+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Configuration`  <a name="cfn-ssm-cloudconnector-configuration"></a>
Property description not available.
*Required*: Yes
*Type*: [CloudConnectorConfiguration](aws-properties-ssm-cloudconnector-cloudconnectorconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-ssm-cloudconnector-description"></a>
The description of the cloud connector.
*Required*: No
*Type*: String
*Pattern*: `^[\p{L}\p{Z}\p{N}\p{P}\p{M}]*$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-ssm-cloudconnector-displayname"></a>
The friendly name of the cloud connector.
*Required*: Yes
*Type*: String
*Pattern*: `^[\p{L}\p{Z}\p{N}\p{P}\p{M}]*$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RoleArn`  <a name="cfn-ssm-cloudconnector-rolearn"></a>
The ARN of the IAM role used by the cloud connector.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[a-z0-9-]*:iam::\d{12}:role/[\w-/.@+=,]{1,1017}$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-ssm-cloudconnector-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-ssm-cloudconnector-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ssm-cloudconnector-return-values"></a>

### Ref
<a name="aws-resource-ssm-cloudconnector-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ssm-cloudconnector-return-values-fn--getatt"></a>

####
<a name="aws-resource-ssm-cloudconnector-return-values-fn--getatt-fn--getatt"></a>

`CloudConnectorArn`  <a name="CloudConnectorArn-fn::getatt"></a>
Property description not available.

`CloudConnectorId`  <a name="CloudConnectorId-fn::getatt"></a>
The ID of the cloud connector.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time the cloud connector was created.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The date and time the cloud connector was last updated.
