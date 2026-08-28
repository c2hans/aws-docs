---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-microvmimage-hooks.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::MicrovmImage Hooks
<a name="aws-properties-lambda-microvmimage-hooks"></a>

Lifecycle hook configuration for MicroVMs and MicroVM images.

## Syntax
<a name="aws-properties-lambda-microvmimage-hooks-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-microvmimage-hooks-syntax.json"></a>

```
{
  "[MicrovmHooks](#cfn-lambda-microvmimage-hooks-microvmhooks)" : {{MicrovmHooks}},
  "[MicrovmImageHooks](#cfn-lambda-microvmimage-hooks-microvmimagehooks)" : {{MicrovmImageHooks}},
  "[Port](#cfn-lambda-microvmimage-hooks-port)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-lambda-microvmimage-hooks-syntax.yaml"></a>

```
  [MicrovmHooks](#cfn-lambda-microvmimage-hooks-microvmhooks): {{
    MicrovmHooks}}
  [MicrovmImageHooks](#cfn-lambda-microvmimage-hooks-microvmimagehooks): {{
    MicrovmImageHooks}}
  [Port](#cfn-lambda-microvmimage-hooks-port): {{Integer}}
```

## Properties
<a name="aws-properties-lambda-microvmimage-hooks-properties"></a>

`MicrovmHooks`  <a name="cfn-lambda-microvmimage-hooks-microvmhooks"></a>
The lifecycle hooks for MicroVM events.
*Required*: No
*Type*: [MicrovmHooks](aws-properties-lambda-microvmimage-microvmhooks.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MicrovmImageHooks`  <a name="cfn-lambda-microvmimage-hooks-microvmimagehooks"></a>
The hooks for MicroVM image build events.
*Required*: No
*Type*: [MicrovmImageHooks](aws-properties-lambda-microvmimage-microvmimagehooks.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-lambda-microvmimage-hooks-port"></a>
The port number on which the hooks listener runs.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
