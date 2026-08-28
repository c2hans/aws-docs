---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-bedrockagentcore-browserprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::BrowserProfile
<a name="aws-resource-bedrockagentcore-browserprofile"></a>

Specifies a browser profile for Amazon Bedrock AgentCore. A browser profile stores persistent browser session data, including cookies, local storage, session storage, and browsing history, enabling AI agents to maintain authenticated sessions and reuse browser state across multiple browser sessions.

For more information, see [Manage browser profiles in Amazon Bedrock AgentCore](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/browser-profiles.html).

See the **Properties** section below for descriptions of both the required and optional properties.

## Syntax
<a name="aws-resource-bedrockagentcore-browserprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-bedrockagentcore-browserprofile-syntax.json"></a>

```
{
  "Type" : "AWS::BedrockAgentCore::BrowserProfile",
  "Properties" : {
      "[Description](#cfn-bedrockagentcore-browserprofile-description)" : {{String}},
      "[Name](#cfn-bedrockagentcore-browserprofile-name)" : {{String}},
      "[Tags](#cfn-bedrockagentcore-browserprofile-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-bedrockagentcore-browserprofile-syntax.yaml"></a>

```
Type: AWS::BedrockAgentCore::BrowserProfile
Properties:
  [Description](#cfn-bedrockagentcore-browserprofile-description): {{String}}
  [Name](#cfn-bedrockagentcore-browserprofile-name): {{String}}
  [Tags](#cfn-bedrockagentcore-browserprofile-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-bedrockagentcore-browserprofile-properties"></a>

`Description`  <a name="cfn-bedrockagentcore-browserprofile-description"></a>
The description of the browser profile.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-bedrockagentcore-browserprofile-name"></a>
The name of the browser profile.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z][a-zA-Z0-9_]{0,47}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-bedrockagentcore-browserprofile-tags"></a>
The tags for the browser profile.
*Required*: No
*Type*: Object of String
*Pattern*: `^[a-zA-Z0-9\s._:/=+@-]*$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-bedrockagentcore-browserprofile-return-values"></a>

### Ref
<a name="aws-resource-bedrockagentcore-browserprofile-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the browser profile. For example:

 `arn:aws:bedrock-agentcore:us-east-1:123456789012:browser-profile/MyBrowserProfile-a1b2c3d4e5`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-bedrockagentcore-browserprofile-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-bedrockagentcore-browserprofile-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the browser profile was created.

`LastSavedAt`  <a name="LastSavedAt-fn::getatt"></a>
The timestamp when browser session data was last saved to this profile.

`LastSavedBrowserId`  <a name="LastSavedBrowserId-fn::getatt"></a>
The identifier of the browser from which data was last saved to this profile.

`LastSavedBrowserSessionId`  <a name="LastSavedBrowserSessionId-fn::getatt"></a>
The identifier of the browser session from which data was last saved to this profile.

`LastUpdatedAt`  <a name="LastUpdatedAt-fn::getatt"></a>
The timestamp when the browser profile was last updated.

`ProfileArn`  <a name="ProfileArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the browser profile.

`ProfileId`  <a name="ProfileId-fn::getatt"></a>
The unique identifier of the browser profile.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the browser profile.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
