---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-osis-pipeline-encryptionatrestoptions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::OSIS::Pipeline EncryptionAtRestOptions
<a name="aws-properties-osis-pipeline-encryptionatrestoptions"></a>

Options to control how OpenSearch encrypts buffer data.

## Syntax
<a name="aws-properties-osis-pipeline-encryptionatrestoptions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-osis-pipeline-encryptionatrestoptions-syntax.json"></a>

```
{
  "[KmsKeyArn](#cfn-osis-pipeline-encryptionatrestoptions-kmskeyarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-osis-pipeline-encryptionatrestoptions-syntax.yaml"></a>

```
  [KmsKeyArn](#cfn-osis-pipeline-encryptionatrestoptions-kmskeyarn): {{String}}
```

## Properties
<a name="aws-properties-osis-pipeline-encryptionatrestoptions-properties"></a>

`KmsKeyArn`  <a name="cfn-osis-pipeline-encryptionatrestoptions-kmskeyarn"></a>
The ARN of the KMS key used to encrypt buffer data. By default, data is encrypted using an AWS owned key.
*Required*: Yes
*Type*: String
*Minimum*: `7`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
