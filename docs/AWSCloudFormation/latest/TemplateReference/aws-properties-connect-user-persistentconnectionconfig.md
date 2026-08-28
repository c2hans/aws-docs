---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-user-persistentconnectionconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::User PersistentConnectionConfig
<a name="aws-properties-connect-user-persistentconnectionconfig"></a>

Configuration settings for persistent connection for a specific channel.

## Syntax
<a name="aws-properties-connect-user-persistentconnectionconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-user-persistentconnectionconfig-syntax.json"></a>

```
{
  "[Channel](#cfn-connect-user-persistentconnectionconfig-channel)" : {{String}},
  "[PersistentConnection](#cfn-connect-user-persistentconnectionconfig-persistentconnection)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-connect-user-persistentconnectionconfig-syntax.yaml"></a>

```
  [Channel](#cfn-connect-user-persistentconnectionconfig-channel): {{String}}
  [PersistentConnection](#cfn-connect-user-persistentconnectionconfig-persistentconnection): {{Boolean}}
```

## Properties
<a name="aws-properties-connect-user-persistentconnectionconfig-properties"></a>

`Channel`  <a name="cfn-connect-user-persistentconnectionconfig-channel"></a>
Configuration settings for persistent connection. **Only `VOICE` is supported for this data type.**
*Required*: Yes
*Type*: String
*Allowed values*: `VOICE | CHAT | TASK | EMAIL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PersistentConnection`  <a name="cfn-connect-user-persistentconnectionconfig-persistentconnection"></a>
Indicates whether persistent connection is enabled. When enabled, the agent's connection is maintained after a call ends, enabling subsequent calls to connect faster.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
