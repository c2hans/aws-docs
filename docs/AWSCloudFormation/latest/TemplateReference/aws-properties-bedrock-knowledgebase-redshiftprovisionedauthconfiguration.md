---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-redshiftprovisionedauthconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase RedshiftProvisionedAuthConfiguration
<a name="aws-properties-bedrock-knowledgebase-redshiftprovisionedauthconfiguration"></a>

Contains configurations for authentication to an Amazon Redshift provisioned data warehouse. Specify the type of authentication to use in the `type` field and include the corresponding field. If you specify IAM authentication, you don't need to include another field.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-redshiftprovisionedauthconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-redshiftprovisionedauthconfiguration-syntax.json"></a>

```
{
  "[DatabaseUser](#cfn-bedrock-knowledgebase-redshiftprovisionedauthconfiguration-databaseuser)" : {{String}},
  "[Type](#cfn-bedrock-knowledgebase-redshiftprovisionedauthconfiguration-type)" : {{String}},
  "[UsernamePasswordSecretArn](#cfn-bedrock-knowledgebase-redshiftprovisionedauthconfiguration-usernamepasswordsecretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-redshiftprovisionedauthconfiguration-syntax.yaml"></a>

```
  [DatabaseUser](#cfn-bedrock-knowledgebase-redshiftprovisionedauthconfiguration-databaseuser): {{String}}
  [Type](#cfn-bedrock-knowledgebase-redshiftprovisionedauthconfiguration-type): {{String}}
  [UsernamePasswordSecretArn](#cfn-bedrock-knowledgebase-redshiftprovisionedauthconfiguration-usernamepasswordsecretarn): {{String}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-redshiftprovisionedauthconfiguration-properties"></a>

`DatabaseUser`  <a name="cfn-bedrock-knowledgebase-redshiftprovisionedauthconfiguration-databaseuser"></a>
The database username for authentication to an Amazon Redshift provisioned data warehouse.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Type`  <a name="cfn-bedrock-knowledgebase-redshiftprovisionedauthconfiguration-type"></a>
The type of authentication to use.
*Required*: Yes
*Type*: String
*Allowed values*: `IAM | USERNAME_PASSWORD | USERNAME`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UsernamePasswordSecretArn`  <a name="cfn-bedrock-knowledgebase-redshiftprovisionedauthconfiguration-usernamepasswordsecretarn"></a>
The ARN of an Secrets Manager secret for authentication.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(|-cn|-us-gov):secretsmanager:[a-z0-9-]{1,20}:([0-9]{12}|):secret:[a-zA-Z0-9!/_+=.@-]{1,512}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
