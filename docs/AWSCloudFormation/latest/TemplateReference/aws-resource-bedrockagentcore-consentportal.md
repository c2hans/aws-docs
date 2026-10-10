---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-consentportal.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::ConsentPortal
<a name="aws-resource-bedrockagentcore-consentportal"></a>

Creates a new consent portal.

## Syntax
<a name="aws-resource-bedrockagentcore-consentportal-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-consentportal-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::ConsentPortal",
  "Properties" : {
      "[Description](#cfn-bedrockagentcore-consentportal-description)" : {{String}},
      "[ExecutionRoleArn](#cfn-bedrockagentcore-consentportal-executionrolearn)" : {{String}},
      "[IdpConfig](#cfn-bedrockagentcore-consentportal-idpconfig)" : {{IdpConfig}},
      "[Name](#cfn-bedrockagentcore-consentportal-name)" : {{String}},
      "[Sources](#cfn-bedrockagentcore-consentportal-sources)" : {{[ ConsentPortalSource, ... ]}},
      "[Tags](#cfn-bedrockagentcore-consentportal-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-consentportal-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::ConsentPortal
Properties:
  [Description](#cfn-bedrockagentcore-consentportal-description): {{String}}
  [ExecutionRoleArn](#cfn-bedrockagentcore-consentportal-executionrolearn): {{String}}
  [IdpConfig](#cfn-bedrockagentcore-consentportal-idpconfig): {{
    IdpConfig}}
  [Name](#cfn-bedrockagentcore-consentportal-name): {{String}}
  [Sources](#cfn-bedrockagentcore-consentportal-sources): {{
    - ConsentPortalSource}}
  [Tags](#cfn-bedrockagentcore-consentportal-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-bedrockagentcore-consentportal-properties"></a>

`Description`  <a name="cfn-bedrockagentcore-consentportal-description"></a>
The description of the consent portal.
*Required*: No
*Type*: String
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionRoleArn`  <a name="cfn-bedrockagentcore-consentportal-executionrolearn"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(-[a-z-]+)?:iam::[0-9]{12}:role/[a-zA-Z0-9+=,.@\-_/]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdpConfig`  <a name="cfn-bedrockagentcore-consentportal-idpconfig"></a>
Property description not available.
*Required*: Yes
*Type*: [IdpConfig](aws-properties-bedrockagentcore-consentportal-idpconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-bedrockagentcore-consentportal-name"></a>
The name of the consent portal.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]{1,50}$`
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Sources`  <a name="cfn-bedrockagentcore-consentportal-sources"></a>
The resources served by the consent portal.
*Required*: Yes
*Type*: Array of [ConsentPortalSource](aws-properties-bedrockagentcore-consentportal-consentportalsource.md)
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-bedrockagentcore-consentportal-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-bedrockagentcore-consentportal-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrockagentcore-consentportal-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-consentportal-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-consentportal-return-values-fn--getatt"></a>

####
<a name="aws-resource-bedrockagentcore-consentportal-return-values-fn--getatt-fn--getatt"></a>

`ConsentPortalArn`  <a name="ConsentPortalArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the consent portal.

`ConsentPortalId`  <a name="ConsentPortalId-fn::getatt"></a>
The unique identifier of the consent portal.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp for when the consent portal was created.

`PortalUrl`  <a name="PortalUrl-fn::getatt"></a>
The URL used to access the consent portal.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the consent portal.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp for when the consent portal was last updated.
