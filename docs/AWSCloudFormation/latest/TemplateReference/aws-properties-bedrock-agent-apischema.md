---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-agent-apischema.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::Agent APISchema
<a name="aws-properties-bedrock-agent-apischema"></a>

 Contains details about the OpenAPI schema for the action group. For more information, see [Action group OpenAPI schemas](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-api-schema.html). You can either include the schema directly in the payload field or you can upload it to an S3 bucket and specify the S3 bucket location in the s3 field.

## Syntax
<a name="aws-properties-bedrock-agent-apischema-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-agent-apischema-syntax.json"></a>

```
{
  "[Payload](#cfn-bedrock-agent-apischema-payload)" : {{String}},
  "[S3](#cfn-bedrock-agent-apischema-s3)" : {{S3Identifier}}
}
```

### YAML
<a name="aws-properties-bedrock-agent-apischema-syntax.yaml"></a>

```
  [Payload](#cfn-bedrock-agent-apischema-payload): {{String}}
  [S3](#cfn-bedrock-agent-apischema-s3): {{
    S3Identifier}}
```

## Properties
<a name="aws-properties-bedrock-agent-apischema-properties"></a>

`Payload`  <a name="cfn-bedrock-agent-apischema-payload"></a>
 The JSON or YAML-formatted payload defining the OpenAPI schema for the action group.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3`  <a name="cfn-bedrock-agent-apischema-s3"></a>
 Contains details about the S3 object containing the OpenAPI schema for the action group.
*Required*: No
*Type*: [S3Identifier](aws-properties-bedrock-agent-s3identifier.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
