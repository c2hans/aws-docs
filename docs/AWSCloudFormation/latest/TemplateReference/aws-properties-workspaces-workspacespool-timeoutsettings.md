---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-workspaces-workspacespool-timeoutsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpaces::WorkspacesPool TimeoutSettings
<a name="aws-properties-workspaces-workspacespool-timeoutsettings"></a>

Describes the timeout settings for the pool.

## Syntax
<a name="aws-properties-workspaces-workspacespool-timeoutsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-workspaces-workspacespool-timeoutsettings-syntax.json"></a>

```
{
  "[DisconnectTimeoutInSeconds](#cfn-workspaces-workspacespool-timeoutsettings-disconnecttimeoutinseconds)" : {{Integer}},
  "[IdleDisconnectTimeoutInSeconds](#cfn-workspaces-workspacespool-timeoutsettings-idledisconnecttimeoutinseconds)" : {{Integer}},
  "[MaxUserDurationInSeconds](#cfn-workspaces-workspacespool-timeoutsettings-maxuserdurationinseconds)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-workspaces-workspacespool-timeoutsettings-syntax.yaml"></a>

```
  [DisconnectTimeoutInSeconds](#cfn-workspaces-workspacespool-timeoutsettings-disconnecttimeoutinseconds): {{Integer}}
  [IdleDisconnectTimeoutInSeconds](#cfn-workspaces-workspacespool-timeoutsettings-idledisconnecttimeoutinseconds): {{Integer}}
  [MaxUserDurationInSeconds](#cfn-workspaces-workspacespool-timeoutsettings-maxuserdurationinseconds): {{Integer}}
```

## Properties
<a name="aws-properties-workspaces-workspacespool-timeoutsettings-properties"></a>

`DisconnectTimeoutInSeconds`  <a name="cfn-workspaces-workspacespool-timeoutsettings-disconnecttimeoutinseconds"></a>
Specifies the amount of time, in seconds, that a streaming session remains active after users disconnect. If users try to reconnect to the streaming session after a disconnection or network interruption within the time set, they are connected to their previous session. Otherwise, they are connected to a new session with a new streaming instance.
*Required*: No
*Type*: Integer
*Minimum*: `60`
*Maximum*: `36000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdleDisconnectTimeoutInSeconds`  <a name="cfn-workspaces-workspacespool-timeoutsettings-idledisconnecttimeoutinseconds"></a>
The amount of time in seconds a connection will stay active while idle.
*Required*: No
*Type*: Integer
*Minimum*: `0`
*Maximum*: `36000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MaxUserDurationInSeconds`  <a name="cfn-workspaces-workspacespool-timeoutsettings-maxuserdurationinseconds"></a>
Specifies the maximum amount of time, in seconds, that a streaming session can remain active. If users are still connected to a streaming instance five minutes before this limit is reached, they are prompted to save any open documents before being disconnected. After this time elapses, the instance is terminated and replaced by a new instance.
*Required*: No
*Type*: Integer
*Minimum*: `600`
*Maximum*: `432000`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
