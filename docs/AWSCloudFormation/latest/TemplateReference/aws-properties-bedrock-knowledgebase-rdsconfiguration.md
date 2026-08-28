---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-rdsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase RdsConfiguration
<a name="aws-properties-bedrock-knowledgebase-rdsconfiguration"></a>

Contains details about the storage configuration of the knowledge base in Amazon RDS. For more information, see [Create a vector index in Amazon RDS](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-setup-rds.html).

## Syntax
<a name="aws-properties-bedrock-knowledgebase-rdsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-rdsconfiguration-syntax.json"></a>

```
{
  "[CredentialsSecretArn](#cfn-bedrock-knowledgebase-rdsconfiguration-credentialssecretarn)" : {{String}},
  "[DatabaseName](#cfn-bedrock-knowledgebase-rdsconfiguration-databasename)" : {{String}},
  "[FieldMapping](#cfn-bedrock-knowledgebase-rdsconfiguration-fieldmapping)" : {{RdsFieldMapping}},
  "[ResourceArn](#cfn-bedrock-knowledgebase-rdsconfiguration-resourcearn)" : {{String}},
  "[TableName](#cfn-bedrock-knowledgebase-rdsconfiguration-tablename)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-rdsconfiguration-syntax.yaml"></a>

```
  [CredentialsSecretArn](#cfn-bedrock-knowledgebase-rdsconfiguration-credentialssecretarn): {{String}}
  [DatabaseName](#cfn-bedrock-knowledgebase-rdsconfiguration-databasename): {{String}}
  [FieldMapping](#cfn-bedrock-knowledgebase-rdsconfiguration-fieldmapping): {{
    RdsFieldMapping}}
  [ResourceArn](#cfn-bedrock-knowledgebase-rdsconfiguration-resourcearn): {{String}}
  [TableName](#cfn-bedrock-knowledgebase-rdsconfiguration-tablename): {{String}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-rdsconfiguration-properties"></a>

`CredentialsSecretArn`  <a name="cfn-bedrock-knowledgebase-rdsconfiguration-credentialssecretarn"></a>
The Amazon Resource Name (ARN) of the secret that you created in AWS Secrets Manager that is linked to your Amazon RDS database.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(|-cn|-us-gov):secretsmanager:[a-z0-9-]{1,20}:([0-9]{12}|):secret:[a-zA-Z0-9!/_+=.@-]{1,512}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DatabaseName`  <a name="cfn-bedrock-knowledgebase-rdsconfiguration-databasename"></a>
The name of your Amazon RDS database.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-]+$`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`FieldMapping`  <a name="cfn-bedrock-knowledgebase-rdsconfiguration-fieldmapping"></a>
Contains the names of the fields to which to map information about the vector store.
*Required*: Yes
*Type*: [RdsFieldMapping](aws-properties-bedrock-knowledgebase-rdsfieldmapping.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ResourceArn`  <a name="cfn-bedrock-knowledgebase-rdsconfiguration-resourcearn"></a>
The Amazon Resource Name (ARN) of the vector store.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws(|-cn|-us-gov):rds:[a-zA-Z0-9-]*:[0-9]{12}:cluster:[a-zA-Z0-9-]{1,63}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`TableName`  <a name="cfn-bedrock-knowledgebase-rdsconfiguration-tablename"></a>
The name of the table in the database.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\.\-]+$`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
