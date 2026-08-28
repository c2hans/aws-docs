---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-redshiftserverlessauthconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase RedshiftServerlessAuthConfiguration
<a name="aws-properties-bedrock-knowledgebase-redshiftserverlessauthconfiguration"></a>

Specifies configurations for authentication to a Redshift Serverless. Specify the type of authentication to use in the `type` field and include the corresponding field. If you specify IAM authentication, you don't need to include another field.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-redshiftserverlessauthconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-redshiftserverlessauthconfiguration-syntax.json"></a>

```
{
  "[Type](#cfn-bedrock-knowledgebase-redshiftserverlessauthconfiguration-type)" : {{String}},
  "[UsernamePasswordSecretArn](#cfn-bedrock-knowledgebase-redshiftserverlessauthconfiguration-usernamepasswordsecretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-redshiftserverlessauthconfiguration-syntax.yaml"></a>

```
  [Type](#cfn-bedrock-knowledgebase-redshiftserverlessauthconfiguration-type): {{String}}
  [UsernamePasswordSecretArn](#cfn-bedrock-knowledgebase-redshiftserverlessauthconfiguration-usernamepasswordsecretarn): {{String}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-redshiftserverlessauthconfiguration-properties"></a>

`Type`  <a name="cfn-bedrock-knowledgebase-redshiftserverlessauthconfiguration-type"></a>
The type of authentication to use.
*Required*: Yes
*Type*: String
*Allowed values*: `IAM | USERNAME_PASSWORD`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UsernamePasswordSecretArn`  <a name="cfn-bedrock-knowledgebase-redshiftserverlessauthconfiguration-usernamepasswordsecretarn"></a>
The ARN of an Secrets Manager secret for authentication.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(|-cn|-us-gov):secretsmanager:[a-z0-9-]{1,20}:([0-9]{12}|):secret:[a-zA-Z0-9!/_+=.@-]{1,512}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
