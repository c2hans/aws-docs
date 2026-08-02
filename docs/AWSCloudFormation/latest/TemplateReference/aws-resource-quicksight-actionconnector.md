---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-quicksight-actionconnector.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::ActionConnector
<a name="aws-resource-quicksight-actionconnector"></a>

Creates an action connector that enables Amazon Quick Sight to connect to external services and perform actions. Action connectors support various authentication methods and can be configured with specific actions from supported connector types like Amazon S3, Salesforce, JIRA.

## Syntax
<a name="aws-resource-quicksight-actionconnector-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-quicksight-actionconnector-syntax.json"></a>

```
{
  "Type" : "AWS::QuickSight::ActionConnector",
  "Properties" : {
      "[ActionConnectorId](#cfn-quicksight-actionconnector-actionconnectorid)" : {{String}},
      "[AuthenticationConfig](#cfn-quicksight-actionconnector-authenticationconfig)" : {{AuthConfig}},
      "[AwsAccountId](#cfn-quicksight-actionconnector-awsaccountid)" : {{String}},
      "[Description](#cfn-quicksight-actionconnector-description)" : {{String}},
      "[Name](#cfn-quicksight-actionconnector-name)" : {{String}},
      "[Permissions](#cfn-quicksight-actionconnector-permissions)" : {{[ ResourcePermission, ... ]}},
      "[Tags](#cfn-quicksight-actionconnector-tags)" : {{[ Tag, ... ]}},
      "[Type](#cfn-quicksight-actionconnector-type)" : {{String}},
      "[VpcConnectionArn](#cfn-quicksight-actionconnector-vpcconnectionarn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-quicksight-actionconnector-syntax.yaml"></a>

```
Type: AWS::QuickSight::ActionConnector
Properties:
  [ActionConnectorId](#cfn-quicksight-actionconnector-actionconnectorid): {{String}}
  [AuthenticationConfig](#cfn-quicksight-actionconnector-authenticationconfig): {{
    AuthConfig}}
  [AwsAccountId](#cfn-quicksight-actionconnector-awsaccountid): {{String}}
  [Description](#cfn-quicksight-actionconnector-description): {{String}}
  [Name](#cfn-quicksight-actionconnector-name): {{String}}
  [Permissions](#cfn-quicksight-actionconnector-permissions): {{
    - ResourcePermission}}
  [Tags](#cfn-quicksight-actionconnector-tags): {{
    - Tag}}
  [Type](#cfn-quicksight-actionconnector-type): {{String}}
  [VpcConnectionArn](#cfn-quicksight-actionconnector-vpcconnectionarn): {{String}}
```

## Properties
<a name="aws-resource-quicksight-actionconnector-properties"></a>

`ActionConnectorId`  <a name="cfn-quicksight-actionconnector-actionconnectorid"></a>
The unique identifier of the action connector.
*Required*: Yes
*Type*: String
*Pattern*: `^[\w\-]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AuthenticationConfig`  <a name="cfn-quicksight-actionconnector-authenticationconfig"></a>
The authentication configuration used to connect to the external service.
*Required*: Yes
*Type*: [AuthConfig](aws-properties-quicksight-actionconnector-authconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AwsAccountId`  <a name="cfn-quicksight-actionconnector-awsaccountid"></a>
The AWS account ID associated with the action connector.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9]{12}$`
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-quicksight-actionconnector-description"></a>
The description of the action connector.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9 _.,!?-]*$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-quicksight-actionconnector-name"></a>
The name of the action connector.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9](?:[\w- ]*[A-Za-z0-9])?$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Permissions`  <a name="cfn-quicksight-actionconnector-permissions"></a>
The permissions configuration that defines which users, groups, or namespaces can access this action connector and what operations they can perform.
*Required*: No
*Type*: Array of [ResourcePermission](aws-properties-quicksight-actionconnector-resourcepermission.md)
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-quicksight-actionconnector-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-quicksight-actionconnector-tag.md)
*Minimum*: `1`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-quicksight-actionconnector-type"></a>
The type of action connector.
*Required*: Yes
*Type*: String
*Allowed values*: `GENERIC_HTTP | SERVICENOW_NOW_PLATFORM | SALESFORCE_CRM | MICROSOFT_OUTLOOK | PAGERDUTY_ADVANCE | JIRA_CLOUD | ATLASSIAN_CONFLUENCE | AMAZON_S3 | AMAZON_BEDROCK_AGENT_RUNTIME | AMAZON_BEDROCK_RUNTIME | AMAZON_BEDROCK_DATA_AUTOMATION_RUNTIME | AMAZON_TEXTRACT | AMAZON_COMPREHEND | AMAZON_COMPREHEND_MEDICAL | MICROSOFT_ONEDRIVE | MICROSOFT_SHAREPOINT | MICROSOFT_TEAMS | SAP_BUSINESSPARTNER | SAP_PRODUCTMASTERDATA | SAP_PHYSICALINVENTORY | SAP_BILLOFMATERIALS | SAP_MATERIALSTOCK | ZENDESK_SUITE | SMARTSHEET | SLACK | ASANA | BAMBOO_HR`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`VpcConnectionArn`  <a name="cfn-quicksight-actionconnector-vpcconnectionarn"></a>
The ARN of the VPC connection used for secure connectivity to the external service.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-quicksight-actionconnector-return-values"></a>

### Ref
<a name="aws-resource-quicksight-actionconnector-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-quicksight-actionconnector-return-values-fn--getatt"></a>

####
<a name="aws-resource-quicksight-actionconnector-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the action connector.

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
The timestamp when the action connector was created.

`EnabledActions`  <a name="EnabledActions-fn::getatt"></a>
The list of actions that are enabled for this connector.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
The date and time when the action connector was last updated.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the action connector.
