---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrock-knowledgebase-redshiftserverlessconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Bedrock::KnowledgeBase RedshiftServerlessConfiguration
<a name="aws-properties-bedrock-knowledgebase-redshiftserverlessconfiguration"></a>

Contains configurations for authentication to Amazon Redshift Serverless.

## Syntax
<a name="aws-properties-bedrock-knowledgebase-redshiftserverlessconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrock-knowledgebase-redshiftserverlessconfiguration-syntax.json"></a>

```
{
  "[AuthConfiguration](#cfn-bedrock-knowledgebase-redshiftserverlessconfiguration-authconfiguration)" : {{RedshiftServerlessAuthConfiguration}},
  "[WorkgroupArn](#cfn-bedrock-knowledgebase-redshiftserverlessconfiguration-workgrouparn)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrock-knowledgebase-redshiftserverlessconfiguration-syntax.yaml"></a>

```
  [AuthConfiguration](#cfn-bedrock-knowledgebase-redshiftserverlessconfiguration-authconfiguration): {{
    RedshiftServerlessAuthConfiguration}}
  [WorkgroupArn](#cfn-bedrock-knowledgebase-redshiftserverlessconfiguration-workgrouparn): {{String}}
```

## Properties
<a name="aws-properties-bedrock-knowledgebase-redshiftserverlessconfiguration-properties"></a>

`AuthConfiguration`  <a name="cfn-bedrock-knowledgebase-redshiftserverlessconfiguration-authconfiguration"></a>
Specifies configurations for authentication to an Amazon Redshift provisioned data warehouse.
*Required*: Yes
*Type*: [RedshiftServerlessAuthConfiguration](aws-properties-bedrock-knowledgebase-redshiftserverlessauthconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WorkgroupArn`  <a name="cfn-bedrock-knowledgebase-redshiftserverlessconfiguration-workgrouparn"></a>
The ARN of the Amazon Redshift workgroup.
*Required*: Yes
*Type*: String
*Pattern*: `^(arn:(aws(-[a-z]+)*):redshift-serverless:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:workgroup/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12})$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
