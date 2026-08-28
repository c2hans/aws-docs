---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-datasource-serversideencryptionconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::DataSource ServerSideEncryptionConfiguration
<a name="aws-properties-bedrock-datasource-serversideencryptionconfiguration"></a>

Contains the configuration for server-side encryption for your managed knowledge base.

## Syntax
<a name="aws-properties-bedrock-datasource-serversideencryptionconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-datasource-serversideencryptionconfiguration-syntax.json"></a>

```
{
  "[KmsKeyArn](#cfn-bedrock-datasource-serversideencryptionconfiguration-kmskeyarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-datasource-serversideencryptionconfiguration-syntax.yaml"></a>

```
  [KmsKeyArn](#cfn-bedrock-datasource-serversideencryptionconfiguration-kmskeyarn): {{String}}
```

## Properties
<a name="aws-properties-bedrock-datasource-serversideencryptionconfiguration-properties"></a>

`KmsKeyArn`  <a name="cfn-bedrock-datasource-serversideencryptionconfiguration-kmskeyarn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key used to encrypt the resource.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-cn|-us-gov|-eusc|-iso(-[b-f])?)?:kms:[a-zA-Z0-9-]*:[0-9]{12}:key/[a-zA-Z0-9-]{36}$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
