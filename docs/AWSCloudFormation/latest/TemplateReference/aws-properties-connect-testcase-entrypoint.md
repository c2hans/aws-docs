---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-testcase-entrypoint.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::TestCase EntryPoint
<a name="aws-properties-connect-testcase-entrypoint"></a>

<a name="aws-properties-connect-testcase-entrypoint-description"></a>The `EntryPoint` property type specifies Property description not available. for an [AWS::Connect::TestCase](aws-resource-connect-testcase.md).

## Syntax
<a name="aws-properties-connect-testcase-entrypoint-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-testcase-entrypoint-syntax.json"></a>

```
{
  "[ChatEntryPointParameters](#cfn-connect-testcase-entrypoint-chatentrypointparameters)" : {{ChatEntryPointParameters}},
  "[Type](#cfn-connect-testcase-entrypoint-type)" : {{String}},
  "[VoiceCallEntryPointParameters](#cfn-connect-testcase-entrypoint-voicecallentrypointparameters)" : {{VoiceCallEntryPointParameters}}
}
```

### YAML
<a name="aws-properties-connect-testcase-entrypoint-syntax.yaml"></a>

```
  [ChatEntryPointParameters](#cfn-connect-testcase-entrypoint-chatentrypointparameters): {{
    ChatEntryPointParameters}}
  [Type](#cfn-connect-testcase-entrypoint-type): {{String}}
  [VoiceCallEntryPointParameters](#cfn-connect-testcase-entrypoint-voicecallentrypointparameters): {{
    VoiceCallEntryPointParameters}}
```

## Properties
<a name="aws-properties-connect-testcase-entrypoint-properties"></a>

`ChatEntryPointParameters`  <a name="cfn-connect-testcase-entrypoint-chatentrypointparameters"></a>
Property description not available.
*Required*: No
*Type*: [ChatEntryPointParameters](aws-properties-connect-testcase-chatentrypointparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-connect-testcase-entrypoint-type"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `VOICE_CALL | CHAT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VoiceCallEntryPointParameters`  <a name="cfn-connect-testcase-entrypoint-voicecallentrypointparameters"></a>
Property description not available.
*Required*: No
*Type*: [VoiceCallEntryPointParameters](aws-properties-connect-testcase-voicecallentrypointparameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
