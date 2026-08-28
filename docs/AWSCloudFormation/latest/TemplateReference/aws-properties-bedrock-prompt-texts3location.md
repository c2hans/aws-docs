---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-prompt-texts3location.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Prompt TextS3Location
<a name="aws-properties-bedrock-prompt-texts3location"></a>

The Amazon S3location of the prompt text.

## Syntax
<a name="aws-properties-bedrock-prompt-texts3location-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-prompt-texts3location-syntax.json"></a>

```
{
  "[Bucket](#cfn-bedrock-prompt-texts3location-bucket)" : {{String}},
  "[Key](#cfn-bedrock-prompt-texts3location-key)" : {{String}},
  "[Version](#cfn-bedrock-prompt-texts3location-version)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-prompt-texts3location-syntax.yaml"></a>

```
  [Bucket](#cfn-bedrock-prompt-texts3location-bucket): {{String}}
  [Key](#cfn-bedrock-prompt-texts3location-key): {{String}}
  [Version](#cfn-bedrock-prompt-texts3location-version): {{String}}
```

## Properties
<a name="aws-properties-bedrock-prompt-texts3location-properties"></a>

`Bucket`  <a name="cfn-bedrock-prompt-texts3location-bucket"></a>
The Amazon S3bucket containing the prompt text.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-z0-9][\.\-a-z0-9]{1,61}[a-z0-9]$`
*Minimum*: `3`
*Maximum*: `63`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Key`  <a name="cfn-bedrock-prompt-texts3location-key"></a>
The object key for the Amazon S3 location.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Version`  <a name="cfn-bedrock-prompt-texts3location-version"></a>
The version of the Amazon S3location to use.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
