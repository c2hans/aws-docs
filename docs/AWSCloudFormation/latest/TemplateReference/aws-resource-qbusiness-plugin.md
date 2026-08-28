---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-qbusiness-plugin.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QBusiness::Plugin
<a name="aws-resource-qbusiness-plugin"></a>

Information about an Amazon Q Business plugin and its configuration.

## Syntax
<a name="aws-resource-qbusiness-plugin-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-qbusiness-plugin-syntax.json"></a>

```
{
  "Type" : "AWS::QBusiness::Plugin",
  "Properties" : {
      "[ApplicationId](#cfn-qbusiness-plugin-applicationid)" : {{String}},
      "[AuthConfiguration](#cfn-qbusiness-plugin-authconfiguration)" : {{PluginAuthConfiguration}},
      "[CustomPluginConfiguration](#cfn-qbusiness-plugin-custompluginconfiguration)" : {{CustomPluginConfiguration}},
      "[DisplayName](#cfn-qbusiness-plugin-displayname)" : {{String}},
      "[ServerUrl](#cfn-qbusiness-plugin-serverurl)" : {{String}},
      "[State](#cfn-qbusiness-plugin-state)" : {{String}},
      "[Tags](#cfn-qbusiness-plugin-tags)" : {{[ Tag, ... ]}},
      "[Type](#cfn-qbusiness-plugin-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-qbusiness-plugin-syntax.yaml"></a>

```
Type: AWS::QBusiness::Plugin
Properties:
  [ApplicationId](#cfn-qbusiness-plugin-applicationid): {{String}}
  [AuthConfiguration](#cfn-qbusiness-plugin-authconfiguration): {{
    PluginAuthConfiguration}}
  [CustomPluginConfiguration](#cfn-qbusiness-plugin-custompluginconfiguration): {{
    CustomPluginConfiguration}}
  [DisplayName](#cfn-qbusiness-plugin-displayname): {{String}}
  [ServerUrl](#cfn-qbusiness-plugin-serverurl): {{String}}
  [State](#cfn-qbusiness-plugin-state): {{String}}
  [Tags](#cfn-qbusiness-plugin-tags): {{
    - Tag}}
  [Type](#cfn-qbusiness-plugin-type): {{String}}
```

## Properties
<a name="aws-resource-qbusiness-plugin-properties"></a>

`ApplicationId`  <a name="cfn-qbusiness-plugin-applicationid"></a>
The identifier of the application that will contain the plugin.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9-]{35}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AuthConfiguration`  <a name="cfn-qbusiness-plugin-authconfiguration"></a>
Authentication configuration information for an Amazon Q Business plugin.
*Required*: Yes
*Type*: [PluginAuthConfiguration](aws-properties-qbusiness-plugin-pluginauthconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomPluginConfiguration`  <a name="cfn-qbusiness-plugin-custompluginconfiguration"></a>
 Configuration information required to create a custom plugin.
*Required*: No
*Type*: [CustomPluginConfiguration](aws-properties-qbusiness-plugin-custompluginconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-qbusiness-plugin-displayname"></a>
The name of the plugin.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9_-]*$`
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerUrl`  <a name="cfn-qbusiness-plugin-serverurl"></a>
The plugin server URL used for configuration.
*Required*: No
*Type*: String
*Pattern*: `^(https?|ftp|file)://([^\s]*)$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`State`  <a name="cfn-qbusiness-plugin-state"></a>
The current status of the plugin.
*Required*: No
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-qbusiness-plugin-tags"></a>
A list of key-value pairs that identify or categorize the data source connector. You can also use tags to help control access to the data source connector. Tag keys and values can consist of Unicode letters, digits, white space, and any of the following symbols: \_ . : / = \+ - @.
*Required*: No
*Type*: Array of [Tag](aws-properties-qbusiness-plugin-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-qbusiness-plugin-type"></a>
The type of the plugin.
*Required*: Yes
*Type*: String
*Allowed values*: `SERVICE_NOW | SALESFORCE | JIRA | ZENDESK | CUSTOM | QUICKSIGHT | SERVICENOW_NOW_PLATFORM | JIRA_CLOUD | SALESFORCE_CRM | ZENDESK_SUITE | ATLASSIAN_CONFLUENCE | GOOGLE_CALENDAR | MICROSOFT_TEAMS | MICROSOFT_EXCHANGE | PAGERDUTY_ADVANCE | SMARTSHEET | ASANA`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-qbusiness-plugin-return-values"></a>

### Ref
<a name="aws-resource-qbusiness-plugin-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the application ID and plugin ID. For example:

 `{"Ref": "ApplicationId|PluginId"}`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-qbusiness-plugin-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-qbusiness-plugin-return-values-fn--getatt-fn--getatt"></a>

`BuildStatus`  <a name="BuildStatus-fn::getatt"></a>
The current status of a plugin. A plugin is modified asynchronously.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp for when the plugin was created.

`PluginArn`  <a name="PluginArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of a plugin.

`PluginId`  <a name="PluginId-fn::getatt"></a>
The identifier of the plugin.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp for when the plugin was last updated.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
