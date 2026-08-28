---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appstream-stack.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::Stack
<a name="aws-resource-appstream-stack"></a>

The `AWS::AppStream::Stack` resource creates a stack to start streaming applications to Amazon WorkSpaces Applications users. A stack consists of an associated fleet, user access policies, and storage configurations.

## Syntax
<a name="aws-resource-appstream-stack-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-appstream-stack-syntax.json"></a>

```
{
  "Type" : "AWS::AppStream::Stack",
  "Properties" : {
      "[AccessEndpoints](#cfn-appstream-stack-accessendpoints)" : {{[ AccessEndpoint, ... ]}},
      "[AgentAccessConfig](#cfn-appstream-stack-agentaccessconfig)" : {{AgentAccessConfig}},
      "[ApplicationSettings](#cfn-appstream-stack-applicationsettings)" : {{ApplicationSettings}},
      "[AttributesToDelete](#cfn-appstream-stack-attributestodelete)" : {{[ String, ... ]}},
      "[ContentRedirection](#cfn-appstream-stack-contentredirection)" : {{ContentRedirection}},
      "[DeleteStorageConnectors](#cfn-appstream-stack-deletestorageconnectors)" : {{Boolean}},
      "[Description](#cfn-appstream-stack-description)" : {{String}},
      "[DisplayName](#cfn-appstream-stack-displayname)" : {{String}},
      "[EmbedHostDomains](#cfn-appstream-stack-embedhostdomains)" : {{[ String, ... ]}},
      "[FeedbackURL](#cfn-appstream-stack-feedbackurl)" : {{String}},
      "[Name](#cfn-appstream-stack-name)" : {{String}},
      "[RedirectURL](#cfn-appstream-stack-redirecturl)" : {{String}},
      "[StorageConnectors](#cfn-appstream-stack-storageconnectors)" : {{[ StorageConnector, ... ]}},
      "[StreamingExperienceSettings](#cfn-appstream-stack-streamingexperiencesettings)" : {{StreamingExperienceSettings}},
      "[Tags](#cfn-appstream-stack-tags)" : {{[ Tag, ... ]}},
      "[UserSettings](#cfn-appstream-stack-usersettings)" : {{[ UserSetting, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-appstream-stack-syntax.yaml"></a>

```
Type: AWS::AppStream::Stack
Properties:
  [AccessEndpoints](#cfn-appstream-stack-accessendpoints): {{
    - AccessEndpoint}}
  [AgentAccessConfig](#cfn-appstream-stack-agentaccessconfig): {{
    AgentAccessConfig}}
  [ApplicationSettings](#cfn-appstream-stack-applicationsettings): {{
    ApplicationSettings}}
  [AttributesToDelete](#cfn-appstream-stack-attributestodelete): {{
    - String}}
  [ContentRedirection](#cfn-appstream-stack-contentredirection): {{
    ContentRedirection}}
  [DeleteStorageConnectors](#cfn-appstream-stack-deletestorageconnectors): {{Boolean}}
  [Description](#cfn-appstream-stack-description): {{String}}
  [DisplayName](#cfn-appstream-stack-displayname): {{String}}
  [EmbedHostDomains](#cfn-appstream-stack-embedhostdomains): {{
    - String}}
  [FeedbackURL](#cfn-appstream-stack-feedbackurl): {{String}}
  [Name](#cfn-appstream-stack-name): {{String}}
  [RedirectURL](#cfn-appstream-stack-redirecturl): {{String}}
  [StorageConnectors](#cfn-appstream-stack-storageconnectors): {{
    - StorageConnector}}
  [StreamingExperienceSettings](#cfn-appstream-stack-streamingexperiencesettings): {{
    StreamingExperienceSettings}}
  [Tags](#cfn-appstream-stack-tags): {{
    - Tag}}
  [UserSettings](#cfn-appstream-stack-usersettings): {{
    - UserSetting}}
```

## Properties
<a name="aws-resource-appstream-stack-properties"></a>

`AccessEndpoints`  <a name="cfn-appstream-stack-accessendpoints"></a>
The list of virtual private cloud (VPC) interface endpoint objects. Users of the stack can connect to WorkSpaces Applications only through the specified endpoints.
*Required*: No
*Type*: Array of [AccessEndpoint](aws-properties-appstream-stack-accessendpoint.md)
*Minimum*: `1`
*Maximum*: `4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AgentAccessConfig`  <a name="cfn-appstream-stack-agentaccessconfig"></a>
The agent access configuration of the stack, if agent access is enabled.
*Required*: No
*Type*: [AgentAccessConfig](aws-properties-appstream-stack-agentaccessconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ApplicationSettings`  <a name="cfn-appstream-stack-applicationsettings"></a>
The persistent application settings for users of the stack. When these settings are enabled, changes that users make to applications and Windows settings are automatically saved after each session and applied to the next session.
*Required*: No
*Type*: [ApplicationSettings](aws-properties-appstream-stack-applicationsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AttributesToDelete`  <a name="cfn-appstream-stack-attributestodelete"></a>
The stack attributes to delete.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ContentRedirection`  <a name="cfn-appstream-stack-contentredirection"></a>
Property description not available.
*Required*: No
*Type*: [ContentRedirection](aws-properties-appstream-stack-contentredirection.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeleteStorageConnectors`  <a name="cfn-appstream-stack-deletestorageconnectors"></a>
 *This parameter has been deprecated.*
Deletes the storage connectors currently enabled for the stack.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-appstream-stack-description"></a>
The description to display.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-appstream-stack-displayname"></a>
The stack name to display.
*Required*: No
*Type*: String
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EmbedHostDomains`  <a name="cfn-appstream-stack-embedhostdomains"></a>
The domains where WorkSpaces Applications streaming sessions can be embedded in an iframe. You must approve the domains that you want to host embedded WorkSpaces Applications streaming sessions.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`FeedbackURL`  <a name="cfn-appstream-stack-feedbackurl"></a>
The URL that users are redirected to after they click the Send Feedback link. If no URL is specified, no Send Feedback link is displayed.
*Required*: No
*Type*: String
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-appstream-stack-name"></a>
The name of the stack.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RedirectURL`  <a name="cfn-appstream-stack-redirecturl"></a>
The URL that users are redirected to after their streaming session ends.
*Required*: No
*Type*: String
*Maximum*: `1000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StorageConnectors`  <a name="cfn-appstream-stack-storageconnectors"></a>
The storage connectors to enable.
*Required*: No
*Type*: Array of [StorageConnector](aws-properties-appstream-stack-storageconnector.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamingExperienceSettings`  <a name="cfn-appstream-stack-streamingexperiencesettings"></a>
The streaming protocol that you want your stack to prefer. This can be UDP or TCP. Currently, UDP is only supported in the Windows native client.
*Required*: No
*Type*: [StreamingExperienceSettings](aws-properties-appstream-stack-streamingexperiencesettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-appstream-stack-tags"></a>
An array of key-value pairs.
*Required*: No
*Type*: Array of [Tag](aws-properties-appstream-stack-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UserSettings`  <a name="cfn-appstream-stack-usersettings"></a>
The actions that are enabled or disabled for users during their streaming sessions. By default, these actions are enabled.
*Required*: No
*Type*: Array of [UserSetting](aws-properties-appstream-stack-usersetting.md)
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also
<a name="aws-resource-appstream-stack--seealso"></a>
+ [CreateStack](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateStack.html) in the *Amazon WorkSpaces Applications API Reference*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
